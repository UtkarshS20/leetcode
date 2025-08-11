import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    employee_id  = pd.merge(employees, employee_uni, left_on="id", right_on="id", how="left").drop(columns=["id"])
    return employee_id

employees=pd.DataFrame([[1 , "Alice"],
[7 , "Bob"],
[11, "Meir"],
[90, "Winston"],
[3 , "Jonathan"]], columns=["id", "name"])

employee_uni  = pd.DataFrame([[3, 1],
[11, 2],
[90, 3]], columns=
["id", "unique_id"])

print(replace_employee_id(employee_uni=employee_uni, employees=employees))