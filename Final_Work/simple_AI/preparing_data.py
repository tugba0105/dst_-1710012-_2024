import pandas as pd

from sklearn import datasets, linear_model
name="dataset_finaldata_set_tugba_0.png" # from the folder building_dataset
final_name="tugba_can"
data = pd.read_csv("datasets/"+name+".csv", sep=";", header=None)
print(type(data))
print(data)
list=[50,51,52,53,54,55,65,66,67]
u=[]
u.append(49)

for x in list:
    u.append(49)
    for y in range(0,10):
        u.append(x)
print(u)
print(len(u))
data[0] = u
print(data)
data.to_csv('./datasets/'+final_name+'.csv', header=None,index=None)
