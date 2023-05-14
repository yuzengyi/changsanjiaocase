from matplotlib import pyplot as plt   # 导入Matplotlib库中的pyplot模块
from matplotlib.figure import Figure   # 导入Matplotlib库中的Figure模块
import numpy as np                     # 导入Numpy库
from Encase3D._cargo import *           # 从Encase3D库中导入_Cargo模块
from Encase3D._container import *       # 从Encase3D库中导入_Container模块

plt.rcParams['axes.unicode_minus'] = False     # 配置Matplotlib绘图时的中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']   # 配置Matplotlib绘图时的中文显示

fig:Figure = plt.figure()      # 创建一个Figure对象
ax = fig.add_subplot(1, 1, 1, projection='3d')   # 在Figure对象中添加一个3D坐标系

# 设置3D坐标系的视角
ax.view_init(elev=20, azim=40)

# 调整子图之间的间距
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)

def draw_reslut(setted_container:Container):
    """
    绘制货物在集装箱中的摆放图
    """
    # 根据集装箱长、宽、高设置画布的坐标轴比例
    plt.gca().set_box_aspect((
        setted_container.length,
        setted_container.width,
        setted_container.height+200
    ))

    # 绘制集装箱的外框
    _draw_container(setted_container)

    # 遍历每个已放置的货物对象，绘制每个货物
    for cargo in setted_container._setted_cargos:
        _draw_cargo(cargo)

    # 展示绘制结果
    plt.show()

def _draw_container(container:Container):
    """
    绘制集装箱的外框
    """
    # 绘制长方体
    _plot_linear_cube(
        0,0,0,
        container.length,
        container.width,
        container.height
    )

def _draw_cargo(cargo:Cargo):
    """
    绘制货物
    """
    # 绘制立方体货物内部
    _plot_opaque_cube(
        cargo.x, cargo.y, cargo.z,
        cargo.length, cargo.width, cargo.height
    )

def _plot_opaque_cube(x=10, y=20, z=30, dx=40, dy=50, dz=60):
    """
    绘制表面不透明的立方体
    """
    xx = np.linspace(x, x+dx, 2)
    yy = np.linspace(y, y+dy, 2)
    zz = np.linspace(z, z+dz, 2)
    xx2, yy2 = np.meshgrid(xx, yy)
    ax.plot_surface(xx2, yy2, np.full_like(xx2, z))
    ax.plot_surface(xx2, yy2, np.full_like(xx2, z+dz))
    yy2, zz2 = np.meshgrid(yy, zz)
    ax.plot_surface(np.full_like(yy2, x), yy2, zz2)
    ax.plot_surface(np.full_like(yy2, x+dx), yy2, zz2)
    xx2, zz2= np.meshgrid(xx, zz)
    ax.plot_surface(xx2, np.full_like(yy2, y), zz2)
    ax.plot_surface(xx2, np.full_like(yy2, y+dy), zz2)

def _plot_linear_cube(x, y, z, dx, dy, dz, color='red'):
    """
    绘制表面不透明的长方体
    """
    xx = [x, x, x+dx, x+dx, x]
    yy = [y, y+dy, y+dy, y, y]
    kwargs = {'alpha': 1, 'color': color}
    ax.plot3D(xx, yy, [z]*5, **kwargs)
    ax.plot3D(xx, yy, [z+dz]*5, **kwargs)
    ax.plot3D([x, x], [y, y], [z, z+dz], **kwargs)
    ax.plot3D([x, x], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y, y], [z, z+dz], **kwargs)
