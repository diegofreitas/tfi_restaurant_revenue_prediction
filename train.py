__author__ = 'diego'

from preprocessing import prepare_data
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

# Escolha um algoritmo usando o Flow chart do Sklearn
#Selecione features para serem usados como dados de entrada  e treine-o
#avalie a performance do algoritmo

selected_features = []


def train():
    x_train, x_test, y_train, y_test = prepare_data()
    lasso = linear_model.Lasso()
    lasso.fit(x_train, y_train)
    y_pred = lasso.predict(x_test)

    return mean_squared_error(y_test, y_pred ) ** 0.5

if __name__ == '__main__':
    train()
