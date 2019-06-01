from __future__ import division  # so that 1/3=0.333 instead of 1/3=0 # not useful in python3 (i supposes~)
import psychopy, glob, datetime, sys, pylab, random, pickle, os
from psychopy import visual, core, data, event, monitors, sound, prefs, tools, gui,logging
from psychopy.tools.filetools import fromFile, toFile
from random import shuffle
from scipy import special
#from pytest import raises
import pandas as pd
import numpy as np

# nat melnik

# =============================================================================
# parameters to adjust
# =============================================================================
startingBlockNumber = 0 #type block-1 to start from specific block (i.e., 3 for block 4).

# =============================================================================
# some functions...
# =============================================================================
def updateTheResponse(captured_string):
    CapturedResponseString.setText(captured_string)
    CapturedResponseString.draw()

def returnNewString(captured_string,print_string,bigLetter = False,twoLetter=False):
    for key in event.getKeys():
        if key in ['escape']:
            win.close()
            core.quit()

        elif key in ['delete', 'backspace']:
            if twoLetter== True:
                captured_string = captured_string[:-1]  # delete last character
                print_string = print_string[:-2]
            else:
                captured_string = captured_string[:-1]  # delete last character
                print_string = print_string[:-1]
            # handle spaces
            #pass  # do nothing when some keys are pressed
        # elif key in ['return']:
        #     pass
            # print captured_string  # write to file
            #captured_string = ''  # reset to zero length
        elif key in ['num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9', 'num_0']:
            captured_string = captured_string + key[-1]
            print_string = print_string + key[-1]
        elif key in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            captured_string = captured_string + key
            print_string = print_string + key
        #else:
        #    captured_string = captured_string + key
        #    print_string = print_string + key
        #    twoLetter = False

            # show it
        #print key
    return captured_string, print_string, bigLetter,twoLetter

def startExpt():
    message1 = visual.TextStim(win, pos=[0,+35],units = 'pix')
    message1.setText('Welcome to our experiment.')
    message2 = visual.TextStim(win, pos=[0, 0],units = 'pix')
    message2.setText('Please give your best esimation.')
    message3 = visual.TextStim(win, pos=[0, -35], units = 'pix')
    message3.setText('Hit spacebar to start practice.')
    message1.draw()
    message2.draw()
    message3.draw()
    win.flip()
    keypress = event.waitKeys(keyList=['space', 'escape'])
    if keypress[0] == 'escape':
        core.quit()

def endPractice():
    end_practice1 = visual.TextStim(win, pos=[0, +35], units='pix')
    end_practice1.setText('This is the end of practice')
    end_practice2 = visual.TextStim(win, pos=[0, 0], units='pix')
    end_practice2.setText('There are 10 blocks of the real experiment, you will see 3 reference images before each block.')
    end_practice3 = visual.TextStim(win, pos=[0, -35], units='pix')
    end_practice3.setText('Hit spacebar to start the real experiment.')
    end_practice1.draw()
    end_practice2.draw()
    end_practice3.draw()
    win.flip()
    keypress = event.waitKeys(keyList=['space', 'escape'])
    if keypress[0] == 'escape':
        core.quit()

