import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # return students.loc[students["student_id"]==101, ["name", "age"]]
    return students[students["student_id"]==101].drop(columns=['student_id'])
    
student_data = pd.DataFrame([[101, "Ulysses", 13],[53, "William", 10],[128, "Henry", 6],[3, "Henry" , 11]], columns = ["student_id", "name", "age"])
print(selectData(students=student_data))