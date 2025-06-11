import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views_same = views[views["author_id"]==views["viewer_id"]]
    ids = pd.DataFrame(sorted(views_same["author_id"].unique()), columns=["id"])
    return ids


views = pd.DataFrame([[1, 3, 5, "2019-08-01"], 
[1, 3, 6, "2019-08-02"], 
[2, 7, 7, "2019-08-01"], 
[2, 7, 6, "2019-08-02"], 
[4, 7, 1, "2019-07-22"], 
[3, 4, 4, "2019-07-21"], 
[3, 4, 4, "2019-07-21"]], columns=["article_id", "author_id", "viewer_id", "view_date"]
)


print(article_views(views=views))