from sys import stdin as std
import collections
def main() :
    input = std.readline
    N,M = map(int,input().split())
    A = tuple(map(int,input().split()))
    B = tuple(map(int,input().split()))
    delta(A,B)


def delta(x: tuple,y: tuple):
    count = collections.Counter
    x_count = count(x)
    y_count = count(y)
    z = y_count & x_count
    if z == y_count :
        print("Yes")
    else :
        print("No")


if __name__ == "__main__":
    main()