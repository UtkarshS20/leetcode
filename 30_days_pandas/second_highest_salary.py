import pandas as pd
# 
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=["salary"])
    if len(employee) < 2:
        return pd.DataFrame([None], columns=["SecondHighestSalary"])
    else:
        employee = employee.sort_values(by="salary" ,ascending=False)
        second_highest = employee.iloc[1]['salary']
        return pd.DataFrame([second_highest], columns=["SecondHighestSalary"])
    
employees = pd.DataFrame([[1, 100],
[2, 600],
[3, 300],
[4, 300]], columns=
["id", "salary"])

print(second_highest_salary(employees))
