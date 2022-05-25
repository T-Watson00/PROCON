from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    n = tuple(range(N))
    XY = set(tuple(map(str,input().split())) for _ in n)
    S = tuple(input().strip())
    result = "No"
    for i in n :
        XY[i].append(str(S[i]))

    print(result)

if __name__ == '__main__':
    main()