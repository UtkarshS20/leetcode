import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity["event_date"] = activity["event_date"].astype('datetime64[ns]')
    activity= activity.sort_values(by=["event_date"]).drop_duplicates(subset=["player_id"], keep="first").drop(columns=["device_id","games_played"]).rename(columns={"event_date":"first_login"})
    return activity
activity = pd.DataFrame([[1, 2, "2016-03-01", 5],
[1, 2, "2016-05-02", 6],
[2, 3, "2017-06-25", 1],
[3, 1, "2016-03-02", 0],
[3, 4, "2018-07-03", 5]], columns=["player_id", "device_id", "event_date", "games_played"])

print(game_analysis(activity))