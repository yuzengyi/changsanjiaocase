import json
import pandas as pd
from Encase3D import *
from Encase3D import drawer
if __name__ == "__main__":
    with open('orderxi_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    cargos = [Cargo(210,200,30) for _ in range(2)]#210,200,30
    dingdan = 1
    order_numbers = []

    vs = []
    for record in data[1:7955]:#1
        if  record['case（订单）'] == dingdan:
            #print(Cargo(record['l（长）'], record['w（宽）'], record['h（高）']))
            cargos.extend([Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])])
        else:
            Cases = [[165, 120, 55], [200, 140, 70], [200, 150, 150], [270, 200, 90], [300, 200, 170]]
            m = 0
            v = [f"订单{dingdan}"]
            case0 = Container(Cases[m][0], Cases[m][1], Cases[m][2])
            print("订单：")
            order_numbers.append(str(dingdan))
            print(dingdan)
            a = encase_cargos_into_container(cargos, case0, VolumeGreedyStrategy)
            print(a)
            v.append(str(a))
            m = 1
            case1 = Container(Cases[m][0], Cases[m][1], Cases[m][2])
            a = encase_cargos_into_container(cargos, case1, VolumeGreedyStrategy)
            print(a)
            v.append(str(a))
            m = 2
            case2 = Container(Cases[m][0], Cases[m][1], Cases[m][2])
            a = encase_cargos_into_container(cargos, case2, VolumeGreedyStrategy)
            print(a)
            v.append(str(a))
            m = 3
            case3 = Container(Cases[m][0], Cases[m][1], Cases[m][2])
            a = encase_cargos_into_container(cargos, case3, VolumeGreedyStrategy)
            print(a)
            v.append(str(a))
            # drawer.draw_reslut(case)
            m = 4
            case4 = Container(Cases[m][0], Cases[m][1], Cases[m][2])
            a = encase_cargos_into_container(cargos, case4, VolumeGreedyStrategy)
            print(a)
            v.append(str(a))
            vs.append(v)
            dingdan= record['case（订单）']
            cargos = [Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])]

# 将数据写入 Excel 文件，按行写入
# 将数据包装为 DataFrame 对象
df = pd.DataFrame(vs, columns=['订单号', '普通1号自营纸箱', '普通2号自营纸箱','普通3号自营纸箱','普通4号自营纸箱','普通5号自营纸箱'])

# 将数据写入 Excel 文件，覆盖已有内容
df.to_excel('output.xlsx', index=False, header=True)
