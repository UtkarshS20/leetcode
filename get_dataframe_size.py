import pandas as pd
from typing import List


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)



data = pd.DataFrame([[1,2], [2,3],[3,4]], columns = ["student_id", "age"])
print(getDataframeSize(data))