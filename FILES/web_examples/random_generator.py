#import libraries
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from random import randrange

rollNum = 15
axLimit = 11

#create figure
f=figure(x_range=(0,axLimit+1),y_range=(0,axLimit+1))

#create columndatasource
source=ColumnDataSource(data=dict(x=[],y=[],size=[]))

#create glyphs
f.circle(x='x',y='y',size='size',fill_color='olive',line_color='yellow',source=source)
f.line(x='x',y='y',line_color='green',source=source)

#create periodic function
def update():
    print source.data['size']   # returns a list type
    new_data=dict(x=[randrange(1,axLimit)],y=[randrange(1,axLimit)],size=[rollNum+1] )
    source.stream(new_data,rollover=rollNum)
    source.data['size'] = [ x-1 for x in source.data['size'] ]
    #print(source.data)

#add figure to curdoc and configure callback
curdoc().add_root(f)
curdoc().add_periodic_callback(update,300)  # freq of mSec
