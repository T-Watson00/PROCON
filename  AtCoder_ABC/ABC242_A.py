A,B,C,X = map(int,input().split())
if 1 <= X <= A  :
    prob = float(1)
    
elif A+1 <= X <= B :
    prob = float(C/(B-A))

else:
    prob = float(0)
print(prob)
