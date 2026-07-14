# this file sole purpose is cleaning the data
# this cleans the data to a workable format that is remove duplicate datas in gen 1 and gen 2 dataset

import pandas as pd

def clean_dataset(df):

    """
    Cleans a Pokemon dataset by:
    1. Removing duplicate Pokemon
    2. Handling missing values
    3. Normalizing text
    4. Resetting the index

    Returns:
        Cleaned DataFrame
    """

    # remove (Exact duplicate rows)
    df_cleaned = df.drop_duplicates().copy()

    # remove rows with same name pokemon
    df_cleaned = df_cleaned.drop_duplicates(subset=["Name"], keep="first")

    # NOT HAVING LEADING OR TRAILING SPACES
    df_cleaned["Name"] = df_cleaned["Name"].str.strip()
    df_cleaned["Type1"] = df_cleaned["Type1"].str.strip()
    df_cleaned["Type2"] = df_cleaned["Type2"].str.strip()

    # NORMALIZING HOW ITS WRITTEN -> Pokemon (Correct) , PoKemon(WRONG), POKEMON (WRONG)
    
    df_cleaned["Type1"] = df_cleaned["Type1"].str.title()
    df_cleaned["Type2"] = df_cleaned["Type2"].str.title()

    # fill missing values for type 2
    df_cleaned["Type2"] = df_cleaned["Type2"].fillna("None")

    # fill missing values for weight
    # if we dont have weight we do the avg weight for that speicfic TYPE1 avg
    df_cleaned["Weight"] = df_cleaned["Weight"].fillna(
        df_cleaned.groupby("Type1")["Weight"].transform("mean")
    )

    # fill missing value for height (same concept as above)
    df_cleaned["Height"] = df_cleaned["Height"].fillna(
        df_cleaned.groupby("Type1")["Height"].transform("mean")
    )

    # if legendary status is not given then we fill it with 0
    df_cleaned["Legendary"] = (
        df_cleaned["Legendary"]
        .fillna(0)
        .astype(int)
    )

    # remove rows with negative weight and height
    df_cleaned = df_cleaned[
        (df_cleaned["Height"] > 0) &
        (df_cleaned["Weight"] > 0)
    ]

    # resetting the index
    df_cleaned = df_cleaned.reset_index(drop=True)

    return df_cleaned