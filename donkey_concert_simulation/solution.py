def main():
    t, a, b = [int(x) for x in input().split()]
    ar_count = ma_count = int((t - 2) / (a + b))
    remain = ((t - 2) / (a + b)) - ar_count
    if remain == 0:
        print(ar_count, ma_count)
    else:
        print(ar_count + 1, ma_count)


if __name__ == "__main__":
    main()
