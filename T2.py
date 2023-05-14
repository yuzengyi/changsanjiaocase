import pandas as pd
Vs = [47500,75000,132000,189000]#47500	75000	132000	189000

def process_excel_file(file_path):
    # 读取Excel文件
    df = pd.read_excel(file_path)
    # 从第二行开始遍历每一行
    for index in range(0, len(df)):
        # 选取当前行中除第一列以外的所有非空值，并转换为数字
        row = df.iloc[index, 1:]
        print(row)
        row = row[row.notna() & (row != '')]
        print(row)
        values = [int(v) for v in row]
        print(values)
        if len(values) == 0:
            # 如果该行中所有单元格都为空，则最小值和最小值位置均为None
            min_value, min_index = None, None
        else:
            # 否则找到最小的值及其位置
            min_value = min(values)
            print(min_value )
            min_index = values.index(min_value) + 1
            print(min_index)

        # 在最后两列插入数据
        df.loc[index, '袋子数'] = min_value
        df.loc[index, '袋子编号'] = min_index
        df.loc[index, '订单耗材体积'] = min_value*Vs[min_index-1]
    # 保存修改后的Excel文件
    df.to_excel('T1仅袋子求解结果.xlsx', index=False)

process_excel_file('daizi1result.xlsx')
