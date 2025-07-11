import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report = report.melt(id_vars=["product"], value_vars=["quarter_1","quarter_2","quarter_3","quarter_4"], value_name="sales", var_name="quarter")
    return(report)

report = pd.DataFrame([["Umbrella",417,224,379,611 ],
["SleepingBag",800,936,93,875]], columns = ["product","quarter_1","quarter_2","quarter_3","quarter_4"])

print(meltTable(report))