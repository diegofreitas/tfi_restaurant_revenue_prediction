__author__ = 'diego.freitas'

import csv

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error


dataframe = pd.read_csv("train.csv")

X = dataframe.values
features = X[:, 5:42]
print features[0]

#city_encoder = LabelEncoder()
#type_encoder = LabelEncoder()
city_group_encoder = LabelEncoder()


##############################################################
##### City and Type not available in the test dataset ########
##############################################################
#raw_city = city_encoder.fit_transform(X[:, 2:3].flatten())
#raw_type = type_encoder.fit_transform(X[:, 4:5].flatten())

raw_city_group = city_group_encoder.fit_transform(X[:, 3:4].flatten())


#features = np.concatenate((np.array([raw_type]).T, features), axis=1)
#features = np.concatenate(( np.array([raw_city]).T, features), axis=1)
features = np.concatenate((np.array([raw_city_group]).T, features ), axis=1)

x_train, x_test, y_train, y_test = train_test_split(features, X[:, 42:43].flatten(), test_size=0.30, random_state=42)

regressor = linear_model.Lasso()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

print "Train Score", mean_squared_error(y_test, y_pred) ** 0.5


#Load Test Data
dataframe = pd.read_csv("test.csv")

X = dataframe.values
features = X[:, 5:42]
print features[0]

raw_city_group = city_group_encoder.transform(X[:, 3:4].flatten())
#raw_city = city_encoder.transform(X[:, 2:3].flatten())
#raw_type = type_encoder.transform(X[:, 4:5].flatten())


#features = np.concatenate((np.array([raw_type]).T, features), axis=1)
#features = np.concatenate((np.array([raw_city]).T, features), axis=1)
features = np.concatenate((np.array([raw_city_group]).T, features ), axis=1)

predicted = regressor.predict(features)

with open('submission_tfi.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Id", "Prediction"])
    for index in xrange(0, len(predicted)):
        writer.writerow([index, predicted[index]])