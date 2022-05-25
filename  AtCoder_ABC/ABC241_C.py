from sys import stdin as std

def main() :
    input = std.readline
    N = int(input())
    S = list(list(input().strip()) for i in range(N))

    #"."を0に,"#"を１に変換
    S =[[int(1) if i == "#" else int(0) for i in t]for t in S]
    n = tuple(range(N))
    m = tuple(range(N-5))
    result = "No"
    if not  sum(map(sum, S)) < 4 :
        for i in n :
            if sum(S[i]) < 4 :
                continue
            for j in m :
                count = S[i][j] + S[i][j+1] + S[i][j+2] + S[i][j+3] + S[i][j+4] + S[i][j+5]
                if count >= 4 :
                    result = "Yes"
                    break
        if result == "No" :
            S_t = [list(x) for x in zip(*S)]
            for i in n :
                if sum(S_t[i]) < 4 :
                    continue
                for j in m :
                    count = S_t[i][j] + S_t[i][j+1] + S_t[i][j+2] + S_t[i][j+3] + S_t[i][j+4] + S_t[i][j+5]
                    if count >= 4 :
                        result = "Yes"
                        break
        if result == "No" :
            for i in m :
                for j in m :
                    count = S[i][j] + S[i+1][j+1] + S[i+2][j+2] + S[i+3][j+3] + S[i+4][j+4] + S[i+5][j+5]
                    if count >= 4 :
                        result = "Yes"
                        break
        if result == "No" :
            for i in m :
                for j in m :
                    count = S[i][N-(j+1)] + S[i+1][N-(j+2)] + S[i+2][N-(j+3)] + S[i+3][N-(j+4)] + S[i+4][N-(j+5)] + S[i+5][N-(j+6)]
                    if count >= 4 :
                        result = "Yes"
                        break

    print(result)


if __name__ == "__main__" :
    main()
