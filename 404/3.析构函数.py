'''
析构函数：
    在结束的时候自动执行的
执行时间：
    1.如果是全局，程序结束自动执行
    2.如果是局部，比如在函数中，函数执行完毕就自动执行
    3.手动删除 del   删除之后不能再次使用
4
垃圾回收（自动）
'''
class Person:

    def __init__(self):
        print("我出生了")

    def eat(self):
        print("吃饭")
    def __del__(self):
        print("我走了")



p=Person()
p.eat()

for i in range(10):
    if i==7:
        del p

p.eat()