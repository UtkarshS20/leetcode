import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = actor_director.groupby(["actor_id", "director_id"]).count().reset_index()
    actor_director = actor_director[actor_director["timestamp"]>=3].drop(columns=["timestamp"])
    return actor_director

actor_director = pd.DataFrame([[1, 1, 0],
[1, 1, 1],
[1, 1, 2],
[1, 2, 3],
[1, 2, 4],
[2, 1, 5],
[2, 1, 6]], columns=["actor_id", "director_id", "timestamp"])

print(actors_and_directors(actor_director))