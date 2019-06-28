import numpy as np 
import matplotlib.pyplot as plt
from math import atan2, pi
from matplotlib.patches import Ellipse
from scipy.spatial import distance

def drawEllipse (e_posi, ka, kb, crowding_cons, newWindowSize, loop_number): 
    """
    This function allows to draw more than one ellipse. The parameter is 
    a list of coordinate (must contain at least two coordinates)
    The direction of ellipses are only radial direction,
    """
    eccentricities = []
    for i in range(len(e_posi)):
        eccentricities0 = distance.euclidean(e_posi[i], (0,0))
        eccentricities.append(eccentricities0)

    angle_deg = []
    for ang in range(len(e_posi)):
        angle_rad0 = atan2(e_posi[ang][1],e_posi[ang][0])
        angle_deg0 = angle_rad0*180/pi
        angle_deg.append(angle_deg0)
    my_e = [Ellipse(xy=e_posi[j], width=eccentricities[j]*ka*2, height=eccentricities[j]*kb*2, angle = angle_deg[j])
            for j in range(len(e_posi))]
    
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    for e in my_e:
        ax.add_artist(e)
        e.set_clip_box(ax.bbox)
        e.set_alpha(np.random.rand())
        e.set_facecolor(np.random.rand(3))
    ax.set_xlim([-800, 800])
    ax.set_ylim([-500, 500])
    ax.set_title('c_%s_wS_%s_eS_%s_%s_E.png' %(crowding_cons,newWindowSize,ka,kb))
    try:
        loop_number
    except NameError:
        var_exists = False
    else:
        var_exists = True
        plt.savefig('%s_c_%s_wS_%s_eS_%s_%s_E.png' %(loop_number,crowding_cons,newWindowSize,ka,kb))

# call the function
eposi = [(-90.0, -60.0), (140.0, 110.0), (-110.0, 150.0), (-140.0, -160.0), (130.0, -20.0), (200.0, 10.0), (200.0, -100.0), (120.0, 180.0), (-230.0, -50.0), (-200.0, 50.0), (-40.0, -140.0), (-220.0, 170.0), (-190.0, 0.0), (140.0, -130.0), (10.0, 120.0), (-100.0, 90.0), (60.0, 160.0), (30.0, 100.0), (-110.0, -10.0), (70.0, -160.0), (220.0, -50.0), (-160.0, -80.0), (250.0, -180.0), (-60.0, 170.0), (70.0, -80.0), (210.0, 110.0), (0.0, -120.0), (-90.0, -170.0), (-20.0, 130.0), (130.0, 50.0), (-160.0, 90.0), (100.0, -60.0), (-70.0, -80.0), (120.0, 10.0), (100.0, -140.0), (-240.0, -180.0), (50.0, 90.0), (80.0, 70.0), (30.0, -140.0), (-100.0, 40.0), (-110.0, -40.0), (-40.0, 100.0), (220.0, 60.0), (-50.0, -90.0), (-120.0, 20.0), (-60.0, 80.0), (50.0, -90.0)]
drawEllipse(e_posi = eposi, ka = 0.25, kb = 0.1, crowding_cons = 0, newWindowSize= 0.5, loop_number=1)







def drawEllipseT (e_posi, ka, kb, crowding_cons, newWindowSize, loop_number): 
    """
    This function allows to draw more than one ellipse. The parameter is 
    a list of coordinate (must contain at least two coordinates)
    The direction of ellipses are only radial direction,
    """
    eccentricities = []
    for i in range(len(e_posi)):
        eccentricities0 = distance.euclidean(e_posi[i], (0,0))
        eccentricities.append(eccentricities0)

    angle_deg = []
    for ang in range(len(e_posi)):
        angle_rad0 = atan2(e_posi[ang][1],e_posi[ang][0])
        angle_deg0 = angle_rad0*180/pi + 90
        angle_deg.append(angle_deg0)
    my_e = [Ellipse(xy=e_posi[j], width=eccentricities[j]*ka*2, height=eccentricities[j]*kb*2, angle = angle_deg[j]+90)
            for j in range(len(e_posi))]
    
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    for e in my_e:
        ax.add_artist(e)
        e.set_clip_box(ax.bbox)
        e.set_alpha(np.random.rand())
        e.set_facecolor(np.random.rand(3))
    ax.set_xlim([-800, 800]) #TODO
    ax.set_ylim([-500, 500]) #TODO
    ax.set_title('c_%s_wS_%s_eS_%s_%s_E.png' %(crowding_cons,newWindowSize,ka,kb))
    try:
        loop_number
    except NameError:
        var_exists = False
    else:
        var_exists = True
        plt.savefig('%s_c_%s_wS_%s_eS_%s_%s_E.png' %(loop_number,crowding_cons,newWindowSize,ka,kb))

def drawEllipse_full(e_posi):
        """
        This function allows to draw more than one ellipse. The parameter is 
        a list of coordinate (must contain at least two coordinates)
        The radial and tangential ellipses for the same coordinates are drawn.
        """
        eccentricities = []
        for i in range(len(e_posi)):
            eccentricities0 = distance.euclidean(e_posi[i], (0,0))
            eccentricities.append(eccentricities0)
        #radial
        angle_deg = []
        for ang in range(len(e_posi)):
            angle_rad0 = atan2(e_posi[ang][1],e_posi[ang][0])
            angle_deg0 = angle_rad0*180/pi
            angle_deg.append(angle_deg0)
        my_e = [Ellipse(xy=e_posi[j], width=eccentricities[j]*ka*2, height=eccentricities[j]*kb*2, angle = angle_deg[j])
                for j in range(len(e_posi))]
        
        #tangential
        angle_deg2 = []
        for ang in range(len(e_posi)):
            angle_rad0_2 = atan2(e_posi[ang][1],e_posi[ang][0])
            angle_deg0_2 = angle_rad0_2*180/pi + 90
            angle_deg2.append(angle_deg0_2)
        my_e2 = [Ellipse(xy=e_posi[j], width=eccentricities[j]*ka*2, height=eccentricities[j]*kb*2, angle = angle_deg[j]+90)
                for j in range(len(e_posi))]
        
        fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
        for e in my_e:
            ax.add_artist(e)
            e.set_clip_box(ax.bbox)
            e.set_alpha(np.random.rand())
            e.set_facecolor(np.random.rand(3))
        for e2 in my_e2:
            ax.add_artist(e2)
            e2.set_clip_box(ax.bbox)
            e2.set_alpha(np.random.rand())
            e2.set_facecolor(np.random.rand(3))
        ax.set_xlim([-800, 800])
        ax.set_ylim([-500, 500])
        ax.set_title('wS_%s_eS_%s_%s_E.png' %(newWindowSize,ka,kb))
        try:
            loop_number
        except NameError:
            var_exists = False
        else:
            var_exists = True
            plt.savefig('%s_wS_%s_eS_%s_%s_E.png' %(loop_number,newWindowSize,ka,kb))
