import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world = world[(world["area"] >= 3000000) | (world["population"]>=25000000)]
    return world.drop(columns=["continent", "gdp"])
    
world = pd.DataFrame([["Afghanistan", "Asia", 652230, 25500100, 20343000000], 
["Albania", "Europe", 28748, 2831741, 12960000000], 
["Algeria", "Africa", 2381741, 37100000, 188681000000], 
["Andorra", "Europe", 468, 78115, 3712000000], 
["Angola", "Africa", 1246700, 20609294, 100990000000]], columns=["name", "continent", "area", "population", "gdp"])

print(big_countries(world))