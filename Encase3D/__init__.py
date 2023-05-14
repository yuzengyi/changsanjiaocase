from typing import Iterable, List
from Encase3D._cargo import *
from Encase3D._container import *

class Strategy(object):
    # 继承此类 重写两个静态函数 实现自定义两个装载策略: 装箱顺序 和 货物.
    @staticmethod
    def encasement_sequence(cargos:Iterable) -> Iterable:
        return cargos

    @staticmethod
    def choose_cargo_poses(cargo:Cargo, container:Container) -> list:
        return list(CargoPose)

def encase_cargos_into_container(
    cargos:Iterable,
    container:Container,
    strategy:type
) -> float:
    sorted_cargos:List[Cargo] = strategy.encasement_sequence(cargos)
    i = 0 # 记录发当前货物
    while i < len(sorted_cargos):
        j = 0 # 记录当前摆放方式
        cargo = sorted_cargos[i]
        poses = strategy.choose_cargo_poses(cargo, container)
        while j < len(poses):
            cargo.pose = poses[j]
            is_encased = container._encase(cargo)
            if is_encased.is_valid:
                break # 可以装入 不在考虑后续摆放方式
            j += 1  # 不可装入 查看下一个摆放方式
        if is_encased.is_valid:
            i += 1 # 成功放入 继续装箱
        elif is_encased == Point(-1,-1,0):
            continue # 没放进去但是修改了参考面位置 重装
        else :
            i += 1 # 纯纯没放进去 跳过看下一个箱子
    return sum(list(map(
            lambda cargo:cargo.volume,container._setted_cargos
        ))) / container.volume
def failed_encase_cargos_into_container(
    cargos: Iterable, # 货物列表，包含所有要装箱的货物
    container: Container, # 集装箱对象
    strategy: type # 装箱策略，必须是 BaseEncasementStrategy 的子类
) -> List[Cargo]:
    """
    将一批货物尽可能地装入集装箱中，并返回未能装入集装箱的货物列表。

    Args:
        cargos (Iterable): 货物列表，包含所有要装箱的货物
        container (Container): 集装箱对象，用于盛放货物
        strategy (type): 装箱策略，必须是 BaseEncasementStrategy 的子类

    Returns:
        List[Cargo]: 未能装入集装箱的货物列表
    """

    # 通过调用装箱策略的方法获取排序后的货物列表
    sorted_cargos:List[Cargo] = strategy.encasement_sequence(cargos)

    i = 0 # 记录当前装箱的货物序号
    failed_cargos = [] # 记录未能装入集装箱的货物列表
    while i < len(sorted_cargos):
        j = 0 # 记录当前摆放方式的序号
        cargo = sorted_cargos[i]

        # 获取当前货物在集装箱中所有可摆放的位置
        poses = strategy.choose_cargo_poses(cargo, container)

        while j < len(poses):
            cargo.pose = poses[j] # 将货物摆放在当前位置
            is_encased = container._encase(cargo) # 尝试将货物装入集装箱

            if is_encased.is_valid:
                break # 可以装入，不再考虑后续摆放方式

            j += 1 # 不可装入，查看下一个摆放方式

        if is_encased.is_valid:
            i += 1 # 当前货物已成功放置，继续装箱
        elif is_encased == Point(-1,-1,0):
            continue # 没有放进去，但是修改了参考面位置，重装
        else :
            failed_cargos.append(cargo) # 将未能装入集装箱的货物添加到列表中
            i += 1 # 跳过看下一个货物

    # 返回未能装入集装箱的货物列表
    return failed_cargos
