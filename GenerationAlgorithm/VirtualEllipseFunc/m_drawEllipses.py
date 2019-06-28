import numpy as np 
import matplotlib.pyplot as plt
from math import atan2, pi
from matplotlib.patches import Ellipse
from scipy.spatial import distance

#想改一下这个函数，最简单的，不动原始的函数，新写一个。
#现在这个函数的第一个参数是e_posi要输入两个或以上点的坐标，函数最后画出以这两点为椭圆心的椭圆。
#但是我现在想呈现画椭圆的过程，比如有10个点，我想让它返回10个图片，从第一张到第10张，每张图片上有1-10个点（例如： 第五张图片上有5个点）。 
#此外，现在的图片只有椭圆，我想把中心点也画上去。但是要作为参数，因为有时我想要中心点，有时候我不想要。第三，可以改一下椭圆的颜色吗，现在用的似乎是随机的颜色。
#我想改成一个浅色的，所有椭圆都一个颜色，有些透明度。

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
#    https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.patches.Ellipse.html
    my_e = [Ellipse(xy=e_posi[j], width=eccentricities[j]*ka*2, height=eccentricities[j]*kb*2, angle = angle_deg[j],color='red',fill=None)#color='red',fill=None
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
#eposi = [(-90.0, -60.0), (140.0, 110.0), (-110.0, 150.0), (-140.0, -160.0), (130.0, -20.0), (200.0, 10.0), (200.0, -100.0), (120.0, 180.0), (-230.0, -50.0), (-200.0, 50.0), (-40.0, -140.0), (-220.0, 170.0), (-190.0, 0.0), (140.0, -130.0), (10.0, 120.0), (-100.0, 90.0), (60.0, 160.0), (30.0, 100.0), (-110.0, -10.0), (70.0, -160.0), (220.0, -50.0), (-160.0, -80.0), (250.0, -180.0), (-60.0, 170.0), (70.0, -80.0), (210.0, 110.0), (0.0, -120.0), (-90.0, -170.0), (-20.0, 130.0), (130.0, 50.0), (-160.0, 90.0), (100.0, -60.0), (-70.0, -80.0), (120.0, 10.0), (100.0, -140.0), (-240.0, -180.0), (50.0, 90.0), (80.0, 70.0), (30.0, -140.0), (-100.0, 40.0), (-110.0, -40.0), (-40.0, 100.0), (220.0, 60.0), (-50.0, -90.0), (-120.0, 20.0), (-60.0, 80.0), (50.0, -90.0)]
#drawEllipse(e_posi = eposi, ka = 0.25, kb = 0.1, crowding_cons = 0, newWindowSize= 0.5, loop_number=1)


# call the function
eposi = [(-90.0, -60.0), (140.0, 110.0), (-110.0, 150.0), (-140.0, -160.0)]

def drawProcess(e_posi, ka, kb, crowding_cons, newWindowSize, loop_number):
    curr_eposi = []
    for i_eposi in eposi:
        curr_eposi.append(i_eposi)
        drawEllipse(e_posi = curr_eposi, ka = 0.25, kb = 0.1, crowding_cons = 0, newWindowSize= 0.5, loop_number=1)

drawProcess(e_posi = eposi, ka = 0.25, kb = 0.1, crowding_cons = 0, newWindowSize= 0.5, loop_number=1)

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
