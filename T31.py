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
    for record in data[1:7955]:#1:7955
        if  record['case（订单）'] == dingdan:
            cargos.extend([Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])])
        else:
            aa = [f"订单号：{dingdan}"]
            dingdan_cargos = cargos
            for i in range(5):
                v = 0
                num = 1
                cargos = dingdan_cargos
                while(True):
                    case.append(Container(Cases[i][0], Cases[i][1], Cases[i][2]))
                    cargos1=yanzhanfailed_encase_cargos_into_container(cargos, case[count], VolumeGreedyStrategy)
                    v = v+case[count].returnv()
                    count = count + 1
                    if cargos1 == []:
                        break
                    elif len(cargos1) == len(cargos):
                        num = 1000
                        break
                    else:
                        cargos = cargos1
                        num = num + 1
                aa.append(str(num))
                aa.append(str(v))
            A.append(aa)
            print(aa)
            dingdan= record['case（订单）']
            cargos = [Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])]
    df = pd.DataFrame(A, columns=['订单号', '普通1号自营纸箱', '普通1号自营纸箱体积和','普通2号自营纸箱', '普通2号自营纸箱体积和', '普通3号自营纸箱', '普通3号自营纸箱体积和','普通4号自营纸箱', '普通4号自营纸箱体积和', '普通5号自营纸箱', '普通5号自营纸箱体积和'])
    df.to_excel('resultT31.xlsx', index=False, header=True)