# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:15:33 2019
This code calculated the generated display's properties (spacing, convexHull, occupancyArea, 
average eccentricity...). And test if the properties for generated stimuli are normal 
distributed.

@author: MiaoLi
"""
import pandas as pd
import Func_CharacterizeStimuli
import os
# sys.path.insert(0, r'C:\Users\MiaoLi\Desktop\SCALab\Programming\Crowding_and_numerosity\Idea1\Stimuli190429\rawStimuli')

# =============================================================================
# input
# =============================================================================
# folderPath = '.\\folder_currentPath\\'
# folderPath = '..\\folder_beforePath\\'
folderPath = '..\\..\\Crowding_and_numerosity\\MatchingAlgorithm\\Idea1\\Stimuli190429\\InputAllStimuliwithProperties\\'
dic_files = {(0.7,1):folderPath +'Idea1_allStimuliInfo_ws0.7_crowdingcon1.xlsx',
             (0.7,0):folderPath +'Idea1_allStimuliInfo_ws0.7_crowdingcon0.xlsx',
             (0.6,1):folderPath +'Idea1_allStimuliInfo_ws0.6_crowdingcon1.xlsx',
             (0.6,0):folderPath +'Idea1_allStimuliInfo_ws0.6_crowdingcon0.xlsx',
             (0.5,1):folderPath +'Idea1_allStimuliInfo_ws0.5_crowdingcon1.xlsx',
             (0.5,0):folderPath +'Idea1_allStimuliInfo_ws0.5_crowdingcon0.xlsx',
             (0.4,1):folderPath +'Idea1_allStimuliInfo_ws0.4_crowdingcon1.xlsx',
             (0.4,0):folderPath +'Idea1_allStimuliInfo_ws0.4_crowdingcon0.xlsx',
             (0.3,1):folderPath +'Idea1_allStimuliInfo_ws0.3_crowdingcon1.xlsx',
             (0.3,0):folderPath +'Idea1_allStimuliInfo_ws0.3_crowdingcon0.xlsx'}

#define the constrains
properties = []
for condition, file in dic_files.items():
    if condition[1] == 0:#constrains according to noCrowding conditions
        properties.append(Func_CharacterizeStimuli.characterizeStimuli(condition[0],condition[1]))

# =============================================================================
# Stimuli folder
# =============================================================================
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


# folderOutputPath = "./OutputMatchedStimili/"
folderOutputPath = '..\\..\\Crowding_and_numerosity\\MatchingAlgorithm\\Idea1\\Stimuli190429\\OutputMatchedStimili\\'
createFolder(folderOutputPath)
# =============================================================================
# functions i need
# =============================================================================
def matchStimuli(ws, crowdingcons, filename):
    
    #read excel
    stimuliInfo_df=pd.read_excel(filename,index_col=0)
    
    #each condition take 5 numerosities
    if ws == 0.7:
        stimuliInfo_df_a = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 54, :]
        stimuliInfo_df_b = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 55, :]
        stimuliInfo_df_c = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 56, :]
        stimuliInfo_df_d = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 57, :]
        stimuliInfo_df_e = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 58, :]

        std_densi = properties[0][2]
        std_sp    = properties[0][4]
        std_aE    = properties[0][3]
        std_cH    = properties[0][5]
        std_oA    = properties[0][6]
        
        df = properties[0][1].loc[['density', 'averageE', 'avg_spacing','convexHull', 'occupancyArea'], [54, 55, 56, 57, 58]]
        df_density = df.loc[['density']]
        df_aE = df.loc[['averageE']]
        df_sp = df.loc[['avg_spacing']]
        df_cH = df.loc[['convexHull']]
        df_oA = df.loc[['occupancyArea']]
        
        desi_mean = df_density.values.tolist()[0]
        aE_mean = df_aE.values.tolist()[0]
        sp_mean = df_sp.values.tolist()[0]
        cH_mean = df_cH.values.tolist()[0]
        oA_mean = df_oA.values.tolist()[0]
        
        
    elif ws == 0.6:
        stimuliInfo_df_a = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 49, :]
        stimuliInfo_df_b = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 50, :]
        stimuliInfo_df_c = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 51, :]
        stimuliInfo_df_d = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 52, :]
        stimuliInfo_df_e = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 53, :]
        
        std_densi = properties[1][2]
        std_sp    = properties[1][4]
        std_aE    = properties[1][3]
        std_cH    = properties[1][5]
        std_oA    = properties[1][6]
        
        df = properties[1][1].loc[['density', 'averageE', 'avg_spacing','convexHull', 'occupancyArea'], [49, 50, 51, 52, 53]]
        df_density = df.loc[['density']]
        df_aE = df.loc[['averageE']]
        df_sp = df.loc[['avg_spacing']]
        df_cH = df.loc[['convexHull']]
        df_oA = df.loc[['occupancyArea']]
        
        desi_mean = df_density.values.tolist()[0]
        aE_mean = df_aE.values.tolist()[0]
        sp_mean = df_sp.values.tolist()[0]
        cH_mean = df_cH.values.tolist()[0]
        oA_mean = df_oA.values.tolist()[0]

    elif ws == 0.5:
        stimuliInfo_df_a = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 41, :]
        stimuliInfo_df_b = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 42, :]
        stimuliInfo_df_c = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 43, :]
        stimuliInfo_df_d = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 44, :]
        stimuliInfo_df_e = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 45, :]

        std_densi = properties[2][2]
        std_sp    = properties[2][4]
        std_aE    = properties[2][3]
        std_cH    = properties[2][5]
        std_oA    = properties[2][6]
        
        df = properties[2][1].loc[['density', 'averageE', 'avg_spacing','convexHull', 'occupancyArea'], [41, 42, 43, 44, 45]]
        df_density = df.loc[['density']]
        df_aE = df.loc[['averageE']]
        df_sp = df.loc[['avg_spacing']]
        df_cH = df.loc[['convexHull']]
        df_oA = df.loc[['occupancyArea']]
        
        desi_mean = df_density.values.tolist()[0]
        aE_mean = df_aE.values.tolist()[0]
        sp_mean = df_sp.values.tolist()[0]
        cH_mean = df_cH.values.tolist()[0]
        oA_mean = df_oA.values.tolist()[0]
    elif ws == 0.4:
        stimuliInfo_df_a = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 31, :]
        stimuliInfo_df_b = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 32, :]
        stimuliInfo_df_c = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 33, :]
        stimuliInfo_df_d = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 34, :]
        stimuliInfo_df_e = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 35, :]
       
        std_densi = properties[3][2]
        std_sp    = properties[3][4]
        std_aE    = properties[3][3]
        std_cH    = properties[3][5]
        std_oA    = properties[3][6]
    
        df = properties[3][1].loc[['density', 'averageE', 'avg_spacing','convexHull', 'occupancyArea'], [31, 32, 33, 34, 35]]
        df_density = df.loc[['density']]
        df_aE = df.loc[['averageE']]
        df_sp = df.loc[['avg_spacing']]
        df_cH = df.loc[['convexHull']]
        df_oA = df.loc[['occupancyArea']]
        
        desi_mean = df_density.values.tolist()[0]
        aE_mean = df_aE.values.tolist()[0]
        sp_mean = df_sp.values.tolist()[0]
        cH_mean = df_cH.values.tolist()[0]
        oA_mean = df_oA.values.tolist()[0]
    elif ws == 0.3:
        stimuliInfo_df_a = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 21, :]
        stimuliInfo_df_b = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 22, :]
        stimuliInfo_df_c = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 23, :]
        stimuliInfo_df_d = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 24, :]
        stimuliInfo_df_e = stimuliInfo_df.loc[stimuliInfo_df.N_disk == 25, :]
        
        std_densi = properties[4][2]
        std_sp    = properties[4][4]
        std_aE    = properties[4][3]
        std_cH    = properties[4][5]
        std_oA    = properties[4][6]
        
        df = properties[4][1].loc[['density', 'averageE', 'avg_spacing','convexHull', 'occupancyArea'], [21, 22, 23, 24, 25]]
        df_density = df.loc[['density']]
        df_aE = df.loc[['averageE']]
        df_sp = df.loc[['avg_spacing']]
        df_cH = df.loc[['convexHull']]
        df_oA = df.loc[['occupancyArea']]
        
        desi_mean = df_density.values.tolist()[0]
        aE_mean = df_aE.values.tolist()[0]
        sp_mean = df_sp.values.tolist()[0]
        cH_mean = df_cH.values.tolist()[0]
        oA_mean = df_oA.values.tolist()[0]
        
    #set constrains: mean±std
    densi_min_a, densi_max_a = desi_mean[0]-std_densi, desi_mean[0]+std_densi
    aE_min_a, aE_max_a = aE_mean[0]-std_aE, aE_mean[0]+std_aE
    sp_min_a, sp_max_a = sp_mean[0]-std_sp, sp_mean[0]+std_sp
    cH_min_a, cH_max_a = cH_mean[0]-std_cH, cH_mean[0]+std_cH
    oA_min_a, oA_max_a = oA_mean[0]-std_oA, oA_mean[0]+std_oA

    densi_min_b, densi_max_b = desi_mean[1]-std_densi, desi_mean[1]+std_densi
    aE_min_b, aE_max_b = aE_mean[1]-std_aE, aE_mean[1]+std_aE
    sp_min_b, sp_max_b = sp_mean[1]-std_sp, sp_mean[1]+std_sp
    cH_min_b, cH_max_b = cH_mean[1]-std_cH, cH_mean[1]+std_cH
    oA_min_b, oA_max_b = oA_mean[1]-std_oA, oA_mean[1]+std_oA
    
    densi_min_c, densi_max_c = desi_mean[2]-std_densi, desi_mean[2]+std_densi
    aE_min_c, aE_max_c = aE_mean[2]-std_aE, aE_mean[2]+std_aE
    sp_min_c, sp_max_c = sp_mean[2]-std_sp, sp_mean[2]+std_sp
    cH_min_c, cH_max_c = cH_mean[2]-std_cH, cH_mean[2]+std_cH
    oA_min_c, oA_max_c = oA_mean[2]-std_oA, oA_mean[2]+std_oA
    
    densi_min_d, densi_max_d = desi_mean[3]-std_densi, desi_mean[3]+std_densi
    aE_min_d, aE_max_d = aE_mean[3]-std_aE, aE_mean[3]+std_aE
    sp_min_d, sp_max_d = sp_mean[3]-std_sp, sp_mean[3]+std_sp
    cH_min_d, cH_max_d = cH_mean[3]-std_cH, cH_mean[3]+std_cH
    oA_min_d, oA_max_d = oA_mean[3]-std_oA, oA_mean[3]+std_oA

    densi_min_e, densi_max_e = desi_mean[4]-std_densi, desi_mean[4]+std_densi
    aE_min_e, aE_max_e = aE_mean[4]-std_aE, aE_mean[4]+std_aE
    sp_min_e, sp_max_e = sp_mean[4]-std_sp, sp_mean[4]+std_sp
    cH_min_e, cH_max_e = cH_mean[4]-std_cH, cH_mean[4]+std_cH
    oA_min_e, oA_max_e = oA_mean[4]-std_oA, oA_mean[4]+std_oA
    
    # find matched stimuli according to density, averageE and spacing
    DensityConstance_a_df          = stimuliInfo_df_a.loc[(stimuliInfo_df_a['density'] >= densi_min_a)                          & (stimuliInfo_df_a['density'] <=densi_max_a)]
    DensityEconstance_a_df         = DensityConstance_a_df.loc[(DensityConstance_a_df['averageE'] >= aE_min_a)                  & (DensityConstance_a_df['averageE'] <= aE_max_a)]
    DensityEspacConstance_a_df     = DensityEconstance_a_df.loc[(DensityEconstance_a_df['avg_spacing'] >= sp_min_a)             & (DensityEconstance_a_df['avg_spacing'] <= sp_max_a)]
    DensityEspacCHConstance_a_df   = DensityEspacConstance_a_df.loc[(DensityEspacConstance_a_df['convexHull'] >= cH_min_a)      & (DensityEspacConstance_a_df['convexHull']<= cH_max_a)]
    DESCO_a_df                     = DensityEspacCHConstance_a_df.loc[(DensityEspacCHConstance_a_df['occupancyArea']>= oA_min_a)& (DensityEspacCHConstance_a_df['occupancyArea'] <= oA_max_a)] 

    DensityConstance_b_df          = stimuliInfo_df_b.loc[(stimuliInfo_df_b['density'] >= densi_min_b)                          & (stimuliInfo_df_b['density'] <=densi_max_b)]
    DensityEconstance_b_df         = DensityConstance_b_df.loc[(DensityConstance_b_df['averageE'] >= aE_min_b)                  & (DensityConstance_b_df['averageE'] <= aE_max_b)]
    DensityEspacConstance_b_df     = DensityEconstance_b_df.loc[(DensityEconstance_b_df['avg_spacing'] >= sp_min_b)             & (DensityEconstance_b_df['avg_spacing'] <= sp_max_b)]
    DensityEspacCHConstance_b_df   = DensityEspacConstance_b_df.loc[(DensityEspacConstance_b_df['convexHull'] >= cH_min_b)      & (DensityEspacConstance_b_df['convexHull']<= cH_max_b)]
    DESCO_b_df                     = DensityEspacCHConstance_b_df.loc[(DensityEspacCHConstance_b_df['occupancyArea']>= oA_min_b)& (DensityEspacCHConstance_b_df['occupancyArea'] <= oA_max_b)] 
    
    DensityConstance_c_df          = stimuliInfo_df_c.loc[(stimuliInfo_df_c['density'] >= densi_min_c)                          & (stimuliInfo_df_c['density'] <=densi_max_c)]
    DensityEconstance_c_df         = DensityConstance_c_df.loc[(DensityConstance_c_df['averageE'] >= aE_min_c)                  & (DensityConstance_c_df['averageE'] <= aE_max_c)]
    DensityEspacConstance_c_df     = DensityEconstance_c_df.loc[(DensityEconstance_c_df['avg_spacing'] >= sp_min_c)             & (DensityEconstance_c_df['avg_spacing'] <= sp_max_c)]
    DensityEspacCHConstance_c_df   = DensityEspacConstance_c_df.loc[(DensityEspacConstance_c_df['convexHull'] >= cH_min_c)      & (DensityEspacConstance_c_df['convexHull']<= cH_max_c)]
    DESCO_c_df                     = DensityEspacCHConstance_c_df.loc[(DensityEspacCHConstance_c_df['occupancyArea']>= oA_min_c)& (DensityEspacCHConstance_c_df['occupancyArea'] <= oA_max_c)] 
   
    DensityConstance_d_df          = stimuliInfo_df_d.loc[(stimuliInfo_df_d['density'] >= densi_min_d)                          & (stimuliInfo_df_d['density'] <=densi_max_d)]
    DensityEconstance_d_df         = DensityConstance_d_df.loc[(DensityConstance_d_df['averageE'] >= aE_min_d)                  & (DensityConstance_d_df['averageE'] <= aE_max_d)]
    DensityEspacConstance_d_df     = DensityEconstance_d_df.loc[(DensityEconstance_d_df['avg_spacing'] >= sp_min_d)             & (DensityEconstance_d_df['avg_spacing'] <= sp_max_d)]
    DensityEspacCHConstance_d_df   = DensityEspacConstance_d_df.loc[(DensityEspacConstance_d_df['convexHull'] >= cH_min_d)      & (DensityEspacConstance_d_df['convexHull']<= cH_max_d)]
    DESCO_d_df                     = DensityEspacCHConstance_d_df.loc[(DensityEspacCHConstance_d_df['occupancyArea']>= oA_min_d)& (DensityEspacCHConstance_d_df['occupancyArea'] <= oA_max_d)] 

    DensityConstance_e_df          = stimuliInfo_df_e.loc[(stimuliInfo_df_e['density'] >= densi_min_e)                          & (stimuliInfo_df_e['density'] <=densi_max_e)]
    DensityEconstance_e_df         = DensityConstance_e_df.loc[(DensityConstance_e_df['averageE'] >= aE_min_e)                  & (DensityConstance_e_df['averageE'] <= aE_max_e)]
    DensityEspacConstance_e_df     = DensityEconstance_e_df.loc[(DensityEconstance_e_df['avg_spacing'] >= sp_min_e)             & (DensityEconstance_e_df['avg_spacing'] <= sp_max_e)]
    DensityEspacCHConstance_e_df   = DensityEspacConstance_e_df.loc[(DensityEspacConstance_e_df['convexHull'] >= cH_min_e)      & (DensityEspacConstance_e_df['convexHull']<= cH_max_e)]
    DESCO_e_df                     = DensityEspacCHConstance_e_df.loc[(DensityEspacCHConstance_e_df['occupancyArea']>= oA_min_e)& (DensityEspacCHConstance_e_df['occupancyArea'] <= oA_max_e)] 
 

    #combine abcde to same df
    final_df = pd.concat([DESCO_a_df, DESCO_b_df, DESCO_c_df, DESCO_d_df, DESCO_e_df], ignore_index=True)
    #add new coloums to differentiate df in each conditaion
    
    final_df['winsize']=ws
    final_df['crowdingcons']=crowdingcons
    #write to sub excel
    with pd.ExcelWriter(folderOutputPath +'Idea1_DensityEspacConstance_ws%s_crowding%s.xlsx' %(ws, crowdingcons)) as writer:
        final_df.to_excel(writer,sheet_name ='ws%s_crowding%s' %(ws, crowdingcons))
    return final_df

#store all sub df
df_list = []
for condition, filename in dic_files.items():
    sub_df = matchStimuli(condition[0],condition[1],filename)
    # stimuliInfo_df=pd.read_excel(file,index_col=0)
    df_list.append(sub_df)
all_df = pd.concat(df_list)

# write to excel
with pd.ExcelWriter(folderOutputPath +'all.xlsx') as writer:
    all_df.to_excel(writer)
