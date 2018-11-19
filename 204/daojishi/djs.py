import time


def main():
    for i in range(60, -1, -1):
        print("\r{}秒后可以再次获取验证码".format(i), end="")
        time.sleep(1)


def DAOJISHI():
    n = 1
    while n > 0:
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                for s in range(59, -1, -1):
                    print("\r剩余{}天{}时{}分{}秒{}".format(n, h, m, s, time.ctime()), end="")
                    time.sleep(1)
                    if h == 0 and m == 20 and s == 0:
                        exit()
        n -= 1


def SHIZHONG():
    print("\r{}".format(time.ctime()), end="")
    time.sleep(1)


if __name__ == "__main__":
    while True:
        SHIZHONG()