# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:15:33 2019
This code calculated the generated display's properties (spacing, convexHull, occupancyArea, 
average eccentricity...). And test if the properties for generated stimuli are normal 
distributed. Run each file one by one.

@author: MiaoLi
"""
import pandas as pd
import ast
from scipy.spatial import ConvexHull
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from math import pi
import os

# =============================================================================
# all imput stimuli in folder
# =============================================================================
# folderPath = '.\\InputRawStimuli\\'
folderPath = '..\\..\\Crowding_and_numerosity\\MatchingAlgorithm\\Idea1\\Stimuli190429\\InputRawStimuli\\'
dic_files = {(0.7,1):folderPath +'idea1_crowdingCons_1_ws_0.7.csv',
             (0.7,0):folderPath +'idea1_crowdingCons_0_ws_0.7.csv',
             (0.6,1):folderPath +'idea1_crowdingCons_1_ws_0.6.csv',
             (0.6,0):folderPath +'idea1_crowdingCons_0_ws_0.6.csv',
             (0.5,1):folderPath +'idea1_crowdingCons_1_ws_0.5.csv',
             (0.5,0):folderPath +'idea1_crowdingCons_0_ws_0.5.csv',
             (0.4,1):folderPath +'idea1_crowdingCons_1_ws_0.4.csv',
             (0.4,0):folderPath +'idea1_crowdingCons_0_ws_0.4.csv',
             (0.3,1):folderPath +'idea1_crowdingCons_1_ws_0.3.csv',
             (0.3,0):folderPath +'idea1_crowdingCons_0_ws_0.3.csv'}

# =============================================================================
# Paramiters to adjust 
# =============================================================================

# which property to test

stimuliPropertyToTest = 'avg_spacing'
# stimuliPropertyToTest = 'convexHull'
# stimuliPropertyToTest = 'occupancyArea'
# stimuliPropertyToTest = 'averageE'
# stimuliPropertyToTest = 'density'

#names to write
ws = 0.7
crowdingDis = 0

# which file to read
my_choice = dic_files[(ws,crowdingDis)]

# =============================================================================
# read csv to df
# =============================================================================
stimuliInfo_df=pd.read_csv(my_choice,header = None)
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
# convexHull and occupancyArea
# =============================================================================
# countConvexHull = []
# occupanyArea = []
# for display in posi_list:
#     array = np.asarray(display) #list to ndarray
#     countConvexHull_t = ConvexHull(array)
#     countConvexHull_t_perimeter= countConvexHull_t.area # in 2D dots array .area returns perimeter and .volume returns surface(area)
#     countConvexHull_t_perimeter_psychopy = countConvexHull_t_perimeter*(0.25/3.82)
#     occupanyArea_t = countConvexHull_t.volume
#     occupanyArea_t_psychopy = occupanyArea_t*((0.25/3.82)**2)
    
#     countConvexHull.append(countConvexHull_t_perimeter_psychopy)
#     occupanyArea.append(occupanyArea_t_psychopy)

# # add convexHull to stimuliInfo
# stimuliInfo_df['convexHull'] = countConvexHull 
# stimuliInfo_df['occupancyArea'] = occupanyArea 


# # # plot convex hull example
# # plt.plot(array[:,0], array[:,1], 'o')
# # for simplex in countConvexHull_t.simplices:
# #     plt.plot(array[simplex, 0], array[simplex, 1], 'k-')

# =============================================================================
# average eccentricity
# =============================================================================
# averageE = []
# for display in posi_list:
#     currentListD = []
#     for posi in display:
#         e = distance.euclidean(posi, (0,0))
#         e_psychopy = e*(0.25/3.82)
#         currentListD.append(e_psychopy)
#     averageE_t = round(sum(currentListD)/len(display),2) #caculate average eccentricity
#     averageE.append(averageE_t)
# # add average eccebtrucutyto stimuliInfo
# stimuliInfo_df['averageE'] = averageE

# =============================================================================
# aggregate surface （所有disks的面积）
# =============================================================================
aggregateSurface = []
for display in posi_list:
    aggregateSurface_t = len(display)*pi*(0.25**2)
    aggregateSurface.append(aggregateSurface_t)

stimuliInfo_df['aggregateSurface'] = aggregateSurface
# =============================================================================
# density
# density1 = numer of disk / convex hull area
# density2 = numer of disk / white frame area
# density3 = aggregate surface / convex hull
# density = aggregate surface / occupancy area
# =============================================================================

# # take winsize out
# winsize_t = stimuliInfo_df['winsize'].tolist()
# whiteFrameArea = []
# for i in range(0, len(posi_list)):
#     if winsize_t[i] == 'condition0.3.xlsx':
#         whiteFrameArea_t = 19.5*11.5 #measured from psychopy
#     elif winsize_t[i] == 'condition0.4.xlsx':
#         whiteFrameArea_t = 21.5*13.5
#     elif winsize_t[i] == 'condition0.5.xlsx':
#         whiteFrameArea_t = 25*16.5
#     elif winsize_t[i] == 'condition0.6.xlsx':
#         whiteFrameArea_t = 27*18.5
#     elif winsize_t[i] == 'condition0.7.xlsx':
#         whiteFrameArea_t = 30*21
#     whiteFrameArea.append(whiteFrameArea_t)

# caculatedDensity2 = []
# caculatedDensity = []
# caculatedDensity3 = []
# caculatedDensity4 = []
caculatedDensity = []

for count, display in enumerate(posi_list):
    array = np.asarray(display)
    convexHullArea_t = ConvexHull(array).volume/(15.28**2)#caculate convexHull area- use .volume function
    # density_t = round(len(display)/convexHullArea_t,5)
    # # density_t2 = round(len(display)/whiteFrameArea[count],5)
    # density_t3 = round(aggregateSurface[count]/countConvexHull[count],5)
    density_t = round(aggregateSurface[count]/convexHullArea_t,5)
    # caculatedDensity.append(density_t)
    # caculatedDensity2.append(density_t2)
    # caculatedDensity3.append(density_t3)
    caculatedDensity.append(density_t)

# # add density to stimuliInfo
# stimuliInfo_df['density1_Ndisk/occupancyArea'] = caculatedDensity
# stimuliInfo_df['density2_Ndisk/whiteF'] = caculatedDensity2
# stimuliInfo_df['density3_AS/convexH'] = caculatedDensity3
stimuliInfo_df['density'] = caculatedDensity

# ============================================================================
# inspect disks fall into others crowding zones
# =============================================================================

# dic_count_in_crowdingZone = {}
# list_count_in_crowdingZone = []
# for indexPosiList in range(0,len(posi_list)):
#     display_posi = posi_list[indexPosiList]
#     #final ellipses
#     ellipses = []
#     for posi in display_posi:
#         e = defineVirtualEllipses(posi)
#         ellipses.append(e)
#     # final_ellipses = list(set(ellipses)) #if order doest matter
#     final_ellipses = list(OrderedDict.fromkeys(ellipses)) #ordermatters
#     count_in_crowdingZone = 0
#         #crowding zones after reomve overlapping areas
#     for count, i in enumerate(final_ellipses, start = 1):
#         ellipsePolygon = ellipseToPolygon([i])[0] #radial ellipse
#         # ellipsePolygonT = ellipseToPolygon([i])[1]#tangential ellipse
#         epPolygon = Polygon(ellipsePolygon)
#         # epPolygonT = Polygon(ellipsePolygonT)
#         # radial_area_dic[(i[0],i[1])] = [] #set the keys of the dictionary--taken_posi
#         for posi in display_posi:
#             if epPolygon.contains(Point(posi)) == True:
#                 count_in_crowdingZone += 1
#     count_number_end = count_in_crowdingZone-len(display_posi)
#     dic_temp_item = {indexPosiList: count_number_end}
#     dic_count_in_crowdingZone.update(dic_temp_item)
#     list_count_in_crowdingZone.append(count_number_end)
    
# stimuliInfo_df.insert(1, 'count_number',list_count_in_crowdingZone)

# =============================================================================
# spacing : average spacing
# =============================================================================
# avg_distance_psychopy = []
# for display in posi_list:
#     distances = [dist(p1, p2) for p1, p2 in combinations(display,2)] # gives combinations without repeat; calculate all distances for each pair
#     # distances2 =[distance.euclidean(p1, p2) for p1, p2 in combinations(display,2)] # another way to calculate distances
#     avg_distance_psychopy_t = sum(distances)/len(distances)*(0.25/3.82)
#     # avg_distance_psychopy2 = sum(distances2)/len(distances2)*(0.25/3.82)
#     avg_distance_psychopy.append(avg_distance_psychopy_t)

# stimuliInfo_df['spacing'] = avg_distance_psychopy 

# =============================================================================
# write detailed stimuliInfo to excel (if needed)
# =============================================================================
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

# folderOutputPath = "./OutputMatchedStimili/"
folderOutputPath = '.\\OutputMatchedStimili_temp\\'
createFolder(folderOutputPath)

writer = pd.ExcelWriter(folderOutputPath+'Idea1_allStimuliInfo_ws%s_crowdingcon%s.xlsx' %(ws, crowdingDis),engine='xlsxwriter')
stimuliInfo_df.to_excel(writer, sheet_name = 'CharacterizedstimuliInfo')
writer.save()

# stimuliInfo_pivotT= pd.pivot_table(stimuliInfo_df, index = ['CrowdingCons'], values = ['convexHull','density1_Ndisk/occupancyArea','density2_Ndisk/whiteF','density3_AS/convexH','averageE', 'aggregateSurface','occupancyArea','spacing','density4_AS/occupencyArea'], columns = ['winsize','N_disk'])
stimuliInfo_pivotT= pd.pivot_table(stimuliInfo_df, values = ['convexHull', 'averageE', 'aggregateSurface','occupancyArea','avg_spacing','density'], columns = ['N_disk'])
stimuliInfo_pivotT.to_excel(folderOutputPath+'Idea1_pivotT_ws%s_crowdingcon%s.xlsx' %(ws, crowdingDis))

#%% =============================================================================
# Plot distribution N_disk
# =============================================================================

# count run times
count_run_times = stimuliInfo_df.shape[0]
print('ws%s_crowdingcons%s run' %(ws, crowdingDis), count_run_times, 'times')

fig, ax = plt.subplots()
width = 0.5 # the width of the bars
N_disk_dist = stimuliInfo_df.groupby('N_disk').size()
ax = N_disk_dist.plot.bar()
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x(), p.get_height()))

ax.set_xlabel("N_disk_ws%s_crowdingCon%s" %(ws, crowdingDis))
ax.set_title('ws%s_crowdingcons%s run %stimes' %(ws, crowdingDis,count_run_times))
plt.savefig("N_disk_ws%s_crowdingCon%s_idea1.png" %(ws, crowdingDis))

#%% =============================================================================
# Whehter normal distributed for each properties
# =============================================================================
def ecdf(data):
    """Compute ECDF (empirical cumlative distribution function) for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n
    return x, y

#plots

# stimuliproperty
x, y = ecdf(stimuliInfo_df[stimuliPropertyToTest])

#plot for stimuli property
plt.figure(figsize=(8,7))
sns.set()
plt.plot(x, y, marker=".", linestyle="none")
plt.xlabel(stimuliPropertyToTest)
plt.ylabel("Cumulative Distribution Function")

# generated normal distrubution using my data's mean and sd
samples = np.random.normal(np.mean(stimuliInfo_df[stimuliPropertyToTest]), np.std(stimuliInfo_df[stimuliPropertyToTest]),size = 10000)
x_theor, y_theor = ecdf(samples)

#compare to see if the sample stimuli are normal distributed
plt.plot(x_theor, y_theor)
plt.legend(('sampleStimiliDistribution', 'Normal Distribution'), loc='lower right')

# statistical result (pvalue > significance value, then normal distributed)
normalTest = stats.normaltest(stimuliInfo_df[stimuliPropertyToTest])

print(normalTest)
print(round(np.mean(stimuliInfo_df[stimuliPropertyToTest]),5), round(np.std(stimuliInfo_df[stimuliPropertyToTest]),5))
