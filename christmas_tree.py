#روش اول
def method1():
    for i in range(1, 14, 2):
        print("{:^13}".format("*"*i))


# روش دوم
def method2(n):
    for i in range(1, n+1, 2):
        c = "*"*i
        print(c.center(n))


if __name__ == "__main__":
    method1()
    method2(33)