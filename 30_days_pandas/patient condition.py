import pandas as pd
import numpy as np
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients["condition_check"] = patients["conditions"].fillna(" ").str.split(" ")
    patients['has_diab'] = patients["condition_check"].apply(lambda condition: any(cond.startswith("DIAB1") for cond in condition))
    patients_filtered = patients[patients["has_diab"]==True]
    patients_filtered.drop(columns=["condition_check", "has_diab"], inplace=True)
    return patients_filtered

patients = pd.DataFrame([[1, "Daniel", "YFEV COUGH"],
[2, "Alice", np.nan],
[3, "Bob", "DIAB100 MYOP"],
[4, "George", "ACNE DIAB100"],
[5, "Alain", "DIAB201"]],
columns=["patient_id", "patient_name", "conditions"])

print(find_patients(patients))