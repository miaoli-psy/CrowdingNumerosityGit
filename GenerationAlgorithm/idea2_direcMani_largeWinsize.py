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
from psychopy import core, monitors, visual
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


#first random disk
    disk_posi = positions[-1] #random.choice(positions)
    positions.pop(-1)
    virtual_e1 = VirtualEllipseFunc.m_defineEllipses.defineVirtualEllipses(disk_posi,ka,kb)
    taken_posi = [disk_posi]
    #all other disks
    while_number = 0
    while len(positions) > 0: 
        disk_posi_new = positions[-1]
        print(while_number)
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
#Add extra disks to non-overlap areas
finalE = [] #all ellipses that have been drawn
for new_posi in taken_posi:
    finalE0 =  VirtualEllipseFunc.m_defineEllipses.defineVirtualEllipses(new_posi,ka,kb)
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

####0% paris
radial_dic_copy = copy.deepcopy(radial_dic) 
tan_dic_copy    = copy.deepcopy(tan_dic)

chosen_posi_r = [] #choose some flowers to make triplets
chosen_posi_t = [] 

#calculate ingtigrate times:
if len(taken_posi)%2 == 0:
    N = round(len(taken_posi)/2)
else:
    N = round(len(taken_posi)/2)-1

for n in range(0, N):
    #radial
    random_key_r = random.choice(commonkeys_r_copy1)
    chosen_posi_r.append(random_key_r)
    commonkeys_r_copy1.remove(random_key_r)
    #tan
    random_key_t = random.choice(commonkeys_t_copy1)
    chosen_posi_t.append(random_key_t)
    commonkeys_t_copy1.remove(random_key_t)

triplet_posi_c1 = []
for central_posi, possible_posi in radial_dic_1_noempty.items():
    if central_posi in chosen_posi_r:
        triplet_posi_c1.append(random.choice(possible_posi))

triplet_posi_c2 = []
for central_posi, possible_posi in radial_dic_2_noempty.items():
    if central_posi in chosen_posi_r:
        triplet_posi_c2.append(random.choice(possible_posi))

triplet_posi_nc1 = []
for central_posi, possible_posi in tan_dic_1_noempty.items():
    if central_posi in chosen_posi_t:
        triplet_posi_nc1.append(random.choice(possible_posi))

triplet_posi_nc2 = []
for central_posi, possible_posi in tan_dic_2_noempty.items():
    if central_posi in chosen_posi_t:
        triplet_posi_nc2.append(random.choice(possible_posi))
#check if the number of ellipse cross is even or odd
if len(taken_posi)%2 == 0:
    extra_posi_c_nopair  = triplet_posi_c1+triplet_posi_c2
    extra_posi_nc_nopair = triplet_posi_nc1+triplet_posi_nc2
else:
    #there will be an ellipse cross contains a pair of discs
    f_key_r = random.choice(commonkeys_r_copy1)
    f_posi_r = [random.choice(radial_dic[f_key_r])]
    
    f_key_t = random.choice(commonkeys_t_copy1)
    f_posi_t = [random.choice(radial_dic[f_key_t])]
    
    extra_posi_c_nopair  = triplet_posi_c1+triplet_posi_c2 + f_posi_r
    extra_posi_nc_nopair = triplet_posi_nc1+triplet_posi_nc2 + f_posi_t

VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_c_nopair, ka, kb)
VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_nc_nopair, ka, kb)

####75% paris
if len(taken_posi) == 29:
    n_pairs,n_triplets,n_singel = 21, 4, 4
elif len(taken_posi) == 30:
    n_pairs,n_triplets,n_singel = 22, 4, 4
elif len(taken_posi) == 31:
    n_pairs,n_triplets,n_singel = 21, 5, 5
elif len(taken_posi) == 32:
    n_pairs,n_triplets,n_singel = 24, 4, 4
elif len(taken_posi) == 33:
    n_pairs,n_triplets,n_singel = 25, 4, 4
elif len(taken_posi) == 34:
    n_pairs,n_triplets,n_singel = 24, 5, 5

chosen_tri_posi_r = [] #choose some flowers to make triplets
chosen_tri_posi_t = []
chosen_sig_posi_r = [] #other flowers to have single disc
chosen_sig_posi_t = []

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
if len(taken_posi) == 29:
    n_pairs,n_triplets,n_singel = 15, 7, 7
