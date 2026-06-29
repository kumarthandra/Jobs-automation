import pandas as pd

EXCLUDE_TITLES = [
    "manager",
    "director",
    "head",
    "chief",
    "vp",
    "vice president",
    "architect"
]


def remove_management_jobs(df: pd.DataFrame):

    pattern = "|".join(EXCLUDE_TITLES)

    return df[
        ~df["title"].str.lower().str.contains(
            pattern,
            na=False
        )
    ]