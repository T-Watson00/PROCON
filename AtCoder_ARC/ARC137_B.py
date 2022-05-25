from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    n = tuple(range(N-1))
    A = tuple(map(int,input().split()))
    result = N + 1
    
    for i in n :
        if A[i] == A[i+1] == 1 :
                count += 1
            else:
                count -= 1
        else :
            continue
    result = result + abs(count)
    print(result)

if __name__ == '__main__':
    main()