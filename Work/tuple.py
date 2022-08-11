import csv
f=open('C:/Users/cony19980509/Desktop/动手学数据分析/practical-python-master/practical-python-master/Work/Data/portfolio.csv')
rows=csv.reader(f)
next(rows)#如果这个地方用dataframe引入还是有点不同
row=next(rows)
t = (row[0], int(row[1]), float(row[2]))
cost=t[1]*t[2]
name, shares, price = t
