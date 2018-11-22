"""Project:PSIT:Blockchain Wallet Users Graph overtime"""
import csv
import pygal as pg
def getfile():
    #get in input from data base in CSV 
    blockchain_user_csv = open('bitcoin_user.csv')
    data_wallet = csv.reader(blockchain_user_csv)
    # "table" is store data that compound with 2 part [date:blockchain wallet user]
    # "table" is contained blockchain user information from 29/11/2012 to 22/11/2018
    table = [row for row in data_wallet]
    sepparate(table)
def sepparate(table):
    #blockchain_user is Blockchain Wallet Users list from 20/11/2011 to 19/11/2018 
    blockchain_user = [int(s[1]) for s in table]
    date = []
    # determine the day to plot to graph in chart.x_labels
    for i in range(0, len(table)):
        date.append(table[i][0][:table[i][0].find(" ")])
    #------------------------------------------------------
    chart = pg.Line(x_label_rotation=20, x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True, truncate_label=100)
    # Chart title
    chart.title = 'Blockchain Wallet Users'
    # X-Axis Label is the day from 29/11/2011 to 19/11/2018
    chart.x_labels = date
    # Y-Axis and label
    chart.add('Blockchain User', blockchain_user)
    # Range of Y-Axis value
    chart.range = [1,32000000]
    # Save chart into file
    chart.render_to_file('blockchain_user.svg')

getfile()
