############################
###Slider and Bokeh server###
##############################
r'''
from bokeh.io import  curdoc
from bokeh.layouts import column 
from bokeh.models import   ColumnDataSource, Slider, CategoricalColorMapper

from bokeh.plotting import figure       #constructor to creates a empty plot with sense
from numpy.random import random

N =300
source = ColumnDataSource(data={'x':random(N), 'y': random(N)})

# Creates plot and widgets
plot = figure()
plot.circle(x='x',y = 'y', source = source)
slider = Slider(start = 100 , end = 1000, value = N ,step =10, title = 'Number of point' )

# adding the callback to widgets
def callback (attr ,old, new):
    N= slider.value
    source.data={'x':random (N), 'y': random(N)}
slider.on_change('value', callback)
 # arrange plots and widgets  in layouts

layout =  column(slider,plot)

curdoc().add_root(layout)
'''

r'''
############################
###  Dropdown menus and Bokeh server###
##############################

from bokeh.io import  curdoc
from bokeh.layouts import column 
from bokeh.models import   ColumnDataSource, Select, CategoricalColorMapper

from bokeh.plotting import figure       #constructor to creates a empty plot with sense
from numpy.random import random, normal , lognormal

N =1000
source = ColumnDataSource(data={'x':random(N), 'y': random(N)})

# Creates plot and widgets
plot = figure()
plot.circle(x='x',y = 'y', source = source)

menu = Select(options = ['uniform','normal','lognormal'], value = 'uniform', title = 'distribution') # Dropdown "option" Lists of option "value" Default option selected

# adding the callback to widgets
def callback (attr ,old, new):
    if menu.value == 'uniform': f =random
    elif menu.value == 'normal': f= normal
    else:                       f = lognormal
    source.data={'x':f(size=N), 'y': f(size=N)}
menu.on_change('value', callback)
 # arrange plots and widgets  in layouts

layout =  column(menu,plot)

curdoc().add_root(layout)

'''

######################################
### Buttons menus and Bokeh server ###
######################################
r'''
# Strucuture general of button widget
from bokeh.models import Button
button = Button(label='press me')
def update():

 # Do something interesting
button.on_click(update)
'''
r'''
Ejemplo de uso de botones
from bokeh.models import CheckboxGroup, RadioGroup, Toggle
toggle = Toggle(label='Some on/off', button_type='success')
checkbox = CheckboxGroup(labels=['foo', 'bar', 'baz'])
radio = RadioGroup(labels=['2000', '2010', '2020'])
def callback(active):
# Active tells which button is active

# Import CheckboxGroup, RadioGroup, Toggle from bokeh.models
from bokeh.models import CheckboxGroup, RadioGroup, Toggle

# Add a Toggle: toggle
toggle = Toggle(button_type = 'success',label='Toggle button')

# Add a CheckboxGroup: checkbox
checkbox = CheckboxGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add a RadioGroup: radio
radio = RadioGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add widgetbox(toggle, checkbox, radio) to the current document
curdoc().add_root(widgetbox (toggle,checkbox,radio))

'''