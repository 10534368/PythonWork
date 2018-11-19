#-*- coding: utf-8 -*-
# re模块
import re
# re.match()三个参数 1 匹配规则 2 要匹配的字符串 3 匹配模式
# re.I 忽略大小写
# re.M 多行匹配
a="ukdHavHvaHdbmbjcHbajbajHbksuhghdfhohhfiohg,,,soihsoihgoihfdksfhhvdnlbskljdbjkbfljvndskjbskudf--bkaHbalnaslkndlnvlaknlknaldskblajsxnlkncxzx4"
print(re.match("H",a))
#只能匹配开头
print(re.search("H",a))
print(re.findall(".",a,re.I))
print(a.count("H"))


# 正则规则
# . [^abkjsbf] \d \D \w \W \s \S
print(re.findall("[b-zB-Z0-9-]",a))

# 锚字符 边界字符
# ^  $ \A \Z \b \B

# () x?  x*  x+  x{n} x{n,} x|y