import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities_counts = activities.groupby("sell_date").agg(num_sold =('product', lambda x:x.nunique()),
                                                            products = ('product', lambda x:','.join(sorted(set(x))))).reset_index()
    return activities_counts


activities = pd.DataFrame(
[["2020-05-30", "Headphone"],
["2020-06-01", "Pencil"],
["2020-06-02", "Mask"],
["2020-05-30", "Basketball"],
["2020-06-01", "Bible"],
["2020-06-02", "Mask"],
["2020-05-30", "T-Shirt"]], columns=["sell_date", "product"])

print(categorize_products(activities))
