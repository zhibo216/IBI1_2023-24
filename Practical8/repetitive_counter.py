# seq= 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
# c=0 # the number of repetitive sequence
# a=len(seq)
# for i in range(a-5):
#     if seq[i:i+6]=='GTGTGT'or seq[i:i+6]=='GTCTGT':
#         c+=1
# print(f'there are {c} repeat elements')

import re

seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'

# 使用正则表达式查找所有匹配的元素
pattern1 = 'GTGTGT'
pattern2 = 'GTCTGT'

# 找到所有匹配的索引
matches1 = [m.start() for m in re.finditer(pattern1, seq)]
matches2 = [m.start() for m in re.finditer(pattern2, seq)]

print(f"'{pattern1}' found at positions: {matches1}")
print(f"'{pattern2}' found at positions: {matches2}")