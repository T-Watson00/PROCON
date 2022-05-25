from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    S = "1"
    if N == 1:
        print(S)
        exit()
    for i in range(1,N):
        S = S+str(i+1)+S
    print(' '.join(map(str, S)))


if __name__ == '__main__':
    main()