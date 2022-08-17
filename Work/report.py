# report.py
#
# Exercise 2.4
#直接读入和打开
import csv

portfolio = []
with open((
          'C:/Users/cony19980509/Desktop/动手学数据分析/practical-python-master/practical-python-master/Work/Data/portfolio.csv'),
          'rt') as f:
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        holding = (row[0], int(row[1]), float(row[2]))
        portfolio.append(holding)
#通过设置外部函数和调用的形式
import csv

def read_portfolio(filename):
    portfolio=[]
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

port=read_portfolio('C:/Users/cony19980509/Desktop/动手学数据分析/practical-python-master/practical-python-master/Work/Data/portfolio.csv')

