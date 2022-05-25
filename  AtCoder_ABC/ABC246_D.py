from math import pow
from math import floor
from math import ceil
import sympy as sp
N = int(input())
if N == 0:
    print(N)
else :
    for i in range(1,5):
        if i == 1:
            a = floor(pow(N/i,1/3))
        if i == 4:
            a = ceil(pow(N/i,1/3))
        delta = (N/a**3)-1
        x = sp.Symbol('x')
        sol = sp.solve(x**3+x**2+x-delta,x)
        b = ceil(sol[0]*a)
        print(a,b)
        if i == 1:
            X = (a**2+b**2)*(a+b)

        else :
            if X > (a**2+b**2)*(a+b):
                X = (a**2+b**2)*(a+b)
    print(X)
