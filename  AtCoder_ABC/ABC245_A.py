
from datetime import time

a,b,c,d = map(int,input().split())
if time(a,b,0) > time(c,d,1) :
    result = "Aoki"
else :
    result =  "Takahashi"
print(result)