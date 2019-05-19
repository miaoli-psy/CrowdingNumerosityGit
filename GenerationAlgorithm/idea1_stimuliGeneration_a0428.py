# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:36:16 2018

@author: Miao
This scrip :
    #TODO
    
"""
import numpy as np 
import math, random, csv
from scipy.spatial import distance, ConvexHull
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017454145014176
import VirtualEllipseFunc.m_defineEllipses
import VirtualEllipseFunc.m_drawEllipses
from itertools import combinations

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
# Possible positions
# =============================================================================

# =============================================================================
# Some global variables (100pix = 3.75cm = 3.75 deg in this setting)
# =============================================================================
def runStimuliGeneration(crowding_cons, newWindowSize, visualization = False, ka = 0.25, kb = 0.1,loop_number = 1):
    
    if crowding_cons == 1:
        if ka > kb:
            tempk = ka
            ka = kb
            kb = tempk
    elif crowding_cons == 0:
        if ka < kb:
            tempk = ka
            ka = kb
            kb = tempk
    elif crowding_cons == 2:
        pass
    else:
        raise NameError ('crowding_cons should be 0,1 or 2 for no-crowding, crowding and references')
    
    
    #define a smaller visual window (presentation area)
    
    maxCorrdinate = max(VirtualEllipseFunc.m_defineEllipses.removefovelPositions())
    del_p2 = []
    positions = VirtualEllipseFunc.m_defineEllipses.removefovelPositions()
    tempList2 = positions.copy()
    for outPosi in positions:
        if abs(outPosi[0]) > maxCorrdinate[0]*newWindowSize or abs(outPosi[1]) > maxCorrdinate[1]*newWindowSize:
            del_p2.append(outPosi)
            try:
                tempList2.remove(outPosi)
            except ValueError:
                pass
    positions = tempList2
    
    random.shuffle(positions)
    
    # =============================================================================
    # Generate disks with corresponding virtual ellipses
    # =============================================================================
    
    #first random disk
    disk_posi = positions[-1] #random.choice(positions)
    positions.pop(-1)
    virtual_e1 = VirtualEllipseFunc.m_defineEllipses.defineVirtualEllipses(disk_posi,ka,kb)
    taken_posi = [disk_posi]
    #all other disks
    while_number = 0
    while len(positions) > 0: 
        disk_posi_new = positions[-1] 
        new_list = VirtualEllipseFunc.m_defineEllipses.caclulateNewList(disk_posi_new,taken_posi,positions,ka,kb)
        while_number = while_number + 1
    # print ("taken_list", taken_posi,"Numbers", len(taken_posi))
    
    # =============================================================================
    # stimuli properties
    # =============================================================================
    taken_posi_array = np.asarray(taken_posi)
    convexHull_t = ConvexHull(taken_posi_array)
    convexHull_perimeter = convexHull_t.area*(0.25/3.82)
    occupancyArea = convexHull_t.volume*(((0.25/3.82)**2))
    
    ListD = []
    for p in taken_posi:
        eD = distance.euclidean(p,(0,0))*(0.25/3.82)
        ListD.append(eD)
    averageE = round(sum(ListD)/len(taken_posi),2)
    # spacing 18.26	19.74
    distances =[distance.euclidean(p1,p2) for p1, p2 in combinations(taken_posi,2)]
    avg_spacing = round(sum(distances)/len(distances)*(0.25/3.82),2)
    
    # =============================================================================
    # write to csv
    # =============================================================================
    csv_data = [loop_number, len(taken_posi), taken_posi, convexHull_perimeter, averageE, avg_spacing, occupancyArea]
    with open('idea1_crowdingCons_%s_ws_%s.csv' %(crowding_cons, newWindowSize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data)

    # =============================================================================
    # Visualization
    # =============================================================================
    if visualization == True:
        '''see ellipses'''
        if crowding_cons == 1: #crowding = 1, nocrowding = 0
            drawER = VirtualEllipseFunc.m_drawEllipses.drawEllipseT(taken_posi, ka, kb, crowding_cons,newWindowSize, loop_number)
        else:
            drwaET = VirtualEllipseFunc.m_drawEllipses.drawEllipse(taken_posi, ka, kb, crowding_cons,newWindowSize, loop_number)
# runStimuliGeneration(1,2,0.3)