from bokeh.io import output_file, show  #librarys to save the plot html file
from bokeh.plotting import figure       #constructor to creates a empty plot with sense
import numpy as np
from bokeh.sampledata.iris import flowers  # Pandas data frame
x = [1,2,3,4,5]
y=[8,6,5,2,3]


r'''

#####Introduction############
plot  = figure(plot_width=400, tools='pan,box_zoom')     # Creatin simple plot zone 400px height
#plot.circle(x=[1,2,3,4,5], y=[8,6,5,2,3], size = [10,20,30,40,50],color='blue', size=10, alpha=0.8)   #bubble plot
plot.circle(x=[1,2,3,4,5], y=[8,6,5,2,3], color='blue', size=10, alpha=0.8) 
plot.x(x=[1,2,3,4,5], y=[10,12,9,7,4])          #is posible to add any figure (glyps) in any moment
output_file ('circle.html')             #output file
show(plot) 


###### Line Markers ############
plot= figure () 
plot.line(x,y,line_width=3)
plot.circle(x1=[1,2,3,4,5], y1=[8,6,5,2,3], size = [10,20,30,40,50],color='blue', size=10, alpha=0.8)
output_file('line.html')
#show(plot)

###### Combine Glyphs ############

plot= figure () 
plot.line(x,y,line_width=3)
plot.circle(x=[1,2,3,4,5], y=[11,13,4,8,9], size = [10,20,30,40,50],color='blue', alpha=0.8) # alpha transparency
output_file('line.html')
show(plot)

##### Patches ######## Dibujar areas

xs = [[1,1,2,2],[2,2,4],[2,2,3,3]]
ys = [[2,5,5,2],[3,5,5],[2,3,4,2]]
plot = figure()
plot.patches(xs,ys ,fill_color=['red','blue','green'],line_color='white')
show(plot)

##### Data types ########
##### Numpy ########
x= np.linspace(0, 10, 1000)
y = np.sin(x)+np.random.random(1000)*0.2
plot= figure()
plot.line(x,y)
output_file('numpy.html')
show(plot)

##### Pandas data frame ########

plot= figure()
plot.circle(flowers['petal_length'],flowers['sepal_length'],size = 10)
output_file('pandas.html')
show(plot)
'''

r'''
##### Columns Datasource ########

from bokeh.models import ColumnDataSource

source=ColumnDataSource(data ={'x':[1,2,3,4,5],'y':[8,6,5,2,3]}) # source data should be the same length
print (source.data)
from bokeh.sampledata.iris import flowers as df   # data source from pandas 
source1=ColumnDataSource(df)
print (source1.data)
'''

# I.E using datasource ######
#source = ColumnDataSource(df)           # Coverting pandas dataframe in columdatasource
# Add circle glyphs to the figure p
#p.circle('Year', 'Time', size= 8 , color = 'color',  source=source)  ## Columnadata source is used
r'''
##############################################
###### 2020 04 18 customizing glyphs #########
##############################################
plot = figure (tools = 'box_select, lasso_select')          # slecting 'Boxselect and lasso selct tools
# Selected points are painted in red and no selected becomes in gray color
plot.circle('petal_length','sepal_length',selection_color='red',nonselection_fill_alpha=0.2 , nonselection_fill_color = 'grey',source = source1)
#show(plot)
'''
r'''
# Hover tools#
from bokeh.models import HoverTool
hover = HoverTool(tooltips=None, mode='hline')  #'hline' Resalta horizontal 'vline' Resalta Vertical
plot = figure (tools=[hover, 'crosshair'])   #### Creates a hover tool como punto de mira
#p.add_tools(hover) other way to add hover to plot
plot.circle('petal_length','sepal_length',size = 15, hover_color = 'red', source = source1)  # El punto de mira resalta los punto del eje y en rojo
show(plot)
'''

r'''
# color mapper #

from bokeh.models import   CategoricalColorMapper
from bokeh.sampledata.iris import flowers as df   # data source from pandas 
from bokeh.models import ColumnDataSource
source1=ColumnDataSource(df)
mapper = CategoricalColorMapper(factors=['setosa','virginica', 'versicolor'],palette= ['red','green','blue'])   # Define el color de cada specie
plot = figure(x_axis_label = 'petal length', y_axis_label= 'sepal legth')
plot.circle('petal_length','sepal_length',size= 10, source=source1,color = {'field':'species','transform':mapper})   #Se mapea el campo y la vaiable maper
# se puede poner legenda dentro del color usando ---> color=dict(field='origin', transform=color_mapper),legend='origin')
output_file('especies.html')
show(plot)

'''
r'''
####################################
#####  Introdution to layouts ######
####################################

# Row plots

from bokeh.models import   CategoricalColorMapper
from bokeh.sampledata.iris import flowers as df   # data source from pandas 
from bokeh.models import ColumnDataSource
source1=ColumnDataSource(df)

p1 = figure(x_axis_label = 'petal length', y_axis_label= 'sepal legth')
p2 = figure(x_axis_label = 'petal length', y_axis_label= 'sepal legth')
p3 = figure(x_axis_label = 'petal length', y_axis_label= 'sepal legth')

p1.circle('petal_length','sepal_length',size= 10,color = 'red', source=source1)
p2.circle('petal_length','sepal_length',size= 10,color = 'blue', source=source1) 
p3.circle('petal_length','sepal_length',size= 10,color = 'green', source=source1)   

from bokeh.layouts import row 

layout_row= row(p1, p2, p3)    # row function allow create a different plots into same page
output_file = ('row.html')
show(layout_row)

# column  plot 
from bokeh.layouts import column 

layout_column= column(p1, p2, p3)    # row function allow create a different plots into same page
output_file = ('column.html')
show(layout_column)

layout_nested = row(column(p1,p2),p3)
output_file = ('nested.html')
show(layout_nested)
'''

