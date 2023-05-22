from sys import stdin as std

def main():
    input = std.readline
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    S = sum([ (i+1)*A[i] for i in range(M)])
    S_list = [S]
    Sum_M = 0
    Sum_M_list = [Sum_M]
    for i in range(N) :
        Sum_M += A[i]
        Sum_M_list.append(Sum_M)
    for j in range(N-M) :
        S = S-Sum_M_list[j+M]+Sum_M_list[j]+M*A[j+M]
        S_list.append(S)
    print(max(S_list))





if __name__ == '__main__':
    main()