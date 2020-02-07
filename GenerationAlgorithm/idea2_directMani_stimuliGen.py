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
    new_list = VirtualEllipseFunc.m_defineEllipses.caclulateNewList_2direction(disk_posi_new,taken_posi,positions,ka,kb)
    while_number = while_number + 1
# print ("taken_list", taken_posi,"Numbers", len(taken_posi))

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

# #try
# for i in presentaiton_area:
#     plt.plot(i[0],i[1],'ko')
    
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

#%% =============================================================================
# display type
# =============================================================================
## crowding pairs

#display1 100% crowding pairs
radial_posi = []
tan_posi = []
for central_posi, possible_posi in radial_dic.items():
    radial_posi.append(random.choice(possible_posi))
#display2 100% no-crowding paris
for central_posi, possible_posi in tan_dic.items():
    tan_posi.append(random.choice(possible_posi))

## 1 vs 3

#display3 100%: take out all additional discs, and place them as triplets
radial_dic_copy = copy.deepcopy(radial_dic)
tan_dic_copy    = copy.deepcopy(tan_dic)

chosen_posi_r = [] #choose some flowers to make triplets
chosen_posi_t = [] 

#calculate ingtigrate times:
if len(taken_posi)%2 == 0:
    N = round(len(taken_posi)/2)
else:
    N = round(len(taken_posi)/2)-1

commonkeys_r_copy = copy.deepcopy(commonkeys_r)
commonkeys_t_copy = copy.deepcopy(commonkeys_t)
for n in range(0, N):
    #radial
    random_key_r = random.choice(commonkeys_r_copy)
    chosen_posi_r.append(random_key_r)
    commonkeys_r_copy.remove(random_key_r)
    #tan
    random_key_t = random.choice(commonkeys_t_copy)
    chosen_posi_t.append(random_key_t)
    commonkeys_t_copy.remove(random_key_t)

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
    extra_posi_c  = triplet_posi_c1+triplet_posi_c2
    extra_posi_nc = triplet_posi_nc1+triplet_posi_nc2

    # for i in taken_posi+triplet_posi_c1+triplet_posi_c2:
    #     plt.plot(i[0],i[1],'ko')
    # for i in taken_posi+triplet_posi_nc1+triplet_posi_nc2:
    #     plt.plot(i[0],i[1],'ko')
    # len(taken_posi+triplet_posi_c1+triplet_posi_c2)
else:
    #there will be an ellipse cross contains a pair of discs
    f_key_r = random.choice(commonkeys_r_copy)
    f_posi_r = [random.choice(radial_dic[f_key_r])]
    
    f_key_t = random.choice(commonkeys_t_copy)
    f_posi_t = [random.choice(radial_dic[f_key_t])]
    
    extra_posi_c  = triplet_posi_c1+triplet_posi_c2 + f_posi_r
    extra_posi_nc = triplet_posi_nc1+triplet_posi_nc2 + f_posi_t

    # for i in taken_posi+triplet_posi_c1+triplet_posi_c2+f_posi:
    #     plt.plot(i[0],i[1],'ko')
    # len(taken_posi+triplet_posi_c1+triplet_posi_c2+f_posi_r)

VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_c, ka, kb)
VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, extra_posi_nc, ka, kb)

#%% =============================================================================
# other conditions-to reduce clustering
# =============================================================================

# =============================================================================
# stimuli properties
# =============================================================================
#crowding
taken_posi_c = taken_posi+f_extraP_radial
taken_posi_array_c = np.asarray(taken_posi_c)
convexHull_t_c = ConvexHull(taken_posi_array_c)
convexHull_perimeter_c = convexHull_t_c.area*(0.25/3.82)
occupancyArea_c = convexHull_t_c.volume*(((0.25/3.82)**2))

ListD_c = []
for p in taken_posi_c:
    eD = distance.euclidean(p,(0,0))*(0.25/3.82)
    ListD_c.append(eD)
averageE_c = round(sum(ListD_c)/len(taken_posi_c),2)
# spacing 18.26	19.74
distances_c =[distance.euclidean(p1,p2) for p1, p2 in combinations(taken_posi_c,2)]
avg_spacing_c = round(sum(distances_c)/len(distances_c)*(0.25/3.82),2)


#no-crowding
taken_posi_nc = taken_posi+f_extraP_tan
taken_posi_array_nc = np.asarray(taken_posi_nc)
convexHull_t_nc = ConvexHull(taken_posi_array_nc)
convexHull_perimeter_nc = convexHull_t_nc.area*(0.25/3.82)
occupancyArea_nc = convexHull_t_nc.volume*(((0.25/3.82)**2))

ListD_nc = []
for p in taken_posi_nc:
    eD = distance.euclidean(p,(0,0))*(0.25/3.82)
    ListD_nc.append(eD)
averageE_nc = round(sum(ListD_nc)/len(taken_posi_nc),2)
# spacing 18.26	19.74
distances_nc =[distance.euclidean(p1,p2) for p1, p2 in combinations(taken_posi_nc,2)]
avg_spacing_nc = round(sum(distances_nc)/len(distances_nc)*(0.25/3.82),2)

# =============================================================================
# write to csv
# =============================================================================
csv_data_crowding   = [loop_number, len(taken_posi_c), len(taken_posi), len(f_extraP_radial), taken_posi_c,convexHull_perimeter_c, averageE_c, avg_spacing_c, occupancyArea_c]
csv_data_nocrowding = [loop_number, len(taken_posi_nc), len(taken_posi), len(f_extraP_tan), taken_posi_nc,convexHull_perimeter_nc, averageE_nc, avg_spacing_nc, occupancyArea_nc]
with open('idea2_crowding_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_data_crowding)

with open('idea2_nocrowding_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_data_nocrowding)
# =============================================================================
# Visualization
# =============================================================================
if visualization == True:
    #crowding
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, f_extraP_radial, ka, kb)
    #no-crowding
    VirtualEllipseFunc.m_drawEllipses.drawEllipse_full(taken_posi, f_extraP_tan, ka, kb)
#%% =============================================================================
# Run
# =============================================================================
# runStimuliGeneration(newWindowSize = 0.6, visualization = True, ka = 0.25, kb = 0.1,loop_number = 1)

#%% =============================================================================
# show psychoPy sample display
# =============================================================================
