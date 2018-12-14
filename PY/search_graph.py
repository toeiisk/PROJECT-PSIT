import csv
import pygal as pg
from pygal.style import DarkSolarizedStyle
def getfile():
    #get in input from data base in CSV 
    bitcoin_price = open('C:\\Users\\User\\Desktop\\projectpsit\\search_history\\search_history.csv')
    data_price = csv.reader(bitcoin_price)
    # "table" is store data that compound with 2 part [date:search percent]
    # "table" is contained price information from 2/4/2017 to 1/4/2018
    table = [row for row in data_price]
    sepparate(table)
def sepparate(table):
    #price is bitcoin price list from 20/11/2016 to 19/11/2018 
    price = [int(table[s][1]) for s in range(1, len(table)-1)]
    date = [table[s][0] for s in range(1, len(table)-1)]

    # determine the day to plot to graph in chart.x_labels
    #------------------------------------------------------
    chart = pg.Bar(style= DarkSolarizedStyle, x_label_rotation=20, x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True, truncate_label=100)
    # Chart title
    chart.title = 'Interested Rate from Google Trend (May2017-May2018)'
    # X-Axis Label is the day from 20/11/2016 to 19/11/2018
    chart.x_labels = date
    # Y-Axis and label
    chart.add( " Search \"Bitcoin\"", price, rounded_bars=3)
    # Range of Y-Axis value
    chart.range = [1,100]
    # Save chart into file
    chart.render_to_file('C:\\Users\\User\\Desktop\\projectpsit\\search_history\\search_history.svg')

getfile()
