# analysis/analysis_functions.py
import pandas as pd
from sklearn.linear_model import LinearRegression

def realizar_regressao_linear(data):
    """
    Realiza uma regressão linear nos dados fornecidos.

    Parâmetros:
    data (DataFrame): Um DataFrame contendo os dados para a regressão linear. 
                      Deve incluir as variáveis independentes (X) e a variável dependente (y).

    Retorna:
    tuple: Uma tupla contendo os coeficientes da regressão (model.coef_) e a interceptação (model.intercept_).

    Exemplo:
    >>> coef, intercept = realizar_regressao_linear(data)
    >>> print("Coeficientes:", coef)
    >>> print("Interceptação:", intercept)
    """
    # ... (lógica para realizar regressão linear com scikit-learn)
    model = LinearRegression()
    # ... (preparar os dados)
    model.fit(X, y)
    # ... (retornar os resultados)
    return model.coef_, model.intercept_