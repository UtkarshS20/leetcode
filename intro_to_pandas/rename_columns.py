import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={"id" : "student_id", "first" : "first_name", "last" : "last_name", "age" : "age_in_years"})
    
    
students = pd.DataFrame([[1, "Mason", "King", 6],
[2, "Ava", "Wright", 7],
[3, "Taylor", "Hall", 16],
[4, "Georgia", "Thompson", 18],
[5, "Thomas", "Moore", 10]], columns=["id", "first", "last", "age"])

print(renameColumns(students))


