import plotly.express as px
import json
import pandas as pd

#####数据获取
#filename = 'test/data/eq_data_1_day_m1.json'
filename = 'test/data/all_month.geojson'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)
    
"""
#文件内容测试 
readable_file = 'test/data/all_month.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) 
""" 

   
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, titles, lons, lats  = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    #数据添加到列表
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

mags = [max(0, mag) for mag in mags]
#过滤了负数，若为负数，取0
#不然颜色映射模块会报错，原因是不能接受负值
'''
#验证数据测试    
print(mags[:10])
print(titles[0:2])
print(lons[0:5])
print(lats[0:5])
'''

####数据处理
data =pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)
data.head()

# ####绘制图表
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title=f'全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
)

# #fig.write_html('chart/global_earthquakes_30day_end.html')
fig.show()