# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:36:16 2018

@author: Miao
This scrip :
    #TODO
    
"""
#%% =============================================================================
# import modules
# =============================================================================
import numpy as np 
import random, csv, math
from math import pi
from scipy.spatial import distance, ConvexHull
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017454145014176
import VirtualEllipseFunc.m_defineEllipses
import VirtualEllipseFunc.m_drawEllipses
from itertools import combinations
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
import copy

#%% =============================================================================
# Run multiple times with os
# =============================================================================
# try:
#     _, loop_number = sys.argv
# except Exception as e:
#     pass
#     #print('Usage: python loop_times')
#     #sys.exit(0)
#%% =============================================================================
# Some global variables (100pix = 3.75cm = 3.75 deg in this setting)
# =============================================================================
percentage_extra = 1#How many disc to add
r = 100 #The radius of protected fovea area
#%% =============================================================================
# some functions
# =============================================================================
def get_display_properties(displayPositions):
    displayPositions_array = np.asarray(displayPositions)
    convexHull_t = ConvexHull(displayPositions_array)
    convexHull_perimeter = round(convexHull_t.area*(0.25/3.82),2)
    occupancyArea = round(convexHull_t.volume*(((0.25/3.82)**2)),2)
    
    ListD = []
    for p in displayPositions:
        eD = distance.euclidean(p,(0,0))*(0.25/3.82)
        ListD.append(eD)
    averageE = round(sum(ListD)/len(displayPositions),2)
    # spacing 18.26	19.74
    distances =[distance.euclidean(p1,p2) for p1, p2 in combinations(displayPositions,2)]
    avg_spacing_c = round(sum(distances)/len(distances)*(0.25/3.82),2)
    
    return convexHull_perimeter, occupancyArea, averageE, avg_spacing_c
#%% =============================================================================
# Stimuli generation
# =============================================================================
# def runStimuliGeneration(newWindowSize, visualization = True, ka = 0.25, kb = 0.1,loop_number = 1):
newWindowSize = 0.6
visualization = True
ka = 0.25
kb = 0.1
loop_number = 1


grid_dimention_x = 101
grid_dimention_y = 75
linelength = 10
start_x = -0.5*linelength*grid_dimention_x + 0.5*linelength
start_y = -0.5*linelength*grid_dimention_y + 0.5*linelength

generation = True
while generation == True:
    positions =[]
    for x_count in range(0, grid_dimention_x):
        new_x = start_x + x_count*linelength
        for y_count in range(0, grid_dimention_y):
            new_y = start_y + y_count*linelength
            positions.append((new_x, new_y))
    
    '''(0, 0) should not be in the positions list'''
    try:
        positions.remove((0,0))
    except ValueError:
        pass
    
    ''' Define and remove a fovea area (a circle) of r == ??'''
    del_p = []
    tempList = positions.copy()
    for tempP in positions:
        if math.sqrt((tempP[0]**2) + (tempP[1]**2)) < r:
            del_p.append(tempP)
            try:
                tempList.remove(tempP)
            except ValueError:
                pass
    positions = tempList
    
    '''define a smaller visual window (presentation area)'''
    maxCorrdinate = max(positions)
    del_p2 = []
    tempList2 = positions.copy()
    for outPosi in positions:
        if abs(outPosi[0]) > maxCorrdinate[0]*newWindowSize or abs(outPosi[1]) > maxCorrdinate[1]*newWindowSize:
            del_p2.append(outPosi)
            try:
                tempList2.remove(outPosi)
            except ValueError:
                pass
    positions = tempList2
    # positions_copy = copy.deepcopy(positions)
    random.shuffle(positions)
    
    # presentaion area - winthin the winsize, no foveal
    presentaiton_area = copy.deepcopy(positions)
# only pre-selected number of ellipse cross will be generated

#first random disk
    disk_posi = positions[-1] #random.choice(positions)
    positions.pop(-1)
    virtual_e1 = VirtualEllipseFunc.m_defineEllipses.defineVirtualEllipses(disk_posi,ka,kb)
    taken_posi = [disk_posi]
    #all other disks
    while_number = 0
    while len(positions) > 0: 
        disk_posi_new = positions[-1] 
        new_list = VirtualEllipseFunc.m_defineEllipses.caclulateNewList_2direction(disk_posi_new,taken_posi,positions,ka,kb)
        while_number = while_number + 1
    # print ("taken_list", taken_posi,"Numbers", len(taken_posi))
    
    if newWindowSize == 0.6:
        if len(taken_posi)> 34 or len(taken_posi) < 29:
            generation = True
        else:
            generation =False
    if newWindowSize == 0.3:
        if len(taken_posi)> 16 or len(taken_posi) < 11:
            generation = True
        else:
            generation =False
    if newWindowSize == 0.4:
        if len(taken_posi)> 22 or len(taken_posi) < 17:
            generation = True
        else:
            generation =False
#Add extra disks to non-overlap areas
finalE = [] #all ellipses that have been drawn
for new_posi in taken_posi:
    finalE0 =  VirtualEllipseFunc.m_defineEllipses.defineVirtualEllipses(new_posi,0.5,0.2)
    finalE.append(finalE0)
    
#remove overlapping area
del_p3 =[]
tempTemplist = presentaiton_area.copy() #full list that removes the foveal area
for i in finalE:
    tempER = VirtualEllipseFunc.m_defineEllipses.ellipseToPolygon([i])[0]
    tempERpolygon = Polygon(tempER)
    tempET = VirtualEllipseFunc.m_defineEllipses.ellipseToPolygon([i])[1]
    tempETpolygon = Polygon(tempET)
    for tempP in tempList:
        if tempERpolygon.contains(Point(tempP)) == True and tempETpolygon.contains(Point(tempP)) == True:
            del_p3.append(tempP)
            try:
                tempTemplist.remove(tempP)
            except ValueError:
                pass
tempListF= tempTemplist # all position positions to add extra disks + area outside ellipse-cross
presentaiton_area2 = copy.deepcopy(tempListF) # all position positions to add extra disks + area outside ellipse-cross

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

    for posi in tempListF:
        if epPolygon.contains(Point(posi)):
            if distance.euclidean(taken_posi[count-1], (0,0)) > distance.euclidean(posi, (0,0)): # close to foveal
                radial_dic_1[(i[0], i[1])].append(posi)
            else: #away from foveal (take this)
                radial_dic_2[(i[0],i[1])].append(posi)
                
            tempListF.remove(posi)
        elif epPolygonT.contains(Point(posi)):
            tan_dic[(i[0],i[1])].append(posi) #all disks in tangential area within ellipse cross
            
            tempListF.remove(posi)
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

presentaiton_area3 = copy.deepcopy(tempListF) # positions outside ellipse cross

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

####100% paris
radial_posi_100p = []
tan_posi_100p    = []
for central_posi, possible_posi in radial_dic.items():
    radial_posi_100p.append(random.choice(possible_posi))
for central_posi, possible_posi in tan_dic.items():
    tan_posi_100p.append(random.choice(possible_posi))

VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, radial_posi_100p, ka, kb)
VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, tan_posi_100p, ka, kb)

####75% paris
if newWindowSize == 0.6:
    if len(taken_posi) == 29:
        n_pairs75,n_triplets75,n_singe75 = 21, 4, 4
    elif len(taken_posi) == 30:
        n_pairs75,n_triplets75,n_singe75 = 22, 4, 4
    elif len(taken_posi) == 31:
        n_pairs75,n_triplets75,n_singe75 = 21, 5, 5
    elif len(taken_posi) == 32:
        n_pairs75,n_triplets75,n_singe75 = 24, 4, 4
    elif len(taken_posi) == 33:
        n_pairs75,n_triplets75,n_singe75 = 25, 4, 4
    elif len(taken_posi) == 34:
        n_pairs75,n_triplets75,n_singe75 = 24, 5, 5

if newWindowSize == 0.3:
    if len(taken_posi) == 11:
        n_pairs75,n_triplets75,n_singe75 = 9, 1, 1
    elif len(taken_posi) == 12:
        n_pairs75,n_triplets75,n_singe75 = 8, 2, 2
    elif len(taken_posi) == 13:
        n_pairs75,n_triplets75,n_singe75 = 9, 2, 2
    elif len(taken_posi) == 14:
        n_pairs75,n_triplets75,n_singe75 = 10, 2, 2
    elif len(taken_posi) == 15:
        n_pairs75,n_triplets75,n_singe75 = 11, 2, 2
    elif len(taken_posi) == 16:
        n_pairs75,n_triplets75,n_singe75 = 12, 2, 2

if newWindowSize == 0.4:
    if len(taken_posi) == 17:
        n_pairs75,n_triplets75,n_singe75 = 13, 2, 2
    elif len(taken_posi) == 18:
        n_pairs75,n_triplets75,n_singe75 = 14, 2, 2
    elif len(taken_posi) == 19:
        n_pairs75,n_triplets75,n_singe75 = 15, 2, 2
    elif len(taken_posi) == 20:
        n_pairs75,n_triplets75,n_singe75 = 16, 2, 2
    elif len(taken_posi) == 21:
        n_pairs75,n_triplets75,n_singe75 = 15, 3, 3
    elif len(taken_posi) == 22:
        n_pairs75,n_triplets75,n_singe75 = 16, 3, 3
chosen_tri_posi_r = [] #choose some flowers to make triplets
chosen_tri_posi_t = []
chosen_sig_posi_r = [] #other flowers to have single disc
chosen_sig_posi_t = []

for n in range(0, n_triplets75):
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

for n in range(0, n_singe75):
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
if newWindowSize == 0.6:
    if len(taken_posi) == 29:
        n_pairs50,n_triplets50,n_singe50 = 15, 7, 7
    elif len(taken_posi) == 30:
        n_pairs50,n_triplets50,n_singe50 = 16, 7, 7
    elif len(taken_posi) == 31:
        n_pairs50,n_triplets50,n_singe50 = 15, 8, 8
    elif len(taken_posi) == 32:
        n_pairs50,n_triplets50,n_singe50 = 16, 8, 8
    elif len(taken_posi) == 33:
        n_pairs50,n_triplets50,n_singe50 = 17, 8, 8
    elif len(taken_posi) == 34:
        n_pairs50,n_triplets50,n_singe50 = 16, 9, 9

if newWindowSize == 0.3:
    if len(taken_posi) == 13:
        n_pairs50,n_triplets50,n_singe50 = 7, 3, 3
    elif len(taken_posi) == 14:
        n_pairs50,n_triplets50,n_singe50 = 8, 3, 3
    elif len(taken_posi) == 15:
        n_pairs50,n_triplets50,n_singe50 = 7, 4, 4
    elif len(taken_posi) == 16:
        n_pairs50,n_triplets50,n_singe50 = 8, 4, 4
    elif len(taken_posi) == 11:
        n_pairs50,n_triplets50,n_singe50 = 5, 3, 3
    elif len(taken_posi) == 12:
        n_pairs50,n_triplets50,n_singe50 = 6, 3, 3

if newWindowSize == 0.4:
    if len(taken_posi) == 17:
        n_pairs50,n_triplets50,n_singe50 = 9, 4, 4
    elif len(taken_posi) == 18:
        n_pairs50,n_triplets50,n_singe50 = 10, 4, 4
    elif len(taken_posi) == 19:
        n_pairs50,n_triplets50,n_singe50 = 9, 5, 5
    elif len(taken_posi) == 20:
        n_pairs50,n_triplets50,n_singe50 = 10, 5, 5
    elif len(taken_posi) == 21:
        n_pairs50,n_triplets50,n_singe50 = 11, 5, 5
    elif len(taken_posi) == 22:
        n_pairs50,n_triplets50,n_singe50 = 12, 5, 5
chosen_tri_posi_r = [] #choose some flowers to make triplets
chosen_tri_posi_t = []
chosen_sig_posi_r = [] #other flowers to have single disc
chosen_sig_posi_t = []

for n in range(0, n_triplets50):
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

for n in range(0, n_singe50):
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
if newWindowSize == 0.6:
    if len(taken_posi) == 29:
        n_pairs25,n_triplets25,n_singe25 = 7, 11, 11
    elif len(taken_posi) == 30:
        n_pairs25,n_triplets25,n_singe25 = 8, 11, 11
    elif len(taken_posi) == 31:
        n_pairs25,n_triplets25,n_singe25 = 7, 12, 12
    elif len(taken_posi) == 32:
        n_pairs25,n_triplets25,n_singe25 = 8, 12, 12
    elif len(taken_posi) == 33:
        n_pairs25,n_triplets25,n_singe25 = 9, 12, 12
    elif len(taken_posi) == 34:
        n_pairs25,n_triplets25,n_singe25 = 8, 13, 13

if newWindowSize == 0.3:
    if len(taken_posi) == 11:
        n_pairs25,n_triplets25,n_singe25 = 3, 4, 4
    elif len(taken_posi) == 12:
        n_pairs25,n_triplets25,n_singe25 = 4, 4, 4
    elif len(taken_posi) == 13:
        n_pairs25,n_triplets25,n_singe25 = 3, 5, 5
    elif len(taken_posi) == 14:
        n_pairs25,n_triplets25,n_singe25 = 4, 5, 5
    elif len(taken_posi) == 15:
        n_pairs25,n_triplets25,n_singe25 = 3, 6, 6
    elif len(taken_posi) == 16:
        n_pairs25,n_triplets25,n_singe25 = 4, 6, 6

if newWindowSize == 0.4:
    if len(taken_posi) == 17:
        n_pairs25,n_triplets25,n_singe25 = 5, 6, 6
    elif len(taken_posi) == 18:
        n_pairs25,n_triplets25,n_singe25 = 4, 7, 7
    elif len(taken_posi) == 19:
        n_pairs25,n_triplets25,n_singe25 = 5, 7, 7
    elif len(taken_posi) == 20:
        n_pairs25,n_triplets25,n_singe25 = 6, 7, 7
    elif len(taken_posi) == 21:
        n_pairs25,n_triplets25,n_singe25 = 5, 8, 8
    elif len(taken_posi) == 22:
        n_pairs25,n_triplets25,n_singe25 = 6, 8, 8
chosen_tri_posi_r = [] #choose some flowers to make triplets
chosen_tri_posi_t = []
chosen_sig_posi_r = [] #other flowers to have single disc
chosen_sig_posi_t = []

for n in range(0, n_triplets25):
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

for n in range(0, n_singe25):
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

####0% paris
if newWindowSize == 0.6:
    if len(taken_posi) == 29:
        n_pairs0,n_triplets0,n_singe0 = 1, 14, 14
    elif len(taken_posi) == 30:
        n_pairs0,n_triplets0,n_singe0 = 0, 15, 15
    elif len(taken_posi) == 31:
        n_pairs0,n_triplets0,n_singe0 = 1, 15, 15
    elif len(taken_posi) == 32:
        n_pairs0,n_triplets0,n_singe0 = 0, 16, 16
    elif len(taken_posi) == 33:
        n_pairs0,n_triplets0,n_singe0 = 1, 16, 16
    elif len(taken_posi) == 34:
        n_pairs0,n_triplets0,n_singe0 = 0, 17, 17
if newWindowSize == 0.3:
    if len(taken_posi) == 11:
        n_pairs0,n_triplets0,n_singe0 = 1, 5, 5
    elif len(taken_posi) == 12:
        n_pairs0,n_triplets0,n_singe0 = 0, 6, 6
    elif len(taken_posi) == 13:
        n_pairs0,n_triplets0,n_singe0 = 1, 6, 6
    elif len(taken_posi) == 14:
        n_pairs0,n_triplets0,n_singe0 = 0, 7, 7
    elif len(taken_posi) == 15:
        n_pairs0,n_triplets0,n_singe0 = 1, 7, 7
    elif len(taken_posi) == 16:
        n_pairs0,n_triplets0,n_singe0 = 0, 8, 8
if newWindowSize == 0.4:
    if len(taken_posi) == 17:
        n_pairs0,n_triplets0,n_singe0 = 1, 8, 8
    elif len(taken_posi) == 18:
        n_pairs0,n_triplets0,n_singe0 = 0, 9, 9
    elif len(taken_posi) == 19:
        n_pairs0,n_triplets0,n_singe0 = 1, 9, 9
    elif len(taken_posi) == 20:
        n_pairs0,n_triplets0,n_singe0 = 0, 10, 10
    elif len(taken_posi) == 21:
        n_pairs0,n_triplets0,n_singe0 = 1, 10,10
    elif len(taken_posi) == 22:
        n_pairs0,n_triplets0,n_singe0 = 0, 11, 11

chosen_tri_posi_r = [] #choose some flowers to make triplets
chosen_tri_posi_t = []
chosen_sig_posi_r = [] #other flowers to have single disc
chosen_sig_posi_t = []

for n in range(0, n_triplets0):
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

for n in range(0, n_singe0):
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

extra_posi_c_0pair  = triplet_posi_c1 + triplet_posi_c2 + pairs_r
extra_posi_nc_0pair = triplet_posi_nc1 + triplet_posi_nc2 + pairs_t

VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_c_0pair, ka, kb)
VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_nc_0pair, ka, kb)

#%% =============================================================================
# stimuli properties
# =============================================================================

#100% pairs
properties_fullpairs_c  = get_display_properties(taken_posi+radial_posi_100p)
properties_fullpairs_nc = get_display_properties(taken_posi+tan_posi_100p)

#0% pair
properties_0pair_c  = get_display_properties(taken_posi+extra_posi_c_0pair)
properties_0pair_nc = get_display_properties(taken_posi+extra_posi_nc_0pair)

#75% pairs
properties_75pairs_c  = get_display_properties(taken_posi+extra_posi_c_75pairs)
properties_75pairs_nc = get_display_properties(taken_posi+extra_posi_nc_75pairs)

#50% paris
properties_50pairs_c  = get_display_properties(taken_posi+extra_posi_c_50pairs)
properties_50pairs_nc = get_display_properties(taken_posi+extra_posi_nc_50pairs)

#25% paris
properties_25pairs_c  = get_display_properties(taken_posi+extra_posi_c_25pairs)
properties_25pairs_nc = get_display_properties(taken_posi+extra_posi_nc_25pairs)
# =============================================================================
# write to csv
# =============================================================================


csv_data_fullpairs_c   = [loop_number, len(taken_posi), len(radial_posi_100p), taken_posi,\
                          radial_posi_100p, properties_fullpairs_c[0], properties_fullpairs_c[1],\
                          properties_fullpairs_c[2], properties_fullpairs_c[3],\
                          len(taken_posi), 0, 0]
csv_data_fullpairs_nc  = [loop_number, len(taken_posi), len(tan_posi_100p), taken_posi,\
                          tan_posi_100p, properties_fullpairs_nc[0], properties_fullpairs_nc[1],\
                          properties_fullpairs_nc[2], properties_fullpairs_nc[3],\
                          len(taken_posi), 0, 0]

csv_data_0pair_c   = [loop_number, len(taken_posi), len(extra_posi_c_0pair), taken_posi,\
                          extra_posi_c_0pair, properties_0pair_c[0], properties_0pair_c[1],\
                          properties_0pair_c[2], properties_0pair_c[3],\
                          n_pairs0,n_triplets0,n_singe0]
csv_data_0pair_nc  = [loop_number, len(taken_posi), len(extra_posi_nc_0pair), taken_posi,\
                          extra_posi_nc_0pair, properties_0pair_nc[0], properties_0pair_nc[1],\
                          properties_0pair_nc[2], properties_0pair_nc[3],\
                          n_pairs0,n_triplets0,n_singe0]

csv_data_75pairs_c   = [loop_number, len(taken_posi), len(extra_posi_c_75pairs), taken_posi,\
                          extra_posi_c_75pairs, properties_75pairs_c[0], properties_75pairs_c[1],\
                          properties_75pairs_c[2], properties_75pairs_c[3],\
                          n_pairs75,n_triplets75,n_singe75]
csv_data_75pairs_nc  = [loop_number, len(taken_posi), len(extra_posi_nc_75pairs), taken_posi,\
                          extra_posi_nc_75pairs, properties_75pairs_nc[0], properties_75pairs_nc[1],\
                          properties_75pairs_nc[2], properties_75pairs_nc[3],\
                          n_pairs75,n_triplets75,n_singe75]


csv_data_50pairs_c   = [loop_number, len(taken_posi), len(extra_posi_c_50pairs), taken_posi,\
                          extra_posi_c_50pairs, properties_50pairs_c[0], properties_50pairs_c[1],\
                          properties_50pairs_c[2], properties_50pairs_c[3],\
                          n_pairs50,n_triplets50,n_singe50]
csv_data_50pairs_nc  = [loop_number, len(taken_posi), len(extra_posi_nc_50pairs), taken_posi,\
                          extra_posi_nc_50pairs, properties_50pairs_nc[0], properties_50pairs_nc[1],\
                          properties_50pairs_nc[2], properties_50pairs_nc[3],\
                          n_pairs50,n_triplets50,n_singe50]

csv_data_25pairs_c   = [loop_number, len(taken_posi), len(extra_posi_c_25pairs), taken_posi,\
                          extra_posi_c_25pairs, properties_25pairs_c[0], properties_25pairs_c[1],\
                          properties_25pairs_c[2], properties_25pairs_c[3],\
                          n_pairs25,n_triplets25,n_singe25]
csv_data_25pairs_nc  = [loop_number, len(taken_posi), len(extra_posi_nc_25pairs), taken_posi,\
                          extra_posi_nc_25pairs, properties_25pairs_nc[0], properties_25pairs_nc[1],\
                          properties_25pairs_nc[2], properties_25pairs_nc[3],\
                          n_pairs25,n_triplets25,n_singe25]

with open('fullpairsc_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_data_fullpairs_c)

with open('fullpairsnc_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_data_fullpairs_nc)

with open('no_pairc_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_data_0pair_c)

with open('no_pairnc_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_data_0pair_nc)

with open('pairs75c_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_data_75pairs_c)

with open('pairs75nc_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_data_75pairs_nc)

with open('pairs50c_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_data_50pairs_c)

with open('pairs50nc_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_data_50pairs_nc)

with open('pairs25c_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_data_25pairs_c)

with open('pairs25nc_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_data_25pairs_nc)

#%% =============================================================================
# Run
# =============================================================================
# runStimuliGeneration(newWindowSize = 0.6, visualization = True, ka = 0.25, kb = 0.1,loop_number = 1)

#%% =============================================================================
# show psychoPy sample display
# =============================================================================
