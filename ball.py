import numpy as np
import turtle

v0 = 20  # 初速度（m/s）
theta = np.radians(30)  # 初始化抛射角（rad）
g = 10  # 重力加速度（m/s2）
x = 0  # 任意时刻，x方向坐标
y = 0  # 任意时刻，y方向坐标
t = 0  # 起始时间设置为0
attenuation_factor = 0.8  # 每次小球撞击地面后，速度的衰减倍率
x_init = [0]  # t = 0 时x方向的坐标
y_init = [100]  # t = 0时y方向上的坐标，即起始高度
x_array = []  # 用于存储所有时刻，x方向上坐标
y_array = []  # 用于存储所有时刻，y方向上坐标

v_x_init = v0 * np.cos(theta)  # 斜抛运动x方向上的初速度
v_y_init = v0 * np.cos(theta)  # 斜抛运动y方向上的初速度


while v_x_init >= 0.01 * v0 * np.cos(theta):  # 如果x方向上的速度衰减为原来的1%，则退出循环
    if (y > 0) or (y == 0):  # 如果小球依然在空中
        # 分别计算x, y方向上的速度
        v_x = v_x_init
        v_y = v_y_init - g * t

    # 如果小球碰到了地面,则开始一段新的斜抛运动
    else:
        # 用x_init, y_init存储上一段斜抛运动的终点坐标
        y_init.append(0)
        x_init.append(x)
        # 重置时间
        t = 0
        # 撞击地面后，更新速度
        v_x *= attenuation_factor
        v_y = (-1) * v_y * attenuation_factor  # y方向上速度方向取反，大小乘以一个attenuation_factor
        # 重设初速度，即开始一段新的斜抛运动
        v_x_init = v_x
        v_y_init = v_y

    # 计算坐标点
    x = v_x_init * t + x_init[-1]
    y = v_y_init * t - 0.5 * g * t * t + y_init[-1]

    t += 0.04  # t越小，轨迹越平滑
    x_array.append(x)
    y_array.append(y)


# 用turtle模块进行可视化
turtle.pencolor('green')
turtle.goto(500, 0)
turtle.goto(0, 0)
turtle.goto(0, 100)
turtle.pencolor('white')
turtle.goto(x_array[0], y_array[0])
turtle.setup(width=0.8)
turtle.pencolor("red")
turtle.width(4)
turtle.speed(1)
turtle.shape("circle")

for i in range(1, len(x_array)):
    turtle.goto(x_array[i], y_array[i])
