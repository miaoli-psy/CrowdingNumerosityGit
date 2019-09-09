# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:36:16 2018

@author: Miao
This scrip :
    #TODO
    
"""
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

# =============================================================================
# Run multiple times with os
# =============================================================================
# try:
#     _, loop_number = sys.argv
# except Exception as e:
#     pass
#     #print('Usage: python loop_times')
#     #sys.exit(0)
# =============================================================================
# Some global variables (100pix = 3.75cm = 3.75 deg in this setting)
# =============================================================================
percentage_extra = 1#How many disc to add
r = 100 #The radius of protected fovea area

def runStimuliGeneration(newWindowSize, visualization = False, ka = 0.25, kb = 0.1,loop_number = 1):

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
    positions_copy = positions
    random.shuffle(positions)
    
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
    tempTemplist = tempList.copy() #full list that removes the foveal area
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
    tempListF= tempTemplist # all position positions to add extra disks

    radial_dic_1 = {} #extra positions: radial and tangential direction
    radial_dic_2 = {} 
    
    # for each disc position, take the radial area (away from foveal as base)
    for count, i in enumerate(finalE, start = 1):
        ellipsePolygon = VirtualEllipseFunc.m_defineEllipses.ellipseToPolygon([i])[0] #radial ellipse
        # ellipsePolygonT = ellipseToPolygon([i])[1]#tangential ellipse
        epPolygon = Polygon(ellipsePolygon)
        # epPolygonT = Polygon(ellipsePolygonT)
        radial_dic_1[(i[0],i[1])] = [] #set the keys of the dictionary--taken_posi
        radial_dic_2[(i[0],i[1])] = []
        # tan_dic[(i[0],i[1])] = []
        for posi in tempListF:
            if epPolygon.contains(Point(posi)):
                if distance.euclidean(taken_posi[count-1], (0,0)) > distance.euclidean(posi, (0,0)): # close to foveal (we dont use it cause the position might fall into the foveal protected area)
                    radial_dic_1[(i[0], i[1])].append(posi)
                else: #away from foveal (take this)
                    radial_dic_2[(i[0],i[1])].append(posi)
    
    # rotate pi/2, pi, 1.5pi to get the other possible positions in other 3 areas
    radial_dic_1_new = {}
    tan_dic_1 = {} 
    tan_dic_2 = {} 
    for centralPosi, possiblePois in radial_dic_2.items():
        # print(centralPosi,possiblePois)
        radial_dic_1_new[centralPosi] = []
        tan_dic_1[centralPosi] =[]
        tan_dic_2[centralPosi] =[]
        for p in possiblePois:
            p_radial1 = VirtualEllipseFunc.m_defineEllipses.rotateposi(centralPosi, p, theta = pi)
            p_tan1 = VirtualEllipseFunc.m_defineEllipses.rotateposi(centralPosi, p, theta = pi/2)
            p_tan2 = VirtualEllipseFunc.m_defineEllipses.rotateposi(centralPosi, p, theta = 1.5*pi)
            radial_dic_1_new[centralPosi].append(p_radial1)
            tan_dic_1[centralPosi].append(p_tan1)
            tan_dic_2[centralPosi].append(p_tan2)
    
    # random chose to add raidal disc to close to foveal or away to foveal area
    radial_choice = random.choice([1, 2])
    extraP_radial = []
    if radial_choice == 1: #add the extra disc close to foveal
        for centralPosi, extra_posi in radial_dic_1_new.items():
            chose_extra = random.choice(extra_posi)
            extraP_radial.append(chose_extra)
    else: #radial_choice == 2:
        for centralPosi, extra_posi in radial_dic_2.items():
            chose_extra = random.choice(extra_posi)
            extraP_radial.append(chose_extra)
    
    # random chose to add tangential disc
    tan_choice = random.choice([3, 4])
    extraP_tan = []
    if tan_choice == 3:
        for centralPosi_t, extra_posi_t in tan_dic_1.items():
            chose_extra_t = random.choice(extra_posi_t)
            extraP_tan.append(chose_extra_t)
    else:
        for centralPosi_t, extra_posi_t in tan_dic_2.items():
            chose_extra_t = random.choice(extra_posi_t)
            extraP_tan.append(chose_extra_t)
    
    # sometimes you don't want to add all extra posi
    random.shuffle(extraP_radial)
    random.shuffle(extraP_tan)
    
    n_remove = round((1-percentage_extra)*len(extraP_radial))
    f_extraP_radial = extraP_radial[: len(extraP_radial)-n_remove]
    f_extraP_tan = extraP_tan[: len(extraP_tan)-n_remove]
    
    
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
    with open('idea1_crowding_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data_crowding)

    with open('idea1_nocrowding_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data_nocrowding)

# runStimuliGeneration(newWindowSize = 0.3, visualization = True, ka = 0.25, kb = 0.1,loop_number = 1)

