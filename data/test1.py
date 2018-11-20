"""Project:PSIT:Bitcoin"""
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
    price = [float(s[1]) for s in table]
    date = [str(s[0]) for s in table]
    result_x = [x for x in range(2017, 2019)]
    #define variable to sepparate the data to each mount
    #2017
    """jan2017, feb2017, mar2017, april2017, may2017 ,june2017 ,july2017, aug2017, sep2017, oct2017, nov2017, dec2017 = [], [], [], [], [], [], [], [], [], [], [], []
    jan2018, feb2018, mar2018, april2018, may2018, june2018, july2018, august2018, september2018 = [], [], [], [], [], [], [], [], []
    lst2017, lst2018 = [], []"""
    chart = pg.Line(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True, truncate_label=100)
    # Chart title
    chart.title = 'Bitcoin price from 2017-2018'
    # X-Axis Label
    chart.x_labels = [str(x) for x in result_x]
    # Y-Axis and label
    chart.add('price(US)', price)
    # Range of Y-Axis value
    chart.range = [1, 20000]
    # Save chart into file
    chart.render_to_file('chart.svg')
getfile()
