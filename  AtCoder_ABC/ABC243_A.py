from sys import stdin as std

def main():
    input = std.readline
    V,A,B,C = map(int,input().split())
    total = A + B + C
    lest = int(V % total)
    if lest - A < 0 :
        print("F")
    else :
        lest = lest - A
        if lest - B < 0 :
            print("M")
        else :
            print("T")

if __name__ == '__main__':
    main()