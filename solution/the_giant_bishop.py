def main():
    x, y = map(int, input().split())

    for i in range(2, 8):
        if (i, i) != (x, y):
            if x == 2 and y == 2:
                print(1)
                print(7)
                print(7)
                return
            print(1)
            print(i)
            print(i)
            return


if __name__ == "__main__":
    main()
