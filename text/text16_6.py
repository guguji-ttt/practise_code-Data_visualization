import plotly.express as px
import json
import pandas as pd

#####数据获取
#filename = 'text/data/eq_data_1_day_m1.json'
filename = 'text/data/eq_data_30_day_m1.json'


def obtain_json_eq(filename):
    '''
    获取json文件中的数据，返回4个list
    @mags
    @titles
    @lons
    @lats
    '''
    with open(filename) as f:
        all_eq_data = json.load(f)
    all_eq_dicts = all_eq_data['features']
    mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
    titles = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]
    lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
    lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
    return mags, titles, lons, lats

mags, titles, lons, lats  = obtain_json_eq(filename)
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

####绘制图表
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
)
#fig.write_html('chart/global_earthquakes_30day_end.html')
fig.show()