import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses_count = courses["class"].value_counts()
    classes = courses_count[courses_count>=5].reset_index().drop(columns=["count"])
    return classes


courses = pd.DataFrame([["A", "Math"],
["B", "English"],
["C", "Math"],
["D", "Biology"],
["E", "Math"],
["F", "Computer"],
["G", "Math"],
["H", "Math"],
["I", "Math"]], columns=["student", "class"])

print(find_classes(courses))
