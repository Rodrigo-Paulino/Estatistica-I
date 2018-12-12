# BIBLIOTECA
import numpy as np
# FUNÇÃO DE ESTATÍSTICA
from scipy import stats

# LISTA DE SALÁRIOS
jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]

# MÉDIA
np.mean(jogadores)

# MEDIANA
np.median(jogadores)

# QUARTIS
quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1])

# DESVIO PADRÃO
np.std(jogadores, ddof = 1)

# RESUMO
stats.describe(jogadores)