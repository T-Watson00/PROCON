from sys import stdin as std


def main():
    input = std.readline
    K = int(input())
    minute = str(K % 60).zfill(2)
    hour = str(21+K // 60)
    answer = hour+":"+minute
    print(answer)


if __name__ == '__main__':
    main()