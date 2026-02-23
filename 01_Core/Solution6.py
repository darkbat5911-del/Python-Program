numer  = int(input("Enter Number "))
factorial = 1

while numer>0:
    factorial *=numer
    numer-=1
print("Factorial", factorial)