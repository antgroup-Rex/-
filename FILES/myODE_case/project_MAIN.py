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

# plotting package elements
import  matplotlib.pyplot       as      plt
from    mpl_toolkits.mplot3d    import  Axes3D
from    matplotlib.patches      import  FancyArrowPatch, Circle, Rectangle
import  mpl_toolkits.mplot3d.art3d as   art3d
from    mpl_toolkits.mplot3d    import  proj3d

# local packages or classes
import quadSys              # the dynamic model
import gui_plots            # the custom plots for me
import data_handlers        # file outputs functions

##################################
# the physics definitions and integration of ODE for solution 

quads = quadSys.quadSys()
quads.setDimensionalParametrs()
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
data_handlers.simulation_data_to_csv(timeVector, stateSol, "quad_sim.csv")

##################################
# conduct plots

fig1 = gui_plots.plot_Phase_Space(stateSol[:,0] , stateSol[:,1], xLb='x', xDtLb='x dot') # todo: option to combine the 3 in 1 fig
fig2 = gui_plots.plot_Phase_Space(stateSol[:,2] , stateSol[:,3], xLb='y', xDtLb='y dot')
fig3 = gui_plots.plot_Phase_Space(stateSol[:,4] , stateSol[:,5], xLb='theta', xDtLb='theta dot')

fig4 = gui_plots.plot_Var_Vs_Time(stateSol[:,2], timeVector, lgndStr='yp(t)' , title='y vs time')

print stateSol
fig5 = gui_plots.plot_quad_system_geometry(stateSol, 0)

gui_plots.show_the_constructed_plots()

