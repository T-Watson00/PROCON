from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    A = int(str(input().replace(" ","").strip()),2)
    n = tuple(range(1,N))
    Set = set({0})
    new_set = set({0})
    for i in n:
        new = tuple(new_set)
        new_set = set({})
        for j in new :
            x,y = 2*j,(2**i-1)^j
            new_set = new_set | {x,y}
    if A in new_set :
        result = "Yes"
    else :
        result = "No"
    print(result)

if __name__ == '__main__':
    main()