import matplotlib.pyplot as plt
import numpy as np
from die import Die

###中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#创建1个D6 1个D10
die_1 = Die()

#投掷几次骰子并将结果存在列表中
results = []
for roll_num in range(50_000):
    result = die_1.roll()
    results.append(result)

# 创建画布
plt.figure(figsize=(10, 6))

# 绘制直方图
plt.hist(
    results,                   # 输入数据
    bins=np.arange(0.5, 7.5, 1), # 关键！柱子边界设置
    edgecolor='black',          # 柱子边框颜色
    linewidth=1.2,             # 边框粗细
    color='skyblue',           # 柱子填充色
    alpha=0.7                  # 透明度(0-1)
)

#样式设置
plt.title('6面骰子点数分布 (n=50000)', fontsize=15, pad=20)  # 标题字体大小及上下间距
plt.xlabel('骰子点数', fontsize=12)  # X轴标签字体
plt.xticks(range(1,7))          # 强制X轴只显示1-6整数刻度
plt.ylabel('出现次数', fontsize=12)  # y轴标签字体
#设置y轴刻度
plt.ylim(0, 10000)  # 略高于理论期望值8333
plt.yticks(range(0, 10001, 2000))  # 0到9000，步长2000
plt.grid(axis='y', alpha=0.3)   # 仅显示横向网格线(透明度30%)
plt.tight_layout()              # 自动调整子图间距

# 显示理论概率线（红色虚线）
expected = len(results)/6  # 计算理论期望值(50,000/6≈8,333次)
plt.axhline(
    expected,   # 水平线位置
    color='red', # 线颜色
    linestyle='--', # 虚线样式
    label=f'理论期望值 ({expected:.0f}次)'  # 图例标签
    )
plt.legend()     # 显示图例

plt.tight_layout()
plt.show()