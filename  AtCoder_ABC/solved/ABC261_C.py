from sys import stdin as std

def main():
    input = std.readline
    N = int(input())
    String_dictionary = dict()
    for _ in range(1,N+1):
        Input_String = input().strip()
        if not Input_String in String_dictionary :
            print(Input_String)
            String_dictionary[Input_String] = 1
        else :
            print(Input_String+f"({String_dictionary[Input_String]})")
            String_dictionary[Input_String] += 1


if __name__ == '__main__':
    main()
    