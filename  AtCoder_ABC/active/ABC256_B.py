from sys import stdin as std


def main():
    input = std.readline
    N = int(input())
    A = list(map(int,input().split()))
    Board = [0,0,0,0,0]
    for a in A:
        Board[0] += 1
        for i in [3,2,1,0] :
            number = Board[i]
            if i+a <= 3 :
                Board[i+a] += number
                Board[i] = 0
            else :
                Board[4] += number
                Board[i] = 0
    print(Board[4])


if __name__ == '__main__':
    main()