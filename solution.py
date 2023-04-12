import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp
# Используем критерий Андерсон-Дарлинга

chat_id = 1219503064 # Ваш chat ID, не меняйте название переменной

# Нулевая гипотеза - выборки однородны, если p_value > alpha, то принимаем нулевую гипотезу

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.04
    p = anderson_ksamp([x, y]).significance_level
    return (p < alpha)
