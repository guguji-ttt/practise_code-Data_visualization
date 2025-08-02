import matplotlib.pyplot as plt
###中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

from random_walk import RandomWalk

#只要程序处于活跃状态，就不断进行模拟随机漫步
while True:
    #创建实例
    rw = RandomWalk(50_000_0)
    rw.fill_walk()
    #调用fill_walk()方法生成所有点并存在类列表

    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
               edgecolors='none', s=15)
    
    #突出起始点和终点
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
               edgecolors='none', s=100)
    
    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break