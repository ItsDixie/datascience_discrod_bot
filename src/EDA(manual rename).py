import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

while True:

	choose = input('Choose type of analyse(1-chats, 2-users)')

	if(choose == '2'):

		data = pd.read_csv('USERSdata.csv')

		X = data.drop(['id', 'amount of bad words', '%% of bad words'], axis=1)
		y = data['amount of bad words']

		lr = LinearRegression()
		lr.fit(X, y)

		lr = LinearRegression()
		lr.fit(X, y)

		y_pred = lr.predict(X)
		mse = mean_absolute_error(y, y_pred)
		print('MAE:', mse)

		print('intercept (b):', lr.intercept_)
		print('slope (k):', lr.coef_)

		new_x = np.array([7505, 5004,250,150,50,10,100,300,1300,1120,2034]).reshape(-1,1)
		y_pred = lr.predict(new_x)

		plt.scatter(X, y, c='green', label='Real data')
		plt.scatter(new_x, y_pred, c='red', label='Predicted data')
		plt.xlabel('Messages')
		plt.ylabel('Messages with bad words')
		plt.legend()
		plt.show()
	if(choose == '1'):

		data = pd.read_csv('CHATSdata.csv')

		X = data.drop(['id of chat', 'amount of bad words', '%% of bad words'], axis=1)
		y = data['amount of bad words']

		lr = LinearRegression()
		lr.fit(X, y)

		lr = LinearRegression()
		lr.fit(X, y)

		y_pred = lr.predict(X)
		mse = mean_absolute_error(y, y_pred)
		print('MAE:', mse)

		print('intercept (b):', lr.intercept_)
		print('slope (k):', lr.coef_)

		new_x = np.array([7505, 5004,250,150,50,10,100,300,1300,1120,2034]).reshape(-1,1)
		y_pred = lr.predict(new_x)

		plt.scatter(X, y, c='green', label='Real data')
		plt.scatter(new_x, y_pred, c='red', label='Predicted data')
		plt.xlabel('Messages')
		plt.ylabel('Messages with bad words')
		plt.legend()
		plt.show()

	else:
		print('Wrong number')