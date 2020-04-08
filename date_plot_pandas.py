#! /usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
dir=f'/Users/stevenzhang/Downloads/ticker_fixed_raw_monthly_sales/d1553426-51fb-4a7b-87a0-21f2c5e3aea8.csv'
df = pd.read_csv(dir)
df['year']=df['year'].map(lambda  x:str(x))
df['month']=df['month'].map(lambda  x:str(x))
df['year'].str.cat(df['month'],sep='-')
df['date']=df['year']+'-'+df['month']
df['date'] = pd.to_datetime(df['date'], format ='%Y-%m')
print(df.dtypes)
print(df)
plt.title(f"monthly sales of ticker_{2222}")
plt.xlabel('Date (2017-11 to 2019-10)')
plt.ylabel('SALES unit: billion ふウェ絵rgJPY')
plt.plot(df['date'],df['sales'])
plt.xticks(rotation=40)  # 这里是调节横坐标的倾斜度，rotation是度数
plt.show()
plt.close()
