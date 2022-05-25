from sys import stdin as std

def main():
    input = std.readline
    N,V = map(int,input().split())
    A = tuple(map(int,input().split()))
    n = tuple(range(N))
    place = -1
    for i in reversed(n):
        if A[i] == V:
            place = i
            break
    print(place)
if __name__ == '__main__':
    main()