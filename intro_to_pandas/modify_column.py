import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"]*2
    return employees
    
    
employees = pd.DataFrame([["Jack", 19666],["Piper", 74754],["Mia", 62509],["Ulysses", 54866]], columns=["name", "salary"])

print(modifySalaryColumn(employees))