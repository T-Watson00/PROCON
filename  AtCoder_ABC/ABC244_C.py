from sys import stdin
from sys import stdout

def main():
    input = stdin.readline
    N = int(input())
    A = set(range(1,2*N+2))
    ans = -1
    while ans != 0 :
        print(A.pop())
        stdout.flush()
        ans = int(input())
        A.discard(ans)


if __name__ == '__main__':
    main()