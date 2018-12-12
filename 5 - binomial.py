# Importação
from scipy.stats import binom

# Jogar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?
#                X  N   P
prob = binom.pmf(3, 5, 0.5)

# Passar por 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde
# 0, 1, 2, 3 ou 4 vezes seguidas?
#         X  N   P
binom.pmf(0, 4, 0.25)
#         X  N   P
binom.pmf(1, 4, 0.25)
#         X  N   P
binom.pmf(2, 4, 0.25)
#         X  N   P
binom.pmf(3, 4, 0.25)
#         X  N   P
binom.pmf(4, 4, 0.25)

# E se forem sinais de dois tempos?
binom.pmf(4, 4, 0.5)

# Probabilidade acumulativa
binom.cdf(4, 4, 0.25)

# Concurso com 12 questões, qual a probabilidade de acertar 7 questões considerando
# que cada questão tem 4 alternativas?
#         X  N     P
binom.pmf(7, 12, 0.25) * 100 # jogando em porcentagem

# E para acertar todas as questões da prova no chute?
#         X  N     P
binom.pmf(12, 12, 0.25) * 100