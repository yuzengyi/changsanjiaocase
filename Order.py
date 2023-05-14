import pandas as pd
import json

# 读取Excel文件
df = pd.read_excel("附件1-装箱数据.xlsx", sheet_name="订单数据", usecols="A:E", skiprows=0, nrows=10000)

# 将DataFrame转换为字典
data = df.to_dict(orient='records')

# 存储成json格式
with open('all_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
