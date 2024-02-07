from main import *

run_cases = [
    (
        [
            "Rivendale",
            "The Morgoth Mountains",
            "The Lonely Island",
            "Mordia",
            "Mordane",
            "Gondolin",
        ],
        [
            "The Morgoth Mountains",
            "The Lonely Island",
            "Mordia",
        ],
    ),
]

submit_cases = run_cases + [
    (
        [
            "Pogsmeade",
            "Dogwarts",
            "The Leaky Pot",
            "The Screaming Hut",
        ],
        [
            "Dogwarts",
        ],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = trim_strongholds(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
