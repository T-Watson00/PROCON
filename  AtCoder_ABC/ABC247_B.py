from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    name = list(set(map(str,input().split())) for _ in range(N))
    Set = set()
    for i in range(N-1) :
        Set.add(name[i])
        for j in range(i+1,N) :
            if (name[j] & Set) != set() :
                name[i] = name[i] - (name[i] & name[j])
                name[j] = name[j] - (name[j] & Set)
                if name[i] == set() or name[j] == set() :
                    print("No")
                    exit()
    print("Yes")

if __name__ == '__main__':
    main()