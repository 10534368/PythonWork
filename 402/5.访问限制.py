'''
访问限制
私有：只能自己使用的，别人不能使用
好处：外部不能随意更改，安全性提高
        数据过滤
'''

class Person:
    def __init__(self):
        self.name=None
        self.__age=None

    def setAge(self,a):
        if a<0:
            print("不合法")
        else:
            self.__age=a

    def getAge(self):
        return self.__age

p1=Person()
p1.setAge(-10)
print(p1.getAge())
