from sys import stdin as std

def main():
    input = std.readline
    X,A,D,N = map(int,input().split())
    
    for s in S_int :
    (s-X)%D
    delta_min = 10**20
    for delta in S_X_delta :
        if delta % 1 == 0 :
            delta_min = min(delta_min,abs(delta))
    print(delta_min)


if __name__ == '__main__':
    main()