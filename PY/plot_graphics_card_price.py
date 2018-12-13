"""Project:PSIT:Graphics Card Price"""
import csv
import pygal as pg
from pygal.style import NeonStyle
def getfile():
    #get in input from data base in CSV 
    graphics_price = open('Graphics_Card_Price.csv')
    data_price = csv.reader(graphics_price)
    # "table" is store data that compound with 6 part [GPU : MSRP: April 2017 : November 2017 : January 2018 : May 2018]
    table = [row for row in data_price]
    sepparate(table)
def sepparate(table):
    """convert string to integer"""
    price = [[s[0], s[1], s[2], s[3], s[4], s[5]] for s in table]
    for i in range(1, len(price)):
        for j in range(1, 6):
            if price[i][j] != "":
                if "," in price[i][j][1:-1]:
                    price[i][j] = int(price[i][j].replace(",", "")[1:-1])
                elif "," not in price[i][j][1: -1]:
                    price[i][j] = int(price[i][j][1:-1])
            else:
                price[i][j] = None
        print(price[i])
    #--------------------Nvidia GPU Price----------------------------------
    chart = pg.Line(fill=True, style=NeonStyle ,interpolate='hermite', interpolation_parameters={'type': 'kochanek_bartels', 'b': -1, 'c': 1, 't': 1}, truncate_legend=40, legend_at_bottom=True, truncate_label=100, show_x_guides=True)
    # Chart title
    chart.title = 'Nvidia Graphics Card Price on Peak of Bitcoin'
    # X-Axis Label is the day from may 2017 - may 2018
    chart.x_labels = price[0][1:]
        # Y-Axis and label
    for i in range(1, 8):
        chart.add(price[i][0], price[i][1:], dots_size = 8.5)
    # Range of Y-Axis value
    chart.range = [1, 1200]
    # Save chart into file
    chart.render_to_file('price_nvidia.svg')

    #----------------------AMD GPU Price------------------

    chart2 = pg.Line(fill=True, style=NeonStyle, interpolate='hermite', interpolation_parameters={'type': 'kochanek_bartels', 'b': -1, 'c': 1, 't': 1}, truncate_legend=40, legend_at_bottom=True, truncate_label=100, show_x_guides=True)
    # chart2 title
    chart2.title = 'AMD Radeon Graphics Card Price on Peak of Bitcoin'
    # X-Axis Label is the day from may 2017 - may 2018
    chart2.x_labels = price[0][1:]
        # Y-Axis and label
    for i in range(8, 14):
        chart2.add(price[i][0], price[i][1:], dots_size = 8.5)
    # Range of Y-Axis value
    chart2.range = [1, 1200]
    # Save chart2 into file
    chart2.render_to_file('price_amd.svg')

getfile()