# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:43:19 2019

@author: MiaoLi
"""
import os
import pandas as pd

# =============================================================================
# path and files
# =============================================================================
path = "./"
files = os.listdir(path) 

# we need only .png
imageFiles = []
[imageFiles.append(file) for file in files if file.lower().endswith('.png')]

# =============================================================================
# separate each windowsize
# =============================================================================
[ws03, ws04, ws05, ws06, ws07 ] = [[] for i in range(5)]
[ws03_21, ws03_22, ws03_23, ws03_24, ws03_25,ws04_31, ws04_32, ws04_33, ws04_34, ws04_35, \
 ws05_41, ws05_42, ws05_43, ws05_44, ws05_45, ws06_49, ws06_50, ws06_51, ws06_52, ws06_53,\
 ws07_54, ws07_55, ws07_56, ws07_57, ws07_58] = [[] for i in range(25)] 

[ws03.append(file) for file in imageFiles if file.lower().startswith('ws0.3')]
[ws04.append(file) for file in imageFiles if file.lower().startswith('ws0.4')]
[ws05.append(file) for file in imageFiles if file.lower().startswith('ws0.5')]
[ws06.append(file) for file in imageFiles if file.lower().startswith('ws0.6')]
[ws07.append(file) for file in imageFiles if file.lower().startswith('ws0.7')]


[ws03_21.append(f) for f in imageFiles if f.lower().endswith('21.png')]
[ws03_22.append(f) for f in imageFiles if f.lower().endswith('22.png')]
[ws03_23.append(f) for f in imageFiles if f.lower().endswith('23.png')]
[ws03_24.append(f) for f in imageFiles if f.lower().endswith('24.png')]
[ws03_25.append(f) for f in imageFiles if f.lower().endswith('25.png')]

[ws04_31.append(f) for f in imageFiles if f.lower().endswith('31.png')]
[ws04_32.append(f) for f in imageFiles if f.lower().endswith('32.png')]
[ws04_33.append(f) for f in imageFiles if f.lower().endswith('33.png')]
[ws04_34.append(f) for f in imageFiles if f.lower().endswith('34.png')]
[ws04_35.append(f) for f in imageFiles if f.lower().endswith('35.png')]

[ws05_41.append(f) for f in imageFiles if f.lower().endswith('41.png')]
[ws05_42.append(f) for f in imageFiles if f.lower().endswith('42.png')]
[ws05_43.append(f) for f in imageFiles if f.lower().endswith('43.png')]
[ws05_44.append(f) for f in imageFiles if f.lower().endswith('44.png')]
[ws05_45.append(f) for f in imageFiles if f.lower().endswith('45.png')]

[ws06_49.append(f) for f in imageFiles if f.lower().endswith('49.png')]
[ws06_50.append(f) for f in imageFiles if f.lower().endswith('50.png')]
[ws06_51.append(f) for f in imageFiles if f.lower().endswith('51.png')]
[ws06_52.append(f) for f in imageFiles if f.lower().endswith('52.png')]
[ws06_53.append(f) for f in imageFiles if f.lower().endswith('53.png')]

[ws07_54.append(f) for f in imageFiles if f.lower().endswith('54.png')]
[ws07_55.append(f) for f in imageFiles if f.lower().endswith('55.png')]
[ws07_56.append(f) for f in imageFiles if f.lower().endswith('56.png')]
[ws07_57.append(f) for f in imageFiles if f.lower().endswith('57.png')]
[ws07_58.append(f) for f in imageFiles if f.lower().endswith('58.png')]
# =============================================================================
# write to excels
# =============================================================================
columNames = ['imageFile', 'N_disk', 'CrowdingCons']

ws03df = pd.DataFrame({columNames[0]:ws03_21 + ws03_22 + ws03_23 + ws03_24 + ws03_25})
ws04df = pd.DataFrame({columNames[0]:ws04_31 + ws04_32 + ws04_33 + ws04_34 + ws04_35})
ws05df = pd.DataFrame({columNames[0]:ws05_41 + ws05_42 + ws05_43 + ws05_44 + ws05_45})
ws06df = pd.DataFrame({columNames[0]:ws06_49 + ws06_50 + ws06_51 + ws06_52 + ws06_53})
ws07df = pd.DataFrame({columNames[0]:ws07_54 + ws07_55 + ws07_56 + ws07_57 + ws07_58})

ws03_ndisk = [21]*10 + [22]*10 + [23]*10 + [24]*10 + [25]*10
ws04_ndisk = [31]*10 + [32]*10 + [33]*10 + [34]*10 + [35]*10
ws05_ndisk = [41]*10 + [42]*10 + [43]*10 + [44]*10 + [45]*10
ws06_ndisk = [49]*10 + [50]*10 + [51]*10 + [52]*10 + [53]*10
ws07_ndisk = [54]*10 + [55]*10 + [56]*10 + [57]*10 + [58]*10

crowdingcon = [0]*5 + [1]*5 + [0]*5 + [1]*5 + [0]*5 + [1]*5 + [0]*5 + [1]*5 + [0]*5 + [1]*5

ws03df['N_disk'] = ws03_ndisk
ws04df['N_disk'] = ws04_ndisk
ws05df['N_disk'] = ws05_ndisk
ws06df['N_disk'] = ws06_ndisk
ws07df['N_disk'] = ws07_ndisk

ws03df['CrowdingCons'] = crowdingcon
ws04df['CrowdingCons'] = crowdingcon
ws05df['CrowdingCons'] = crowdingcon
ws06df['CrowdingCons'] = crowdingcon
ws07df['CrowdingCons'] = crowdingcon



writer = pd.ExcelWriter('condition0.3.xlsx', engine = 'xlsxwriter')
ws03df.to_excel(writer, index = False)
writer.save()

writer = pd.ExcelWriter('condition0.4.xlsx', engine = 'xlsxwriter')
ws04df.to_excel(writer, index = False)
writer.save()

writer = pd.ExcelWriter('condition0.5.xlsx', engine = 'xlsxwriter')
ws05df.to_excel(writer, index = False)
writer.save()

writer = pd.ExcelWriter('condition0.6.xlsx', engine = 'xlsxwriter')
ws06df.to_excel(writer, index = False)
writer.save()

writer = pd.ExcelWriter('condition0.7.xlsx', engine = 'xlsxwriter')
ws07df.to_excel(writer, index = False)
writer.save()
