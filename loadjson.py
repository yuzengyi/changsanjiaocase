import json
from Encase3D import *
from Encase3D import drawer

# 从json文件中加载数据
with open('orderxi_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(len(data))
# num = 25837
# cargos = [Cargo(170, 110, 27) for _ in range(7)]
# for record in data[1:10000]:
#     cargos.extend([Cargo(record['l（长）'], record['w（宽）'], record['h（高）']) for _ in range(record['num（数量）'])])
#
# # 获取第一个货物的长度参数
# # 获取第一个货物的长度参数
# length = cargos[8].length
# print(cargos[0])
# print(cargos[num-1])
#print(cargos[0])
#print(cargos[0]._point)#._shape
#print(cargos[0]._shape)