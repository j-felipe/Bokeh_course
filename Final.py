import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool,CategoricalColorMapper ,Slider, Button
import sys
from bokeh.io import  curdoc
from bokeh.layouts import column 


file_data = r'C:\Users\HP\projects\Bokeh_course\data\gapminder_tidy.csv'
df = pd.read_csv(file_data)
source = ColumnDataSource(df)

#print (df_1970.describe(include = "all"))

mapper = CategoricalColorMapper(factors=['South Asia','Europe & Central Asia', 'Middle East & North Africa','Sub-Saharan Africa',
                                'America','East Asia & Pacific'],palette= ['red','green','blue','gray','yellow','black'])

p = figure(title='1970', x_axis_label='Fertility (children per woman)', y_axis_label='Life Expectancy (years)',
           plot_height=400, plot_width=700,
           tools=[HoverTool(tooltips='@Country')])

p.circle(x='fertility', y='life', source=source,
            color = {'field':'region','transform':mapper}, legend='region')


# creating an slider

slider = Slider(start = 1970, end= 2010, step= 1, value =1970, title='year')
# Button to stop the server
button = Button(label="Stop", button_type="success")


# defining a callback function
#  button to stop the server
def button_callback():
    sys.exit()
# Slider to change the data
def update_plot (attr, old, new):
    yr =slider.value
    
    file_data = r'C:\Users\HP\projects\Bokeh_course\data\gapminder_tidy.csv'
    df = pd.read_csv(file_data)
    
    is_year=df['Year']== yr               # filtering data by 'year' == 1970 
    data_year = df[is_year]
    
    new_data = ColumnDataSource(data_year)  
    #print (new_data.data['fertility']) 
    source.data = {'fertility': new_data.data['fertility'] , 'life': new_data.data['life'], 'region': new_data.data['region'], 'Country': new_data.data['Country'] }
    #print (source.data['fertility'])
    p.title.text = str(yr)
    
# add  a callback to its value
slider.on_change('value', update_plot)
button.on_click(button_callback)

layout =  column(slider,p,button)

curdoc().add_root(layout)

# Example with range Create the figure: plot
#plot = figure(title='Gapminder Data for 1970', plot_height=400, plot_width=700,  x_range=(xmin, xmax), y_range=(ymin, ymax))