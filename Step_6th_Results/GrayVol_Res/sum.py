# import glob
# import pandas as pd
# path = '/Users/qingchen/Desktop/cc/Rho*'
# file = glob.glob(path)
#
# for i in file:
#     print(i)
#     region = i.split('/')[-1][0:-4]
#     print(region)
#     box = pd.read_csv(i, sep='\t')
#     r = box.columns[0]

import glob
import pandas as pd

# 初始化一个空字典来存储region和r值
data_dict = {}

# 设置搜索模式，假设文件扩展名为.txt
path = '/Users/qingchen/Desktop/cc/pRho*.txt'
file_pattern = glob.glob(path)

# 遍历匹配的文件
for file_path in file_pattern:

    # 从文件路径中提取region名称
    region = file_path.split('/')[-1][:-4]  # 假设文件名格式为'region_something.txt'
    print('region--',region)

    # 读取CSV文件，假设r值是第一列
    box = pd.read_csv(file_path, sep='\t')

    r = box.columns[0]
    print('r',r)
    # 将region和r值保存到字典中
    data_dict[region] = r

# 将字典转换为DataFrame
df = pd.DataFrame(list(data_dict.items()), columns=['Region', 'R_Value'])


df.to_csv('./region_p_values.csv', index=False)