def startBlock(ref_image1, ref_image2, ref_image3, ref_image4, ref_image5, Number1, Number2, Number3, Number4, Number5):
    fix = visual.TextStim(win, pos=[0, 0], bold=True, units='pix')
    block_text = visual.TextStim(win, pos=[0, 0], units='pix')
    block_text.setText('Fixate to the center of screen and press spacebar to see the reference display.')
    block_text.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    fix.setText('+')
    fix.setColor(u'black')
    fix.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    image_ref = visual.ImageStim(win, image=ref_image1, units='pix')
    image_ref.draw()
    win.flip()
    core.wait(0.15)

    image_ref_text = visual.TextStim(win, pos=[0, 15], units='pix')
    image_ref_text2 = visual.TextStim(win, pos=[0, -15], units='pix')
    image_ref_text3 = visual.TextStim(win, pos=[0, 0], units='pix')
    image_ref_text.setText('The number of the reference disks is %s:' % (int(Number1)))
    image_ref_text2.setText('Press C to continue')
    image_ref_text.draw()
    image_ref_text2.draw()
    win.flip()
    event.waitKeys(keyList=['c'])
    # image_ref_text2.setText(Number1)
    image_ref_text3.setText('Fixate to the center and press spacebar to see another reference display.')
    # image_ref_text.draw()
    # image_ref_text2.draw()
    image_ref_text3.draw()
    win.flip()
    keypress = event.waitKeys(keyList=['space', 'escape'])
    if keypress[0] == 'escape':
        core.quit()
    # block_text.setText('+')
    # block_text.setColor(u'black')
    # block_text.draw()
    fix.draw()
    win.flip()
    keypress = event.waitKeys(keyList=['space', 'escape'])
    if keypress[0] == 'escape':
        core.quit()

    image_ref2 = visual.ImageStim(win, image=ref_image2, units='pix')
    image_ref2.draw()
    win.flip()
    core.wait(0.15)

    image_ref_text.setText('The number of the reference disks is %s:' % (int(Number2)))
    # image_ref_text2.setText(Number2)
    # image_ref_text2.setText('Press spacebar to continue')
    image_ref_text.draw()
    image_ref_text2.draw()
    win.flip()
    event.waitKeys(keyList=['c'])

    image_ref_text3.draw()
    win.flip()
    keypress = event.waitKeys(keyList=['space', 'escape'])
    if keypress[0] == 'escape':
        core.quit()

    fix.draw()
    win.flip()
    keypress = event.waitKeys(keyList=['space', 'escape'])
    if keypress[0] == 'escape':
        core.quit()

    image_ref3 = visual.ImageStim(win, image=ref_image3, units='pix')
    image_ref3.draw()
    win.flip()
    core.wait(0.15)

    image_ref_text.setText('The number of the reference disks is %s:' % (int(Number3)))
    image_ref_text.draw()
    image_ref_text2.draw()
    win.flip()
    event.waitKeys(keyList=['c'])

    image_ref_text3.setText('Press spacebar to start the real experiment.')
    image_ref_text3.draw()
    win.flip()
    keypress = event.waitKeys(keyList=['space', 'escape'])
    if keypress[0] == 'escape':
        core.quit()
    
    image_ref4 = visual.ImageStim(win, image=ref_image4, units='pix')
    image_ref4.draw()
    win.flip()
    core.wait(0.15)

    image_ref_text.setText('The number of the reference disks is %s:' % (int(Number4)))
    image_ref_text.draw()
    image_ref_text2.draw()
    win.flip()
    event.waitKeys(keyList=['c'])

    image_ref_text3.draw()
    win.flip()
    keypress = event.waitKeys(keyList=['space', 'escape'])
    if keypress[0] == 'escape':
        core.quit()

    image_ref5 = visual.ImageStim(win, image=ref_image5, units='pix')
    image_ref5.draw()
    win.flip()
    core.wait(0.15)

    image_ref_text.setText('The number of the reference disks is %s:' % (int(Number5)))
    image_ref_text.draw()
    image_ref_text2.draw()
    win.flip()
    event.waitKeys(keyList=['c'])

    image_ref_text3.setText('Press spacebar to start the real experiment.')
    image_ref_text3.draw()
    win.flip()
    keypress = event.waitKeys(keyList=['space', 'escape'])
    if keypress[0] == 'escape':
        core.quit()

def runTrial(training=False, trialInfo=None, nFrames=10, strictResponse=True, blockNo=None):
    print ('runs trial')
    
    trialClock = core.Clock()
    fixation = visual.TextStim(win, color=(-1, -1, -1), bold=True, units='pix')
    fixation.setText('+')
    fixation.draw()
    win.flip()
    
    keypress = event.waitKeys(keyList=['space', 'escape'])
    if keypress[0] == 'escape':
        core.quit()
    if training:
        image.setImage(u'training.png') #set parctice image #TODO
    else:
        imageFile = trialInfo['imageFile']
        image.setImage(imageFile)
    image.draw()
    
    for i in range(0,nFrames):
        win.flip()
    
    win.flip()
    done=False
    
    trialClock.reset()
    
    captured_stringbottom = ''  # empty for now.. this is a string of zero length that
    pcaptured_stringbottom = ''  # empty for now.. this is a string of zero length that

    while not done:
        captured_stringbottom, pcaptured_stringbottom, bigLetter, twoLetter = returnNewString(captured_stringbottom, pcaptured_stringbottom)
        
        CapturedResponseString.setText(captured_stringbottom)
        CapturedResponseString.draw()
        
        win.flip()
        
        keys = event.getKeys(keyList=['return', 'escape'], timeStamped=trialClock)
        if strictResponse:
            if captured_stringbottom!='':
                if len(keys) != 0:
                    thiskey = keys.pop()
                    if thiskey[0] == 'escape':
                        core.quit()
                    else:
                        rt1 = thiskey[1]
                        pk1 = thiskey[0]
                        print (captured_stringbottom, pk1,rt1)
                        done = True
        else:
            if len(keys) != 0:
                thiskey = keys.pop()
                if thiskey[0] == 'escape':
                    core.quit()
                else:
                    rt1 = thiskey[1]
                    pk1 = thiskey[0]
                    print (captured_stringbottom, pk1,rt1)
                    done = True
    with open(alternative_filename, 'a') as f:
        line = "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n" % (captured_stringbottom, 
                                                               pk1, 
                                                               rt1, 
                                                               training, 
                                                               trialInfo,
                                                               nFrames,
                                                               strictResponse,
                                                               blockNo,
                                                               expInfo['expName'],
                                                               expInfo['blockOrder'])
        f.write(line)
    event.clearEvents()

def doBreak():
    break_text2 = visual.TextStim(win, text='Take a short break. Press spacebar to continue.', pos=[0, 0], units='pix')
    break_text2.draw()
    win.flip()
    keypress = event.waitKeys(keyList=['space', 'escape'])
    if keypress[0] == 'escape':
        core.quit()

