#-*- coding: utf-8 -*-
#  异常处理
#  从上到下依次执行  报错就不再执行后半段
#  异常处理的目的 程序出错之后 给出错误提示信息 程序继续执行
# 格式  try...except...else
#       try...except...finally

a=10
b=10
list=[]
try:
    print(a/b)
    print(list)
except ZeroDivisionError as e:
    print("除数不能为零")
except IndexError as e:
    print("错了哟")
else:
    print("True")
finally:
    print("不管有没有错误都执行")
print("over")






