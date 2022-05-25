from sys import stdin as std
input = std.readline
a,b = map(int,input().split())
if b-a == 1 or (b == 10 and a == 1) :
    print("Yes")
else :
    print("No")
