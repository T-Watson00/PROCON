from sys import stdin as std

def main():
    input = std.readline
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    room_num = 1
    bonus = 0
    if M > bonus :
        bonus_room,bonus_time= map(int,input().split())
        bonus += 1
        while room_num < N :
            T -= A[room_num-1]
            if T <= 0 :
                print("No")
                exit()
            room_num += 1
            if  room_num < bonus_room :
                continue
            elif room_num == bonus_room :
                T += bonus_time
                bonus += 1
                if bonus <= M :
                    bonus_room,bonus_time= map(int,input().split())
        print("Yes")
    else :
        if T > sum(A) :
            print("Yes")
        else :
            print("No")

if __name__ == '__main__':
    main()