# IMPORTA BIBLIOTECA
import pandas as pd
import numpy as np

# ABRE O DATASET .CSV
base = pd.read_csv('iris.csv')
# VISUALIZAR OS DADOS
base

# (TAMANHO) CONFERIR QUANTIDADE DE LINHAS E COLUNAS
base.shape

# SEMENTE GERADORA ALEATÓRIA 
np.random.seed(2345)

# CRIAR AMOSTRA ALEATÓRIA            TAMANHO       COM REPOSIÇÃO   PROBABILIDADE DO SORTEIO
amostra = np.random.choice(a = [0, 1], size = 150, replace = True, p = [0.5, 0.5])

# TAMANHO DO VETOR
len(amostra)

# TAMANHO DO VETOR COM CADA REGISTRO ESPECÍFICO (0,1)
len(amostra[amostra == 1])
len(amostra[amostra == 0])