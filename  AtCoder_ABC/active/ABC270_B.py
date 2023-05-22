from sys import stdin as std

def distance_solver(x:int,y:int,z:int) :
    if x<y and y<z :
        if 0<y :
            return abs(x)
        elif y<0 and 0<z :
            return 2*z-x
        elif z<0 :
            return abs(x)

    elif  x<z and z<y :
        if 0<y :
            return abs(x)
        else :
            return -1

    elif y<x and x<z :
        if 0<y :
            return -1
        else :
            return abs(x)

    elif y<z and z<x :
        if 0<y :
            return -1
        else :
            return abs(x)

    elif z<x and x<y :
        if 0<y :
            return abs(x)
        else :
            return -1

    elif z<y and y<x :
        if 0<z :
            return x
        elif z<0 and 0<y :
            return 2*abs(z)+x
        else :
            return abs(x)


def main():
    input = std.readline
    X,Y,Z = map(int,input().split())
    print(distance_solver(X,Y,Z))



if __name__ == '__main__':
    main()