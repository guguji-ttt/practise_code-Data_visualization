import json

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    
"""
#文件内容测试 
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) 
"""
   

all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))

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

'''
#验证数据测试    
print(mags[:10])
print(titles[0:2])
print(lons[0:5])
print(lats[0:5])
'''

