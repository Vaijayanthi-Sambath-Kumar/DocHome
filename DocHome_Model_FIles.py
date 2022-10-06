from sklearn.neural_network import MLPClassifier
import pandas as pd
import pickle

df_comb = pd.read_csv("dis_sym_dataset_comb.csv") # Disease combination
df_norm = pd.read_csv("dis_sym_dataset_norm.csv") # Individual Disease

X = df_comb.iloc[:, 1:]
Y = df_comb.iloc[:, 0]
mlp=MLPClassifier()
mlp.fit(X,Y)

with open('model_pkl', "wb") as file:
    pickle.dump(mlp, file)