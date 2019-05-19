# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:33:13 2019

@author: MiaoLi
"""
import pandas as pd
import os
from psychopy import core, monitors, visual
import ast
# =============================================================================
# path selected stimuli
# =============================================================================
folderPath = '..\\..\\Crowding_and_numerosity\\MatchingAlgorithm\\Idea1\\Stimuli190429\\selectedMatchedStimuli\\'
# folderPath = ''

# =============================================================================
# read selected stimuli
# =============================================================================
stimuliInfo_df=pd.read_excel(folderPath + 'Idea1_DESCO.xlsx')

#jiamian
# stimuliInfo_df = pd.read_excel( 'Idea1_DESCO.xlsx')

# reset index
stimuliInfo_df.reset_index(drop=True, inplace=True)
# stimuliInfo_dict = stimuliInfo_df.to_dict()

combine_dic = {}
combine_list = []
for index, row in stimuliInfo_df.iterrows():
    combine_dic[index] = [row['index_stimuliInfo'],row['N_disk'],row['winsize'],row['crowdingcons']]
    combine_list.append([row['index_stimuliInfo'],row['N_disk'],row['winsize'],row['crowdingcons']])

stimuliInfo_df['combine'] = combine_list

# df to list
posi_lists_temp = stimuliInfo_df['positions'].tolist()
posi_list=[]
for i in posi_lists_temp:
    i = ast.literal_eval(i)# megic! remore ' ' of the str
    posi_list.append(i)

# =============================================================================
# PsychoPy
# =============================================================================

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

# add a white frame

def generatePsychopyDis(displayN):
    for i in range(len(posi_list[displayN])):
          trgt_disk.setPos(posi_list[displayN][i]) 
          trgt_disk.draw()
    # fixation 
    fixation = visual.TextStim(win, text= '+',bold = True, color=(-1.0, -1.0, -1.0))
    fixation.setPos([0,0])
    fixation.draw()
    # win.flip()

    frame = visual.Rect(win,size = frameSize,units = 'pix') #window size 0.8
    frame.draw()
    win.flip()
    
    #保存一帧屏幕
    win.getMovieFrame()
    win.saveMovieFrames('ws%s_crowding%s_n%s_Ndisk%s.png' %(combine_list[displayN][2], combine_list[displayN][3], combine_list[displayN][0], combine_list[displayN][1]))
    # win.close()

for n in range(0,len(posi_lists_temp)):
    if combine_list[n][2] == 0.7:
        frameSize = [1650,1100]
    elif combine_list[n][2] == 0.6:
        frameSize = [1450,950]
    elif combine_list[n][2] == 0.5:
        frameSize = [1300,850]
    elif combine_list[n][2] == 0.4:
        frameSize = [1150, 750]
    elif combine_list[n][2] == 0.3:
        frameSize = [850,550]
    generatePsychopyDis(n)

win.close()