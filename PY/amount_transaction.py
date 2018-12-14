import csv
import pygal as pg
from pygal.style import DarkSolarizedStyle
def getfile():
    #get in input from data base in CSV 
    bitcoin_user = open('C:\\Users\\User\\Desktop\\projectpsit\\transations\\n-transactions.csv')
    data_user = csv.reader(bitcoin_user)
    # "table" is store data that compound with 2 part [date:search percent]
    # "table" is contained user information from 3/1/2009 to 26/11/2018
    table = [row for row in data_user]
    print(table)
    sepparate(table)
def sepparate(table):
    #user is bitcoin user list from 3/1/2009 to 19/11/2018 
    user = [int(table[s][1][:-2]) for s in range(len(table))]
    date = [table[s][0][:table[s][0].find(" ")] for s in range(len(table))]

    # determine the day to plot to graph in chart.x_labels
    #------------------------------------------------------
    chart = pg.Bar(style= DarkSolarizedStyle, x_label_rotation=20, x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True, truncate_label=100)
    # Chart title
    chart.title = 'Amount of transactions each day'
    # X-Axis Label is the day from 3/1/2016 to 19/11/2018
    chart.x_labels = date
    # Y-Axis and label
    chart.add( "User", user, rounded_bars=3)
    # Range of Y-Axis value
    chart.range = [1,430000]
    # Save chart into file
    chart.render_to_file('C:\\Users\\User\\Desktop\\projectpsit\\transations\\amount_transaction_graph.svg')

getfile()
