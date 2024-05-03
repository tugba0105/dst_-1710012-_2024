import matplotlib.pyplot as plt
import pickle as p1
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


final_name="tugba_can"
train_data = pd.read_csv("datasets/"+final_name+".csv", sep=",",header=None)
data_X=train_data.iloc[:,1:]
data_Y=train_data.iloc[:,0:1]
#print(train_data.columns)
print(data_X,type(data_X))
print(data_Y)

#colum_train=['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']


regr = linear_model.Ridge(alpha=.5)
preditor_linear_model=regr.fit(data_X, data_Y)
preditor_Pickle = open('./model_predictor', 'wb')
print("model_predictor")
p1.dump(preditor_linear_model, preditor_Pickle)

rr=regr.score(data_X, data_Y)
print("coef. Correl",rr)