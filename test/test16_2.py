import csv
from datetime import datetime
import matplotlib.pyplot as plt

# 中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 文件路径
filename_dv = 'test/data/death_valley_2018_simple.csv'  # 死亡谷数据集
filename_sitka = 'test/data/sitka_weather_2018_simple.csv'  # Sitka数据集

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
dates_dv, highs_dv, lows_dv = read_temperature_data(filename_dv)
dates_sitka, highs_sitka, lows_sitka = read_temperature_data(filename_sitka)

# 创建图形
plt.style.use('ggplot')
fig, ax = plt.subplots()

# 绘制死亡谷数据（红色系）
ax.plot(dates_dv, highs_dv, c='red', alpha=0.5, label='死亡谷最高温')
ax.plot(dates_dv, lows_dv, c='salmon', alpha=0.5, label='死亡谷最低温')
ax.fill_between(dates_dv, highs_dv, lows_dv, facecolor='red', alpha=0.1)

# 绘制Sitka数据（蓝色系）
ax.plot(dates_sitka, highs_sitka, c='blue', alpha=0.5, label='Sitka最高温')
ax.plot(dates_sitka, lows_sitka, c='lightblue', alpha=0.5, label='Sitka最低温')
ax.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)

# 设置图形格式
ax.set_title("2018年死亡谷与Sitka每日温度对比", fontsize=16)
ax.set_xlabel('日期', fontsize=12)
ax.set_ylabel('温度 (F)', fontsize=12)
fig.autofmt_xdate()  # 自动旋转日期标签
ax.legend(loc='upper left', fontsize=10)  # 添加图例

# 设置网格和刻度
ax.grid(True, linestyle='--', alpha=0.6)
ax.tick_params(axis='both', which='major', labelsize=10)

plt.tight_layout()
plt.show()
    
    