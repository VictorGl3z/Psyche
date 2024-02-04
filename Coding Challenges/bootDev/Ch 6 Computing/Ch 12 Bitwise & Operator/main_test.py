from main import *

run_cases = [
    (0b0110, False, True, True, False),
    (0b1111, True, True, True, True),
    (0b0000, False, False, False, False),
]

submit_cases = run_cases + [
    (0b1001, True, False, False, True),
    (0b1000, True, False, False, False),
    (0b0100, False, True, False, False),
    (0b0010, False, False, True, False),
    (0b0001, False, False, False, True),
]


def test(
    input1, expected_output1, expected_output2, expected_output3, expected_output4
):
    print("---------------------------------")
    print(f"Inputs: {input1:04b}")
    print(f"Expecting can_create: {expected_output1}")
    print(f"Expecting can_review: {expected_output2}")
    print(f"Expecting can_delete: {expected_output3}")
    print(f"Expecting can_edit: {expected_output4}")

    result1 = can_create_bits(input1) == can_create_guild
    result2 = can_review_bits(input1) == can_review_guild
    result3 = can_delete_bits(input1) == can_delete_guild
    result4 = can_edit_bits(input1) == can_edit_guild
    print(f"Actual can_create: {result1}")
    print(f"Actual can_review: {result2}")
    print(f"Actual can_delete: {result3}")
    print(f"Actual can_edit: {result4}")
    if (
        result1 == expected_output1
        and result2 == expected_output2
        and result3 == expected_output3
        and result4 == expected_output4
    ):
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
