import plotly.graph_objects as go
import numpy as np

from random_walk import RandomWalk

#生成随机漫步数据
rw = RandomWalk()
rw.fill_walk()
x = rw.x_values
y = rw.y_values

# 创建颜色映射（根据点的顺序渐变）
colors = np.linspace(0, 1, len(x))  # 从0到1的线性渐变

# 创建散点图
fig = go.Figure()

# 主路径（带颜色渐变）
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='markers',  # 点模式
    marker=dict(
        size=8,
        color=colors,
        colorscale='blues',  # 改用更鲜艳的色阶
        showscale=True,
        colorbar=dict(title='漫步进度'),
        opacity=0.7
    ),
    name='漫步路径'
))

# 突出起点和终点
fig.add_trace(go.Scatter(
    x=[x[0], x[-1]],
    y=[y[0], y[-1]],
    mode='markers',
    marker=dict(
        size=15,
        color=['green', 'red'],  # 起点绿色，终点红色
        symbol=['x', 'star'],    # 特殊形状标记
        line=dict(width=2, color='black')
    ),
    name='起点/终点'
))

fig.update_layout(
    title={
        'text': "随机漫步",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='X轴',
    yaxis_title='Y轴',
    hovermode='closest',  # 鼠标悬停时显示最近点数据
    legend=dict(
        x=0.02,  # 将图例放在左侧
        y=0.98,  # 靠近顶部
        bgcolor='rgba(255,255,255,0.5)',  # 半透明背景
        bordercolor='rgba(0,0,0,0.2)'
    )
)

# 显示图表（Jupyter Notebook中直接显示）
fig.show()

# 保存为HTML文件
fig.write_html("text/text15_10/scatter_plot.html")