def endExpt():
    thankmesg1 = visual.TextStim(win, pos=[0, +35], units='pix')
    thankmesg1.setText('This is the end of the experiment.')
    thankmesg2 = visual.TextStim(win, pos=[0, 0], units='pix')
    thankmesg2.setText('Thank you for your participation.')
    thankmesg1.draw()
    thankmesg2.draw()
    keypress = event.waitKeys(keyList=['n', 'escape'])
    if keypress[0] == 'escape':
        core.quit()

# Ensure that relative paths start from the same directory as this script

# when we put all other files in the same dir
# _thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding()) #python 2
# _thisDir = os.path.dirname(os.path.abspath(__file__)) #python 3
# os.chdir(_thisDir)

# Miao:  other files in other dir
_thisDirLocal =  '..\\..\\Crowding_and_numerosity\\setupExp_psychopy\\Psychopybuilder\\Crowding\\Exp1_rerun\\'
os.chdir(_thisDirLocal)# change dir to where the images, condition and blockorder are

currentDir = os.path.dirname(os.path.abspath(__file__))

# Store info about the experiment session
expName = 'Crwdng_Nmrsty_older_runOnLab1'
expInfo = {u'handedness'   : ['Right handed', 'Left handed'],
           u'participant'  : u'',
           u'age'          : u'',
           u'blockOrder'   : u'',
           u'sex'          : ['Female','Male'],
           u'group'        : ['1','2']} #1 for normal, 2 for dyslexic
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# =============================================================================
# Test me
# =============================================================================
if expInfo['blockOrder'] == '':
    expInfo['blockOrder'] = 30
    print ('this is test')

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = currentDir + os.sep + u'data_Crwdng_Nmrsty1\\group%s_participant%s_date%s' % (expInfo['group'], expInfo['participant'], expInfo['date'])
alternative_filename = currentDir + os.sep + u'data_Crwdng_Nmrsty1\\alternative_group%s_participant%s_date%s' % (expInfo['group'], expInfo['participant'], expInfo['date'])

# with open(alternative_filename, 'a', newline = '') as f:
#     firstline = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\n" % ('subjID', 
#                                                                                        'session',
#                                                                                        'blockNo', 
#                                                                                        'trialno', 
#                                                                                        'rt1',
#                                                                                        'correct1', 
#                                                                                        'pk1', 
#                                                                                        'corransw',
#                                                                                        'helperSpacing',
#                                                                                        'flankerSpacing', 
#                                                                                        'crowded',
#                                                                                        'helper', 
#                                                                                        'targetO',
#                                                                                        'flankerstr', 
#                                                                                        'leftObjParams',
#                                                                                        'rightObjParams',
#                                                                                        'downObjParams', 
#                                                                                        'presentedTo',
#                                                                                        'contrast', 
#                                                                                        'helperOri',
#                                                                                        'flankerCategory')
#     f.write(firstline)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name        = expName,
                                 version     = '',
                                 extraInfo   = expInfo, 
                                 runtimeInfo = None,
                                 originPath  = None,
                                 savePickle  = True, 
                                 saveWideText= True,
                                 dataFileName=filename)

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

myMonitor= monitors.Monitor('CRT_Lille', width = 40.5, distance = 57)#TODO
win = visual.Window(monitor  = myMonitor,
                    size     = [1024, 768],
                    screen   = 1,
                    units    = 'pix',
                    fullscr  = False,
                    allowGUI = False,
                    winType  = 'pyglet',
                    color    = (0,0,0))

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60  # could not measure, so guess

# initialize some components
CapturedResponseString = visual.TextStim(win,
                                        units     = 'pix',
                                        height    = 20,
                                        pos       = [0, 0],
                                        text      = '',
                                        alignHoriz= 'left',
                                        alignVert = 'center',
                                        color     = 'white')

image = visual.ImageStim(win=win, pos=(0, 0), interpolate=True)

blocks= pd.read_csv("blockOrder"+str(expInfo['blockOrder'])+".csv", sep=',')#maybe needs no str

# =============================================================================
# starts the experiment here
# =============================================================================

#welcome message
startExpt()

#practice
for i in range(3):
    runTrial(training=True,strictResponse=False, blockNo='training')# 3 practice trials
endPractice()

#real experiment
for b in range(startingBlockNumber,len(blocks)):
    print (blocks['winsize'][b])

    startBlock(blocks['ref_image1'][b], 
               blocks['ref_image2'][b], 
               blocks['ref_image3'][b],
               blocks['ref_image4'][b], 
               blocks['ref_image5'][b], 
               blocks['Number1'][b],
               blocks['Number2'][b],
               blocks['Number3'][b],
               blocks['Number4'][b],
               blocks['Number5'][b])

    trials = data.TrialHandler(nReps       = 1, 
                               method      = 'random',
                               extraInfo   = expInfo, 
                               originPath  = -1,
                               trialList   = data.importConditions(blocks['winsize'][b]),
                               seed        = None, 
                               name        = 'trials')
    for trial in trials:
        runTrial(strictResponse=False, training=False, trialInfo = trial ,blockNo = blocks['winsize'][b])
    doBreak()

#end mesage
endExpt()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(alternative_filename+'.csv')
thisExp.saveAsPickle(alternative_filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
