from sys import stdin as std
def main():
    input = std.readline
    a,b,c,d,e,f,x = map(int,input().split())
    takahashi = a+c
    aoki = d+f
    t_set = (x // takahashi)*a
    a_set = (x // aoki)*d
    t_mod = x % takahashi
    a_mod = x % aoki
    if t_mod >= a :
        t_set += a
    else :
        t_set += t_mod
    if a_mod >= d :
        a_set += d
    else :
        a_set += a_mod
    t_distance = b*t_set
    a_distance = e*a_set
    if t_distance > a_distance :
        print("Takahashi")
    elif t_distance == a_distance :
        print("Draw")
    else :
        print("Aoki")


if __name__ == '__main__':
    main()