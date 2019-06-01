# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 18:18:25 2019

@author: MiaoLi

This code generates the condition files for each participants.
"""

from numpy.random import shuffle
import copy, sys, csv
from random import randint

# # Run multiple times
# try:
#     _, loop_number = sys.argv
# except Exception as e:
#     pass

def runBlockorder(runN):
    # The block list I want 
    myCons = ['condition0.3.xlsx', 'condition0.7.xlsx', 'condition0.6.xlsx', 'condition0.5.xlsx', 'condition0.4.xlsx']
    shuffle(myCons)
    myCons2 = copy.copy(myCons)
    myCons2.reverse()
    myCons.extend(myCons2)
    print(myCons)

    ref_ws03   = {'ws0.3_crowding2_n115_Ndisk23.png': 23,
                  'ws0.3_crowding2_n24_Ndisk24.png' : 24,
                  'ws0.3_crowding2_n70_Ndisk21.png' : 21,
                  'ws0.3_crowding2_n7_Ndisk22.png'  : 22,
                  'ws0.3_crowding2_n93_Ndisk25.png' : 25}

    ref_ws03_keys = list(ref_ws03.keys())
    ref_ws03_values = list(ref_ws03.values())

    ref_ws04   = {'ws0.4_crowding2_n106_Ndisk35.png':35,
                  'ws0.4_crowding2_n118_Ndisk34.png':34,
                  'ws0.4_crowding2_n196_Ndisk31.png':31,
                  'ws0.4_crowding2_n1_Ndisk33.png'  :33,
                  'ws0.4_crowding2_n20_Ndisk32.png' :32}

    ref_ws04_keys = list(ref_ws04.keys())
    ref_ws04_values = list(ref_ws04.values())

    ref_ws05   = {'ws0.5_crowding2_n22_Ndisk41.png': 41,
                  'ws0.5_crowding2_n24_Ndisk44.png': 44,
                  'ws0.5_crowding2_n29_Ndisk45.png': 45,
                  'ws0.5_crowding2_n64_Ndisk43.png': 43,
                  'ws0.5_crowding2_n99_Ndisk42.png': 42}

    ref_ws05_keys = list(ref_ws05.keys())
    ref_ws05_values = list(ref_ws05.values())

    ref_ws06   = {'ws0.6_crowding2_n17_Ndisk52.png': 52,
                  'ws0.6_crowding2_n25_Ndisk51.png': 51,
                  'ws0.6_crowding2_n48_Ndisk49.png': 49,
                  'ws0.6_crowding2_n4_Ndisk53.png' : 53,
                  'ws0.6_crowding2_n9_Ndisk50.png' : 50}
    ref_ws06_keys = list(ref_ws06.keys())
    ref_ws06_values = list(ref_ws06.values())
    ref_ws07   = {'ws0.7_crowding2_n12_Ndisk55.png': 55,
                  'ws0.7_crowding2_n13_Ndisk58.png': 58,
                  'ws0.7_crowding2_n30_Ndisk54.png': 54,
                  'ws0.7_crowding2_n39_Ndisk56.png': 56,
                  'ws0.7_crowding2_n41_Ndisk57.png': 57}

    ref_ws07_keys = list(ref_ws07.keys())
    ref_ws07_values = list(ref_ws07.values())

    random_index_a1 = randint(0, 4)
    random_index_b1 = randint(0, 4)
    random_index_c1 = randint(0, 4)
    random_index_d1 = randint(0, 4)
    random_index_e1 = randint(0, 4)
    random_index_a2 = randint(0, 4)
    random_index_b2 = randint(0, 4)
    random_index_c2 = randint(0, 4)
    random_index_d2 = randint(0, 4)
    random_index_e2 = randint(0, 4)
    random_index_a3 = randint(0, 4)
    random_index_b3 = randint(0, 4)
    random_index_c3 = randint(0, 4)
    random_index_d3 = randint(0, 4)
    random_index_e3 = randint(0, 4)
    random_index_a4 = randint(0, 4)
    random_index_b4 = randint(0, 4)
    random_index_c4 = randint(0, 4)
    random_index_d4 = randint(0, 4)
    random_index_e4 = randint(0, 4)
    random_index_a5 = randint(0, 4)
    random_index_b5 = randint(0, 4)
    random_index_c5 = randint(0, 4)
    random_index_d5 = randint(0, 4)
    random_index_e5 = randint(0, 4)

    myConsDic = { 'condition0.3.xlsx': [ref_ws03_keys[random_index_a1], ref_ws03_values[random_index_a1], ref_ws04_keys[random_index_b1], ref_ws04_values[random_index_b1], ref_ws05_keys[random_index_c1], ref_ws05_values[random_index_c1], ref_ws06_keys[random_index_d1], ref_ws06_values[random_index_d1], ref_ws07_keys[random_index_e1], ref_ws07_values[random_index_e1]],
                  'condition0.7.xlsx': [ref_ws03_keys[random_index_a2], ref_ws03_values[random_index_a2], ref_ws04_keys[random_index_b2], ref_ws04_values[random_index_b2], ref_ws05_keys[random_index_c2], ref_ws05_values[random_index_c2], ref_ws06_keys[random_index_d2], ref_ws06_values[random_index_d2], ref_ws07_keys[random_index_e2], ref_ws07_values[random_index_e2]],
                  'condition0.6.xlsx': [ref_ws03_keys[random_index_a3], ref_ws03_values[random_index_a3], ref_ws04_keys[random_index_b3], ref_ws04_values[random_index_b3], ref_ws05_keys[random_index_c3], ref_ws05_values[random_index_c3], ref_ws06_keys[random_index_d3], ref_ws06_values[random_index_d3], ref_ws07_keys[random_index_e3], ref_ws07_values[random_index_e3]],
                  'condition0.5.xlsx': [ref_ws03_keys[random_index_a4], ref_ws03_values[random_index_a4], ref_ws04_keys[random_index_b4], ref_ws04_values[random_index_b4], ref_ws05_keys[random_index_c4], ref_ws05_values[random_index_c4], ref_ws06_keys[random_index_d4], ref_ws06_values[random_index_d4], ref_ws07_keys[random_index_e4], ref_ws07_values[random_index_e4]],
                  'condition0.4.xlsx': [ref_ws03_keys[random_index_a5], ref_ws03_values[random_index_a5], ref_ws04_keys[random_index_b5], ref_ws04_values[random_index_b5], ref_ws05_keys[random_index_c5], ref_ws05_values[random_index_c5], ref_ws06_keys[random_index_d5], ref_ws06_values[random_index_d5], ref_ws07_keys[random_index_e5], ref_ws07_values[random_index_e5]]}

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