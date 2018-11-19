'''
re
'''
import re
'''
pattern：匹配规则（写规则的地方）
string：要匹配(验证)的字符串
flags=0：匹配模式
    re.I:忽略大小写
    re.M:多行匹配
'''
# match:只能匹配开头
print(re.match("l","hello...word"))
# search：从左到右查找，找到就停止
print(re.search("l","hello...word"))
# findall:找到所有的元素，并把元素添加到新的列表中
print(re.findall("l","helLo...word\nabl",re.I))