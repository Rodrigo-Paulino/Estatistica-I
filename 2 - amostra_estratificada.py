# IMPORTA BIBLIOTECA
import pandas as pd
# IMPORTA BIBLIOTECA COM A FUNÇÃO P/ FAZER A DIVISÃO DA BASE DE DADOS
from sklearn.model_selection import train_test_split

# ABRIR O ARQUIVO .CSV
iris = pd.read_csv('iris.csv')

# CONTAGEM DO ATRIBUTO/COLUNA 'CLASS'
iris['class'].value_counts()

# GERAR UMA AMOSTRAGEM COM 50% DOS DADOS
# CRIA VARIÁVEL / USA A FUNÇÃO / ILOC (PARTE ESPECIFICA) 
X, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4], test_size = 0.5, stratify = iris.iloc[:,4])

# VERIFICAR A QUANTIDADE DE VALORES RETORNADOS
y.value_counts()
X.value_counts()


# ---------- DATASET INFERT ----------

# ABRIR O ARQUIVO .CSV
infert = pd.read_csv('infert.csv')

# CONFERIR QUANTIDADE DE LINHAS E COLUNAS
infert.shape

# CONFERIR QUANTIDADE DE REGISTROS
len(infert)

# CONFERIR OS REGISTROS DE CADA INTERVALO DA COLUNA
infert['education'].value_counts()

# DESCOBRINDO A PROPORÇÃO DOS REGISTROS
# 6-11yrs    120
(120 / 248) * 100

# 12+ yrs    116
(116 / 248) * 100

# 0-5yrs      12
(12 / 248) * 100

# CRIA AMOSTRA USANDO A PROPORÇÃO DOS REGISTROS
X1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1],
                                test_size = 0.6, 
                                stratify = infert.iloc[:, 1])

# CONTANDO REGISTROS
y1.value_counts()