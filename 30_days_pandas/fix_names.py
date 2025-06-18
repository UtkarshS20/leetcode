import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    # users["name"] = users["name"][0].upper()
    return users.sort_values(by="user_id")

users = pd.DataFrame([[3, "aLice"],
[2, "bOB"]], columns=
["user_id", "name"])

print(fix_names(users))