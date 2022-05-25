from sys import stdin as std
from collections import deque
import numpy as np

def main():
    input = std.readline
    N,K = map(int,input().split())
    n = tuple(range(N-1))
    A = tuple(map(int,input().split()))
    B = tuple(map(int,input().split()))
    a = deque([True])
    b = deque([True])
    result = "No"
    error = False
    for i in n:
        if abs(A[i]-A[i+1]) <= K and a[i]==True :
            a.append(True)
        elif abs(B[i]-A[i+1]) <= K and b[i]==True:
            a.append(True)
        else :
            a.append(False)
        if abs(A[i]-B[i+1]) <= K and a[i]==True :
            b.append(True)
        elif abs(B[i]-B[i+1]) <= K and b[i]==True:
            b.append(True)
        else :
            b.append(False)
        if a[i+1] == False and b[i+1] == False :
            error = True
            break
    if not error == True :
        result = "Yes"
    print(result)


if __name__ == '__main__':
    main()