elif len(taken_posi) == 30:
    n_pairs,n_triplets,n_singel = 16, 7, 7
elif len(taken_posi) == 31:
    n_pairs,n_triplets,n_singel = 15, 8, 8
elif len(taken_posi) == 32:
    n_pairs,n_triplets,n_singel = 16, 8, 8
elif len(taken_posi) == 33:
    n_pairs,n_triplets,n_singel = 17, 8, 8
elif len(taken_posi) == 34:
    n_pairs,n_triplets,n_singel = 16, 9, 9

chosen_tri_posi_r = [] #choose some flowers to make triplets
chosen_tri_posi_t = []
chosen_sig_posi_r = [] #other flowers to have single disc
chosen_sig_posi_t = []

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
if len(taken_posi) == 29:
    n_pairs,n_triplets,n_singel = 7, 11, 11
elif len(taken_posi) == 30:
    n_pairs,n_triplets,n_singel = 8, 11, 11
elif len(taken_posi) == 31:
    n_pairs,n_triplets,n_singel = 7, 12, 12
elif len(taken_posi) == 32:
    n_pairs,n_triplets,n_singel = 8, 12, 12
elif len(taken_posi) == 33:
    n_pairs,n_triplets,n_singel = 9, 12, 12
elif len(taken_posi) == 34:
    n_pairs,n_triplets,n_singel = 8, 13, 13

chosen_tri_posi_r = [] #choose some flowers to make triplets
chosen_tri_posi_t = []
chosen_sig_posi_r = [] #other flowers to have single disc
chosen_sig_posi_t = []

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
#%% =============================================================================
# psychopy display
# =============================================================================

fullPairs_c  = taken_posi + radial_posi
fullPairs_nc = taken_posi + tan_posi
pairs75_c    = taken_posi + extra_posi_c_75pairs
pairs75_nc   = taken_posi + extra_posi_nc_75pairs
pairs50_c    = taken_posi + extra_posi_c_50pairs
pairs50_nc   = taken_posi + extra_posi_nc_50pairs
pairs25_c    = taken_posi + extra_posi_c_25pairs
pairs25_nc   = taken_posi + extra_posi_nc_25pairs
noPair       = taken_posi + extra_posi_c_nopair
noPair       = taken_posi + extra_posi_nc_nopair
D = {'fullPairs_c': taken_posi + radial_posi,
     'fullPairs_nc': taken_posi + tan_posi,
     'pairs75_c' :taken_posi + extra_posi_c_75pairs,
     'pairs75_nc':taken_posi + extra_posi_nc_75pairs,
     'pairs50_c' :taken_posi + extra_posi_c_50pairs,
     'pairs50_nc':taken_posi + extra_posi_nc_50pairs,
     'pairs25_c' :taken_posi + extra_posi_c_25pairs,
     'pairs25_nc':taken_posi + extra_posi_nc_25pairs,
     'noPair_c'  :taken_posi + extra_posi_c_nopair,
     'noPair_nc' :taken_posi + extra_posi_nc_nopair}

disk_radius = 3.82

# monitor specifications
monsize = [1024, 768]
fullscrn = False
scr = 0
mondist = 57
monwidth = 41
Agui = False
monitorsetting = monitors.Monitor('miaoMonitor', width=monwidth, distance=mondist)
monitorsetting.setSizePix(monsize)

# creat new window
win = visual.Window(monitor=monitorsetting, size=monsize, screen=scr, units='pix', fullscr=fullscrn, allowGUI=Agui, color=[0 ,0 ,0])

# target disk
trgt_disk = visual.Circle(win, radius = disk_radius, lineColor = "black", fillColor = "black")

for posi in D['noPair_nc']:
    trgt_disk.setPos(posi)
    trgt_disk.draw()

# fixation 
fixation = visual.TextStim(win, text= '+',bold = True, color=(-1.0, -1.0, -1.0))
fixation.setPos([0,0])
fixation.draw()

#draw a frame
frameSize = [1450, 950]
frame = visual.Rect(win,size = frameSize,units = 'pix')
frame.draw()

win.flip()

win.getMovieFrame()
win.saveMovieFrames('display_noPair_nc.png')
win.close()
