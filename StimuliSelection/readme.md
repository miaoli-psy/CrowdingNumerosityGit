## About exp1 new matched stimuli

1. folder: InputRawStimuli
    contains raw stimuli generated from GenerateAlgorithm
    are input for CharacterizeStimuli_Idea1_new.py and Func_CharacterizeStimuli.py
2. folder: InputAllStimuliwithProperities
    contains output of CharacterizeStimuli_Idea1_new.py
    are the input for GenerateMatchedStimuli.py
3. folder: OutputMatchedStimuli
    contains output of GenerateMatchedStimuli.py

4. 'CharacterizedStimuli_Idea1_new.py'
    calculated the generated display's properties (spacing, convexHull, occupancyArea, 
    average eccentricity...). And test if the properties for generated stimuli are normal 
    distributed.
5. 'Func_CharacterizeStimuli.py'
    similar with 'CharactherizedStimuli_Idea1_new.py' but a function. It returns properties
    of the input stimuli:
    
    -N_disk_dist: eg. how many times numerosity 54 appears
    -stimuliInfo_pivotT: numerosity as rows, stimuli properites as coloums
    -round(np.std(stimuliInfo_df['density']),5) 
    -round(np.std(stimuliInfo_df['averageE']),5)
    -round(np.std(stimuliInfo_df['avg_spacing']),5)
6. 'CharacterizedselectedStimuli.py'
    characterize the final selected stimuli. The output is a pivot table per property
7. 'GenerateDisplay.py'
    generate the final displays that will be used in the experiments and the input is the 
    selceted position details named "Idea1_DESCO.xlsx" saved in '..\\..\\Crowding_and_numerosity\\MatchingAlgorithm\\Idea1\\Stimuli190429\\selectedMatchedStimuli\\'

## Runme:
1. Put raw stimuli named  eg."idea1_crowdingCons_0_ws_0.3.csv" into '..\\..\\Crowding_and_numerosity\\MatchingAlgorithm\\Idea1\\Stimuli190429\\InputRawStimuli\\'
2. run CharacterizeStimuli_Idea1_new.py
    -note that adjust the paramiters first
    -one run generate the output for 1 condition
    -results saved in .\\OutputMatchedStimuli_temp
    -results named eg. "Idea1_allStimuliInfo_ws0.3_crowdingcon0.xlsx"
3. If there is updates in the frist 2 steps, put output xlsx file to '..\\..\\Crowding_and_numerosity\\MatchingAlgorithm\\Idea1\\Stimuli190429\\InputAllStimuliwithProperties\\'
4. run GenerateMatchedStimuli.py
    -you find the final selected stimuli in '..\\..\\Crowding_and_numerosity\\MatchingAlgorithm\\Idea1\\Stimuli190429\\OutputMatchedStimili\\'
5. manually choose the mached stimuli according to the ouptups.
    -save the selection as "Idea1_DESCO.xlsx", and put in path '..\\..\\Crowding_and_numerosity\\MatchingAlgorithm\\Idea1\\Stimuli190429\\selectedMatchedStimuli\\'
6. run CharacterizedselectedStimuli.py
    -output named 'finalSelectedStimuliProperties_pivotT.xlsx' is saved in '..\\..\\Crowding_and_numerosity\\MatchingAlgorithm\\Idea1\\Stimuli190429\\selectedMatchedStimuli\\'
7. run GenerateDisplay.py
    -get the final displays we use