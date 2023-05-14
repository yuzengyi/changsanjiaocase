import json
import pandas as pd
from Encase3D import *
from Encase3D import drawer
if __name__ == "__main__":
    with open('orderxi_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    cargos = [Cargo(210,200,30) for _ in range(1)]#210,200,30
    dingdan = 1
    case = []
    Cases = [[165, 120, 55], [200, 140, 70], [200, 150, 150], [270, 200, 90], [300, 200, 170]]
    A = []
    aa = [f'订单号：1']
    count = 0
    num = [0, 0, 0, 0, 0]

    for record in data[1:4]:#1:7955
        if  record['case（订单）'] == dingdan:
            cargos.extend([Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])])
        else:
            aa = [f"订单号：{dingdan}"]
            dingdan_cargos = cargos
            num = [0, 0, 0, 0, 0]
            while(True):
                maxcargos = dingdan_cargos
                if maxcargos == []:
                    break
                else:
                    max = 0
                    for i in range(5):
                        case.append(Container(Cases[i][0], Cases[i][1], Cases[i][2]))
                        cargos1=failed_encase_cargos_into_container(dingdan_cargos, case[count], VolumeGreedyStrategy)
                        count = count +1
                        # if cargos1 == []:
                        #     break
                        # elif len(cargos1) == len(cargos):
                        #     num = 1000
                        #     break
                        # else:
                        #     cargos = cargos1
                        #     num = num + 1
                        if max < len(cargos)-len(cargos1):
                            maxi = i
                            maxcargos = cargos1
                    num[maxi] = num[maxi]+1
                    dingdan_cargos = maxcargos
            for i in range(5):
                aa.append(str(num[0]))
            A.append(aa)
            print(num)
            dingdan= record['case（订单）']
            cargos = [Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])]
    df = pd.DataFrame(A, columns=['订单号', '普通1号自营纸箱', '普通2号自营纸箱', '普通3号自营纸箱','普通4号自营纸箱', '普通5号自营纸箱'])
    df.to_excel('result.xlsx', index=False, header=True)