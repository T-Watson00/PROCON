from sys import stdin as std

def main():
    input = std.readline
    N = input()
    T = tuple(input())
    xy_ang = [[0,0],[1,0]]
    for t in T :
        move(xy_ang,t)
    print(xy_ang[0][0],xy_ang[0][1])

def move(x:list,y:str) :
    if y == "S" :
        x[0][0] += x[1][0]
        x[0][1] += x[1][1]

    elif y == "R" :
        if x[1] == [1,0] :
            x[1] = [0,-1]
        elif x[1] == [0,-1]:
            x[1] = [-1,0]
        elif x[1] == [-1,0] :
            x[1] = [0,1]
        else :
            x[1] = [1,0]



if __name__ == '__main__':
    main()