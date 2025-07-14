import numpy as np
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    conditions = [accounts["income"] < 20000, (accounts["income"] >= 20000) & (accounts["income"] <= 50000), accounts["income"] > 50000]
    value = ["Low Salary", "Average Salary", "High Salary"]
    accounts["category"] = np.select(conditions, value)
    salary_counts = accounts['category'].value_counts().reindex(value, fill_value=0)
    result = salary_counts.reset_index()
    result.columns = ["category", "accounts_count"]
    result = result.sort_values(by=["accounts_count"], ascending=True)
    return result

accounts = pd.DataFrame([[3, 108939],
[2, 12747],
[8, 87709],
[6, 91796]], columns=["account_id", "income"])

print(count_salary_categories(accounts))
