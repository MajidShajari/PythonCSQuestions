def main():
    time, a, b = map(int, input().split())

    cycle_len = a + b + 2
    full_cycles = time // cycle_len

    arars = full_cycles
    mamas = full_cycles

    remaining = time % cycle_len

    if remaining >= 1:
        arars += 1
        remaining -= 1

    if remaining >= a:
        remaining -= a
    else:
        remaining = 0

    if remaining >= 1:
        mamas += 1

    print(arars, mamas)


if __name__ == "__main__":
    main()
