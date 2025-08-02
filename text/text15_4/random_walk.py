from random import choice

class RandomWalk:
    """一个生成随机漫步数据的类"""
    
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性
        num_points指定数据点的个数"""
        self.num_points = num_points
        
        #所有随机漫步都始于(0, 0),创建两个存储点的列表
        self.x_values = [0]
        self.y_values = [0]
        #方向选择和距离选择列表
        self.dir_select = [-1, 1]
        self.dis_select = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        
        while len(self.x_values) < self.num_points:
            
            #决定x轴前进方向以及沿着这个方向前进的距离
            x_direction = choice(self.dir_select)
            x_distance = choice(self.dis_select)
            
            x_step = x_direction * x_distance
            
            #决定y轴前进方向以及沿着这个方向前进的距离
            y_direction = choice(self.dir_select)
            y_distance = choice(self.dis_select)
            
            y_step = y_direction * y_distance
            
            #拒绝原地等待
            if x_step == 1 and y_step == 1:
                continue
            
            #计算下一个点的x值与y值
            x_next = self.x_values[-1] + x_step
            y_next = self.y_values[-1] + y_step
            
            #添加到列表
            self.x_values.append(x_next)
            self.y_values.append(y_next)
            
            
        
        