def main():
    temperatures = []

    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line.lower() == "exit":
            break

        try:
            temp = float(line)
            temperatures.append(temp)
        except ValueError:
            continue

    if not temperatures:
        return

    avg = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    below_avg = [str(t) for t in temperatures if t < avg]
    print(f"Average: {avg:.2f}")
    print(f"Max: {max_temp}")
    print(f"Min: {min_temp}")
    print("Below average:")
    for t in below_avg:
        print(t)


if __name__ == "__main__":
    main()
