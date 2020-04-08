# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:08:22 2017

@author: Administrator
"""

import csv

from matplotlib import pyplot as plt

filename = '/Users/stevenzhang/Downloads/store_sales_distribution_fixed_raw_dailysplit.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #dates, highs, lows = [],[],[]
    store_name_code, sales = [], []
    counter=1
    for row in reader:
        # try:
            #print(row[0],row[1])
            #current_date = datetime.strptime(row[0], "%Y-%m-%d")
            #store_name_code=row[0]
        if counter<=2000:
            store_name_code.append(counter)
            sales.append(row[1])
        else:
            break
        counter+=1
        # except ValueError:
        #     #print(current_date, 'missing data')
        #     pass
        # else:
        #     # dates.append(current_date)
        #     store_name_code.append(store_name_code)
        #     sales.append(sales)

    #print(store_name_code, sales)



# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
#处的实参alpha 指定颜色的透明度。 Alpha 值为0表示完全透明，
#1（ 默认设置） 表示完全不透明
plt.plot(store_name_code,sales, c='red', alpha=0.5)
#plt.plot(store_name_code, lows, c='blue', alpha=0.5)

# 设置图形的格式
plt.title("store sales distribution", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Number(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
