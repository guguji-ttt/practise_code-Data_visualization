import csv
import plotly.express as px
import pandas as pd

import matplotlib.pyplot as plt

###中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


filename = 'test/data/world_fires_1_day.csv'
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
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    #从文件中获得经度，纬度和火灾强度
    lats, lons, brightnesses = [], [], []
    for row in reader:
        lat = float(row[0])
        lon = float(row[1])
        brightness = float(row[2])
        lats.append(lat)
        lons.append(lon)
        brightnesses.append(brightness)
    
    #打印温度信息列表    
    #print(brightnesses)

####################利用matplotlib绘制    
#绘制散点图
plt.style.use('ggplot')
fig, ax =plt.subplots()
scatter = ax.scatter(x=lats, y=lons, 
        c=brightnesses,
        s=[b/10 for b in brightnesses],  # 大小按火灾强度缩放
        cmap='hot_r',  # 使用热力图颜色
        alpha=0.5,  # 半透明效果
        edgecolors='none',  # 无边框
        )

# 添加颜色条
cbar = plt.colorbar(scatter)
cbar.set_label('火灾温度 (K)')

# 设置图形属性
ax.set_xlabel('经度')
ax.set_ylabel('纬度')
ax.set_title('全球火灾分布热力图')
ax.grid(True, linestyle='--', alpha=0.5)

# plt.tight_layout()
plt.show()

####################利用plotly绘制

data =pd.DataFrame(
    data=zip(lons, lats, brightnesses), columns=['经度', '纬度', '火灾强度']
)
data.head()

####绘制图表
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    width=1600,
    height=1600,
    title='全球火灾热源散点图',
    size='火灾强度',
    size_max=10,
    color='火灾强度',
)
fig.write_html('test/data/global_fire.html')
fig.show()