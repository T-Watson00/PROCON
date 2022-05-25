x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
A = (x2-x1,y2-y1)
B = (x3-x1,y3-y1)
C = (x3-x2,y3-y2)
if A[0] != 0 and A[1] != 0 :
    x,y = x1+x2-x3,y1+y2-y3
elif B[0] != 0 and B[1] != 0 :
    x,y = x1+x3-x2,y1+y3-y2
elif C[0] != 0 and C[1] != 0 :
    x,y = x2+x3-x1,y2+y3-y1
print(str(x)+" "+str(y))