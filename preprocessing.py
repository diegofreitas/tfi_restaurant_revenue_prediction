__author__ = 'diego'

from load import load_data
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split


#dicas: np.concatenate, np.random.shuffle

def prepare_data():

    X = load_data()
    features = X[:, 5:43]

    city_encoder = LabelEncoder()
    city_group_encoder = LabelEncoder()
    type_encoder = LabelEncoder()

    raw_city = city_encoder.fit_transform(X[:, 2:3].flatten())
    raw_city_group = city_group_encoder.fit_transform(X[:, 3:4].flatten())
    raw_type = type_encoder.fit_transform(X[:, 4:5].flatten())

    features =np.concatenate((np.array([raw_type]).T, features), axis=1)
    features =np.concatenate((np.array([raw_city_group]).T, features ), axis=1)
    features =np.concatenate(( np.array([raw_city]).T, features), axis=1)

    return train_test_split(features, X[:, 42:43].flatten(), test_size=0.33, random_state=42)


if __name__ == '__main__':
    prepare_data()