import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(department, left_on="departmentId", right_on="id")
    max_salaries = merged_df.groupby("departmentId")["salary"].max().reset_index()
    max_salaries.rename(columns={"salary":"max_salary"}, inplace=True)
    result = merged_df.merge(max_salaries, on="departmentId")
    top_earners = result[result["salary"] == result["max_salary"]].drop(columns=["max_salary"])
    top_earners=top_earners.rename(columns = {"name_y":"Department", "name_x":"Employee", "salary":"Salary"}).drop(columns=["id_x", "departmentId", "id_y"])
    return top_earners


employee = pd.DataFrame([[1, "Joe", 70000, 1],
[2, "Jim", 90000, 1],
[3, "Henry", 80000, 2],
[4, "Sam", 60000, 2],
[5, "Max", 90000, 1]], columns= ["id", "name", "salary", "departmentId"])

department = pd.DataFrame([[1, "IT"],
[2, "Sales"]], columns=["id", "name"])

print(department_highest_salary(employee, department))