r'''
####################################
#####  advanced layouts ###########
####################################

#grid layout
from bokeh.models import   CategoricalColorMapper
from bokeh.sampledata.iris import flowers as df   # data source from pandas 
from bokeh.models import ColumnDataSource
source1=ColumnDataSource(df)
from bokeh.layouts import row 
from bokeh.layouts import column 


p1 = figure(x_axis_label = 'petal length', y_axis_label= 'sepal legth')
p2 = figure(x_axis_label = 'petal length', y_axis_label= 'sepal legth')
p3 = figure(x_axis_label = 'petal length', y_axis_label= 'sepal legth')

p1.circle('petal_length','sepal_length',size= 10,color = 'red', source=source1)
p2.circle('petal_length','sepal_length',size= 10,color = 'blue', source=source1) 
p3.circle('petal_length','sepal_length',size= 10,color = 'green', source=source1)  

from bokeh.layouts import gridplot

layout = gridplot([[None,p1],[p2,p3]],toolbar_location = None )
output_file('grid.html')
show(layout)

##tabbed layouts

from bokeh.models.widgets import Tabs, Panel

#create a panel with a title for every tab

first = Panel (child = row (p1,p2), title = 'first')
second = Panel (child=row(p3),title='second')
# put the pannels in tab object
# crea una columna que se adapta a la pantalla row2 = row([mpg_hp, mpg_weight], sizing_mode='scale_width')

tabs =  Tabs(tabs=[first,second])
output_file ('tapped.html')
show(tabs)
r'''

r'''
#####################33333
###Linking plotting together
##############################

from bokeh.models import   CategoricalColorMapper
from bokeh.sampledata.iris import flowers as df   # data source from pandas 
from bokeh.models import ColumnDataSource
source1=ColumnDataSource(df)
from bokeh.layouts import row 
from bokeh.layouts import column 


p1 = figure(tools= 'lasso_select,box_select',title = ' petal lenght vs sepal length',x_axis_label = 'petal length', y_axis_label= 'sepal length')
p2 = figure(title = ' petal lenght vs sepal width', x_axis_label = 'petal length', y_axis_label= 'sepal width')
p3 = figure(title = ' petal lenght vs petal width', x_axis_label = 'petal length', y_axis_label= 'petal width')

p1.circle('petal_length','sepal_length',size= 10,color = 'red', source=source1)
p2.circle('petal_length','sepal_width',size= 10,color = 'blue', source=source1) 
p3.circle('petal_length','petal_width',size= 10,color = 'green', source=source1, line_color='red',fill_color=None)

#linking axis

p3.x_range=p2.x_range=p1.x_range
p3.y_range=p2.y_range=p1.y_range

layout = row (p1,p2,p3)

output_file ('linkin.html')
show(layout)            # si se comparte el mismo datasource la seleccion de los datos ve en los otros plots


'''


############################
###Annotation and guides
##############################

from bokeh.models import   CategoricalColorMapper
from bokeh.sampledata.iris import flowers as df   # data source from pandas 
from bokeh.models import ColumnDataSource
source1=ColumnDataSource(df)
from bokeh.layouts import row 
from bokeh.layouts import column 

from bokeh.models import HoverTool

hover = HoverTool (tooltips=[('species name','@species'),
                            ('petal length', '@petal_length'),
                            ('sepal length','@sepal_length') ])

mapper = CategoricalColorMapper(factors=['setosa','virginica', 'versicolor'],palette= ['red','green','blue'])   # Define el color de cada specie
plot = figure(tools = [hover,'pan','wheel_zoom'],x_axis_label = 'petal length', y_axis_label= 'sepal legth')
plot.circle('petal_length','sepal_length',size= 10, source=source1,color = {'field':'species','transform':mapper},legend='species')   #Se mapea el campo y la vaiable maper

plot.legend.location='top_left'
#p.legend.background_fill_color = 'lightgray'

output_file('anotation1.html')
show(plot)




