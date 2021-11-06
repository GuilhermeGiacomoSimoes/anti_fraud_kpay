from sklearn.preprocessing import StandardScaler
from joblib import load
import numpy as np

cliente_para_ser_analisado = [ 
                        "Guilherme Giácomo Simões",
                        '15/01/1996',
                        '439.268.638-89',
                        'R Conselheiro Saraiva',
                        866,
                        'Centro',
                        'Limeira',
                        'SP']

 
X = cliente_para_ser_analisado

reglinear = load('filename.joblib')

escala = StandardScaler()
escala.fix(X)

X_futuro = np.array([[  ]])
X_futuro_norm = escala.transform(X_futuro)


