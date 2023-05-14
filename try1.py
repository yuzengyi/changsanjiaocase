import json
from Encase3D import *
from Encase3D import drawer
if __name__ == "__main__":
    cargos = [Cargo(100, 100, 100) for _ in range(1)]
    #cargos.extend([Cargo(170, 110, 27) for _ in range(7)])
    Cases = [[165, 120, 55], [200, 140, 70], [200, 150, 150], [270, 200, 90], [300, 200, 170]]
    m = 0
    case0 = Container(Cases[m][0], Cases[m][1], Cases[m][2])
    print(
        encase_cargos_into_container(cargos, case0, VolumeGreedyStrategy)
    )
    m = 1
    case1 = Container(Cases[m][0], Cases[m][1], Cases[m][2])
    print(
        encase_cargos_into_container(cargos, case1, VolumeGreedyStrategy)
    )
    m = 2
    case2 = Container(Cases[m][0], Cases[m][1], Cases[m][2])
    print(
        encase_cargos_into_container(cargos, case2, VolumeGreedyStrategy)
    )
    m = 3
    case3 = Container(Cases[m][0], Cases[m][1], Cases[m][2])
    print(
        encase_cargos_into_container(cargos, case3, VolumeGreedyStrategy)
    )
    # drawer.draw_reslut(case)
    m = 4
    case4 = Container(Cases[m][0], Cases[m][1], Cases[m][2])
    print(
        encase_cargos_into_container(cargos, case4, VolumeGreedyStrategy)
    )
    # case = Container(850, 570, 480)
    # print(
    #     encase_cargos_into_container(cargos, case, VolumeGreedyStrategy)
    # )
    # case.save_encasement_as_file()
    # drawer.draw_reslut(case)
    # with open('orderxi_data.json', 'r', encoding='utf-8') as f:
    #     data = json.load(f)
    # num = 25837
    # cargos = [Cargo(170, 110, 27) for _ in range(7)]
    # for record in data[1:7955]:
    #     cargos.extend([Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])])
    # cargos = [Cargo(210,200,30) for _ in range(1)]#210,200,30
    # dingdan = 1
    # for record in data[1:7955]:
    #     if  record['case（订单）'] == dingdan:
    #         cargos.extend([Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])])
    #     else:
    #
    #         dingdan= record['case（订单）']
    #         cargos = [Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])]
