import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
   scores["rank"] = scores["score"].rank(method= "dense", ascending=False)
   scores.sort_values(by = ["score"], ascending=False, inplace=True)
   return scores.drop(columns=["id"])

scores = pd.DataFrame([[1, 3.5], [2, 3.65], [3, 4], [4, 3.85], [5, 4], [6, 3.65]], columns=["id", "score"])

print(order_scores(scores))