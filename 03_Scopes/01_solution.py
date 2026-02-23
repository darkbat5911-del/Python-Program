username = "Hiren"

def func():
    username = "Chai"
    print(username)
print(username)
func()

def chia(num):
    def actual(x):
        return x ** num
    return actual
squar = chia(2)
cube = chia(3)

print(squar(3))
print(cube(3))

def f1():
    # print(x)
    def f2():
        x = 5
    f2()
    print(x)
f1()