import matplotlib.pyplot as plt

###中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x_values = range(1,1001)
y_values = [x**2 for x in x_values]
plt.style.use(style='ggplot')
fig, ax = plt.subplots()

#传递数，可以画点图
#ax.scatter(2, 4, s=100)

#传递列表指定颜色和尺寸
# ax.scatter(x_values, y_values, c='red', s=10)

#通过c参数设置RGB颜色（传一个RGB元组）
#ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

#颜色深浅映射，c，cmap会随值的增大而加深指定颜色
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

#设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

#设置刻度标记的大小。
ax.tick_params(axis='both', which='major', labelsize=14)
#设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])#ax.axis([xmin, xmax, ymin, ymax])
#展示图表
#plt.show()

#自动保存图表
#@第一个参数指定保存路径
#@第二个参数代表处理方法，'tight'表示裁掉多余的空白部分
plt.savefig('squres_plot.png', bbox_inches='tight')