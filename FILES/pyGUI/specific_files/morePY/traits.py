"""
from http://www.scipy-lectures.org/packages/traits/index.html
"""
#####################
from traits.api import HasTraits, Str, Float, Range, Instance, \
                        DelegatesTo, Event, Property, PrototypedFrom, \
                        Enum, List
from traitsui.api import View, Item, Group, VGroup


class IrrigationArea(HasTraits):
    name = Str
    surface = Float(desc='Surface [ha]')
    crop = Enum('Alfalfa', 'Wheat', 'Cotton')

class Turbine(HasTraits):
    turbine_type = Str
    power = Float(1.0, desc='Maximal power delivered by the turbine [Mw]')


class Reservoir(HasTraits):

    name = Str
#    max_storage = Float(100, desc='description for trait float variable')
    max_storage = Float(1e6, desc='Maximal storage [hm3]')
    max_release = Float(10, desc='Maximal release [m3/s]')
    head        = Float(10, desc='Hydraulic head [m]')
    efficiency  = Range(0, 1.)
    irrigated_areas = List(IrrigationArea)

    turbine = Instance(Turbine)
    installed_capacity = PrototypedFrom('turbine', 'power')
    
    total_crop_surface = Property(depends_on='irrigated_areas.surface')
    
    def _get_total_crop_surface(self):
        return sum([iarea.surface for iarea in self.irrigated_areas])

    
    def energy_production(self, release):
        ''' Returns the energy production [Wh] for the given release [m3/s]
        '''
        power = 1000 * 9.81 * self.head * release * self.efficiency
        return power * 3600
    
    traits_view = View(
        Item('name'),
        Item('max_storage'),
        Item('max_release'),
        Item('head'),
        Item('efficiency'),
        Item('irrigated_areas'),
        Item('total_crop_surface'),
        resizable = True
    )
    
    traits_view2 = View(
        'name', 'max_storage', 'max_release', 'head', 'efficiency',
        title = 'Reservoir',
        resizable = True,
    )
    
    
    def _name_default(self):
        """ Complex initialisation of the reservoir name. """
        return 'Undefined'
    
    def _max_storage_default(self):
        """ Complex initialisation of the reservoir name. """
        return 123456

reservoir0 = Reservoir()
print reservoir0.name
print reservoir0.max_storage
reservoir0.edit_traits()  # The Traits library is also aware of user interfaces and can pop up a default view for the Reservoir class
print reservoir0.name
print reservoir0.max_storage

reservoir = Reservoir(name='Lac de Vouglans', max_storage=605)
print reservoir.name
print reservoir.max_storage
#print reservoir.name.default_value
#print reservoir.max_storage.default_value_type



if __name__ == '__main__':
    turbine = Turbine(turbine_type='type1', power=5.0)
    
    upper_block = IrrigationArea(name='Section C', surface=2000, crop='Wheat')
    
    reservoir = Reservoir(
                        name = 'Project A',
                        max_storage = 30,
                        max_release = 100.0,
                        head = 60,
                        efficiency = 0.8,
                        turbine = turbine,
                        irrigated_areas=[upper_block]
                    )

    print 'installed capacity is initialised with turbine.power'
    print reservoir.installed_capacity

    print '-' * 15
    print 'updating the turbine power updates the installed capacity'
    turbine.power = 10
    print reservoir.installed_capacity

    print '-' * 15
    print 'setting the installed capacity breaks the link between turbine.power'
    print 'and the installed_capacity trait'

    reservoir.installed_capacity = 8
    print turbine.power, reservoir.installed_capacity
    
    release = 80
    print 'Releasing {} m3/s produces {} kWh'.format(
                        release, reservoir.energy_production(release)
                    )
    
    
    reservoir.configure_traits()  # awaits for the user to finish inputs. 

if 1==2:
    # Every trait does validation when the user tries to set its content:
    reservoir.max_storage = '230' 
#####################

class ReservoirState(HasTraits):
    """Keeps track of the reservoir state given the initial storage.
    """
    reservoir = Instance(Reservoir, ())
    name = DelegatesTo('reservoir')
#    min_storage = Float
    max_storage = DelegatesTo('reservoir')
    min_release = Float
    max_release = DelegatesTo('reservoir')

#    # state attributes
#    storage = Range(low='min_storage', high='max_storage')

    # state attributes
    storage = Property(depends_on='inflows, release')
    
    # control attributes
    inflows =  Float(desc='Inflows [hm3]')
    release = Range(low='min_release', high='max_release')
#    spillage = Float(desc='Spillage [hm3]')
    spillage = Property(
            desc='Spillage [hm3]', 
            depends_on=['storage', 'inflows', 'release']
        )
    ### Private traits.
    _storage = Float
    
      ### Traits view
    traits_view = View(
        Group(
            VGroup(Item('name'), Item('storage'), Item('spillage'),
                label = 'State', style = 'readonly'
            ),
            VGroup(Item('inflows'), Item('release'), label='Control'),
        )
    )
    
      ### Traits property implementation.
    def _get_storage(self):
        new_storage = self._storage - self.release + self.inflows
        return min(new_storage, self.max_storage)

    def _set_storage(self, storage_value):
        self._storage = storage_value

    def _get_spillage(self):
        new_storage = self._storage - self.release  + self.inflows
        overflow = new_storage - self.max_storage
        return max(overflow, 0)    
    
    update_storage = Event(desc='Updates the storage to the next time step')

    def _update_storage_fired(self):
        # update storage state
        new_storage = self.storage - self.release  + self.inflows
        self.storage = min(new_storage, self.max_storage)
        overflow = new_storage - self.max_storage
#        self.spillage = max(overflow, 0)

    @on_trait_change('storage')
    def print_state(self):
        print 'Storage\tRelease\tInflows\tSpillage'
        str_format = '\t'.join(['{:7.2f}'for i in range(4)])
        print str_format.format(self.storage, self.release, self.inflows,
                self.spillage)
        print '-' * 79

    ### Traits listeners ###########
    def _release_changed(self, new):
        """When the release is higher than zero, warn all the inhabitants of
        the valley.
        """

        if new > 0:
            print 'Warning, we are releasing {} hm3 of water'.format(new)

def wake_up_watchman_if_spillage(new_value):
    if new_value > 0:
        print 'Wake up watchman! Spilling {} hm3'.format(new_value)
        
if __name__ == '__main__':
    projectA = Reservoir(
            name = 'Project A',
            max_storage = 30,
            max_release = 100.0,
            hydraulic_head = 60,
            efficiency = 0.8
        )

    state = ReservoirState(reservoir=projectA, storage=10)
    
    #register the dynamic listener
    state.on_trait_change(wake_up_watchman_if_spillage, name='spillage')
    
    state.release = 90
    state.inflows = 0
    state.print_state()

    print 'How do we update the current storage ?'
    
    print 'Forcing spillage'
    state.inflows = 100
    state.release = 0

    print 'Why do we have two executions of the callback ?'
    
    state = ReservoirState(reservoir=projectA, storage=25)
    state.release = 4
    state.inflows = 0

    state.print_state()
    state.configure_traits()


if __name__ == '__main__':
    print "entering project B"
    print "******************"
    
    projectB = Reservoir(
        name = 'Project B',
        max_storage = 30,
        max_release = 5.0,
        hydraulic_head = 60,
        efficiency = 0.8
    )

    state = ReservoirState(reservoir=projectB, storage=15)
    state.release = 5
    state.inflows = 0

    # release the maximum amount of water during 3 time steps
    state.update_storage = True
    state.print_state()
    state.update_storage = True
    state.print_state()
    state.update_storage = True
    state.print_state()

#####################
