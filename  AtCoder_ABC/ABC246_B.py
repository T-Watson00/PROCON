from math import sqrt
A,B = map(int,input().split())
D = sqrt(A**2+B**2)
x,y = A/D,B/D
print(x,y)