# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:59:42 2020

@author: Miao
"""
#%% =============================================================================
# import modules
# =============================================================================
import math,copy,random,csv
import matplotlib.pyplot as plt
import VirtualEllipseFunc.m_defineEllipses
import VirtualEllipseFunc.m_drawEllipses
from shapely.geometry import Point, Polygon
from scipy.spatial import distance, ConvexHull
from math import pi
#%% =============================================================================
# parameters
# =============================================================================
#windowsize = 0.4
#ka, kb = 0.25, 0.1
#loop_number = 1
#%% =============================================================================
# initial positions
# =============================================================================
def runStimuliGeneration(windowsize, visualization = True, ka = 0.25, kb = 0.1,loop_number = 1):
    def getallposi(grid_x = 101, grid_y = 75, linelength = 10):
        '''get full positions in a dimention of grid_x*grid_y'''
        start_x = -0.5*linelength*grid_x + 0.5*linelength
        start_y = -0.5*linelength*grid_y + 0.5*linelength
        positions = []
        for x in range(0, grid_x):
            new_x = start_x + x*linelength
            for y in range(0, grid_y):
                new_y = start_y + y*linelength
                positions.append((new_x, new_y))
        try:
            positions.remove((0,0))#remove the center
        except ValueError:
            pass
        return positions
    
    def getfovealemptyposi(fovelr = 100):
        '''get positions around fovel region'''
        fullposi  = getallposi() #get full positon lists
        fovealemptyposi = []
        for p in fullposi:
            if math.sqrt((p[0]**2) + (p[1]**2)) < fovelr:
                fovealemptyposi.append(p)
        return fovealemptyposi
    
    def getallowedposi(winsize = windowsize):
        '''get positions for given windowsize'''
        fullposi = getallposi() #get full postion lists
        
        ###remove the foveal position
        fovealemptyposi = getfovealemptyposi()
        for p in fovealemptyposi:
            fullposi.remove(p)
            
        ###remove all positions outsite the defined windowsize
        fullposi_t = copy.deepcopy(fullposi) #deepcopy, without influence to the inital list
        maxcorrdinate = max(fullposi) #get the corridinate of the furtherest posi
        for p in fullposi_t:
            if abs(p[0]) > maxcorrdinate[0]*winsize or abs(p[1])> maxcorrdinate[1]*winsize:
                fullposi.remove(p)
        return fullposi
    #%% =============================================================================
    # get stimuli postions
    # =============================================================================
    generation = True
    while generation == True:
        positions = getallowedposi()
        presentaiton_area = copy.deepcopy(positions)
        random.shuffle(positions)
        
        #first random disk
        disk_posi = positions[-1] 
        #virtual_e1 = VirtualEllipseFunc.m_defineEllipses.defineVirtualEllipses(disk_posi,ka,kb)
        taken_posi = []
        taken_posi.append(disk_posi)
        positions.pop(-1)
        
        #all other disks
        while_number = 0
        while len(positions) > 0: 
            disk_posi_new = positions[-1]
            VirtualEllipseFunc.m_defineEllipses.caclulateNewList_2direction(disk_posi_new,taken_posi,positions,ka,kb)
            while_number = while_number + 1
            print(while_number)
    
        taken_posi = copy.deepcopy(taken_posi) #TODO
        print("taken_list", taken_posi,"Numbers", len(taken_posi))
        
        #generation = False
        if windowsize == 0.4:
            if len(taken_posi)> 22 or len(taken_posi) < 17:
                generation = True
            else:
                generation =False
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, [], ka, kb)
    #%% =============================================================================
    # extra discs
    # =============================================================================
    
    ####remove overlapping area
    finalE = [] #all ellipses that have been drawn
    for new_posi in taken_posi:
        finalE0 =  VirtualEllipseFunc.m_defineEllipses.defineVirtualEllipses(new_posi,ka,kb)
        finalE.append(finalE0)
    
    presentaiton_area = presentaiton_area + getfovealemptyposi()
    del_p3 =[]
    tempTemplist = presentaiton_area.copy() #full list that removes the foveal area
    for i in finalE:
        tempER = VirtualEllipseFunc.m_defineEllipses.ellipseToPolygon([i])[0]
        tempERpolygon = Polygon(tempER)
        tempET = VirtualEllipseFunc.m_defineEllipses.ellipseToPolygon([i])[1]
        tempETpolygon = Polygon(tempET)
        for tempP in presentaiton_area:
            if tempERpolygon.contains(Point(tempP)) == True and tempETpolygon.contains(Point(tempP)) == True:
                del_p3.append(tempP)
                try:
                    tempTemplist.remove(tempP)
                except ValueError:
                    pass
    presentaiton_area2 = copy.deepcopy(tempTemplist) # all position positions to add extra disks + area outside ellipse-cross
    
    #%%
    ####get extra postions
    radial_dic_1 = {} #extra positions: radial and tangential direction
    radial_dic_2 = {} 
    tan_dic = {}
    # out_ellispecross = []
    # for each disc position, take the radial area (away from foveal as base)
    for count, i in enumerate(finalE, start = 1):
        ellipsePolygon = VirtualEllipseFunc.m_defineEllipses.ellipseToPolygon([i])[0] #radial ellipse
        ellipsePolygonT = VirtualEllipseFunc.m_defineEllipses.ellipseToPolygon([i])[1]#tangential ellipse
        epPolygon = Polygon(ellipsePolygon)
        epPolygonT = Polygon(ellipsePolygonT)
        radial_dic_1[(i[0],i[1])] = [] #set the keys of the dictionary--taken_posi
        radial_dic_2[(i[0],i[1])] = []
        tan_dic[(i[0],i[1])] = []
    
        for posi in presentaiton_area2:
            if epPolygon.contains(Point(posi)):
                if distance.euclidean(taken_posi[count-1], (0,0)) > distance.euclidean(posi, (0,0)): # close to foveal
                    radial_dic_1[(i[0], i[1])].append(posi)
                else: #away from foveal (take this)
                    radial_dic_2[(i[0],i[1])].append(posi)
                    
                presentaiton_area2.remove(posi)
            elif epPolygonT.contains(Point(posi)):
                tan_dic[(i[0],i[1])].append(posi) #all disks in tangential area within ellipse cross
                
                presentaiton_area2.remove(posi)
            # else: # outside ellipse cross
            #     out_ellispecross.append(posi)
    
    
    #remove empty items in the dictionary
    radial_dic_1_noempty = copy.deepcopy(radial_dic_1)
    radial_dic_2_noempty = copy.deepcopy(radial_dic_2)
    
    empty_keys1 = [k for k,v in radial_dic_1_noempty.items() if not v]
    empty_keys2 = [k for k,v in radial_dic_2_noempty.items() if not v]
    for k in empty_keys1:
        del radial_dic_1_noempty[k]
    for k in empty_keys2:
        del radial_dic_2_noempty[k]
    
    
    #%%
    presentaiton_area3 = copy.deepcopy(presentaiton_area2) # positions outside ellipse cross
    
    # rotate pi/2, pi, 1.5pi to get the other possible positions in other 3 areas
    # radial_dic_1_new = {}
    tan_dic_1 = {} 
    tan_dic_2 = {} 
    for centralPosi, possiblePois in radial_dic_2.items():
        # print(centralPosi,possiblePois)
        # radial_dic_1_new[centralPosi] = []
        tan_dic_1[centralPosi] =[]
        tan_dic_2[centralPosi] =[]
        for p in possiblePois:
            p_radial1 = VirtualEllipseFunc.m_defineEllipses.rotateposi(centralPosi, p, theta = pi)
            p_tan1 = VirtualEllipseFunc.m_defineEllipses.rotateposi(centralPosi, p, theta = pi/2)
            p_tan2 = VirtualEllipseFunc.m_defineEllipses.rotateposi(centralPosi, p, theta = 1.5*pi)
            # radial_dic_1_new[centralPosi].append(p_radial1)
            tan_dic_1[centralPosi].append(p_tan1)
            tan_dic_2[centralPosi].append(p_tan2)
    
    #remove empty items in the dictionary
    tan_dic_1_noempty = copy.deepcopy(tan_dic_1)
    tan_dic_2_noempty = copy.deepcopy(tan_dic_2)
    
    empty_keys3 = [k for k,v in tan_dic_1_noempty.items() if not v]
    empty_keys4 = [k for k,v in tan_dic_2_noempty.items() if not v]
    for k in empty_keys3:
        del tan_dic_1_noempty[k]
    for k in empty_keys4:
        del tan_dic_2_noempty[k]
    #%%
    #combine radial dictionaries
    
    #radial_dic combine directly
    ds = [radial_dic_1, radial_dic_2]
    radial_dic = {}
    for k in radial_dic_1.keys():
        radial_dic[k] = tuple(radial_dic[k] for radial_dic in ds)
    
    #radial_dic combined by noempty dict - 2 list shares some same keys
    radial_dic_1_noempty_t = copy.deepcopy(radial_dic_1_noempty)
    radial_dic_2_noempty_t = copy.deepcopy(radial_dic_2_noempty)
    tan_dic_1_noempty_t    = copy.deepcopy(tan_dic_1_noempty)
    tan_dic_2_noempty_t    = copy.deepcopy(tan_dic_2_noempty)
    
    radial_dic1_keys = list(radial_dic_1_noempty_t.keys())
    radial_dic2_keys = list(radial_dic_2_noempty_t.keys())
    tan_dic1_keys    = list(tan_dic_1_noempty_t.keys())
    tan_dic2_keys    = list(tan_dic_2_noempty_t.keys())
    
    #central positions that could give triplets
    commonkeys_r = []
    commonkeys_t = []
    
    for key in radial_dic1_keys:
        if key in radial_dic2_keys:
            commonkeys_r.append(key)
    for key in tan_dic1_keys:
        if key in tan_dic2_keys:
            commonkeys_t.append(key)
    #items lists into 1
    for key, item in radial_dic.items():
        radial_dic[key] = item[0]+item[1]
    
    commonkeys_r_copy1 = copy.deepcopy(commonkeys_r)
    commonkeys_t_copy1 = copy.deepcopy(commonkeys_t)
    
    commonkeys_r_copy2 = copy.deepcopy(commonkeys_r)
    commonkeys_t_copy2 = copy.deepcopy(commonkeys_t)
    
    commonkeys_r_copy3 = copy.deepcopy(commonkeys_r)
    commonkeys_t_copy3 = copy.deepcopy(commonkeys_t)
    
    commonkeys_r_copy4 = copy.deepcopy(commonkeys_r)
    commonkeys_t_copy4 = copy.deepcopy(commonkeys_t)
    
    #%% =============================================================================
    # display type
    # =============================================================================
    #used functions
    ####100% paris
    radial_posi = []
    tan_posi    = []
    for central_posi, possible_posi in radial_dic.items():
        radial_posi.append(random.choice(possible_posi))
    for central_posi, possible_posi in tan_dic.items():
        tan_posi.append(random.choice(possible_posi))
    
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, radial_posi, ka, kb)
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, tan_posi, ka, kb)
    
    #### 0 pairs
    if len(taken_posi) == 17:
        n_pairs,n_triplets,n_singel = 1, 8, 8
    elif len(taken_posi) == 18:
        n_pairs,n_triplets,n_singel = 0, 9, 9
    elif len(taken_posi) == 19:
        n_pairs,n_triplets,n_singel = 1, 9, 9
    elif len(taken_posi) == 20:
        n_pairs,n_triplets,n_singel = 0, 10, 10
    elif len(taken_posi) == 21:
        n_pairs,n_triplets,n_singel = 1, 10, 10
    elif len(taken_posi) == 22:
        n_pairs,n_triplets,n_singel = 0, 11, 11
    
    chosen_tri_posi_r = [] #choose some flowers to make triplets
    chosen_tri_posi_t = []
    chosen_sig_posi_r = [] #other flowers to have single disc
    chosen_sig_posi_t = []
    
    if n_triplets > len(commonkeys_r):
        return []
    
    for n in range(0, n_triplets):
        #radial
        random_key_r = random.choice(commonkeys_r_copy1)
        chosen_tri_posi_r.append(random_key_r)
        commonkeys_r_copy1.remove(random_key_r)
        #tan
        random_key_t = random.choice(commonkeys_t_copy1)
        chosen_tri_posi_t.append(random_key_t)
        commonkeys_t_copy1.remove(random_key_t)
        
    chosen_keys_r = list(set(taken_posi) - set(chosen_tri_posi_r))
    chosen_keys_t = list(set(taken_posi) - set(chosen_tri_posi_t))
    
    for n in range(0, n_singel):
        #radial
        random_key_r = random.choice(chosen_keys_r)
        chosen_sig_posi_r.append(random_key_r)
        chosen_keys_r.remove(random_key_r)
        #tan
        random_key_t = random.choice(chosen_keys_t)
        chosen_sig_posi_t.append(random_key_t)
        chosen_keys_t.remove(random_key_t)
    
    triplet_posi_c1 = []
    for central_posi, possible_posi in radial_dic_1_noempty.items():
        if central_posi in chosen_tri_posi_r:
            triplet_posi_c1.append(random.choice(possible_posi))
    
    triplet_posi_c2 = []
    for central_posi, possible_posi in radial_dic_2_noempty.items():
        if central_posi in chosen_tri_posi_r:
            triplet_posi_c2.append(random.choice(possible_posi))
    
    triplet_posi_nc1 = []
    for central_posi, possible_posi in tan_dic_1_noempty.items():
        if central_posi in chosen_tri_posi_t:
            triplet_posi_nc1.append(random.choice(possible_posi))
    
    triplet_posi_nc2 = []
    for central_posi, possible_posi in tan_dic_2_noempty.items():
        if central_posi in chosen_tri_posi_t:
            triplet_posi_nc2.append(random.choice(possible_posi))
    
    chosen_paris_posi_r = set(taken_posi) - set(chosen_sig_posi_r) - set(chosen_tri_posi_r)
    chosen_paris_posi_t = set(taken_posi) - set(chosen_sig_posi_t) - set(chosen_tri_posi_t)
    
    pairs_r = []
    pairs_t = []
    for central_posi, possible_posi in radial_dic.items():
        if central_posi in chosen_paris_posi_r:
            pairs_r.append(random.choice(possible_posi))
    for central_posi, possible_posi in tan_dic.items():
        if central_posi in chosen_paris_posi_t:
            pairs_t.append(random.choice(possible_posi))
    
    extra_posi_c_nopair  = triplet_posi_c1 + triplet_posi_c2 + pairs_r
    extra_posi_nc_nopair = triplet_posi_nc1 + triplet_posi_nc2 + pairs_t
    
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_c_nopair, ka, kb)
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_nc_nopair, ka, kb)
    
    #%%
    ####75% paris
    
    if len(taken_posi) == 17:
        n_pairs,n_triplets,n_singel = 13, 2, 2
    elif len(taken_posi) == 18:
        n_pairs,n_triplets,n_singel = 14, 2, 2
    elif len(taken_posi) == 19:
        n_pairs,n_triplets,n_singel = 15, 2, 2
    elif len(taken_posi) == 20:
        n_pairs,n_triplets,n_singel = 14, 3, 3
    elif len(taken_posi) == 21:
        n_pairs,n_triplets,n_singel = 15, 3, 3
    elif len(taken_posi) == 22:
        n_pairs,n_triplets,n_singel = 16, 3, 3
    
    chosen_tri_posi_r = [] #choose some flowers to make triplets
    chosen_tri_posi_t = []
    chosen_sig_posi_r = [] #other flowers to have single disc
    chosen_sig_posi_t = []
    if n_triplets > len(commonkeys_r):
        return []
    for n in range(0, n_triplets):
        #radial
        random_key_r = random.choice(commonkeys_r_copy2)
        chosen_tri_posi_r.append(random_key_r)
        commonkeys_r_copy2.remove(random_key_r)
        #tan
        random_key_t = random.choice(commonkeys_t_copy2)
        chosen_tri_posi_t.append(random_key_t)
        commonkeys_t_copy2.remove(random_key_t)
        
    chosen_keys_r = list(set(taken_posi) - set(chosen_tri_posi_r))
    chosen_keys_t = list(set(taken_posi) - set(chosen_tri_posi_t))
    
    for n in range(0, n_singel):
        #radial
        random_key_r = random.choice(chosen_keys_r)
        chosen_sig_posi_r.append(random_key_r)
        chosen_keys_r.remove(random_key_r)
        #tan
        random_key_t = random.choice(chosen_keys_t)
        chosen_sig_posi_t.append(random_key_t)
        chosen_keys_t.remove(random_key_t)
    
    triplet_posi_c1 = []
    for central_posi, possible_posi in radial_dic_1_noempty.items():
        if central_posi in chosen_tri_posi_r:
            triplet_posi_c1.append(random.choice(possible_posi))
    
    triplet_posi_c2 = []
    for central_posi, possible_posi in radial_dic_2_noempty.items():
        if central_posi in chosen_tri_posi_r:
            triplet_posi_c2.append(random.choice(possible_posi))
    
    triplet_posi_nc1 = []
    for central_posi, possible_posi in tan_dic_1_noempty.items():
        if central_posi in chosen_tri_posi_t:
            triplet_posi_nc1.append(random.choice(possible_posi))
    
    triplet_posi_nc2 = []
    for central_posi, possible_posi in tan_dic_2_noempty.items():
        if central_posi in chosen_tri_posi_t:
            triplet_posi_nc2.append(random.choice(possible_posi))
    
    chosen_paris_posi_r = set(taken_posi) - set(chosen_sig_posi_r) - set(chosen_tri_posi_r)
    chosen_paris_posi_t = set(taken_posi) - set(chosen_sig_posi_t) - set(chosen_tri_posi_t)
    
    pairs_r = []
    pairs_t = []
    for central_posi, possible_posi in radial_dic.items():
        if central_posi in chosen_paris_posi_r:
            pairs_r.append(random.choice(possible_posi))
    for central_posi, possible_posi in tan_dic.items():
        if central_posi in chosen_paris_posi_t:
            pairs_t.append(random.choice(possible_posi))
    
    extra_posi_c_75pairs  = triplet_posi_c1 + triplet_posi_c2 + pairs_r
    extra_posi_nc_75pairs = triplet_posi_nc1 + triplet_posi_nc2 + pairs_t
    
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_c_75pairs, ka, kb)
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_nc_75pairs, ka, kb)
    
    ####50% paris
    
    if len(taken_posi) == 17:
        n_pairs,n_triplets,n_singel = 9, 4, 4
    elif len(taken_posi) == 18:
        n_pairs,n_triplets,n_singel = 8, 5, 5
    elif len(taken_posi) == 19:
        n_pairs,n_triplets,n_singel = 9, 5, 5
    elif len(taken_posi) == 20:
        n_pairs,n_triplets,n_singel = 10, 5, 5
    elif len(taken_posi) == 21:
        n_pairs,n_triplets,n_singel = 11, 5, 5
    elif len(taken_posi) == 22:
        n_pairs,n_triplets,n_singel = 12, 5, 5
    
    
    chosen_tri_posi_r = [] #choose some flowers to make triplets
    chosen_tri_posi_t = []
    chosen_sig_posi_r = [] #other flowers to have single disc
    chosen_sig_posi_t = []
    if n_triplets > len(commonkeys_r):
        return []
    for n in range(0, n_triplets):
        #radial
        random_key_r = random.choice(commonkeys_r_copy3)
        chosen_tri_posi_r.append(random_key_r)
        commonkeys_r_copy3.remove(random_key_r)
        #tan
        random_key_t = random.choice(commonkeys_t_copy3)
        chosen_tri_posi_t.append(random_key_t)
        commonkeys_t_copy3.remove(random_key_t)
        
    chosen_keys_r = list(set(taken_posi) - set(chosen_tri_posi_r))
    chosen_keys_t = list(set(taken_posi) - set(chosen_tri_posi_t))
    
    for n in range(0, n_singel):
        #radial
        random_key_r = random.choice(chosen_keys_r)
        chosen_sig_posi_r.append(random_key_r)
        chosen_keys_r.remove(random_key_r)
        #tan
        random_key_t = random.choice(chosen_keys_t)
        chosen_sig_posi_t.append(random_key_t)
        chosen_keys_t.remove(random_key_t)
    
    triplet_posi_c1 = []
    for central_posi, possible_posi in radial_dic_1_noempty.items():
        if central_posi in chosen_tri_posi_r:
            triplet_posi_c1.append(random.choice(possible_posi))
    
    triplet_posi_c2 = []
    for central_posi, possible_posi in radial_dic_2_noempty.items():
        if central_posi in chosen_tri_posi_r:
            triplet_posi_c2.append(random.choice(possible_posi))
    
    triplet_posi_nc1 = []
    for central_posi, possible_posi in tan_dic_1_noempty.items():
        if central_posi in chosen_tri_posi_t:
            triplet_posi_nc1.append(random.choice(possible_posi))
    
    triplet_posi_nc2 = []
    for central_posi, possible_posi in tan_dic_2_noempty.items():
        if central_posi in chosen_tri_posi_t:
            triplet_posi_nc2.append(random.choice(possible_posi))
    
    chosen_paris_posi_r = list(set(taken_posi) - set(chosen_sig_posi_r) - set(chosen_tri_posi_r))
    chosen_paris_posi_t = list(set(taken_posi) - set(chosen_sig_posi_t) - set(chosen_tri_posi_t))
    
    pairs_r = []
    pairs_t = []
    for central_posi, possible_posi in radial_dic.items():
        if central_posi in chosen_paris_posi_r:
            pairs_r.append(random.choice(possible_posi))
    for central_posi, possible_posi in tan_dic.items():
        if central_posi in chosen_paris_posi_t:
            pairs_t.append(random.choice(possible_posi))
    
    extra_posi_c_50pairs  = triplet_posi_c1 + triplet_posi_c2 + pairs_r
    extra_posi_nc_50pairs = triplet_posi_nc1 + triplet_posi_nc2 + pairs_t
    
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_c_50pairs, ka, kb)
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_nc_50pairs, ka, kb)
    
    ####25% paris
    if len(taken_posi) == 17:
        n_pairs,n_triplets,n_singel = 5, 6, 6
    elif len(taken_posi) == 18:
        n_pairs,n_triplets,n_singel = 6, 6, 6
    elif len(taken_posi) == 19:
        n_pairs,n_triplets,n_singel = 5, 7, 7
    elif len(taken_posi) == 20:
        n_pairs,n_triplets,n_singel = 6, 7, 7
    elif len(taken_posi) == 21:
        n_pairs,n_triplets,n_singel = 5, 8, 8
    elif len(taken_posi) == 22:
        n_pairs,n_triplets,n_singel = 6, 8, 8
    
    chosen_tri_posi_r = [] #choose some flowers to make triplets
    chosen_tri_posi_t = []
    chosen_sig_posi_r = [] #other flowers to have single disc
    chosen_sig_posi_t = []
    if n_triplets > len(commonkeys_r):
        return []
    for n in range(0, n_triplets):
        #radial
        random_key_r = random.choice(commonkeys_r_copy4)
        chosen_tri_posi_r.append(random_key_r)
        commonkeys_r_copy4.remove(random_key_r)
        #tan
        random_key_t = random.choice(commonkeys_t_copy4)
        chosen_tri_posi_t.append(random_key_t)
        commonkeys_t_copy4.remove(random_key_t)
    
    chosen_keys_r = list(set(taken_posi) - set(chosen_tri_posi_r))
    chosen_keys_t = list(set(taken_posi) - set(chosen_tri_posi_t))
    
    for n in range(0, n_singel):
        #radial
        random_key_r = random.choice(chosen_keys_r)
        chosen_sig_posi_r.append(random_key_r)
        chosen_keys_r.remove(random_key_r)
        #tan
        random_key_t = random.choice(chosen_keys_t)
        chosen_sig_posi_t.append(random_key_t)
        chosen_keys_t.remove(random_key_t)
    
    triplet_posi_c1 = []
    for central_posi, possible_posi in radial_dic_1_noempty.items():
        if central_posi in chosen_tri_posi_r:
            triplet_posi_c1.append(random.choice(possible_posi))
    
    triplet_posi_c2 = []
    for central_posi, possible_posi in radial_dic_2_noempty.items():
        if central_posi in chosen_tri_posi_r:
            triplet_posi_c2.append(random.choice(possible_posi))
    
    triplet_posi_nc1 = []
    for central_posi, possible_posi in tan_dic_1_noempty.items():
        if central_posi in chosen_tri_posi_t:
            triplet_posi_nc1.append(random.choice(possible_posi))
    
    triplet_posi_nc2 = []
    for central_posi, possible_posi in tan_dic_2_noempty.items():
        if central_posi in chosen_tri_posi_t:
            triplet_posi_nc2.append(random.choice(possible_posi))
    
    chosen_paris_posi_r = list(set(taken_posi) - set(chosen_sig_posi_r) - set(chosen_tri_posi_r))
    chosen_paris_posi_t = list(set(taken_posi) - set(chosen_sig_posi_t) - set(chosen_tri_posi_t))
    
    pairs_r = []
    pairs_t = []
    for central_posi, possible_posi in radial_dic.items():
        if central_posi in chosen_paris_posi_r:
            pairs_r.append(random.choice(possible_posi))
    for central_posi, possible_posi in tan_dic.items():
        if central_posi in chosen_paris_posi_t:
            pairs_t.append(random.choice(possible_posi))
    
    extra_posi_c_25pairs  = triplet_posi_c1 + triplet_posi_c2 + pairs_r
    extra_posi_nc_25pairs = triplet_posi_nc1 + triplet_posi_nc2 + pairs_t
    
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_c_25pairs, ka, kb)
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_nc_25pairs, ka, kb)
    # =============================================================================
    # to csv
    # =============================================================================
    fullPairs_c  = taken_posi + radial_posi
    fullPairs_nc = taken_posi + tan_posi
    pairs75_c    = taken_posi + extra_posi_c_75pairs
    pairs75_nc   = taken_posi + extra_posi_nc_75pairs
    pairs50_c    = taken_posi + extra_posi_c_50pairs
    pairs50_nc   = taken_posi + extra_posi_nc_50pairs
    pairs25_c    = taken_posi + extra_posi_c_25pairs
    pairs25_nc   = taken_posi + extra_posi_nc_25pairs
    noPair_c     = taken_posi + extra_posi_c_nopair
    noPair_nc    = taken_posi + extra_posi_nc_nopair
    
    csv_data_fullPairs_c  = [loop_number, len(taken_posi), len(radial_posi), taken_posi, radial_posi, fullPairs_c]
    csv_data_fullPairs_nc  = [loop_number, len(taken_posi), len(tan_posi), taken_posi, tan_posi, fullPairs_nc]
    csv_data_pairs75_c  = [loop_number, len(taken_posi), len(extra_posi_c_75pairs), taken_posi, extra_posi_c_75pairs, pairs75_c]
    csv_data_pairs75_nc  = [loop_number, len(taken_posi), len(extra_posi_nc_75pairs), taken_posi, extra_posi_nc_75pairs, pairs75_nc]
    csv_data_pairs50_c  = [loop_number, len(taken_posi), len(extra_posi_c_50pairs), taken_posi, extra_posi_c_50pairs, pairs50_c]
    csv_data_pairs50_nc  = [loop_number, len(taken_posi), len(extra_posi_nc_50pairs), taken_posi, extra_posi_nc_50pairs, pairs50_nc]
    csv_data_pairs25_c  = [loop_number, len(taken_posi), len(extra_posi_c_25pairs), taken_posi, extra_posi_c_25pairs, pairs25_c]
    csv_data_pairs25_nc  = [loop_number, len(taken_posi), len(extra_posi_nc_25pairs), taken_posi, extra_posi_nc_25pairs, pairs25_nc]
    csv_data_noPair_c  = [loop_number, len(taken_posi), len(extra_posi_c_nopair), taken_posi, extra_posi_c_nopair, noPair_c]
    csv_data_noPair_nc  = [loop_number, len(taken_posi), len(extra_posi_nc_nopair), taken_posi, extra_posi_nc_nopair, noPair_nc]
    
    with open('fullpairsc_ws_%s.csv' %(windowsize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data_fullPairs_c)
    
    with open('fullpairsnc_ws_%s.csv' %(windowsize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data_fullPairs_nc)
    
    with open('no_pairc_ws_%s.csv' %(windowsize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data_noPair_c)
    
    with open('no_pairnc_ws_%s.csv' %(windowsize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data_noPair_nc)
    
    with open('pairs75c_ws_%s.csv' %(windowsize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data_pairs75_c)
    
    with open('pairs75nc_ws_%s.csv' %(windowsize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data_pairs75_nc)
    
    with open('pairs50c_ws_%s.csv' %(windowsize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data_pairs50_c)
    
    with open('pairs50nc_ws_%s.csv' %(windowsize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data_pairs50_nc)
    
    with open('pairs25c_ws_%s.csv' %(windowsize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data_pairs25_c)
    
    with open('pairs25nc_ws_%s.csv' %(windowsize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data_pairs25_nc)
#runStimuliGeneration(windowsize=0.4, visualization = True, ka = 0.25, kb = 0.1,loop_number = 1)