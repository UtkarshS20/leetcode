import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_sales = daily_sales.groupby(["date_id", "make_name"]).agg(unique_leads=("lead_id", "nunique"), unique_partners=("partner_id", "nunique")).reset_index()
    return daily_sales

daily_sales = pd.DataFrame([["2020-12-8", "toyota", 0, 1],
["2020-12-8", "toyota", 1, 0],
["2020-12-8", "toyota", 1, 2],
["2020-12-7", "toyota", 0, 2],
["2020-12-7", "toyota", 0, 1],
["2020-12-8", "honda", 1, 2],
["2020-12-8", "honda", 2, 1],
["2020-12-7", "honda", 0, 1],
["2020-12-7", "honda", 1, 2],
["2020-12-7", "honda", 2, 1]], columns=["date_id", "make_name", "lead_id", "partner_id"])

print(daily_leads_and_partners(daily_sales))