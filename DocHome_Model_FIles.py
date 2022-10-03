#!/usr/bin/env python
# coding: utf-8

# In[10]:


from sklearn.neural_network import MLPClassifier
import pandas as pd
import joblib
import pickle

df_comb = pd.read_csv("dis_sym_dataset_comb.csv") # Disease combination
df_norm = pd.read_csv("dis_sym_dataset_norm.csv") # Individual Disease

X = df_comb.iloc[:, 1:]
Y = df_comb.iloc[:, 0:1]
mlp=MLPClassifier()
mlp.fit(X,Y)

filename = 'Disease_prediction_model.joblib'
joblib.dump(mlp,filename)


# In[12]:


df_comb = pd.read_csv("dis_sym_dataset_comb.csv") # Disease combination
df_norm = pd.read_csv("dis_sym_dataset_norm.csv") # Individual Disease

joblib.dump(df_comb,'df_comb')
joblib.dump(df_norm,'df_norm')

