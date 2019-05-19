# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:15:33 2019
This function takes raw stimuli as input, and adds aggregateSurface and density coloums.
return info that needed in GenerateMatchedStimuli.py

@author: MiaoLi
"""
import pandas as pd
import ast
from scipy.spatial import ConvexHull
import numpy as np
from math import pi

# folderPath = '.\\folder_currentPath\\'
# folderPath = '..\\folder_beforePath\\'
# folderPath = '.\\InputRawStimuli\\'
folderPath = '..\\..\\Crowding_and_numerosity\\MatchingAlgorithm\\Idea1\\Stimuli190429\\InputRawStimuli\\'

def characterizeStimuli(ws , crowdingDis):
    if ws == 0.7:
        if crowdingDis == 0:
            file = folderPath + 'idea1_crowdingCons_0_ws_0.7.csv'
        elif crowdingDis == 1:
            file = folderPath + 'idea1_crowdingCons_1_ws_0.7.csv'
        else:
            raise ValueError('crowdingDis could be 0 (noCrowidng) or 1 (crowding)')
    elif ws == 0.6:
        if crowdingDis == 0:
            file = folderPath + 'idea1_crowdingCons_0_ws_0.6.csv'
        elif crowdingDis == 1:
            file = folderPath + 'idea1_crowdingCons_1_ws_0.6.csv'
        else:
            raise ValueError('crowdingDis could be 0 (noCrowidng) or 1 (crowding)')
    elif ws == 0.5:
        if crowdingDis == 0:
            file = folderPath + 'idea1_crowdingCons_0_ws_0.5.csv'
        elif crowdingDis == 1:
            file = folderPath + 'idea1_crowdingCons_1_ws_0.5.csv'
        else:
            raise ValueError('crowdingDis could be 0 (noCrowidng) or 1 (crowding)')
    elif ws == 0.4:
        if crowdingDis == 0:
            file = folderPath + 'idea1_crowdingCons_0_ws_0.4.csv'
        elif crowdingDis == 1:
            file = folderPath + 'idea1_crowdingCons_1_ws_0.4.csv'
        else:
            raise ValueError('crowdingDis could be 0 (noCrowidng) or 1 (crowding)')
    elif ws == 0.3:
        if crowdingDis == 0:
            file = folderPath + 'idea1_crowdingCons_0_ws_0.3.csv'
        elif crowdingDis == 1:
            file ='idea1_crowdingCons_1_ws_0.3.csv'
        else:
            raise ValueError('crowdingDis could be 0 (noCrowidng) or 1 (crowding)')
    else:
        raise ValueError('ws for idea1 are defined from 0.3 to 0.7')
    # file = folderPath + r'D:\MiaoProject\count\backup\SelectedStimuliInfo.xlsx'

    stimuliInfo_df=pd.read_csv(file,header = None)
    posi_lists_temp = stimuliInfo_df[2].tolist()

    # add meaningful names to existed colums
    name_list = list(range(0,stimuliInfo_df.shape[1]))
    name_list = [str(x) for x in name_list]
    name_list[0] = 'index_stimuliInfo'
    name_list[1] = 'N_disk'
    name_list[2] = 'positions'
    name_list[3] = 'convexHull'
    name_list[4] = 'averageE'
    name_list[5] = 'avg_spacing'
    name_list[6] = 'occupancyArea'
    stimuliInfo_df.columns = name_list
    stimuliInfo_df = stimuliInfo_df[['index_stimuliInfo','N_disk','positions', 'convexHull', 'averageE', 'avg_spacing','occupancyArea']]# Only these columns are useful 

    # df to list
    posi_list=[]
    for i in posi_lists_temp:
        i = ast.literal_eval(i)# megic! remore ' ' of the str
        posi_list.append(i)

    # =============================================================================
    # aggregate surface （所有disks的面积）
    # =============================================================================
    aggregateSurface = []
    for display in posi_list:
        aggregateSurface_t = len(display)*pi*(0.25**2)
        aggregateSurface.append(aggregateSurface_t)

    stimuliInfo_df['aggregateSurface'] = aggregateSurface
    # =============================================================================
    # density = aggregate surface / occupancy area
    # =============================================================================
    caculatedDensity = []
    for count, display in enumerate(posi_list):
        array = np.asarray(display)
        convexHullArea_t = ConvexHull(array).volume/(15.28**2)#caculate convexHull area- use .volume function
        density_t = round(aggregateSurface[count]/convexHullArea_t,5)
        caculatedDensity.append(density_t)

    stimuliInfo_df['density'] = caculatedDensity

    # stimuli properties
    stimuliInfo_pivotT= pd.pivot_table(stimuliInfo_df, values = ['convexHull', 'averageE', 'aggregateSurface','occupancyArea','avg_spacing','density'], columns = ['N_disk'])
    
    #distribution N_disk
    N_disk_dist = stimuliInfo_df.groupby('N_disk').size()

    return [N_disk_dist, stimuliInfo_pivotT, 
            round(np.std(stimuliInfo_df['density']),5), 
            round(np.std(stimuliInfo_df['averageE']),5), 
            round(np.std(stimuliInfo_df['avg_spacing']),5),
            round(np.std(stimuliInfo_df['convexHull']),5),
            round(np.std(stimuliInfo_df['occupancyArea']),5)]



