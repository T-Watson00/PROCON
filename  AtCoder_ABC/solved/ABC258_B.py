from sys import stdin as std
import numpy as np

def main():
    input = std.readline
    N = int(input())
    A = [str(input().strip()*3) for _ in range(N)]
    answer = 0
    for i in range(N) :
        horizontal_list = np.array(list(map(int,A[i][0:N])))
        for n in range(N) :
            horizontal = "".join(list(map(str,list(np.roll(horizontal_list,n)))))
            answer = max(answer,int(horizontal))
            h_reversed = "".join(list(reversed(horizontal)))
            answer = max(answer,int(h_reversed))
    for j in range(N) :
        vartical_list = np.array(list(map(int,[A[v][j] for v in range(N)])))
        for n in range(N) :
            vartical = "".join(list(map(str,list(np.roll(vartical_list,n)))))
            answer = max(answer,int(vartical))
            v_reversed = "".join(list(reversed(vartical)))
            answer = max(answer,int(v_reversed))
    for k in range(N) :
        right_down_list = np.array(list(map(int,[A[R][k+R]  for R in range(N)])))
        for n in range(N) :
            right_down = "".join(list(map(str,list(np.roll(right_down_list,n)))))
            answer = max(answer,int(right_down))
            r_reversed = "".join(list(reversed(right_down)))
            answer = max(answer,int(r_reversed))
    for l in range(N) :
        left_down_list = np.array(list(map(int,[A[L][-l-1-L]  for L in range(N)])))
        for n in range(N) :
            left_down = "".join(list(map(str,list(np.roll(left_down_list,n)))))
            answer = max(answer,int(left_down))
            l_reversed = "".join(list(reversed(left_down)))
            answer = max(answer,int(l_reversed))

    print(answer)




if __name__ == '__main__':
    main()