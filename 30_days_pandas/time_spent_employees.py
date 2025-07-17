import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    employees = employees.groupby(["event_day", "emp_id"]).total_time.sum().reset_index()
    employees = employees.sort_values(by="emp_id", ascending=True).rename(columns={"event_day":"day"})
    return employees


employees = pd.DataFrame([[1, "2020-11-28", 4, 32],
[1, "2020-11-28", 55, 200],
[1, "2020-12-3", 1, 42],
[2, "2020-11-28", 3, 33],
[2, "2020-12-9", 47, 74]],
columns=["emp_id", "event_day", "in_time", "out_time"])

print(total_time(employees))