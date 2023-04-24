def student_ranking(student_scores, student_names):
    return [f"{index}. {student_name}: {student_score}" for index,(student_score, student_name) in enumerate(zip(student_scores, student_names), 1)]


def perfect_score(student_info):
    perfect_stud = []
    for student in student_info:
        if student[1] == 100:
            perfect_stud = student
    return perfect_stud


print(perfect_score([["Charles", 90], ["Tony", 80], ["Alex", 100]]))
