def plus(*args):
    for i in args:
        print(i*2)
    return sum(args)
print("Sum Of this : ",plus(1,2,3))