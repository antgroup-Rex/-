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
# imports 

# Scientific and math libraries 
import  numpy           as      np
from    numpy           import  sin       # for better later code readability
from    numpy           import  cos       # for better later code readability
from    scipy.integrate import  odeint
from    math            import  sqrt
from    random          import  randint

# local packages or classes
import quadSys              # the dynamic model
import data_handlers        # file outputs functions

##################################
# the physics definitions and integration of ODE for solution 

quads = quadSys.quadSys()
quads.setDimensionalParametrs()
quads.setDimensionalParametrs(
                                k1  = 150.0,
                                L01 = 1.0,
                                mp  = 1.0,
                                hp  = 1,
                                wp  = 2)
quads.setDimensionalParametrs(
                                k1  = 150.0,
                                L01 = 1.0,
                                mp  = 1.0,
                                hp  = 1,
                                wp  = 3)

quads.setNonDimensionalParameters()
quads.setInitialState()
quads.setIntegrationTimeVector()
quads.setU()
quads.setEnvironmentFactors()
quads.integrateSystem()  # TODO! : enable inner communication module to transmit selected data outside.

timeVector = quads.timeVector
stateSol   = quads.stateSol

##################################
# output data to a file. for later offline investigations 


headString = quads.getHeaderStringForCSV()
data_handlers.simulation_data_to_csv(timeVector, stateSol, fileStr, headString)

# data_handlers.simulation_data_to_csv(timeVector, stateSol, fileStr)  # dont pass headString: write csv without header line

