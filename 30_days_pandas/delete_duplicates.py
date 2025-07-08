import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id',ascending=True,inplace=True)
    person = person.drop_duplicates(subset="email", keep="first")
    

person = pd.DataFrame([[1, "john@example.com"],
[2, "bob@example.com"],
[3, "john@example.com"]], columns=["id", "email"])

print(delete_duplicate_emails(person))