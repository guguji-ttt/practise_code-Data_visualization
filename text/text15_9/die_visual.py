from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

#创建1个D6 1个D10
die_1 = Die()
die_2 = Die(10)

#投掷几次骰子并将结果存在列表中
results = [die_1.roll() * die_2.roll() for i in range(50_000)]#改为列表解析

#分析结果
frquencies = []
#遍历 2个 面1到骰子面数 所有值的结果
max_result = die_1.num_sizes * die_2.num_sizes
for value in range(1, max_result+1):
    frquency = results.count(value)
    frquencies.append(frquency)    

#对结果可视化
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frquencies)]

x_axis_config = {'title': '结果', 'dtick':1}
y_axis_config = {'title': '结果的频率'}
title_config = {
        'text': '投掷1个D6,1个D10,值相乘 50000次的结果',
        'x': 0.5,  # 设置标题水平居中
        'xanchor': 'center'  # 设置锚点为中心
    } 
my_layout = Layout(title=title_config, xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout,}, filename= 'text/text15_9/c_d6_d10_x.html')