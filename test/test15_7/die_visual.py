from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

#创建3个D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

#投掷几次骰子并将结果存在列表中
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll() +die_3.roll()
    results.append(result)

#分析结果
frquencies = []
#遍历 2个 面1到骰子面数 所有值的结果
max_result = die_1.num_sizes + die_2.num_sizes +die_3.num_sizes
for value in range(1, max_result+1):
    frquency = results.count(value)
    frquencies.append(frquency)    

#对结果可视化
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frquencies)]

x_axis_config = {'title': '结果', 'dtick':1}
y_axis_config = {'title': '结果的频率'}
title_config = {
        'text': '投掷 3个D6 50000次的结果',
        'x': 0.5,  # 设置标题水平居中
        'xanchor': 'center'  # 设置锚点为中心
    } 
my_layout = Layout(title=title_config, xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout,}, filename= 'test/test15_7/d6x3.html')