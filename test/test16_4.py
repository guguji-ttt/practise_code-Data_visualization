import csv
from datetime import datetime
import matplotlib.pyplot as plt

# 中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 文件路径
filename = 'test/data/sitka_weather_2018_simple.csv'  #数据集

title_name = filename.split('/')[-1].split('.')[0]  # 提取"death_valley_2018_simple"

def read_temperature_data(filename):
    """从CSV文件读取温度数据"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])  # 最高温
                low = int(row[6])   # 最低温
            except ValueError:
                print(f"Missing data for {row[2]}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
        return dates, highs, lows

# 读取两个数据集
dates, highs, lows = read_temperature_data(filename)

# 创建图形
plt.style.use('ggplot')
fig, ax = plt.subplots()

# 绘制死亡谷数据（红色系）
ax.plot(dates, highs, c='red', alpha=0.5, label='最高温')
ax.plot(dates, lows, c='salmon', alpha=0.5, label='最低温')
ax.fill_between(dates, highs, lows, facecolor='red', alpha=0.1)



# 设置图形格式
ax.set_title(f"2018年每日温度对比({title_name})", fontsize=16)
ax.set_xlabel('日期', fontsize=12)
ax.set_ylabel('温度 (F)', fontsize=12)
fig.autofmt_xdate()  # 自动旋转日期标签
ax.legend(loc='upper left', fontsize=10)  # 添加图例

# 设置网格和刻度
ax.grid(True, linestyle='--', alpha=0.6)
ax.tick_params(axis='both', which='major', labelsize=10)

plt.tight_layout()
plt.show()