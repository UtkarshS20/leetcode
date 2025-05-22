import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace=True)
    return products

products = pd.DataFrame([["Wristwatch", None, 135], 
["WirelessEarbuds", None, 821], 
["GolfClubs", 779, 9319], 
["Printer", 849, 3051]], columns=["name", "quantity", "price"])   

print(fillMissingValues(products))