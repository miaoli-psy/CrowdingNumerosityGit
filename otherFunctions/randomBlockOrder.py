# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 18:18:25 2019

@author: MiaoLi

This code generates the condition files for each participants.
"""

from numpy.random import shuffle
import copy, sys, csv
from random import randint
import random

# # Run multiple times
# try:
#     _, loop_number = sys.argv
# except Exception as e:
#     pass
# runN = 1
def runBlockorder(runN):
    # The block list I want 
    myCons = ['condition0.3.xlsx', 'condition0.7.xlsx', 'condition0.6.xlsx', 'condition0.5.xlsx', 'condition0.4.xlsx']
    shuffle(myCons)
    myCons2 = copy.copy(myCons)
    myCons2.reverse()
    myCons.extend(myCons2)
    print(myCons)
    
    ref_ws03   = {'wS_0.3_eS_0.17_0.17_17.png'     : 17,
                  'wS_0.3_eS_0.145_0.145_29.png'   : 29,
                  'wS_0.3_eS_0.1581_0.1581_20.png' : 20,
                  'wS_0.3_eS_0.1581_0.1581_23.png' : 23,
                  'wS_0.3_eS_0.1581_0.1581_26.png' : 26}
    
    ref_ws03_keys = list(ref_ws03.keys())
    ref_ws03_values = list(ref_ws03.values())
    
    ref_ws04   = {'wS_0.4_eS_0.145_0.145_41.png'   :41,
                  'wS_0.4_eS_0.175_0.175_25.png'   :25,
                  'wS_0.4_eS_0.1581_0.1581_30.png' :30,
                  'wS_0.4_eS_0.1581_0.1581_33.png' :33,
                  'wS_0.4_eS_0.1581_0.1581_36.png' :36}
    
    ref_ws04_keys = list(ref_ws04.keys())
    ref_ws04_values = list(ref_ws04.values())
    
    ref_ws05   = {'wS_0.5_eS_0.14_0.14_49.png'    : 49,
                  'wS_0.5_eS_0.14_0.14_54.png'    : 54,
                  'wS_0.5_eS_0.17_0.17_37.png'    : 37,
                  'wS_0.5_eS_0.18_0.18_32.png'    : 32,
                  'wS_0.5_eS_0.1581_0.1581_43.png': 43}
    
    ref_ws05_keys = list(ref_ws05.keys())
    ref_ws05_values = list(ref_ws05.values())
    
    ref_ws06   = {'wS_0.6_eS_0.14_0.14_64.png'    : 64,
                  'wS_0.6_eS_0.17_0.17_44.png'    : 44,
                  'wS_0.6_eS_0.18_0.18_38.png'    : 38,
                  'wS_0.6_eS_0.145_0.145_58.png'  : 58,
                  'wS_0.6_eS_0.1581_0.1581_51.png': 51}
    ref_ws06_keys = list(ref_ws06.keys())
    ref_ws06_values = list(ref_ws06.values())
    ref_ws07   = {'wS_0.7_eS_0.17_0.17_49.png'    : 49,
                  'wS_0.7_eS_0.18_0.18_42.png'    : 42,
                  'wS_0.7_eS_0.145_0.145_63.png'  : 63,
                  'wS_0.7_eS_0.145_0.145_70.png'  : 70,
                  'wS_0.7_eS_0.1581_0.1581_56.png': 56}
    
    ref_ws07_keys = list(ref_ws07.keys())
    ref_ws07_values = list(ref_ws07.values())
    
    
    index1 = index2 = index3 = index4 = index5 = [0, 1, 2, 3, 4]
    random.shuffle(index1)
    random.shuffle(index2)
    random.shuffle(index3)
    random.shuffle(index4)
    random.shuffle(index5)
    
    myConsDic = { 'condition0.3.xlsx': [ref_ws03_keys[index1[0]], ref_ws03_values[index1[0]], ref_ws03_keys[index1[1]], ref_ws03_values[index1[1]], ref_ws03_keys[index1[2]], ref_ws03_values[index1[2]], ref_ws03_keys[index1[3]], ref_ws03_values[index1[3]], ref_ws03_keys[index1[4]], ref_ws03_values[index1[4]]],
                  'condition0.7.xlsx': [ref_ws07_keys[index2[0]], ref_ws07_values[index2[0]], ref_ws07_keys[index2[1]], ref_ws07_values[index2[1]], ref_ws07_keys[index2[2]], ref_ws07_values[index2[2]], ref_ws07_keys[index2[3]], ref_ws07_values[index2[3]], ref_ws07_keys[index2[4]], ref_ws07_values[index2[4]]],
                  'condition0.6.xlsx': [ref_ws06_keys[index3[0]], ref_ws06_values[index3[0]], ref_ws06_keys[index3[1]], ref_ws06_values[index3[1]], ref_ws06_keys[index3[2]], ref_ws06_values[index3[2]], ref_ws06_keys[index3[3]], ref_ws06_values[index3[3]], ref_ws06_keys[index3[4]], ref_ws06_values[index3[4]]],
                  'condition0.5.xlsx': [ref_ws05_keys[index4[0]], ref_ws05_values[index4[0]], ref_ws05_keys[index4[1]], ref_ws05_values[index4[1]], ref_ws05_keys[index4[2]], ref_ws05_values[index4[2]], ref_ws05_keys[index4[3]], ref_ws05_values[index4[3]], ref_ws05_keys[index4[4]], ref_ws05_values[index4[4]]],
                  'condition0.4.xlsx': [ref_ws04_keys[index5[0]], ref_ws04_values[index5[0]], ref_ws04_keys[index5[1]], ref_ws04_values[index5[1]], ref_ws04_keys[index5[2]], ref_ws04_values[index5[2]], ref_ws04_keys[index5[3]], ref_ws04_values[index5[3]], ref_ws04_keys[index5[4]], ref_ws04_values[index5[4]]]}
    
    #write them to a csv
    with open ('blockOrder%s.csv' %(runN), 'a+', newline='') as csvfile:
        fieldnames = ['winsize','ref_image1','Number1','ref_image2','Number2','ref_image3','Number3', 'ref_image4','Number4', 'ref_image5','Number5'] #headers
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for idx, condition in enumerate(myCons): #correct indexing
            if idx == 5:
                idx = 4
            elif idx == 6:
                idx = 3
            elif idx == 7:
                idx =2
            elif idx == 8:
                idx =1
            elif idx == 9:
                idx =0
            writer.writerow({'winsize'     : condition, 
                              'ref_image1'  : myConsDic.get(condition)[0],
                              'Number1'     : myConsDic.get(condition)[1], 
                              'ref_image2'  : myConsDic.get(condition)[2],
                              'Number2'     : myConsDic.get(condition)[3],
                              'ref_image3'  : myConsDic.get(condition)[4],
                              'Number3'     : myConsDic.get(condition)[5],
                              'ref_image4'  : myConsDic.get(condition)[6],
                              'Number4'     : myConsDic.get(condition)[7],
                              'ref_image5'  : myConsDic.get(condition)[8],
                              'Number5'     : myConsDic.get(condition)[9]})

i = 1
while i <= 40:
    runBlockorder(runN=i)
    i += 1