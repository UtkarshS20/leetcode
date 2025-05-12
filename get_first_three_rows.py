import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

employees = pd.DataFrame([[3,"Bob","Operations" ,48675],[90, "Alice", "Sales", 11096  ],[9, "Tatiana", "Engineering", 33805  ],[60, "Annabelle", "InformationTechnology", 37678 ]], columns=["employee_id", "name", "department", "salary"])

print(selectFirstRows(employees=employees))