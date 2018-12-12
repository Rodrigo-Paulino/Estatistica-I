# IMPORTA BIBLIOTECA
import numpy as np
import pandas as pd

# FUNÇÃO PARA ARREDONDAMENTO (ceil)
from math import ceil

# CRIANDO AS VARIÁVEIS
populacao = 150
amostra = 15
k = ceil(populacao / amostra)

# CRIANDO O SORTEIO / MENOR VALOR / MAIOR VALOR / QTD 1
r = np.random.randint(low = 1, high = k + 1, size = 1)

acumulador = r[0]
sorteados = []
for i in range(amostra):
    #print(acumulador)
    sorteados.append(acumulador)
    acumulador += k
    
# RETORNAR OS REGISTROS DA BASE DE DADOS DE ACORDO COM OS ÍNDICES ALEATÓRIOS
base = pd.read_csv('iris.csv')
base_final = base.loc[sorteados]
