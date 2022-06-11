from sys import stdin as std
from collections  import deque
import math
def main():
    input = std.readline
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    Coordinates = [tuple(map(int,input().split())) for _ in range(N)]
    r_need = 0
    for coordinate in Coordinates :
        r = deque([10**15])
        for a in A :
            center = Coordinates[a-1]
            distance = math.sqrt((coordinate[0]-center[0])**2+(coordinate[1]-center[1])**2)
            r .append(distance)
        r_need = max(r_need,min(r))
    print(r_need)

if __name__ == '__main__':
    main()