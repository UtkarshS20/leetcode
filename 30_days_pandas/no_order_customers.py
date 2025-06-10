import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    found_customers = pd.merge(customers, orders, left_on='id', right_on='customerId', how='outer')
    non_customers = found_customers[found_customers['customerId'].isna()]
    non_customers.rename(columns={"name":"Customers"}, inplace=True)
    result = non_customers[["Customers"]]
    return result
    
customers = pd.DataFrame([[1, "Joe"],
[2, "Henry"],
[3, "Sam"],
[4, "Max"]], columns= ["id", "name"])

orders = pd.DataFrame([[1, 3],
[2, 1]], columns = ["id", "customerId"])

print(find_customers(customers=customers, orders=orders))