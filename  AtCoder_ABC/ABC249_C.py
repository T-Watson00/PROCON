from sys import stdin as std

def main():
    input = std.readline
    n,k = map(int,input().split())
    S_set = tuple( set(tuple(input().replace('\n',''))) for _ in range(n))
    alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    count = [0]*26
    result = 0
    for s in S_set :
        for i in alphabet :
            if i in s :
                count[int(ord(i)-97)] += 1
    max_ans = max(count)
    
if __name__ == '__main__':
    main()