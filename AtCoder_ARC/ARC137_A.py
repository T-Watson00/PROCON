from sys import stdin as std
import math

def main():
    input = std.readline
    L,R = map(int,input().split())
    for d in range(R-L,0,-1):
        for x in range(L,R-d+1,1):
            if math.gcd(x,d) == 1 :
                print(d)
                exit()

if __name__ == '__main__':
    main()