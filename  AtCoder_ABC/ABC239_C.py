from sys import stdin as std

def main():
    input = std.readline
    x1,y1,x2,y2 = map(int,input().split())
    A = latpoint(x1,y1)
    B = latpoint(x2,y2)
    if len(A & B) > 0 :
        print("Yes")
    else :
        print("No")

def latpoint(x:int,y:int):
    lat = {(x+1,y+2),(x+2,y+1),(x+1,y-2),(x+2,y-1),(x-1,y+2),(x-2,y+1),(x-1,y-2),(x-2,y-1)}
    return lat

if __name__ == '__main__':
    main()