from sys import stdin as std

def solved_finder(point:int) :
    if point == 0 :
        return "000"
    elif point == 1 :
        return "100"
    elif point == 2 :
        return "010"
    elif point == 3 :
        return "110"
    elif point == 4 :
        return "001"
    elif point == 5 :
        return "101"
    elif point == 6 :
        return "011"
    elif point == 7 :
        return "111"


def main():
    input = std.readline
    A,B = map(int,input().split())
    takahashi_solved = solved_finder(A)
    aoki_solved = solved_finder(B)
    sunuke_point = 0
    if takahashi_solved[0] == "1" or aoki_solved[0] == "1" :
        sunuke_point += 1
    if takahashi_solved[1] == "1" or aoki_solved[1] == "1" :
        sunuke_point += 2
    if takahashi_solved[2] == "1" or aoki_solved[2] == "1" :
        sunuke_point += 4
    print(sunuke_point)


if __name__ == '__main__':
    main()