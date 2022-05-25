from sys import stdin as std

def main():
    input = std.readline
    N,X = map(int,input().split())
    n = tuple(range(N))
    x = tuple(range(X))
    AB = list(list(map(int,input().split())) for i in n)
    A = [i[0] for i in AB]
    B = [i[1] for i in AB]
    dp = [[0]*(X+1) for i in range(N+1)]
    dp[0][0] = 1
    result = "No"
    if sum(A) <= X <= sum(B) :
        for i in n :
            for j in x :
                if dp[i][j] == 1 :
                    if j+ A[i] <= X :
                        dp[i+1][j+A[i]] = 1
                    if j+ B[i] <= X :
                        dp[i+1][j+B[i]] = 1
        if dp[N][X] == 1 :
            result = "Yes"
    print(result)

if __name__ == '__main__':
    main()