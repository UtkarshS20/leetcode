import pandas as pd
# ["subject_count"]
def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.drop_duplicates(subset=["teacher_id", "subject_id"]).groupby("teacher_id")["subject_id"].count().reset_index().rename(columns={"subject_id":"cnt"})
    return teacher
teacher = pd.DataFrame([[1, 2, 3],
[1, 2, 4],
[1, 3, 3],
[2, 1, 1],
[2, 2, 1],
[2, 3, 1],
[2, 4, 1]], columns=["teacher_id", "subject_id", "dept_id"])

print(count_unique_subjects(teacher))