"""
File: boston_housing_competition.py
Name: WU YU CHEN
--------------------------------
This file demonstrates how to analyze boston
housing dataset. Students will upload their 
results to kaggle.com and compete with people
in class!

You are allowed to use pandas, sklearn, or build the
model from scratch! Go data scientists!
"""
import math
import pandas as pd
from sklearn import preprocessing, linear_model, metrics, model_selection
import matplotlib.pyplot as plt

TRAINING_FILE = 'boston_housing/train.csv'
TESTING_FILE = 'boston_housing/test.csv'
#EPOCH ? ALPHA?


def main():

	# Data preprocessing
	training_data = data_preprocessing(TRAINING_FILE, mode = 'Train')
	training_data, val_data = model_selection.train_test_split(training_data, test_size=0.6)
	testing_data = data_preprocessing(TESTING_FILE, mode = 'Test')

	# Extract the y (labels)
	y_train , y_val = training_data.pop('medv'), val_data.pop('medv')

	# Pop the columns that we don't need
	training_data.pop('ID')
	val_data.pop('ID')
	ID_ind = testing_data.pop("ID")
	# One-hot encoding

	# Normalization
	# normalizer = preprocessing.MinMaxScaler()
	# X_nor = normalizer.fit_transform(training_data)

	# Standardization
	standardizer = preprocessing.StandardScaler()
	X_std = standardizer.fit_transform(training_data)

	# Start training
	h = linear_model.LinearRegression()
	classifier = h.fit(training_data, y_train) # Only training_data will train the 'Weights'.

	train_pred = classifier.predict(training_data)
	val_pred = classifier.predict(val_data)

	print('Train Acc of training_data:', train_pred)
	print('Val ACC of validation_data', val_pred)
	print('*'*100)
	print('Train: ', metrics.mean_squared_error(train_pred, y_train) ** 0.5)
	print('Val: ', metrics.mean_squared_error(val_pred,  y_val)**0.5)
	print('-'*50)
	# Prediction, using test data
	# X_test_nor = normalizer.transform(testing_data)
	X_test_std = standardizer.transform(testing_data)
	predictions = classifier.predict(testing_data)
	print('-'*50)
	print(predictions)
	out_file(predictions,'basic_training.csv' ,ID_ind)

	# RMS
	# RMS_labels = rms_func(labels, ID_ind)



def data_preprocessing(filename, mode = 'Train', training_data = None ):
	data = pd.read_csv(filename)
	# Check Missing_value
	check_missing = data.count()
	print(check_missing)
	#print(data.info)

	# Training data input
	if mode == 'Train':
		return data
	elif mode == 'Test':
		return data

	# plt.figure(figsize=(15, 6))
	# ############
	# plt.subplot2grid((3, 4), (0, 0))
	# data.crim.value_counts(normalize=True).sort_index().plot(kind='bar')
	# plt.title('Crim')

	# plt.subplot2grid((3, 4), (0, 1))
	# plt.hist(data.crim.value_counts(normalize=True).sort_index(), bins=50)

	#plt.hist(data['crim'],color = 'blue', edgecolor = 'black', bins = int(180/5))
	fig, ax = plt.subplots()
	ax.plot(data["crim"], data["medv"],marker = 'o', linestyle = "None", color = 'b' )
	plt.show()
	#check if there is missing value


# def rms_func(labels, ID_ind):
# 	lst = []
# 	print(labels)
# 	print(ID_ind)
# 	for i in range(le):
# 		if i+1 == int(ID_ind[i]):
# 			lst.append(labels[i+1])
# 	print(lst)


def out_file(predictions, filename, ID_ind):
	"""
	: param predictions: numpy.array, a list-like data structure that stores 0's and 1's
	: param filename: str, the filename you would like to write the results to
	"""
	print('\n===============================================')
	print(f'Writing predictions to --> {filename}')
	with open(filename, 'w') as out:
		out.write('ID, medv\n')
		start_id = 0
		for ans in predictions:
			out.write(str(ID_ind[start_id])+','+str(ans)+'\n')
			start_id += 1
	print('===============================================')






if __name__ == '__main__':
	main()
