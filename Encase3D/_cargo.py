from enum import Enum


class CargoPose(Enum):  # 定义枚举类型，用于描述货物的不同摆放方式
    tall_wide = 0
    tall_thin = 1
    mid_wide = 2
    mid_thin = 3
    short_wide = 4
    short_thin = 5


class Point(object):  # 定义一个坐标点类，表示三维空间中的一个点
    def __init__(self, x: int, y: int, z: int) -> None:  # Point类的构造函数，初始化x、y、z三个坐标值
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:  # 将Point对象转换成字符串表示形式
        return f"({self.x},{self.y},{self.z})"

    def __eq__(self, __o: object) -> bool:  # 重载==操作符，用于比较两个Point对象是否相等
        return self.x == __o.x and self.y == __o.y and self.z == __o.z

    @property
    def is_valid(self) -> bool:  # 判断坐标点是否合法（即坐标值都是非负整数）
        return self.x >= 0 and self.y >= 0 and self.z >= 0

    @property
    def tuple(self) -> tuple:  # 将Point对象转换为元组
        return (self.x, self.y, self.z)


class Cargo(object):  # 定义货物类
    def __init__(self, length: int, width: int, height: int) -> None:  # Cargo类的构造函数，初始化货物的长、宽、高
        self._point = Point(-1, -1, -1)  # 表示货物的坐标点（初始值为-1，表示未确定）
        # 表示货物的形状（用集合来存储，即使属性_shape被定义为集合类型，也应该注意到集合类型是无序的。因此，当你创建Cargo对象时，属性_shape中元素的顺序是不确定的）
        self._shape = {length, width,height}
        self._pose = CargoPose.tall_thin  # 表示货物的摆放方式（默认为tall_thin）

    def is_setted(self):
        return self.x >= 0

    def __repr__(self) -> str:  # 将Cargo对象转换成字符串表示形式
        return f"{self._point} {self.shape}"

    @property
    def pose(self) -> CargoPose:  # 获取货物的摆放方式
        return self._pose

    @pose.setter
    def pose(self, new_pose: CargoPose):  # 设置货物的摆放方式
        self._pose = new_pose

    @property
    def _shape_swiche(self) -> dict:  # 根据不同的摆放方式，返回货物的形状（长、宽、高）
        edges = sorted(self._shape)
        return {
            CargoPose.tall_thin: (edges[1], edges[0], edges[-1]),
            CargoPose.tall_wide: (edges[0], edges[1], edges[-1]),
            CargoPose.mid_thin: (edges[-1], edges[0], edges[1]),
            CargoPose.mid_wide: (edges[0], edges[-1], edges[-1]),
            CargoPose.short_thin: (edges[-1], edges[1], edges[0]),
            CargoPose.short_wide: (edges[1], edges[-1], edges[0])
        }

    @property
    def point(self):  # 获取货物的坐标点
        return self._point

    @point.setter
    def point(self, new_point: Point):  # 设置货物的坐标点
        self._point = new_point

    @property
    def x(self) -> int:  # 获取货物的x坐标
        return self._point.x

    @x.setter
    def x(self, new_x: int):  # 设置货物的x坐标
        self._point = Point(new_x, self.y, self.z)

    @property
    def y(self) -> int:  # 获取货物的y坐标
        return self._point.y

    @y.setter
    def y(self, new_y: int):  # 设置货物的y坐标
        self._point = Point(self.x, new_y, self.z)

    @property
    def z(self) -> int:  # 获取货物的z坐标
        return self._point.z

    @z.setter
    def z(self, new_z: int):  # 设置货物的z坐标
        self._point = Point(self.z, self.y, new_z)

    @property
    def length(self) -> int:  # 获取货物的长
        return self.shape[0]

    @property
    def width(self) -> int:  # 获取货物的宽
        return self.shape[1]

    @property
    def height(self) -> int:  # 获取货物的高
        return self.shape[-1]

    def get_shadow_of(self, planar: str) -> tuple:  # 返回货物在某个平面上的投影区域
        if planar in ("xy", "yx"):
            x0, y0 = self.x, self.y
            x1, y1 = self.x + self.length, self.y + self.width
        elif planar in ("xz", "zx"):
            x0, y0 = self.x, self.z
            x1, y1 = self.x + self.length, self.z + self.height
        elif planar in ("yz", "zy"):
            x0, y0 = self.y, self.z
            x1, y1 = self.y + self.width, self.z + self.height
        return (x0, y0, x1, y1)

    @property
    def shape(self) -> tuple:  # 获取货物的形状（长、宽、高）
        return self._shape_swiche[self._pose]

    @shape.setter
    def shape(self, length, width, height):  # 设置货物的形状（长、宽、高）
        self._shape = {length, width, height}

    @property
    def volume(self) -> int:  # 计算货物的体积
        reslut = 1
        for i in self._shape:
            reslut *= i
        return reslut
