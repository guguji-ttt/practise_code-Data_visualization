import matplotlib.pyplot as plt

###中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x_values = range(1,6)
y_values = [x**3 for x in x_values]

#设置画图格式
plt.style.use('ggplot')
fig_0, ax = plt.subplots()
ax.scatter(x_values, y_values, c='blue', s=100)

#设置图表标题并给坐标轴加上标签。
ax.set_title("立方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的立方", fontsize=14)

x_values_more = range(1,5001)
y_values_more = [x**3 for x in x_values_more]

#设置画图格式
plt.style.use('ggplot')
fig_1, bx = plt.subplots()
bx.scatter(x_values_more, y_values_more, c=y_values_more, cmap=plt.cm.YlOrBr, s=10)#颜色映射-随y值

#设置图表标题并给坐标轴加上标签。
bx.set_title("立方数", fontsize=24)
bx.set_xlabel("值", fontsize=14)
bx.set_ylabel("值的立方", fontsize=14)

plt.show()