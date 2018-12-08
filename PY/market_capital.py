"""Project:PSIT:Top 10 alternative cryptocurrency in pie graph"""
import csv
import pygal as pg
def getfile():
    #get in input from data base in CSV 
    market_capital_csv = open('market_capital.csv')
    data_capital = csv.reader(market_capital_csv)
    # "table" is store data that compound with 10 part 
    # [Ranking : Name : Symbol : Market capital : Price : Transaction : Volume : %1h : %2h : %7d]
    table = [row for row in data_capital]
    sepparate(table)
def sepparate(table):
    #Summary of Cryptocurrency in 2017 by market capital
    top10marketcap_name = []
    top10marketcap_symbol = []
    top10marketcap_captital = []
    top10marketcap_price = []
    blank = ""
    #append data to list prepare for plot gragh
    for i in range(1, 12):
        top10marketcap_name.append(table[i][1])
        top10marketcap_symbol.append(table[i][2])
        #make string from raw data to integer by cutting off "$" and backspace from data and append
        top10marketcap_captital.append(int(table[i][3][1:].rstrip(" ").replace(",", "")))
        top10marketcap_price.append(table[i][4][1:])
    other_cryto = (sum(top10marketcap_captital)-top10marketcap_captital[0])
    other_cryto = float("%.2f"%other_cryto)
    #------------------------------------------------------
    pie_chart = pg.Pie(inner_radius=.4, truncate_legend=40, legend_at_bottom=True, truncate_label=100)
    pie_chart.title = 'Market capital of cryptocurrency'
    pie_chart.add('Other', other_cryto)
    for i in range(1, 11):
        pie_chart.add(top10marketcap_name[i], (top10marketcap_captital[i])//1)
    pie_chart.render_to_file('market_cap.svg')

getfile()
