def get_test_score(answer_sheet, student_answers):
    result = 0
    for i in range(len(answer_sheet)):
        if answer_sheet[i] == student_answers[i+1]:
            result = result + 1
    result = result*100/len(answer_sheet)
    return student_answers[0], result