def yanzhanfailed_encase_cargos_into_container(
    cargos: Iterable, # 货物列表，包含所有要装箱的货物
    container: Container, # 集装箱对象
    strategy: type # 装箱策略，必须是 BaseEncasementStrategy 的子类
) -> List[Cargo]:
    """
    将一批货物尽可能地装入集装箱中，并返回未能装入集装箱的货物列表。

    Args:
        cargos (Iterable): 货物列表，包含所有要装箱的货物
        container (Container): 集装箱对象，用于盛放货物
        strategy (type): 装箱策略，必须是 BaseEncasementStrategy 的子类

    Returns:
        List[Cargo]: 未能装入集装箱的货物列表
    """

    # 通过调用装箱策略的方法获取排序后的货物列表
    sorted_cargos:List[Cargo] = strategy.encasement_sequence(cargos)

    i = 0 # 记录当前装箱的货物序号
    failed_cargos = [] # 记录未能装入集装箱的货物列表
    while i < len(sorted_cargos):
        j = 0 # 记录当前摆放方式的序号
        cargo = sorted_cargos[i]

        # 获取当前货物在集装箱中所有可摆放的位置
        poses = strategy.choose_cargo_poses(cargo, container)

        while j < len(poses):
            cargo.pose = poses[j] # 将货物摆放在当前位置
            is_encased = container.yanzhan_encase(cargo) # 尝试将货物装入集装箱

            if is_encased.is_valid:
                break # 可以装入，不再考虑后续摆放方式

            j += 1 # 不可装入，查看下一个摆放方式

        if is_encased.is_valid:
            i += 1 # 当前货物已成功放置，继续装箱
        elif is_encased == Point(-1,-1,0):
            continue # 没有放进去，但是修改了参考面位置，重装
        else :
            failed_cargos.append(cargo) # 将未能装入集装箱的货物添加到列表中
            i += 1 # 跳过看下一个货物

    # 返回未能装入集装箱的货物列表
    return failed_cargos
#daizi_encase
def daizifailed_encase_cargos_into_container(
    cargos: Iterable, # 货物列表，包含所有要装箱的货物
    container: Container, # 集装箱对象
    strategy: type # 装箱策略，必须是 BaseEncasementStrategy 的子类
) -> List[Cargo]:
    """
    将一批货物尽可能地装入集装箱中，并返回未能装入集装箱的货物列表。

    Args:
        cargos (Iterable): 货物列表，包含所有要装箱的货物
        container (Container): 集装箱对象，用于盛放货物
        strategy (type): 装箱策略，必须是 BaseEncasementStrategy 的子类

    Returns:
        List[Cargo]: 未能装入集装箱的货物列表
    """

    # 通过调用装箱策略的方法获取排序后的货物列表
    sorted_cargos:List[Cargo] = strategy.encasement_sequence(cargos)

    i = 0 # 记录当前装箱的货物序号
    failed_cargos = [] # 记录未能装入集装箱的货物列表
    while i < len(sorted_cargos):
        j = 0 # 记录当前摆放方式的序号
        cargo = sorted_cargos[i]

        # 获取当前货物在集装箱中所有可摆放的位置
        poses = strategy.choose_cargo_poses(cargo, container)

        while j < len(poses):
            cargo.pose = poses[j] # 将货物摆放在当前位置
            is_encased = container.daizi_encase(cargo) # 尝试将货物装入集装箱

            if is_encased.is_valid:
                break # 可以装入，不再考虑后续摆放方式

            j += 1 # 不可装入，查看下一个摆放方式

        if is_encased.is_valid:
            i += 1 # 当前货物已成功放置，继续装箱
        elif is_encased == Point(-1,-1,0):
            continue # 没有放进去，但是修改了参考面位置，重装
        else :
            failed_cargos.append(cargo) # 将未能装入集装箱的货物添加到列表中
            i += 1 # 跳过看下一个货物

    # 返回未能装入集装箱的货物列表
    return failed_cargos
