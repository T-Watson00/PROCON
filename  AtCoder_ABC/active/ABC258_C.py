from sys import stdin as std

def main():
    input = std.readline
    N,Q = map(int,input().split())
    S = input().strip()
    Query = [tuple(map(int,input().split())) for _ in range(Q)]
    for i in range(Q) :
        if Query[i][0] == 1 :
            S=operation_1(S,N,Query[i][1])
            continue
        elif Query[i][0] == 2:
            operation_2(S,Query[i][1])
            continue



def operation_1(s:str,n:int,x:int) :
    rolling = s[-x:]+s[:n-x]
    return rolling

def operation_2(s:str,x:int) :
    print(s[x-1])



if __name__ == '__main__':
    main()