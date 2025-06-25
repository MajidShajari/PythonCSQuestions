import subprocess
import sys


def run_test(test_num, input_str, expected_output):
    try:
        result = subprocess.run(
            [sys.executable, "solution.py"],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=2,
            check=False,
        )
        actual_output = result.stdout.replace("\n", " ", 2).replace("\n", "")
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
        (1, "4 4\n", "1 2 2"),
        (2, "1 2\n", "1 2 2"),
        (3, "3 7\n", "1 2 2"),
        (4, "5 5\n", "1 2 2"),
        (5, "1 5\n", "1 2 2"),
        (6, "2 3\n", "1 2 2"),
        (7, "2 4\n", "1 2 2"),
        (8, "8 4\n", "1 2 2"),
        (9, "2 2\n", "1 7 7"),
        (10, "7 7\n", "1 2 2"),
    ]

    for test_num, input_str, expected_output in tests:
        run_test(test_num, input_str, expected_output)


if __name__ == "__main__":
    main()
