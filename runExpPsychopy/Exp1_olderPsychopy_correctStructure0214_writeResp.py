#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on February 14, 2019, at 13:04
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""
#relative files (condition files and stimuli pictures, in C:\Users\MiaoLi\Desktop\SCALab\Programming\Crowding_and_numerosity\setupExp_psychopy\Psychopybuilder\Crowding\Miao_exp_lilleLab\Exp1_short_olderPsychopy)
from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound, monitors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Crwdng_Nmrsty_older_runOnLab1'  # from the Builder filename that created this script
expInfo = {u'handedness': ['Right handed', 'Left handed'], 
           u'participant': u'',
           u'age': u'', 
           u'blockOrder': u'', 
           u'sex': ['Female','Male'], 
           u'group': ['1','2']}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data_Crwdng_Nmrsty1/group_%s_participant_%s_date_%s' % (expInfo['group'], expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
#win = visual.Window(
#    size=(1024, 768), fullscr=True, screen=0,
#    allowGUI=False, allowStencil=False,
#    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
#    blendMode='avg', useFBO=True)
myMonitor= monitors.Monitor('CRT_Lille', width = 57, distance = 40.5)#TODO
myMonitor.setSizePix([1024, 768])
win = visual.Window(monitor=myMonitor, 
                    size = [1024, 768], 
                    screen =1, 
                    units='pix', 
                    fullscr = False, 
                    allowGUI = False, 
                    winType = 'pyglet', 
                    color = (0,0,0))

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 100.0  # could not measure, so guess

#print(expInfo['frameRate'])

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()


# Initialize components for Routine "fixation"
fixationClock = core.Clock()


# Initialize components for Routine "practice"
practiceClock = core.Clock()
p_img = visual.ImageStim(
    win=win, name='p_img',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "endP"
endPClock = core.Clock()


# Initialize components for Routine "instr2"
instr2Clock = core.Clock()


# Initialize components for Routine "fixation"
fixationClock = core.Clock()


# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "break_3"
break_3Clock = core.Clock()


# Initialize components for Routine "thanks"
thanksClock = core.Clock()


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
instr1Components = []
for thisComponent in instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr1"-------
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    message1 = visual.TextStim(win, pos=[0,+30],units = 'pix')
    message1.setText('Welcome to our experiment.')
    message2 = visual.TextStim(win, pos=[0, 0],units = 'pix')
    message2.setText('Please give your best esimation.')
    message3 = visual.TextStim(win, pos=[0, -30], units = 'pix')
    message3.setText('Hit spacebar to start practice.')
    message1.draw()
    message2.draw()
    message3.draw()
    win.flip()
    event.waitKeys(keyList = ['space'])
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
p_trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='p_trials')
thisExp.addLoop(p_trials)  # add the loop to the experiment
thisP_trial = p_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisP_trial.rgb)
if thisP_trial != None:
    for paramName in thisP_trial.keys():
        exec(paramName + '= thisP_trial.' + paramName)

for thisP_trial in p_trials:
    currentLoop = p_trials
    # abbreviate parameter names if possible (e.g. rgb = thisP_trial.rgb)
    if thisP_trial != None:
        for paramName in thisP_trial.keys():
            exec(paramName + '= thisP_trial.' + paramName)
    
    # ------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    # keep track of which components have finished
    fixationComponents = []
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation"-------
    while continueRoutine:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        fixation = visual.TextStim(win, color = (-1, -1, -1), bold = True, units = 'pix')
        fixation.setText('+')
        fixation.draw()
        win.flip()
        event.waitKeys(keyList = ['space'])
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practice"-------
    t = 0
    practiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    p_img.setImage(u'2_c_2_f_100_wS_0.4_eS_0.15811388300841897_0.15811388300841897_33.png')
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    practiceComponents = [p_img, key_resp_2]
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice"-------
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_img* updates
        if t >= 0.0 and p_img.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_img.tStart = t
            p_img.frameNStart = frameN  # exact frame index
            p_img.setAutoDraw(True)
        frameRemains = 0.0 + 0.15- win.monitorFramePeriod * 0.75  # most of one frame period left
        if p_img.status == STARTED and t >= frameRemains:
            p_img.setAutoDraw(False)
        
        # *key_resp_2* updates
        if t >= 0.15 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
