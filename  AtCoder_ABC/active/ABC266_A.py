from sys import stdin as std


def main():
    input = std.readline
    S = input().strip()
    print(S[(len(S)-1)//2])


if __name__ == '__main__':
    main()