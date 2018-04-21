"""
from
http://www.scipy-lectures.org/packages/3d_plotting/index.html

check also
http://code.enthought.com/pages/mayavi-project.html

"""

#%matplotlib wx
import mayavi.mlab as mlab

'''
 Points in 3D, represented with markers (or “glyphs”) and optionaly different sizes.
'''
x, y, z, value = np.random.random((4, 40))
mlab.points3d(x, y, z, value)

'''
A line connecting points in 3D, with optional thickness and varying color.
'''
mlab.clf()  # Clear the figure
t = np.linspace(0, 20, 200)
mlab.plot3d(np.sin(t), np.cos(t), 0.1*t, t)



import numpy as np

r, theta = np.mgrid[0:10, -np.pi:np.pi:10j]
x = r * np.cos(theta)
y = r * np.sin(theta)
z = np.sin(r)/r

mlab.mesh(x, y, z, colormap='gist_earth', extent=[0, 1, 0, 1, 0, 1])
mlab.mesh(x, y, z, extent=[0, 1, 0, 1, 0, 1], \
 representation='wireframe', line_width=1, color=(0.5, 0.5, 0.5))


mlab.colorbar(Out[7], orientation='vertical')
mlab.title('polar mesh')
mlab.outline(Out[7])
mlab.axes(Out[7])



from traits.api import HasTraits, Instance
from traitsui.api import View, Item, HGroup
from mayavi.core.ui.api import SceneEditor, MlabSceneModel

def curve(n_turns):
    "The function creating the x, y, z coordinates needed to plot"
    phi = np.linspace(0, 2*np.pi, 2000)
    return [np.cos(phi) * (1 + 0.5*np.cos(n_turns*phi)),
            np.sin(phi) * (1 + 0.5*np.cos(n_turns*phi)),
            0.5*np.sin(n_turns*phi)]


class Visualization(HasTraits):
    "The class that contains the dialog"
    scene   = Instance(MlabSceneModel, ())

    def __init__(self):
        HasTraits.__init__(self)
        x, y, z = curve(n_turns=2)
        # Populating our plot
        self.plot = self.scene.mlab.plot3d(x, y, z)

    # Describe the dialog
    view = View(Item('scene', height=300, show_label=False,
                    editor=SceneEditor()),
                HGroup('n_turns'), resizable=True)

# Fire up the dialog
Visualization().configure_traits()
