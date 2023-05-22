from sys import stdin as std


def main():
    input = std.readline
    A = tuple(map(int,input().split()))
    B = tuple(map(int,input().split()))
    C = tuple(map(int,input().split()))
    D = tuple(map(int,input().split()))
    Area_set = list(map(Signed_triangle_area,[A,B,C,D],[B,C,D,A],[C,D,A,B]))
    if all(Area_set) == True or not any(Area_set) == True :
        print("Yes")
    else :
        print("No")

def Signed_triangle_area(a:tuple,b:tuple,c:tuple) :
    area = ((a[0]-b[0])*(c[1]-b[1])-(a[1]-b[1])*(c[0]-b[0]))/2
    if area > 0 :
        return True
    else :
        return False



if __name__ == '__main__':
    main()