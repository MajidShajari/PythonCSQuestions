import json
import subprocess
import sys

class TestCase:
    def __init__(self, _question_id, _file_solution_name, _input_prompt_prefix=None):
        self.question_id = _question_id
        self.file_solution_name = _file_solution_name
        self.input_prompt_prefix = _input_prompt_prefix
        self.passed_tests = 0

    def _get_tests(self):
        with open("expected_outputs.json", "r") as f:
            excepted_outputs = json.load(f)
        for question in excepted_outputs:
            if question["question_id"] == self.question_id:
                return question["tests"]
        return []

    def run_tests(self):
        tests = self._get_tests()
        if len(tests) == 0:
            print(f"[❌] No tests found for question_id {self.question_id}")
            return
        for test in tests:
            test_num = test["test_num"]
            input_str = test["input_str"]
            expected_outputs = test.get("expected_outputs", [])
            self.passed_tests=self.passed_tests+1 if self._handle_run_tests(test_num, input_str, expected_outputs)else self.passed_tests
        print(f"\n[🏁]Passed {self.passed_tests} of {len(tests)} tests.")
    def _handle_run_tests(self, test_num, input_str, expected_outputs):
        test_passed = False
        try:
            result = subprocess.run(
                [sys.executable, self.file_solution_name],
                input=input_str,
                capture_output=True,
                text=True,
                check=False,
            )
            actual_output = result.stdout.strip()
            if self.input_prompt_prefix:
                actual_output = (
                    "\n".join(
                        line
                        for line in actual_output.splitlines()
                        if not line.strip().startswith(self.input_prompt_prefix)
                    )
                    .strip()
                    .replace("\n", " ")
                )
            actual_output = actual_output.split() if len(actual_output) > 0 else []
            if actual_output == expected_outputs:
                print(
                    f"[✅] Test {test_num}: PASSED\nInput:\n{input_str.strip()}"
                    f"\nOutput:\n{actual_output}"
                )
                test_passed = True
            else:
                print(
                    f"[❌] Test {test_num}: FAILED\nInput:\n{input_str.strip()}"
                    f"\nExpected:\n{expected_outputs}\nGot:\n{actual_output}"
                    f"\nDiff:\n{self._diff_lists(expected_outputs, actual_output)}"
                )
        except Exception as e:
            print(f"[💥] Test {test_num}: CRASHED\nInput:\n{input_str.strip()}\nerror:\n{str(e)}")
        finally:
            print("-" * 100)
            return test_passed

    def _diff_lists(self, expected, actual):
        return {
            "missing": [x for x in expected if x not in actual],
            "unexpected": [x for x in actual if x not in expected],
        }


def main():
    if len(sys.argv) < 3:
        print(
            "Usage: python test_solutions.py <question_id> <solution file name.py> [input_prompt_prefix]"
        )
        return
    question_id = int(sys.argv[1])
    file_solution_name = sys.argv[2]
    input_prompt_prefix = sys.argv[3] if len(sys.argv) > 3 else None
    test_case = TestCase(question_id, file_solution_name, input_prompt_prefix)
    test_case.run_tests()


if __name__ == "__main__":
    main()
