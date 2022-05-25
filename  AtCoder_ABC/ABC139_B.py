from sys import stdin as std
import math

def main():
    input = std.readline
    A,B = map(int,input().split())
    answer = math.ceil((B-1)/(A-1)) 
    print(answer)

if __name__ == '__main__':
    main()