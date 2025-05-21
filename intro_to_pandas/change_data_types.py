import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students
    
    
    
students = pd.DataFrame([[1, "Ava", 6, 73.0],[2, "Kate", 15, 87.0]], columns=["student_id", "name", "age", "grade"])

print(changeDatatype(students))