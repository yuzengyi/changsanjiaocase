import json
import pandas as pd
from Encase3D import *
from Encase3D import drawer
if __name__ == "__main__":
    with open('orderdaizixi_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    cargos = [Cargo(210,200,30) for _ in range(1)]#210,200,30
    dingdan = 1
    case = []
    Cases = [[250, 190, 1], [300, 250, 1], [400, 330, 1], [450, 420, 1],[165, 120, 55], [200, 140, 70], [200, 150, 150], [270, 200, 90], [300, 200, 170]]
    A = []
    aa = [f'订单号：1']
    count = 0
    for record in data[1:10000]:#1:10000
        if  record['case（订单）'] == dingdan:
            if record['l（长）'] == record['w（宽）'] and record['w（宽）'] == record['h（高）']:
                record['l（长）']= record['l（长）']+1
            cargos.extend([Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])])
        else:
            aa = [f"订单号：{dingdan}"]
            dingdan_cargos = cargos
            for i in range(4):
                num = 1
                cargos = dingdan_cargos
                while(True):
                    case.append(Container(Cases[i][0], Cases[i][1], Cases[i][2]))
                    cargos1=daizifailed_encase_cargos_into_container(cargos, case[count], VolumeGreedyStrategy)
                    #print(cargos1)
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
            for i in range(4,9):
                num = 1
                cargos = dingdan_cargos
                min = 1000
                while(True):
                    case.append(Container(Cases[i][0], Cases[i][1], Cases[i][2]))
                    cargos1=failed_encase_cargos_into_container(cargos, case[count], VolumeGreedyStrategy)
                    #print(cargos1)
                    count = count + 1
                    if cargos1 == []:
                        break
                    elif len(cargos1) == len(cargos):
                        num = 1000
                        break
                    else:
                        cargos = cargos1
                        num = num + 1
                if min>num:
                    min = num
                aa.append(str(num))
            if min <1000:
                A.append(aa)
                print(aa)
            dingdan= record['case（订单）']
            if record['l（长）'] == record['w（宽）'] and record['w（宽）'] == record['h（高）']:
                record['l（长）']= record['l（长）']+1
            cargos = [Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])]
    df = pd.DataFrame(A, columns=['订单号', '普通1号袋','普通2号袋','普通3号袋','普通4号袋','普通1号自营纸箱', '普通2号自营纸箱', '普通3号自营纸箱','普通4号自营纸箱', '普通5号自营纸箱'])#普通1号袋	普通2号袋	普通3号袋	普通4号袋
    df.to_excel('hunheresult.xlsx', index=False, header=True)