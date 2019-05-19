# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:50:59 2019
This script characterize the selcted stimuli

@author: MiaoLi
"""
import pandas as pd
import os

# =============================================================================
# input-the selected stimuli
# =============================================================================
# folderpath = '.\\selectedMatchedStimuli\\'
folderpath = '..\\..\\Crowding_and_numerosity\\MatchingAlgorithm\\Idea1\\Stimuli190429\\selectedMatchedStimuli\\'
stimuliInfo_df=pd.read_excel(folderpath + 'Idea1_DESCO.xlsx',index_col=0)

# =============================================================================
# output-pivot table for the selected stimuli per property
# =============================================================================
stimuliInfo_pivotT= pd.pivot_table(stimuliInfo_df, index = ['crowdingcons'], 
                                                   values = ['convexHull','density','averageE', 'aggregateSurface','occupancyArea','avg_spacing'],
                                                   columns = ['winsize', 'N_disk'])

# =============================================================================
# output path and creat the output folder
# =============================================================================
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

createFolder(folderpath)

stimuliInfo_pivotT.to_excel(folderpath + 'finalSelectedStimuliProperties_pivotT.xlsx')