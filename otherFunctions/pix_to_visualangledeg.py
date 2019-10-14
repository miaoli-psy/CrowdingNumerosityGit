# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:28:32 2019

@author: MiaoLi
"""
# =============================================================================
# pix to visual angle
# =============================================================================
from math import atan2, degrees
h = 30 # Monitor height in cm
d = 57 # Distance between monitor and participant in cm
r = 1024 # Vertical resolution of the monitor
size_in_px = 100 # The stimulus size in pixels
# Calculate the number of degrees that correspond to a single pixel. This will
# generally be a very small value, something like 0.03.
deg_per_px = degrees(atan2(.5*h, d)) / (.5*r)
print ('%s degrees correspond to a single pixel' %(deg_per_px))
# Calculate the size of the stimulus in degrees
size_in_deg = size_in_px * deg_per_px
print ('The size of the stimulus is %s pixels and %s visual degrees' % (size_in_px, size_in_deg))

# =============================================================================
# visual angle to pix
# =============================================================================
h = 30 # Monitor height in cm
d = 57 # Distance between monitor and participant in cm
r = 768 # Vertical resolution of the monitor
size_in_deg = 3. # The stimulus size in pixels
# Calculate the number of degrees that correspond to a single pixel. This will
# generally be a very small value, something like 0.03.
deg_per_px = degrees(atan2(.5*h, d)) / (.5*r)
print ('%s degrees correspond to a single pixel' %(deg_per_px))
# Calculate the size of the stimulus in degrees
size_in_px = size_in_deg/deg_per_px
print ('The size of the stimulus is %s pixels and %s visual degrees' \
    %(size_in_px, size_in_deg))
