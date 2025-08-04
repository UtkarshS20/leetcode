import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders_count = orders['customer_number'].value_counts()
    max_count = orders_count[orders_count>=orders_count.max()].reset_index()
    most_orders = pd.DataFrame(max_count['customer_number'], columns=["customer_number"]).dropna()
    return most_orders
orders = pd.DataFrame([[1, 1],
[2, 2],
[3, 3],
[4, 3]], columns=["order_number", "customer_number"])
print(largest_orders(orders))