import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (
    (~employees["name"].str.startswith("M")) & 
    (employees["employee_id"] % 2 != 0)
    )    
    employees["bonus"] = 0
    employees.loc[condition, "bonus"] = employees.loc[condition, "salary"]
    employees.drop(columns=["name", "salary"], inplace=True)
    return employees.sort_values(by="employee_id")

employee = pd.DataFrame([[2, "Meir", 3000],
[3, "Michael", 3800],
[7, "Addilyn", 7400],
[8, "Juan", 6100],
[9, "Kannon", 7700]], columns=["employee_id", "name", "salary"])

print(calculate_special_bonus(employees=employee))
