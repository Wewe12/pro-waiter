import numpy as np
from sklearn import linear_model

class MachineLearning:
	def __init__(self,file):
		self.featuresList = []
		self.serviceList = []

		#preaparing training data from file
		lines = open(file,"r").readlines()
		serviceTemp = []
		for line in lines:
			data = line.split(";")
			serviceTemp.append(data[-1])
			self.featuresList.append(data[:3])

		self.featuresList = np.array(self.featuresList, float)
		self.serviceList = np.array(serviceTemp, float)


		# Create linear regression object
		self.regression = linear_model.LinearRegression()

	def learn(self):	
		#Train the model using the training sets
		self.regression.fit(self.featuresList,self.serviceList)
		#Print regression score
		# print('score: ',self.regression.score(self.featuresList,self.serviceList))

	def getPrediction(self, data):
		# data = [[14,16,44], [22,22,3],[16,0,3]]
		prediction = self.regression.predict(np.array(data, float))
		print "\nPrediciton: "
		print prediction
		return np.array(prediction).tolist()
		# return prediction[0]