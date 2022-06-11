from sys import stdin as std

def main():
    input = std.readline
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    for q in range(Q):
        X = int(input())
        X_list = [X]*N
        delta_sum = sum(list(map(lambda x, y: abs(x-y),A,X_list)))
        print(delta_sum)

if __name__ == '__main__':
    main()