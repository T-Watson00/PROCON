from sys import stdin as std
def main() :
    input = std.readline
    N = int(input())
    a = [[0]* N for i in range(9)]
    total = 0
    mod = 998244353
    for i in range(9):
        a[i][0] = 1
    for i in range (1,N) :
            a[0][i] = int((a[0][i-1] +  a[1][i-1]) % mod)
            a[1][i] = int((a[0][i-1] +  a[1][i-1] + a[2][i-1]) % mod )
            a[2][i] = int((a[1][i-1] +  a[2][i-1] + a[3][i-1]) % mod )
            a[3][i] = int((a[2][i-1] +  a[3][i-1] + a[4][i-1]) % mod )
            a[4][i] = int((a[3][i-1] +  a[4][i-1] + a[5][i-1]) % mod )
            a[5][i] = a[3][i]
            a[6][i] = a[2][i]
            a[7][i] = a[1][i]
            a[8][i] = a[0][i]
    for i in range(9):
        total += a[i][N-1]
    answer = int(total % mod)
    print(answer)

if __name__ == "__main__":
    main()