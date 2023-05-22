from sys import stdin as std

def main():
    input = std.readline
    X,Y,N = map(int,input().split())
    Price = 0
    if 3*X >= Y :
        Price = Y*(N //3)+ X*(N % 3)
    else :
        Price = X*N
    print(Price)


if __name__ == '__main__':
    main()