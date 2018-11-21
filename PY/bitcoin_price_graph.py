"""Project:PSIT:Bitcoin Price Graph 2 year previous"""
import csv
import pygal as pg
def getfile():
    #get in input from data base in CSV 
    bitcoin_price = open('market-price.csv')
    data_price = csv.reader(bitcoin_price)
    # "table" is store data that compound with 2 part [date:price]
    # "table" is contained price information from 20/11/2016 to 19/10/2018
    table = [row for row in data_price]
    sepparate(table)
def sepparate(table):
    #price is bitcoin price list from 20/11/2016 to 19/11/2018 
    price = [float(s[1]) for s in table]
    date = []
    # determine the day to plot to graph in chart.x_labels
    for i in range(0, len(table)):
        date.append(table[i][0][:10])
    #------------------------------------------------------
    chart = pg.Line(x_label_rotation=20, x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True, truncate_label=100)
    # Chart title
    chart.title = 'Bitcoin price from 20 Nov 2016 - 19 Nov 2018'
    # X-Axis Label is the day from 20/11/2016 to 19/11/2018
    chart.x_labels = date
    # Y-Axis and label
    chart.add('price(US Dollar)', price, dots_size = 0.5, fill=True)
    # Range of Y-Axis value
    chart.range = [1,20000]
    # Save chart into file
    chart.render_to_file('chart.svg')

getfile()
