import subprocess
import sys


def run_test(test_num, input_str, expected_output):
    try:
        result = subprocess.run(
            [sys.executable, "solution.py"],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=1,
            check=False,
        )
        actual_output = result.stdout.strip()
        if actual_output == expected_output:
            print(
                f"[✅] Test {test_num}: PASSED | input: {input_str.strip()} | output: {actual_output}"
            )
        else:
            print(
                f"[❌] Test {test_num}: FAILED | input: {input_str.strip()} | expected: {expected_output} | got: {actual_output}"
            )
    except Exception as e:
        print(
            f"[💥] Test {test_num}: CRASHED | input: {input_str.strip()} | error: {str(e)}"
        )


def main():
    tests = [
        (1, "10 1 1\n", "3 2"),
        (2, "0 1 1\n", "0 0"),
        (3, "1 5 5\n", "1 0"),
        (4, "3 5 5\n", "1 0"),
        (5, "3 1 5\n", "1 1"),
        (6, "4 1 1\n", "1 1"),
        (7, "8 1 1\n", "2 2"),
        (8, "20 5 5\n", "2 2"),
        (9, "6 2 2\n", "1 1"),
        (10, "7 2 2\n", "2 1"),
    ]

    for test_num, input_str, expected_output in tests:
        run_test(test_num, input_str, expected_output)


if __name__ == "__main__":
    main()
