from sys import stdin as std

def main():
    input = std.readline
    N = input()
    A = tuple(map(int,input().split()))
    count = 0
    for i in A:
        if i > 0:
            count += 1
    print(count)
if __name__ == '__main__':
    main()