#            theseKeys = event.getKeys()
            ptext = visual.TextStim(win, pos = [0, 0])
            # theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            theseKeysP = event.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0','return', 'backspace','num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9','num_0'])
            
            # check for quit:
            if "escape" in theseKeysP:
                endExpNow = True
            if len(theseKeysP) > 0:  # at least one key was pressed
                if "backspace" in theseKeysP:
                    key_resp_2.keys=key_resp_2.keys[:-1]
            
                key_resp_2.keys.extend([key for key in theseKeysP if key != "return" and key != "backspace"])
                for n, i in enumerate(key_resp_2.keys):
                    if i =='num_1':
                        key_resp_2.keys[n] = '1'
                    elif i =='num_2':
                        key_resp_2.keys[n] = '2'
                    elif i =='num_3':
                        key_resp_2.keys[n] = '3'
                    elif i =='num_4':
                        key_resp_2.keys[n] = '4' 
                    elif i =='num_5':
                        key_resp_2.keys[n] = '5'
                    elif i =='num_6':
                        key_resp_2.keys[n] = '6'
                    elif i =='num_7':
                        key_resp_2.keys[n] = '7'
                    elif i =='num_8':
                        key_resp_2.keys[n] = '8'
                    elif i =='num_9':
                        key_resp_2.keys[n] = '9'
                    elif i =='num_0':
                        key_resp_2.keys[n] = '0'
                # Atext.setText("".join(key_resp_3.keys))
                
                # convert the list of strings into a single string
                key_str2 = "".join(key_resp_2.keys)
                ptext.setText(key_str2)
                ptext.draw()
                win.flip()
                # # event.waitKeys(5,keyList = ['return'])
                core.wait(0.5)
                
                if len(key_str2) !=0:
                # then convert the string to a number
                    key_num2 = int(key_str2)
            
            if "return" in theseKeysP:
                # ptext.setText('')
                # ptext.draw()
                # win.flip()
                # core.wait(0.5)
                continueRoutine=False
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    p_trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        p_trials.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'p_trials'


