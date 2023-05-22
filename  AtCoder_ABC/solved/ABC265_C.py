from sys import stdin as std

input = std.readline
H,W = map(int,input().split())
G = [list(input().strip()) for _ in range(H)]

def main():
    count = 0
    now_place = (1,1)
    aready_place=set(now_place)
    while count <= H*W :
        new_place = Operation(now_place,G[now_place[0]-1][now_place[1]-1])
        if now_place == new_place :
            print(now_place[0],now_place[1])
            exit()
        else :
            count += 1
            if new_place in aready_place :
                print("-1")
                exit()
            else :
                aready_place.add(new_place)
                now_place = new_place
    print("-1")

def Operation(place:tuple,g:str):
    if g == "U" and place[0] != 1 :
        return (place[0]-1,place[1])

    elif g == "D" and place[0] != H :
        return (place[0]+1,place[1])

    elif g == "L" and place[1] != 1 :
        return (place[0],place[1]-1)

    elif g == "R" and place[1] != W :
        return (place[0],place[1]+1)

    else :
        return place


if __name__ == '__main__':
    main()