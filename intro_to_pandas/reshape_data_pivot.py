import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.pivot(index="month", columns="city", values="temperature")
    return weather
    
    
weather = pd.DataFrame([["Jacksonville", "January", 13],
["Jacksonville", "February", 23],
["Jacksonville", "March", 38],
["Jacksonville", "April", 5],
["Jacksonville", "May", 34],
["ElPaso", "January", 20],
["ElPaso", "February", 6],
["ElPaso", "March", 26],
["ElPaso", "April", 2],
["ElPaso", "May", 43]], columns=["city", "month", "temperature"]) 

print(pivotTable(weather))