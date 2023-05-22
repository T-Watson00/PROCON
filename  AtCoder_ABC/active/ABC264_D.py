
def main():
    S = str(input())
    S_list = list(S)
    String = "atcoder"
    String_list = list(String)
    count = 0
    for s in String :
        s_index_in_S = S_list.index(s)
        s_index_in_String = String_list.index(s)
        if s_index_in_S > s_index_in_String :
            count += s_index_in_S - s_index_in_String
            S_list = String_list[:s_index_in_String+1]+S_list[s_index_in_String:s_index_in_S]+S_list[s_index_in_S+1:]
    print(count)


if __name__ == '__main__':
    main()