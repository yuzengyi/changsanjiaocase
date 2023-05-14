# import pandas as pd
# order_numbers = ['D001', 'D002', 'D003', 'D004', 'D005']
# schemes = [['A', 'C', 'C', 'C', 'C'], ['B', 'C', 'C', 'C', 'C'], ['A', 'D', 'C', 'C', 'C'], ['A', 'B', 'C', 'C', 'C'], ['B', 'D', 'C', 'C', 'C']]
# data = {'订单号': order_numbers}
# for i in range(len(schemes)):
#     data['方案{}'.format(i+1)] = schemes[i]
# print(data)
# df = pd.DataFrame(data)
# df.to_excel('result.xlsx', index=False)
import pandas as pd

# 模拟数据
data = [
    ['John', 25, 'Male'],
    ['Alice', 30, 'Female'],
    ['Bob', 28, 'Male']
]

# 将数据包装为 DataFrame 对象
df = pd.DataFrame(data, columns=['Name', 'Age', 'Gender'])

# 将数据写入 Excel 文件，覆盖已有内容
df.to_excel('output.xlsx', index=False, header=True)


