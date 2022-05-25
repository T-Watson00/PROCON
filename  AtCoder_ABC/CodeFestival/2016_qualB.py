from sys import stdin as std

def main():
    input = std.readline
    N,A,B = map(int,input().split())
    n = tuple(range(N))
    S = tuple(input())
    count_b = 0
    count = 0
    for i in n :
        if S[i] == "a" :
            if count < (A+B) :
                print("Yes")
                count += 1
            else :
                print("No")
        elif S[i] == "b" :
            count_b += 1
            if count < (A+B) and count_b <= B :
                print("Yes")
                count += 1
            else :
                print("No")
        else :
            print("No")

if __name__ == "__main__":
    main()