import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products = products[(products["low_fats"]=="Y") & (products["recyclable"]=="Y")]
    return products.drop(columns=["low_fats", "recyclable"])
    
    
products = pd.DataFrame([[0, "Y", "N"],
[1, "Y", "Y"],
[2, "N", "Y"],
[3, "Y", "Y"],
[4, "N", "N"]], columns=["product_id", "low_fats", "recyclable"])


print(find_products(products))