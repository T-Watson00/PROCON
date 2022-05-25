from sys import stdin as std
from collections import deque

def main():
    input = std.readline
    Q = int(input())
    q = tuple(range(Q))
    pype = deque([])
    query = tuple(tuple(map(int,input().split())) for _ in q)
    for i in q:
        if query[i][0] == 1 :
            plus = list([query[i][1]]*query[i][2])
            pype.extend(plus)
        elif query[i][0] == 2 :
            pype = list(pype)
            out = sum(pype[:query[i][1]])
            del pype[:query[i][1]]
            pype = deque(pype)
            print(out)


if __name__ == '__main__':
    main()