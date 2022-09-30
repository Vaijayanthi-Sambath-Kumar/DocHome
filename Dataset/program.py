import pandas as pd

data = pd.read_csv("Dataset/dis_sym_dataset_comb.csv")
print(data[(data["label_dis"] == "Influenza")])