# ------Prepare to start Routine "endP"-------
t = 0
endPClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
endPComponents = []
for thisComponent in endPComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "endP"-------
while continueRoutine:
    # get current time
    t = endPClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    end_practice1 = visual.TextStim(win, pos=[0,+35],units = 'pix')
    end_practice1.setText('This is the end of practice')
    end_practice2 = visual.TextStim(win, pos=[0, 0], units = 'pix')
    end_practice2.setText('There are 10 blocks of the real experiment, you will see 3 reference images before each block.')
    end_practice3 = visual.TextStim(win, pos=[0, -35], units = 'pix')
    end_practice3.setText('Hit spacebar to start the real experiment.')
    end_practice1.draw()
    end_practice2.draw()
    end_practice3.draw()
    win.flip()
    event.waitKeys(keyList = ['space'])
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endPComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endP"-------
for thisComponent in endPComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "endP" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("blockOrder"+expInfo['blockOrder']+".csv"),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    
    # ------Prepare to start Routine "instr2"-------
    t = 0
    instr2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    # keep track of which components have finished
    instr2Components = []
    for thisComponent in instr2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instr2"-------
    while continueRoutine:
        # get current time
        t = instr2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        fix = visual.TextStim(win, pos = [0, 0], bold = True, units = 'pix')
        block_text = visual.TextStim(win, pos=[0, 0], units = 'pix')
        block_text.setText('Fixate to the center of screen and press spacebar to see the reference display.')
        block_text.draw()
        win.flip()
        event.waitKeys(keyList = ['space'])
        
        fix.setText('+')
        fix.setColor(u'black')
        fix.draw()
        win.flip()
        event.waitKeys(keyList = ['space'])
        
        image_ref = visual.ImageStim(win, image = ref_image1, units = 'pix')
        image_ref.draw()
        win.flip()
        core.wait(0.15)
        
        
        image_ref_text = visual.TextStim(win, pos=[0, 15], units ='pix')
        image_ref_text2 = visual.TextStim(win, pos=[0, -15], units = 'pix')
        image_ref_text3 = visual.TextStim(win, pos=[0, 0], units = 'pix')
        image_ref_text.setText('The number of the reference disks is %s:' %(int(Number1)))
        image_ref_text2.setText('Press C to continue')
        image_ref_text.draw()
        image_ref_text2.draw()
        win.flip()
        event.waitKeys(keyList = ['c'])
        # image_ref_text2.setText(Number1)
        image_ref_text3.setText('Fixate to the center and press spacebar to see another reference display.')
        # image_ref_text.draw()
        # image_ref_text2.draw()
        image_ref_text3.draw()
        win.flip()
        event.waitKeys(keyList = ['space'])
        # block_text.setText('+')
        # block_text.setColor(u'black')
        # block_text.draw()
        fix.draw()
        win.flip()
        event.waitKeys(keyList = ['space'])
        
        
        image_ref2 = visual.ImageStim(win, image = ref_image2, units = 'pix')
        image_ref.draw()
        win.flip()
        core.wait(0.15)
        
        
        image_ref_text.setText('The number of the reference disks is %s:' %(int(Number2)))
        # image_ref_text2.setText(Number2)
        # image_ref_text2.setText('Press spacebar to continue')
        image_ref_text.draw()
        image_ref_text2.draw()
        win.flip()
        event.waitKeys(keyList = ['c'])
        
        image_ref_text3.draw()
        win.flip()
        event.waitKeys(keyList = ['space'])
        
        fix.draw()
        win.flip()
        event.waitKeys(keyList = ['space'])
        
        image_ref3 = visual.ImageStim(win, image = ref_image3, units = 'pix')
        image_ref3.draw()
        win.flip()
        core.wait(0.15)
        
        image_ref_text.setText('The number of the reference disks is %s:' %(int(Number3)))
        image_ref_text.draw()
        image_ref_text2.draw()
        win.flip()
        event.waitKeys(keyList = ['c'])
        
        image_ref_text3.setText('Press spacebar to start the real experiment.')
        image_ref_text3.draw()
        win.flip()
        event.waitKeys(keyList = ['space'])
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr2"-------
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(winsize),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        # ------Prepare to start Routine "fixation"-------
        t = 0
        fixationClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        
        # keep track of which components have finished
        fixationComponents = []
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "fixation"-------
        while continueRoutine:
            # get current time
            t = fixationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            fixation = visual.TextStim(win, color = (-1, -1, -1), bold = True, units = 'pix')
            fixation.setText('+')
            fixation.draw()
            win.flip()
            event.waitKeys(keyList = ['space'])
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        image.setImage(imageFile)
        key_resp_3 = event.BuilderKeyResponse()
        # keep track of which components have finished
        trialComponents = [image, key_resp_3]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if t >= 0.0 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            frameRemains = 0.0 + 0.15- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image.status == STARTED and t >= frameRemains:
                image.setAutoDraw(False)
            
            # *key_resp_3* updates
            if t >= 0.15 and key_resp_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_3.tStart = t
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_3.status == STARTED:
#                theseKeys = event.getKeys()
                Atext=visual.TextStim(win)
                theseKeys = event.getKeys(keyList=['1','2','3','4','5','6','7','8','9','0','return', 'backspace','num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9','num_0'])
                
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                    
                if len(theseKeys) > 0:  # at least one key was pressed
                    if "backspace" in theseKeys:
                        key_resp_3.keys=key_resp_3.keys[:-1]
                        #key_resp_3.rt = key_resp_3.clock.getTime()
                
                    key_resp_3.keys.extend([key for key in theseKeys if key != "return" and key != "backspace"])
                    for n, i in enumerate(key_resp_3.keys):
                        if i =='num_1':
                            key_resp_3.keys[n] = '1'
                        elif i =='num_2':
                            key_resp_3.keys[n] = '2'
                        elif i =='num_3':
                            key_resp_3.keys[n] = '3'
                        elif i =='num_4':
                            key_resp_3.keys[n] = '4' 
                        elif i =='num_5':
                            key_resp_3.keys[n] = '5'
                        elif i =='num_6':
                            key_resp_3.keys[n] = '6'
                        elif i =='num_7':
                            key_resp_3.keys[n] = '7'
                        elif i =='num_8':
                            key_resp_3.keys[n] = '8'
                        elif i =='num_9':
                            key_resp_3.keys[n] = '9'
                        elif i =='num_0':
                            key_resp_3.keys[n] = '0'
                    # Atext.setText("".join(key_resp_3.keys))
                    
                    # convert the list of strings into a single string
                    key_str = "".join(key_resp_3.keys)
                    Atext.setText(key_str)
                    Atext.draw()
                    win.flip()
                    # # event.waitKeys(5,keyList = ['return'])
                    core.wait(0.5)
    
                    if len(key_str) !=0:
                    # then convert the string to a number
                        key_num = int(key_str)
    
                    if "return" in theseKeys:
                        key_resp_3.rt = key_resp_3.clock.getTime()
                        Atext.setText('')
                        Atext.draw()
                        core.wait(0.5)
                        continueRoutine=False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys=None
        trials.addData('key_resp_3.keys',key_num)
        if key_resp_3.keys != None:  # we had a response
            trials.addData('key_resp_3.rt', key_resp_3.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "break_3"-------
        t = 0
        break_3Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if trials.thisN != 24: #TODO
            continueRoutine = False
        
        
        # keep track of which components have finished
        break_3Components = []
        for thisComponent in break_3Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "break_3"-------
        while continueRoutine:
            # get current time
            t = break_3Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            break_text2 = visual.TextStim(win, text = 'Take a short break. Press spacebar to continue.', pos=[0, 0],units = 'pix')
            break_text2.draw()
            win.flip()
            event.waitKeys(keyList = ['space'])
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "break_3"-------
        for thisComponent in break_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "break_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'blocks'


# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
thanksComponents = []
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    thankmesg1 = visual.TextStim(win, pos=[0,+35],units = 'pix')
    thankmesg1.setText('This is the end of the experiment.')
    thankmesg2 = visual.TextStim(win, pos=[0, 0], units = 'pix')
    thankmesg2.setText('Thank you for your participation.')
    thankmesg1.draw()
    thankmesg2.draw()
    
    win.flip()
    event.waitKeys(keyList = ['n'])
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()







# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
