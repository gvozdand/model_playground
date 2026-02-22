#This file just serves as a short cut for easily preparing the data whenever I would like to run an experiment

import polars as pl




def starter():

    model_dict = {1: "wine.parquet", 2: "bank.parquet", 3: "card_one.parquet", 4: "card_two.parquet"}


    print("Great to see you again! Let's get a few questions answered so we can prep your experiment quickly!")


    dataset_index = int(input("""


    Which dataset will we be using of the following options:

    1. Wine (easy)
    2. Bank (medium)
    3. CC Approval (hard)

    (Please just provide the number)

    """))

    #edge case for difficult card set
    if dataset_index == 3:
        dataset_one = pl.read_parquet(f"{model_dict[dataset_index]}")
        dataset_two = pl.read_parquet(f"{model_dict[dataset_index+1]}")
        dataset = dataset_one.join(dataset_two, on="ID")
        return dataset
    dataset = pl.read_parquet(f"{model_dict[dataset_index]}")


    print("Dataset is pulled!")
    return dataset





















