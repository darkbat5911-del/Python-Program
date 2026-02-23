import math
def circle(r):
    area = math.pi * r**2
    circum = 2 * math.pi * r
    return area, circum
A,C = circle(3)
print("Area", round(A, 2), "Circum", round(C,2)) 