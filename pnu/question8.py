import random


def main(target=None):
    target = target if target else random.randint(1, 50)
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = input().strip()
        except EOFError:
            break

        if not guess.isdigit():
            continue

        guess = int(guess)
        attempts += 1

        if guess == target:
            print("Congratulations! You guessed the number.")
            break

    print(f"Attempts: {attempts}")


if __name__ == "__main__":
    # main(target=42)
    main()
