from sys import stdin as std

def main():
    input = std.readline
    S = input()
    n = len(S)
    s_set = set(S[i] for i in range(n))
    s = tuple(s_set)
    Rarge = False
    Small = False
    if len(s_set) != n :
        print("No")
        exit()
    else :
        for j in s :
            if 90 >= ord(j) >= 65 :
                Rarge = True
                break
        if Rarge == False :
            print("No")
            exit()
        else :
            for j in s :
                if 122 >= ord(j) >= 97 :
                    Small = True
                    break
            if Small == False :
                print("No")
            else :
                print("Yes")


if __name__ == '__main__':
    main()