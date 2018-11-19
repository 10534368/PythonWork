#-*- coding: utf-8 -*-
import json
# json.dump()
# json.load()
# 需要自定义函数 即转换规则 (存取对象时)贼复杂 不建议使用

# 列表生成式 :
# list1=range(0,11)
# 列表推导式 根据一定的规则生成列表
# range
l=["ncasbub","DSICdvnslknl",10]
l1=[i.lower() if isinstance(i,str)else i for i in l ]
print(l1)
