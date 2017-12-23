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

################

# system parameters
# dimensional variables
g       =   9.81        # [m/s^2]
k1      =   200.0       # [kg/m^3?] arbitrary given constant
L01     =   1.0         # [m]
mp      =   1.0         # [kg]
hp      =   1*L01       # [m]
wp      =   2*L01       # [m]
omegaS  =   sqrt(k1/mp) # [?]

# non-dimensional variables
gamma       = g * mp / L01 / k1
Ip          =   1./3. * ((hp/wp)**2 + 1) * ((wp/L01)**2)      # geometry of rectangle with 2 wp width, and 2 hp height
alpha       =   1. / Ip
AmatArray   =   np.array([[ 1,   0  ,0      ],
                          [ 0,  -1  ,0      ],
                          [ 0,   0  ,alpha  ]])
Amat        =   np.asmatrix(AmatArray)        # pointer ref to AmatArray

# AmatArray[0, 0] = 5
# Amat = np.mat("1,0,0; 0,-1,0; 0,0,alpha")
print "value of A is : \n", Amat

# ro = 1.225 # [?]

# initial state
xp0       = wp;
yp0       = -(0.5*gamma+hp+1);
theta_p0  = 0;
xpVel0       =0;
ypVel0       =0;
theta_pVel0  =0;

X0 = [xp0, xpVel0, yp0, ypVel0, theta_p0, theta_pVel0]

#######################################

# input U (platform movements)
stopTime    = 50  # [sec]  #simStopTime
# ?? deltaTime   = 0.01  # [sec]
numOfPoints = 10000
timeVector  = np.linspace(0, stopTime, num=numOfPoints+1)

omegaPlatform   = 2#sqrt(2)     # [Hz * omegaS]
forceFactor = 0.0011
x1              = [0 * np.sin(omegaPlatform * t) for t in timeVector]   #list return type
y1              = forceFactor * np.sin(omegaPlatform * timeVector)    #ndarray return type
# x1[i]=0;
# y1=0;
x2=2*wp #
# x2 = x1 + 2*wp;
y2=y1;

# wind velocities
vi=[ [ 0,0 ] ,
     [ 0 , 0 ] ]  # list of (u,v) for each platform i


def EOM(X, t, a, b):
    '''
    state X is : xp,yp,theta_p
    funtion is X''[t] = f(X,t,params)
    variable time-dependent inputs : x1,x2,y1,y2
    X[0] = xp
    X[1] = X[0]'
    X[2] = yp
    X[3] = X[2]'
    X[4] = theta_p
    X[5] = X[4]'
     -->
    X[0]' = X[1]
    X[1]' = X[0]''
    X[2]' = X[3]
    X[3]' = X[2]''
    X[4]' = X[5]
    X[5]' = X[4]''
    '''

    xp      = X[0]
    yp      = X[2]
    theta_p = X[4]

    # tIndex = find
    tIndex=0

    dxpx1 = xp - x1[tIndex]
    dxpx2 = xp - x2#[tIndex]
    dypy1 = yp - y1[tIndex]
    dypy2 = yp - y2[tIndex]

    dx1     =  sin(theta_p) * hp + cos(theta_p) * wp - dxpx1
    dy1     = -sin(theta_p) * wp + cos(theta_p) * hp + dypy1

    dx2     =  sin(theta_p) * hp - cos(theta_p) * wp - dxpx2
    dy2     =  sin(theta_p) * wp + cos(theta_p) * hp + dypy2

    term1   = wp * ( - sin(theta_p) * dxpx1 + cos(theta_p) * dypy1 ) +  \
              hp * ( + sin(theta_p) * dypy1 + cos(theta_p) * dxpx1 )

    term2   = wp * ( - sin(theta_p) * dxpx2 - cos(theta_p) * dypy2 ) +  \
              hp * ( - sin(theta_p) * dypy2 - cos(theta_p) * dxpx2 )

    DX1 = 1 - 1 / sqrt(dx1**2 + dy1**2)
    DX2 = 1 - 1 / sqrt(dx2**2 + dy2**2)

    # current version with no aerpdynamic and dumping forces and moments.. <TODO>
    derivX    = [0 for i in range(6)]
    AeroMat   = [0, 0, 0]       #todo : set those to relevant values
    DumpingMat= [0, 0, 0]    #

    derivX[0] = X[1]
    derivX[1] = 1 * DX1 * dx1 + 1 * DX2 * dx2 - AeroMat[0] - DumpingMat[0];
    derivX[2] = X[3]
    derivX[3] = -1 * DX1 * dy1 - 1 * DX2 * dy2 - gamma  - AeroMat[1] - DumpingMat[1];
    derivX[4] = X[5]
    derivX[5] = alpha * DX1 * term1 - alpha * DX2 * term2  - AeroMat[2] - DumpingMat[2];

    return derivX

#
# -4 inputs as U=(x1,y1) (x2,y2)
# -system variables are geometric and structural parameters
# -non-conservative forces are aerodynamic drag forces (neglecting moments),
#    and structural damping (assumed as damping from cables springs, and from friction in hang points)

a=0
b=0

stateSol = odeint(EOM, X0, timeVector, args=(a, b))

# pass
##################################

# x, y, z, a, b, c, dx, dy, dz, da, db, dc = orbit.T

# Figure
fig = plt.figure(figsize=(13, 8))
ax  = fig.gca()
ax.scatter(stateSol[0], stateSol[2], s=20, c='b') #stateSol[:,0]

# LumpedMass payload
lumpedPayload = Circle((stateSol[0,0], stateSol[0,0]), 13)
Circle.set_color(lumpedPayload, '0.75')
Circle.set_alpha(lumpedPayload, 0.1)
ax.add_patch(lumpedPayload)
# art3d.pathpatch_2d_to_3d(plane, z=0, zdir="z")

# rectangular payload
rectPayload = Rectangle((stateSol[0,0], stateSol[0,0]),13 , 20)
Rectangle.set_color(rectPayload, '0.75')
Rectangle.set_alpha(rectPayload, 0.1)
ax.add_patch(rectPayload)
# art3d.pathpatch_2d_to_3d(plane, z=0, zdir="z")


def axAddStarts(ax):
    # Some stars (real stars should *NOT* move so quickly!)
    ax.set_axis_bgcolor('#060A49')
    for k in range(50):
        fact = 10**8
        fact = 1
        rangeX = 15
        rangeY = 25
        X = randint(-rangeX * fact , rangeX * fact)
        Y = randint(-rangeY * fact * 2, rangeY * fact * 2)
        # Z = randint(-500000 * 2, 4000000 * 2)
        ax.scatter(X, Y, s=0.1, marker='x', c='white')

axAddStarts(ax)

# exit(1)

# 2nd Figure - phase plot
fig = plt.figure(figsize=(13, 8))
ax  = fig.gca()
ax.scatter(stateSol[:,0], stateSol[:,2], s=20, c='y')

fig = plt.figure(figsize=(13, 8))
ax  = fig.gca()
# plt.plot(timeVector, stateSol[:, 0], 'b', label='xp(t)')
plt.plot(timeVector, stateSol[:, 3], 'g', label='yp(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
# plt.show()

# 4th Figure
fig = plt.figure(figsize=(13, 8))
ax  = fig.gca()

# plt.plot(timeVector, stateSol[:, 0], 'b', label='xp(t)')
plt.plot(timeVector, stateSol[:, 2], 'g', label='yp(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()

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
