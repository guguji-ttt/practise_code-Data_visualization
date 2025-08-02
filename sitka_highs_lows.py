import csv
from datetime import datetime

import matplotlib.pyplot as plt

###中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)#生成一个阅读器对象
    header_row = next(reader)
    #调用next,会返回下一行内容，
    # （这里从文件头开始，返回第一行内容）
    
    #输出csv文件第一行
    #print(header_row)
    
    '''
    #获取文件头的索引
    # 得知索引2,5为日期和最高温
    #enumerate函数返回列表的索引及其索引值
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    '''
    
        
    #从文件获得最高温,最低温和日期
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
    #打印温度信息列表    
    #print(highs)
    
    #根据最高温和最低温绘制图形
    plt.style.use('ggplot')
    fig, ax =plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    #设置图形格式
    ax.set_title("2018年每日最高和最低气温", fontsize=24)
    ax.set_xlabel('', fontsize=24)
    fig.autofmt_xdate()#绘制倾斜日期
    ax.set_ylabel('温度(F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
    '''
    #该样式可以复用
    #example
    tick_style = {'axis':'both', 'which':'major', 'labelsize':16}
    ax.tick_params(**tick_style)
    '''
    #plt.savefig('chart/sitka_fill_high&lows_2018.png', dpi=300, bbox_inches='tight')
    plt.show()