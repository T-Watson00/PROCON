def main():
    S = input()
    T = input()
    A = {"R G B", "G B R", "B R G"}
    if (S in A) == (T in A) :
        print("Yes")
    else :
        print("No")

if __name__ == '__main__':
    main()