def daizifailed_encase_cargos_into_container(
    cargos: Iterable, # 货物列表，包含所有要装箱的货物
    container: Container, # 集装箱对象
    strategy: type # 装箱策略，必须是 BaseEncasementStrategy 的子类
) -> List[Cargo]:
    """
    将一批货物尽可能地装入集装箱中，并返回未能装入集装箱的货物列表。

    Args:
        cargos (Iterable): 货物列表，包含所有要装箱的货物
        container (Container): 集装箱对象，用于盛放货物
        strategy (type): 装箱策略，必须是 BaseEncasementStrategy 的子类

    Returns:
        List[Cargo]: 未能装入集装箱的货物列表
    """

    # 通过调用装箱策略的方法获取排序后的货物列表
    sorted_cargos:List[Cargo] = strategy.encasement_sequence(cargos)

    i = 0 # 记录当前装箱的货物序号
    failed_cargos = [] # 记录未能装入集装箱的货物列表
    while i < len(sorted_cargos):
        j = 0 # 记录当前摆放方式的序号
        cargo = sorted_cargos[i]

        # 获取当前货物在集装箱中所有可摆放的位置
        poses = strategy.choose_cargo_poses(cargo, container)

        while j < len(poses):
            cargo.pose = poses[j] # 将货物摆放在当前位置
            is_encased = container.daizi_encase(cargo) # 尝试将货物装入集装箱

            if is_encased.is_valid:
                break # 可以装入，不再考虑后续摆放方式

            j += 1 # 不可装入，查看下一个摆放方式

        if is_encased.is_valid:
            i += 1 # 当前货物已成功放置，继续装箱
        elif is_encased == Point(-1,-1,0):
            continue # 没有放进去，但是修改了参考面位置，重装
        else :
            failed_cargos.append(cargo) # 将未能装入集装箱的货物添加到列表中
            i += 1 # 跳过看下一个货物

    # 返回未能装入集装箱的货物列表
    return failed_cargos
def yanzhandaizifailed_encase_cargos_into_container(
    cargos: Iterable, # 货物列表，包含所有要装箱的货物
    container: Container, # 集装箱对象
    strategy: type # 装箱策略，必须是 BaseEncasementStrategy 的子类
) -> List[Cargo]:
    """
    将一批货物尽可能地装入集装箱中，并返回未能装入集装箱的货物列表。

    Args:
        cargos (Iterable): 货物列表，包含所有要装箱的货物
        container (Container): 集装箱对象，用于盛放货物
        strategy (type): 装箱策略，必须是 BaseEncasementStrategy 的子类

    Returns:
        List[Cargo]: 未能装入集装箱的货物列表
    """

    # 通过调用装箱策略的方法获取排序后的货物列表
    sorted_cargos:List[Cargo] = strategy.encasement_sequence(cargos)

    i = 0 # 记录当前装箱的货物序号
    failed_cargos = [] # 记录未能装入集装箱的货物列表
    while i < len(sorted_cargos):
        j = 0 # 记录当前摆放方式的序号
        cargo = sorted_cargos[i]

        # 获取当前货物在集装箱中所有可摆放的位置
        poses = strategy.choose_cargo_poses(cargo, container)

        while j < len(poses):
            cargo.pose = poses[j] # 将货物摆放在当前位置
            is_encased = container.yanzhandaizi_encase(cargo) # 尝试将货物装入集装箱

            if is_encased.is_valid:
                break # 可以装入，不再考虑后续摆放方式

            j += 1 # 不可装入，查看下一个摆放方式

        if is_encased.is_valid:
            i += 1 # 当前货物已成功放置，继续装箱
        elif is_encased == Point(-1,-1,0):
            continue # 没有放进去，但是修改了参考面位置，重装
        else :
            failed_cargos.append(cargo) # 将未能装入集装箱的货物添加到列表中
            i += 1 # 跳过看下一个货物

    # 返回未能装入集装箱的货物列表
    return failed_cargos
class VolumeGreedyStrategy(Strategy):
    @staticmethod
    def encasement_sequence(cargos:Iterable) -> Iterable:
        return sorted(cargos, key= lambda cargo:cargo.volume,reverse=1)

    @staticmethod
    def choose_cargo_poses(cargo:Cargo, container:Container) -> list:
        return list(CargoPose)