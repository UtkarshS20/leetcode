import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    rearranged_df = pd.melt(products, id_vars=['product_id'], value_vars=["store1", "store2", "store3"], var_name="store", value_name="price")
    rearranged_df.dropna(subset="price", inplace=True)
    rearranged_df.sort_values(by=["product_id"], inplace=True)
    return rearranged_df


products = pd.DataFrame([[0, 95, 100, 105], 
[1, 70, None, 80]], columns=
["product_id", "store1", "store2", "store3"])

print(rearrange_products_table(products))