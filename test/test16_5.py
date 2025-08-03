import csv
from datetime import datetime

import matplotlib.pyplot as plt
###中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

"""对旧金山某地的气候数据可视化"""

filename = 'test/data/san_area.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        
    #从文件获得最高温,最低温和日期
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
    #根据最高温和最低温绘制图形
    plt.style.use('ggplot')
    fig, ax =plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    #设置图形格式
    ax.set_title("2018年每日最高和最低气温(美国旧金山某地)", 
                 fontsize=20)
    ax.set_xlabel('', fontsize=24)
    fig.autofmt_xdate()#绘制倾斜日期
    ax.set_ylabel('温度(F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()
    