# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:53:57 2020

@author: MiaoLi
"""
#%% =============================================================================
# import modules
# =============================================================================
#import numpy as np 
import random, csv, math
from math import atan2, pi, sin, cos
from scipy.spatial import distance, ConvexHull
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017454145014176
import VirtualEllipseFunc.m_defineEllipses
import VirtualEllipseFunc.m_drawEllipses
#from itertools import combinations
import matplotlib.pyplot as plt
#from shapely.geometry import Point, Polygon
#import copy
#from psychopy import core, monitors, visual
from matplotlib.patches import Ellipse
# =============================================================================
# used functions
# =============================================================================
def runStimuliGeneration(newWindowSize, visualization = True, ka = 29, kb = 29,loop_number = 1):
    def defineCircleRegion(coordinate, r):
        angle_rad = atan2(coordinate[1],coordinate[0])
        angle_radial = angle_rad*180/pi
        angle_tangential = angle_radial + 90
        V_circle = (coordinate[0],coordinate[1], r,r, angle_radial, angle_tangential)
        
        return V_circle
    def caclulateNewList_random(random_disk_coordinate, taken_list, positions,ka,kb): 
        # global positions
        # (新生成的随机点，已经保存的点坐标list) # new random disk corrdinate, previous disk corrdinates list
        '''
        This function generate the final list that contains a group of disks coordinate. 
        The newly selected disk position (with a virtual ellipse) will be inspected with all the exited virtual ellipses
        Only the one without intersection could be reutrned.
        '''
        virtual_e_2 = defineCircleRegion(random_disk_coordinate,ka)
        
        for_number = 0
        for exist_n in taken_list: 
            exist_e = defineCircleRegion(exist_n,ka) #perivous ellipses  
            for_number = for_number + 1
            ellipses = [exist_e, virtual_e_2]
            intersectionXList, intersectionYList = VirtualEllipseFunc.m_defineEllipses.ellipse_polyline_intersection_full(ellipses)
            if len(intersectionXList) > 0:
                positions.pop(-1)
                return [0] #breakout the function and  go into the while loop to delete this position
            else:
                continue
    
        taken_list.append(random_disk_coordinate)
        #delete the the current position from the list positions and the corrosponding ellipses points.
        positions.pop(-1)
        return taken_list  #final list of position I want
    
    # =============================================================================
    # generation
    # =============================================================================
#    newWindowSize = 0.6
#    visualization = True
#    ka = 29
#    kb = 29
#    loop_number = 1
#    percentage_extra = 1#How many disc to add
    r = 100 #The radius of protected fovea area
    
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
#        presentaiton_area = copy.deepcopy(positions)
        # only pre-selected number of ellipse cross will be generated
        
        
        #first random disk
        disk_posi = positions[-1] #random.choice(positions)
        positions.pop(-1)
        virtual_e1 = defineCircleRegion(disk_posi,ka)
        taken_posi = [disk_posi]
        #all other disks
    
        while_number = 0
        while len(positions) > 0: 
            disk_posi_new = positions[-1]
    #        print(disk_posi_new)
            print(while_number)
            new_list = caclulateNewList_random(disk_posi_new,taken_posi,positions,ka,kb)
            while_number = while_number + 1
        generation = False
    #    if len(taken_posi) == 60:
    #        generation = False
    csv_data  = [loop_number, len(taken_posi), taken_posi]
    with open('purerandom_ws_%s.csv' %(newWindowSize), 'a+', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_data)
    return taken_posi
#
#taken_posi = runStimuliGeneration(newWindowSize = 0.6, visualization = True, ka = 29, kb = 29,loop_number = 1)
#def drawEllipse (e_posi, ka, kb, crowding_cons, newWindowSize, loop_number): 
#    """
#    This function allows to draw more than one ellipse. The parameter is 
#    a list of coordinate (must contain at least two coordinates)
#    The direction of ellipses are only radial direction,
#    """
#    eccentricities = []
#    for i in range(len(e_posi)):
#        eccentricities0 = distance.euclidean(e_posi[i], (0,0))
#        eccentricities.append(eccentricities0)
#
#    angle_deg = []
#    for ang in range(len(e_posi)):
#        angle_rad0 = atan2(e_posi[ang][1],e_posi[ang][0])
#        angle_deg0 = angle_rad0*180/pi
#        angle_deg.append(angle_deg0)
##    https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.patches.Ellipse.html
#    my_e = [Ellipse(xy=e_posi[j], width=ka*2, height=kb*2, angle = angle_deg[j],color='red',fill=None)#color='red',fill=None
#            for j in range(len(e_posi))]
#    
#
#    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
#    for e in my_e:
#        ax.add_artist(e)
#        e.set_clip_box(ax.bbox)
#    for dot in e_posi:
#        plt.plot(dot[0],dot[1], color = 'k', marker ='o')
#        # plt.show()
#        # e.set_alpha(np.random.rand())
#        # e.set_facecolor(np.random.rand(3))
#    # ax.set_xlim([-800, 800])
#    # ax.set_ylim([-500, 500])
#    ax.set_xlim([-400, 400])
#    ax.set_ylim([-250, 250])
#    # ax.set_title('c_%s_wS_%s_eS_%s_%s_E_%s.png' %(crowding_cons,newWindowSize,ka,kb,len(e_posi)))
#    
#    #边框不可见
#    ax.spines['top'].set_visible(False)
#    ax.spines['right'].set_visible(False)
#    ax.spines['bottom'].set_visible(False)
#    ax.spines['left'].set_visible(False)
#    #坐标不可见
#    ax.axes.get_yaxis().set_visible(False)
#    ax.axes.get_xaxis().set_visible(False)
    

#drawEllipse(taken_posi, ka=0.25, kb = 0.1, crowding_cons = 2, newWindowSize = 0.6, loop_number =1)
#
#disk_radius = 3.82
#
## monitor specifications
#monsize = [1024, 768]
#fullscrn = False
#scr = 0
#mondist = 57
#monwidth = 41
#Agui = False
#monitorsetting = monitors.Monitor('miaoMonitor', width=monwidth, distance=mondist)
#monitorsetting.setSizePix(monsize)
#
## creat new window
#win = visual.Window(monitor=monitorsetting, size=monsize, screen=scr, units='pix', fullscr=fullscrn, allowGUI=Agui, color=[0 ,0 ,0])
#
## target disk
#trgt_disk = visual.Circle(win, radius = disk_radius, lineColor = "black", fillColor = "black")
#
#for posi in taken_posi:
#    trgt_disk.setPos(posi)
#    trgt_disk.draw()
#
## fixation 
#fixation = visual.TextStim(win, text= '+',bold = True, color=(-1.0, -1.0, -1.0))
#fixation.setPos([0,0])
#fixation.draw()
#
##draw a frame
#frameSize = [1450, 950]
#frame = visual.Rect(win,size = frameSize,units = 'pix')
#frame.draw()
#
#win.flip()
#
#win.getMovieFrame()
#win.saveMovieFrames('pureRandomc.png')
#win.close()