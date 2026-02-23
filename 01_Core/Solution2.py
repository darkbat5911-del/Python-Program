num = int(input("num"))
sum_even = 0

for i in range(1, num+1):
    if i%2 == 0:
        sum_even += 1

print("Sum of even number : ", sum_even)