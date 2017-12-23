"""
General:
description of payload hanging on two quadrotros. noted as the hang points.

Purpose:
set the E.O.M of this system payload setup

System constructed out of:
-3 D.O.F,
-4 inputs as U=(x1,y1) (x2,y2)
-system variables are geometric and structural parameters
-non-conservative forces are aerodynamic drag forces (neglecting moments),
   and structural damping (assumed as damping from cables springs, and from friction in hang points)

"""
################
#import project_info

import  numpy           as      np
from    numpy           import  sin       # for better later code readability
from    numpy           import  cos       # for better later code readability
from    scipy.integrate import  odeint
from    math            import  sqrt
from    random          import  randint
################

class quadSys:
    def setDimensionalParametrs(self,*args):
        # system parameters
        # dimensional variables
        self.g       =   9.81        # [m/s^2]
        self.k1      =   200.0       # [kg/m^3?] arbitrary given constant
        self.L01     =   1.0         # [m]
        self.mp      =   1.0         # [kg]
        self.hp      =   1*self.L01             # [m]
        self.wp      =   2*self.L01             # [m]
        self.omegaS  =   sqrt(self.k1/self.mp)  # [?]
        # ro = 1.225 # [?]

    def setNonDimensionalParameters(self):
        # non-dimensional variables
        self.gamma       = self.g * self.mp / self.L01 / self.k1
        # by geometry of rectangle with 2 wp width, and 2 hp height :
        self.Ip          =   1./3. * ((self.hp/self.wp)**2 + 1) * ((self.wp/self.L01)**2)
        self.alpha       =   1. / self.Ip
        # AmatArray   =   np.array([[ 1,   0  ,0      ],
        #                           [ 0,  -1  ,0      ],
        #                           [ 0,   0  ,alpha  ]])
        # Amat        =   np.asmatrix(AmatArray)        # pointer ref to AmatArray

        # # AmatArray[0, 0] = 5
        # # Amat = np.mat("1,0,0; 0,-1,0; 0,0,alpha")
        # print "value of A is : \n", Amat

    def setU(self):
        '''
        conditioned with the timeVector
        :return:
        '''
        omegaPlatform = 2  # sqrt(2)     # [Hz * omegaS]
        forceFactor   = 0.0011
        self.x1 = [0 * np.sin(omegaPlatform * t) for t in self.timeVector]  # list return type
        self.y1 = forceFactor * np.sin(omegaPlatform * self.timeVector)  # ndarray return type
        self.x2 = 2 * self.wp  #        # x2 = x1 + 2*wp;
        self.y2 = self.y1;

    def setInitialState(self):
        '''

        :return:
         X0
        '''
        # initial state
        xp0            = self.wp;
        yp0            = -(0.5*self.gamma+self.hp+1);
        theta_p0       = 0;
        xpVel0         = 0;
        ypVel0         = 0;
        theta_pVel0    = 0;

        self.X0 = [xp0, xpVel0, yp0, ypVel0, theta_p0, theta_pVel0]

    def setIntegrationTimeVector(self):
        '''

        :return: timeVector
        '''
        # input U (platform movements)
        stopTime    = 50  # [sec]  #simStopTime
        # ?? deltaTime   = 0.01  # [sec]
        numOfPoints = 10000
        self.timeVector  = np.linspace(0, stopTime, num=numOfPoints+1)

    def setEnvironmentFactors(self):
        '''
        such as wind interference
        and structural dumping factors
        :return:
        '''
        # wind velocities
        vi=[ [ 0,0 ] ,
             [ 0 , 0 ] ]  # list of (u,v) for each platform i


    def EOM(self, X, t, a, b):
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

        :return:
        derivX - time derivative of state X in time t
        '''

        xp      = X[0]
        yp      = X[2]
        theta_p = X[4]

        hp = self.hp
        wp = self.wp

        # tIndex = find
        tIndex=0

        dxpx1 = xp - self.x1[tIndex]
        dxpx2 = xp - self.x2#[tIndex]
        dypy1 = yp - self.y1[tIndex]
        dypy2 = yp - self.y2[tIndex]

        ###

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

        ###

        derivX[0] = X[1]
        derivX[1] = 1 * DX1 * dx1 + 1 * DX2 * dx2 - AeroMat[0] - DumpingMat[0];
        derivX[2] = X[3]
        derivX[3] = -1 * DX1 * dy1 - 1 * DX2 * dy2 - self.gamma  - AeroMat[1] - DumpingMat[1];
        derivX[4] = X[5]
        derivX[5] = self.alpha * DX1 * term1 - self.alpha * DX2 * term2  - AeroMat[2] - DumpingMat[2];

        return derivX

    def integrateSystem(self):
        #
        # -4 inputs as U=(x1,y1) (x2,y2)
        # -system variables are geometric and structural parameters
        # -non-conservative forces are aerodynamic drag forces (neglecting moments),
        #    and structural damping (assumed as damping from cables springs, and from friction in hang points)

        a=0
        b=0

        self.stateSol = odeint(self.EOM, self.X0, self.timeVector, args=(self,a))

