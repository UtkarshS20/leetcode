import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    all_combos = pd.merge(students, subjects, how='cross')
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name = 'attended_exams')
    result = pd.merge(all_combos, exam_counts, on=['student_id', 'subject_name'], how='left').fillna({'attended_exams':0})
    result['attended_exams'] = result['attended_exams'].astype(int)
    result = result.sort_values(['student_id', 'subject_name'])
    return result

students = pd.DataFrame([[1, "Alice"],
[2, "Bob"],
[13, "John"],
[6, "Alex"]], columns=["student_id", "student_name"])

subjects = pd.DataFrame([["Math"],
["Physics"],
["Programming"]],columns=["subject_name"])

examinations = pd.DataFrame([[1, "Math"],
[1, "Physics"],
[1, "Programming"],
[2, "Programming"],
[1, "Physics"],
[1, "Math"],
[1, "Math"],
[13, "Programming"],
[13, "Physics"],
[2, "Math"],
[1, "Math"]],columns=["student_id", "subject_name"])

print(students_and_examinations(students=students, examinations=examinations, subjects=subjects))
