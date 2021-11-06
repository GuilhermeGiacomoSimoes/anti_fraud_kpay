import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from joblib import dump
from sklearn.linear_model import SGDRegressor 
import unicodedata 
import connect 

clients = connect.getClients() 

def separar(clients):
    y = []
    
    for c in clients:
        y.append(c[8])
        del c[8]

    return clients, y


def normalize(s):
    return ''.join(str(ord(c)) for c in s)


for c in clients:
    c[0] = normalize(c[0])
    c[3] = normalize(c[3])
    c[5] = normalize(c[5])
    c[6] = normalize(c[6])
    c[7] = normalize(c[7])


X, y = separar(clients)

escala = StandardScaler()
escala.fit(X)

X_norm = escala.transform(X)

X_norm_train, X_norm_test, Y_train, Y_test = train_test_split(X_norm, y, test_size=0.35)

reglinear = SGDRegressor(max_iter=2000,tol=0.000001,eta0=0.1,learning_rate="constant",verbose=0)
reglinear.fit(X_norm_train, Y_train)

dump(reglinear, 'serializacao_do_objeto_de_treinamento.joblib')

