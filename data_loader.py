# this file sole purpose is to combine and load the cleaned gen 1 adn gen 2 data set (it will also run drop_duplicate()) just in case as a
# defensive measure 

# It will combine both the data and based on that we will use this "combined data"

import pandas as pd 
from data_cleaner import clean_dataset


def load_data():
    # importing the datasets 
    df_gen1_dirty = pd.read_csv("data/data_gen_1_dirty.csv")
    df_gen2_dirty = pd.read_csv("data/data_gen_2_dirty.csv")

    # cleaning the data 
    df_gen1_clean = clean_dataset(df_gen1_dirty)
    df_gen2_clean = clean_dataset(df_gen2_dirty)

    # defensive programming to drop same value rows 
    # a last final check fo just in case our load_data misses some rows OR teh data is tampered with
    df_gen1_clean = df_gen1_clean.drop_duplicates()
    df_gen2_clean = df_gen2_clean.drop_duplicates()

    #dropping the rows with same pokemon names 
    df_gen1_clean = df_gen1_clean.drop_duplicates(subset = ["Name"],keep="first")
    df_gen2_clean = df_gen2_clean.drop_duplicates(subset = ["Name"],keep="first")


    # combining both the dataset
    workable_data = pd.concat([df_gen1_clean,df_gen2_clean], ignore_index=True)

    # final check for the workable data
    workable_data = workable_data.drop_duplicates(subset=["Name"], keep="first")

    # creating the final data set to work it and storing it as a csv file for user to use 
    workable_data.to_csv("data/workable_data.csv", index=False)

    return workable_data # returning the data frame file to user can just call load_data() and voila data is loaded 

