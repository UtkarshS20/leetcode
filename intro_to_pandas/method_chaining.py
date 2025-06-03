import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # weights = animals["weight"].apply(lambda x: x if x>100 else None)
    animals = animals.query("weight>100").sort_values("weight", ascending=False).drop(columns=[ "species", "age", "weight"])
    return animals
    
    
animals = pd.DataFrame([["Tatiana", "Snake", 98, 464],
["Khaled", "Giraffe", 50, 41],
["Alex", "Leopard", 6, 328],
["Jonathan", "Monkey", 45, 463],
["Stefan", "Bear", 100, 50],
["Tommy", "Panda", 26, 349]], columns=["name", "species", "age", "weight"])

print(findHeavyAnimals(animals))