# san_jiao
# n  输出长度为n
# import time
# print(time.strftime("%Y%m%d%H%M%S"))
# list=[0,1]
def san_jiao(list):
    list1=[0, 1]
    for i in list[1::]:
        print(i,end="\t")
    print("\n")
    n=len(list)
    for i in range(1,n):
        list1.insert(i, list[i-1]+list[i])
    if n==11:
        exit()
    return san_jiao(list1)

# san_jiao(list)


