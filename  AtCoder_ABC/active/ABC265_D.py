from sys import stdin as std

def main():
    input = std.readline
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    Sum_A = [sum(A[:n]) for n in range(1,N+1)]
    for x in range(N-3) :
        Sum_1_x = Sum_A[x]
        


if __name__ == '__main__':
    main()