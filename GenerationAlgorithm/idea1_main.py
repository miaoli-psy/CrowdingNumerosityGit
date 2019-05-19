# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:56:49 2019

@author: MiaoLi
"""
import time
import idea1_stimuliGeneration_a0428
# https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/5-pool/
import multiprocessing as mp
from functools import partial

# =============================================================================
# run with pool
# =============================================================================
start = time.time()
multiParaFunc = partial(idea1_stimuliGeneration_a0428.runStimuliGeneration,2,0.3,False,0.25,0.1)
# def runStimuliGeneration(crowding_cons, newWindowSize, visualization = False, ka = 0.25, kb = 0.1,loop_number=1):
def multicore():
    pool = mp.Pool()
    # https://www.zhihu.com/question/52188800
    # loopnumer == range(1,4)
    pool.map(multiParaFunc, range(1,4)) #range(1,50) runs 49 times from 1 to 49
end = time.time()

runtime = round((end-start)*0.0167,2)
print('This lovely code runs', runtime, 'minutes')
if __name__ == '__main__':
    multicore()


# =============================================================================
# call os to run
# =============================================================================
# import os
# loop_number=1
# start = time.time()
# while(loop_number <= 10):
#     os.system('python xxx.py' + ' ' + str(loop_number))
#     # os.system('start /min python XXX.py' + ' ' + str(loop_number))
#     loop_number += 1
# end = time.time()

# print('time', str(end-start))


