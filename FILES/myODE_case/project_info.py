"""
General:
system dynamics of a rectangular payload (xp,yp,theta_p)
hanged on 2 hanging points (x1,y1) (x2,y2) which can move freely.

Purpose:
show animation
investigate stability

The problem:
-3 D.O.F,
-4 inputs as U=(x1,y1) (x2,y2)
-system variables are geometric and structural parameters
-non-conservative forces are aerodynamic drag forces (neglecting moments),
   and structural damping (assumed as damping from cables springs, and from friction in hang points)

Desired framework:
python 3
solving the dynamics by odeint()
recording each run outputs to csv file
transmiting some selected data online during simulation run
  recieving by client which display graphics , tables, and graphs. with user interaction.

using :
Pandas and Numpy (for data analysis) (considering MapReduced and more..)
ZeroMQ (for data messaging communications)
doxygen documantation

"""
################
# imports of Scientific libraries and others

import  numpy           as      np
from    numpy           import  sin       # for better later code readability
from    numpy           import  cos       # for better later code readability
from    scipy.integrate import  odeint
from    math            import  sqrt
from    random          import  randint

import  matplotlib.pyplot       as      plt
from    mpl_toolkits.mplot3d    import  Axes3D
from    matplotlib.patches      import  FancyArrowPatch, Circle, Rectangle
import  mpl_toolkits.mplot3d.art3d as   art3d
from    mpl_toolkits.mplot3d    import  proj3d

import quadSys              # the dynamic model
################

trialVar = quadSys.quadSys()
trialVar.setDimensionalParametrs()
trialVar.setNonDimensionalParameters()
trialVar.setInitialState()
trialVar.setIntegrationTimeVector()
trialVar.setU()
trialVar.setEnvironmentFactors()
trialVar.integrateSystem()

stateSol   = trialVar.stateSol
timeVector = trialVar.timeVector

##################################

def plot_environment():
    # Figure #1
    fig = plt.figure(figsize=(13, 8))
    ax  = fig.gca()
    ax.scatter(stateSol[0], stateSol[2], s=20, c='b') #stateSol[:,0]

    # LumpedMass payload
    lumpedPayload = Circle((stateSol[0,0], stateSol[0,0]), 13)
    Circle.set_color(lumpedPayload, '0.75')
    Circle.set_alpha(lumpedPayload, 0.1)
    ax.add_patch(lumpedPayload)

    # rectangular payload
    rectPayload = Rectangle((stateSol[0,0], stateSol[0,0]),13 , 20)
    Rectangle.set_color(rectPayload, '0.75')
    Rectangle.set_alpha(rectPayload, 0.1)
    ax.add_patch(rectPayload)

    return ax

def axAddStarts(ax):
    # Some stars (real stars should *NOT* move so quickly!)
    ax.set_axis_bgcolor('#060A49')
    for k in range(50):
        fact = 1
        rangeX = 15
        rangeY = 25
        X = randint(-rangeX * fact , rangeX * fact)
        Y = randint(-rangeY * fact * 2, rangeY * fact * 2)
        # Z = randint(-500000 * 2, 4000000 * 2)
        ax.scatter(X, Y, s=0.1, marker='x', c='white')

# ax = plot_environment()
# axAddStarts(ax)

def plot_Phase_Space(x, xDot, xLb='', xDtLb='', title = 'Phase-Space plot'):
    # 2nd Figure - phase plot
    fig = plt.figure(figsize=(13, 8))
    ax  = fig.gca()
    ax.scatter(x, xDot, s=20, c='y')
    plt.xlabel(xLb)
    plt.ylabel(xDtLb)
    plt.title(title)
    # title
    # axes

plot_Phase_Space(stateSol[:,0] , stateSol[:,1], xLb='x', xDtLb='x dot') # todo: option to combine the 3 in 1 fig
plot_Phase_Space(stateSol[:,2] , stateSol[:,3], xLb='y', xDtLb='y dot')
plot_Phase_Space(stateSol[:,4] , stateSol[:,5], xLb='theta', xDtLb='theta dot')

def plot_Var_Vs_Time(y,t, lgndStr='', title='Var vs Time'):
    #3rd figure
    fig = plt.figure(figsize=(13, 8))
    ax  = fig.gca()
    plt.plot(t, y, 'g', label=lgndStr)
    plt.legend(loc='best')
    plt.xlabel('t')
    # plt.ylabel(title)
    plt.title(title)
    plt.grid()

plot_Var_Vs_Time(stateSol[:,2], timeVector, lgndStr='yp(t)' , title='y vs time')

# # 4th Figure
# fig = plt.figure(figsize=(13, 8))
# ax  = fig.gca()
# plt.plot(timeVector, stateSol[:, 2], 'g', label='yp(t)')
# plt.legend(loc='best')
# plt.xlabel('t')
# plt.grid()

plt.show()


# # Spaceship's orbit
# for k in range(10, len(x), 2270):
#     i = (k - 10) // 2270
#
#     ax.view_init(elev=i / 5, azim=i / 2)
#     ax.set_axis_off()
#     ax.set_xlim(0, 4 * 10 ** 8)
#     ax.set_ylim(-0.5 * 10 ** 8, 3 * 10 ** 8)
#     ax.set_zlim(-500000, 4000000)
#
#     # Moon
#     moon = ax.scatter(x[k], y[k], z[k], s=200, c='gray', marker='o')
#     ax.plot(x[:k], y[:k], z[:k], 'gray', linestyle='dashed', linewidth=0.4)
#
#     # Spaceship
#     spaceship = ax.scatter(a[k], b[k], c[k], s=50, c='red', marker='+')
#     ax.plot(a[:k], b[:k], c[:k], color='red', linestyle='dotted', linewidth=0.2)
#     if i < 10:
#         plt.savefig('animation_three_body/img00' + str(i) + '.png')
#     elif i < 100:
#         plt.savefig('animation_three_body/img0' + str(i) + '.png')
#     else:
#         plt.savefig('animation_three_body/img' + str(i) + '.png')
#     moon.remove()
#     spaceship.remove()
