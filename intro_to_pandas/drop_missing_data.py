import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset="name")
    
students = pd.DataFrame([[32, "Piper", 5], [217, None, 19], [779, "Georgia", 20], [849, "Willow", 14]], columns=["student_id", "name", "age"])
print(dropMissingData(students))