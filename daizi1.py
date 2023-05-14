import json
import pandas as pd
from Encase3D import *
from Encase3D import drawer
if __name__ == "__main__":
    with open('orderdaizixi_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    dingdan = 1
    case = []
    # Cases = [[250, 190, 1], [300, 250, 1], [400, 330, 1], [450, 420, 1]]
    Cases = [[250, 190, 1], [300, 250, 1], [400, 330, 1], [450, 420, 1]]
    cargos = [Cargo(210, 200, 30) for _ in range(1)]
    cargos.extend([Cargo(170, 110, 27) for _ in range(7)])
    #maxx = 0#最大的x
    #maxy = 0#最大的y
    case = Container(450, 420, 1)
    print(
        daizifailed_encase_cargos_into_container(cargos, case, VolumeGreedyStrategy)
    )
    case.save_encasement_as_file()
    drawer.draw_reslut(case)
