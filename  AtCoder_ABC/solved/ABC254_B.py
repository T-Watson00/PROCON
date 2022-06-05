from sys import stdin as std
from math import factorial


def print_binomial_coefficient(n :int) :
    list = ' '.join([str(factorial(n) // factorial(r) // factorial(n - r)) for r in range(n+1)])
    print(list)

def main():
    input = std.readline
    N = int(input())
    for i in range(0,N,1):
        print_binomial_coefficient(i)


if __name__ == '__main__':
    main()