# 2 3 5 7 23 37 53 73 373
# 由题意可知2,3,5,7 及 由2 3 5 7 组成的数字为完美素数
def su_shu(lie_biao=list((2,3,5,7)),num=list((2,3,5,7)),m=10):
    for i in range(m,10*m):
        n = 0
        for j in num:
            if i % j == 0:
                n+=1
        if n==0:
            num.append(i)
            if i//10 in lie_biao and i%m in lie_biao:
                lie_biao.append(i)
    for j in lie_biao:
        if j>m:
            return su_shu(lie_biao,num,10*m)
    return lie_biao

n=su_shu()
print(n)
number = int(input("输入1-1000以内的正整数:"))
try:
    print(n[number - 1])
except:
    print(-1)

