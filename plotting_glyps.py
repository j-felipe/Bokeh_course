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

##### Patches ########

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
##### Columns Datasource ########

from bokeh.models import ColumnDataSource

source=ColumnDataSource(data ={'x':[1,2,3,4,5],'y':[8,6,5,2,3]}) # source data should be the same length
print (source.data)
from bokeh.sampledata.iris import flowers as df   # data source from pandas 
source1=ColumnDataSource(df)
print (source1.data)
 