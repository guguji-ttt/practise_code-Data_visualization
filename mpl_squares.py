import matplotlib.pyplot as plt

###中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False



# 查看所有可用样式
print(plt.style.available)

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use(style='ggplot')
fig, ax = plt.subplots()
ax.plot(input_value, squares, linewidth=3)

#设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

#设置刻度标记的大小。
ax.tick_params(axis='both', labelsize=14)


plt.show()