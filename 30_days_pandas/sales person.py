import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(orders, company, on='com_id', how='inner').query("name=='RED'")
    df2 = sales_person.merge(df, how = "left", left_on = "sales_id",right_on = "sales_id")    
    return df2.query('name_y.isnull()')[['name_x']].rename(columns = {'name_x':'name'})

salesPerson = pd.DataFrame([[1, "John", 100000, 6, "4/1/2006"],
[2, "Amy", 12000, 5, "5/1/2010"],
[3, "Mark", 65000, 12, "12/25/2008"],
[4, "Pam", 25000, 25, "1/1/2005"],
[5, "Alex", 5000, 10, "2/3/2007"]], columns=["sales_id", "name", "salary", "commission_rate", "hire_date"])

company = pd.DataFrame([[1, "RED", "Boston"],
[2, "ORANGE", "New York"],
[3, "YELLOW", "Boston"],
[4, "GREEN", "Austin"]],
columns= ["com_id", "name", "city"])

orders =pd.DataFrame([[1, "1/1/2014", 3, 4, 10000],
[2, "2/1/2014", 4, 5, 5000],
[3, "3/1/2014", 1, 1, 50000],
[4, "4/1/2014", 1, 4, 25000]], columns=["order_id", "order_date", "com_id", "sales_id", "amount"]
)

print(sales_person(salesPerson, company, orders))