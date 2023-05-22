from sys import stdin as std


def main():
    input = std.readline
    R,C = map(int,input().split())
    Max_distance = max(abs(R-8),abs(C-8))
    if Max_distance % 2 == 0 :
        print("white")
    else :
        print("black")

if __name__ == '__main__':
    main()