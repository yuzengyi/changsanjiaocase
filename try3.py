from Encase3D import *
from Encase3D import drawer
import json
import pandas as pd

if __name__ == "__main__":
    with open('orderxi_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 初始化数据
    cargos = [Cargo(210, 200, 30) for _ in range(1)]
    dingdan = 1
    order_numbers = []
    vs = []

    for record in data[1:1180]:
        if record['case（订单）'] == dingdan:
            cargos.extend(
                [Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])])
        else:
            # 箱子方案列表
            Cases = [[165, 120, 55], [200, 140, 70], [200, 150, 150], [270, 200, 90], [300, 200, 170]]
            v = []
            for m in range(5):
                case = Container(Cases[m][0], Cases[m][1], Cases[m][2])
                result = encase_cargos_into_container(cargos, case, VolumeGreedyStrategy)
                res_str = ', '.join([str(len(r.cargos)) for r in result])
                print(res_str)
                v.append(res_str)
            # 将 v 调整为长度为5的列表
            if len(v) < 5:
                v.extend([''] * (5 - len(v)))
            vs.append(v[:5])

            # 记录订单号
            order_numbers.append(str(dingdan))

            # 更新订单和货物
            dingdan = record['case（订单）']
            cargos = [Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])]

    # 将数据写入 Excel 文件
    data = {'订单号': order_numbers}
    for i in range(len(vs)):
        data['方案{}'.format(i + 1)] = vs[i]
    df = pd.DataFrame(data)
    df.to_excel('result.xlsx', index=False)
