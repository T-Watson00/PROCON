from sys import stdin as std
import math

def main():
    input = std.readline
    H = int(input())
    horizon = math.sqrt(H*(128*(10**5)+H))
    print(horizon)

if __name__ == '__main__':
    main()