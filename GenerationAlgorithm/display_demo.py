# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:54:41 2020

@author: Miao
"""

# =============================================================================
# import modules
# =============================================================================
import numpy as np 
import random, csv, math
from math import atan2, pi
from scipy.spatial import distance, ConvexHull
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017454145014176
import VirtualEllipseFunc.m_defineEllipses
import VirtualEllipseFunc.m_drawEllipses
from itertools import combinations
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
import copy
from matplotlib.patches import Ellipse

# =============================================================================
#positions 
# =============================================================================
centerposi = [(140.0, -150.0), (60.0, 170.0), (260.0, -110.0), (-140.0, 120.0), (170.0, -40.0), (-180.0, -160.0), (-250.0, 160.0), (140.0, 20.0), (170.0, 180.0), (-260.0, 30.0), (-60.0, 80.0), (-60.0, 160.0), (240.0, 30.0), (0.0, -170.0), (-100.0, -20.0), (110.0, -50.0), (140.0, 100.0), (-140.0, -80.0), (290.0, 140.0), (50.0, -130.0), (-150.0, 0.0), (-300.0, -110.0), (-90.0, -150.0), (0.0, 110.0), (-80.0, -80.0), (70.0, -80.0), (-110.0, 40.0), (80.0, 60.0), (-140.0, 220.0), (80.0, -220.0), (0.0, -100.0), (60.0, 100.0), (0.0, 220.0)]

## 100 paris
extra_c = [(170.0, -160.0), (50.0, 150.0), (280.0, -140.0), (-110.0, 90.0), (190.0, -30.0), (-210.0, -180.0), (-210.0, 150.0), (110.0, 20.0), (140.0, 160.0), (-230.0, 40.0), (-70.0, 100.0), (-70.0, 190.0), (200.0, 30.0), (10.0, -190.0), (-120.0, -20.0), (100.0, -40.0), (110.0, 80.0), (-110.0, -70.0), (250.0, 140.0), (60.0, -160.0), (-130.0, 10.0), (-270.0, -80.0), (-70.0, -140.0), (0.0, 130.0), (-90.0, -100.0), (80.0, -100.0), (-100.0, 30.0), (100.0, 70.0), (-110.0, 190.0), (80.0, -190.0), (0.0, -120.0), (70.0, 120.0), (10.0, 180.0)]
extra_nc = [(120.0, -180.0), (20.0, 180.0), (270.0, -50.0), (-150.0, 90.0), (170.0, -10.0), (-200.0, -140.0), (-220.0, 190.0), (130.0, 40.0), (180.0, 150.0), (-260.0, 60.0), (-80.0, 70.0), (-90.0, 150.0), (240.0, 0.0), (-20.0, -180.0), (-100.0, -40.0), (120.0, -30.0), (160.0, 70.0), (-160.0, -60.0), (260.0, 200.0), (30.0, -140.0), (-140.0, -20.0), (-300.0, -70.0), (-100.0, -130.0), (-20.0, 110.0), (-70.0, -100.0), (60.0, -90.0), (-120.0, 20.0), (90.0, 50.0), (-170.0, 180.0), (130.0, -200.0), (-10.0, -100.0), (80.0, 90.0), (30.0, 220.0)]

## 50% pairs
extra_c_50p = [(150.0, -30.0), (-140.0, -130.0), (150.0, 150.0), (-230.0, 20.0), (-50.0, 140.0), (110.0, 80.0), (-110.0, -60.0), (-70.0, -140.0), (190.0, -30.0), (-210.0, -200.0), (200.0, 210.0), (-290.0, 40.0), (-70.0, 180.0), (170.0, 120.0), (-160.0, -100.0), (-110.0, -160.0), (80.0, 200.0), (290.0, -130.0), (-130.0, 100.0), (-290.0, 180.0), (-70.0, 100.0), (0.0, -130.0), (240.0, 140.0), (50.0, -110.0), (-240.0, -80.0), (0.0, 130.0), (-100.0, -90.0), (-130.0, 50.0), (90.0, 70.0), (-110.0, 170.0), (90.0, -190.0), (0.0, -120.0), (70.0, 120.0)]
extra_nc_50p = [(170.0, -140.0), (-170.0, 100.0), (-80.0, 160.0), (-90.0, -30.0), (-70.0, -90.0), (-120.0, 30.0), (70.0, 80.0), (50.0, 110.0), (110.0, -170.0), (-110.0, 150.0), (-30.0, 180.0), (-100.0, 0.0), (-90.0, -70.0), (-100.0, 60.0), (90.0, 40.0), (80.0, 90.0), (80.0, 160.0), (160.0, -60.0), (-270.0, 120.0), (130.0, 50.0), (210.0, 140.0), (-250.0, -20.0), (-80.0, 70.0), (150.0, 70.0), (-160.0, -60.0), (270.0, 180.0), (70.0, -130.0), (-150.0, 30.0), (-270.0, -150.0), (-120.0, -130.0), (20.0, 110.0), (-20.0, -100.0), (-30.0, 210.0)]

## 0% pair
extra_c_0p = [(130.0, -120.0), (200.0, -90.0), (-120.0, 100.0), (150.0, -50.0), (-170.0, -130.0), (120.0, 20.0), (130.0, 140.0), (-50.0, 140.0), (10.0, -150.0), (120.0, 90.0), (-120.0, -80.0), (50.0, -110.0), (-130.0, 0.0), (-70.0, -120.0), (-100.0, 30.0), (50.0, 90.0), (150.0, -170.0), (290.0, -120.0), (-160.0, 150.0), (200.0, -50.0), (-210.0, -190.0), (160.0, 20.0), (210.0, 220.0), (-80.0, 170.0), (0.0, -190.0), (160.0, 110.0), (-160.0, -100.0), (60.0, -160.0), (-170.0, 0.0), (-110.0, -160.0), (-130.0, 40.0), (70.0, 120.0), (-70.0, 100.0)]
extra_nc_0p = [(170.0, -140.0), (-170.0, 100.0), (-80.0, 160.0), (-90.0, -30.0), (-70.0, -90.0), (-120.0, 30.0), (70.0, 80.0), (50.0, 110.0), (110.0, -170.0), (-110.0, 150.0), (-30.0, 180.0), (-100.0, 0.0), (-90.0, -70.0), (-100.0, 60.0), (90.0, 40.0), (80.0, 90.0), (80.0, 160.0), (160.0, -60.0), (-270.0, 120.0), (130.0, 50.0), (210.0, 140.0), (-250.0, -20.0), (-80.0, 70.0), (150.0, 70.0), (-160.0, -60.0), (270.0, 180.0), (70.0, -130.0), (-150.0, 30.0), (-270.0, -150.0), (-120.0, -130.0), (20.0, 110.0), (-20.0, -100.0), (-30.0, 210.0)]


# =============================================================================
# draw ellipse
# =============================================================================
def drawEllipse_full(e_posi, extra_posi, ka, kb,ellipseColor_r = 'orangered', ellipseColor_t = 'lime'):
        """
        This function allows to draw more than one ellipse. The parameter is 
        a list of coordinate (must contain at least two coordinates)
        The radial and tangential ellipses for the same coordinates are drawn.
        """
        eccentricities = []
        for i in range(len(e_posi)):
            eccentricities0 = distance.euclidean(e_posi[i], (0,0))
            eccentricities.append(eccentricities0)
        #radial
        angle_deg = []
        for ang in range(len(e_posi)):
            angle_rad0 = atan2(e_posi[ang][1],e_posi[ang][0])
            angle_deg0 = angle_rad0*180/pi
            angle_deg.append(angle_deg0)
        my_e = [Ellipse(xy=e_posi[j], width=eccentricities[j]*ka*2, height=eccentricities[j]*kb*2, angle = angle_deg[j])
                for j in range(len(e_posi))]
        
        #tangential
        angle_deg2 = []
        for ang in range(len(e_posi)):
            angle_rad0_2 = atan2(e_posi[ang][1],e_posi[ang][0])
            angle_deg0_2 = angle_rad0_2*180/pi + 90
            angle_deg2.append(angle_deg0_2)
        my_e2 = [Ellipse(xy=e_posi[j], width=eccentricities[j]*ka*2, height=eccentricities[j]*kb*2, angle = angle_deg[j]+90)
                for j in range(len(e_posi))]
        
        fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
        for e in my_e:
            ax.add_artist(e)
            e.set_clip_box(ax.bbox)
            e.set_alpha(0.5)
            e.set_facecolor(ellipseColor_r)
        for e2 in my_e2:
            ax.add_artist(e2)
            e2.set_clip_box(ax.bbox)
            e2.set_alpha(0.5)
            e2.set_facecolor(ellipseColor_t)
        
        #show the discs on the ellipses-flower
        for dot in e_posi:
            plt.plot(dot[0],dot[1], color = 'k', marker ='o')
        # plt.show()
        for dot1 in extra_posi:
            plt.plot(dot1[0],dot1[1],color = 'r', marker = 'o')
        # plt.show()
        # ax.set_xlim([-800, 800])
        # ax.set_ylim([-500, 500])
        ax.set_xlim([-400, 400])
        ax.set_ylim([-260, 260])
        # ax.set_title('wS_%s_eS_%s_%s_E.png' %(newWindowSize,ka,kb))
        
        #边框不可见
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        #坐标不可见
        ax.axes.get_yaxis().set_visible(False)
        ax.axes.get_xaxis().set_visible(False)
        plt.show()
        
        try:
            loop_number
        except NameError:
            var_exists = False
        else:
            var_exists = True
            # plt.savefig('%s_wS_%s_eS_%s_%s_E.png' %(loop_number,newWindowSize,ka,kb))

drawEllipse_full(centerposi, [], 0.25, 0.1)
drawEllipse_full(centerposi, extra_c, 0.25, 0.1)
drawEllipse_full(centerposi, extra_nc, 0.25, 0.1)
drawEllipse_full(centerposi, extra_c_50p, 0.25, 0.1)
drawEllipse_full(centerposi, extra_nc_50p, 0.25, 0.1)
drawEllipse_full(centerposi, extra_c_0p, 0.25, 0.1)
drawEllipse_full(centerposi, extra_nc_0p, 0.25, 0.1)
