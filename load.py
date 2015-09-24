__author__ = 'diego'

import pandas as pd

#Carregar os dados
def load_data():
    dataframe = pd.read_csv("test.csv")
    #print dataframe.values
    return dataframe.values


if __name__ == '__main__':
    load_data()

