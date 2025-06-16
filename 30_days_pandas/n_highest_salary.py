import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries  = employee.drop_duplicates(subset=["salary"]).sort_values(by="salary" ,ascending=False)
    if N <= len(unique_salaries) and N > 0 :
        nth_salary = unique_salaries.iloc[N - 1]
        return pd.DataFrame({f"getNthHighestSalary({N})": [nth_salary["salary"]]})
    else:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})    

employee = pd.DataFrame([[1, 100],
[2, 200],
[3, 100]], columns=
["id", "salary"])

n = 2
print(nth_highest_salary(employee=employee, N=n))