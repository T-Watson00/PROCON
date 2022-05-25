from sys import stdin as std
def main():
    input = std.readline
    A = tuple(map(int,input().split()))
    number = 0
    count = tuple(range(3))
    for c in count :
        number = A[number]
    print(number)

if __name__ == "__main__":
    main()
