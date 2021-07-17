import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

def createdataset(dataset, look_back = 1):
    dataX, dataY = [], []

    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append([dataset[i + look_back, 0]])

    return np.array(dataX), np.array(dataY)


dataset = pd.read_csv("HDB.csv", usecols=["Close"])

dataset = dataset.values

dataset = dataset.astype('float32')

predictedvalues = np.empty_like(dataset)

predictedvalues[::] = np.nan

look_back = 5

scaler = MinMaxScaler(feature_range=(0,1))

dataset = np.reshape(dataset, (-1,1))
dataset = scaler.fit_transform(dataset)

data, y = createdataset(dataset, look_back)

data = np.reshape(data, (data.shape[0], 1, data.shape[1]))

print(data)


model = load_model("lstm_model.h5")



predictionlength = 20

predictionsstartingpoints = [50, 100, 150, 200]

for start in predictionsstartingpoints:

    for days in range(predictionlength):
        new_data = data [start - look_back +days]
        print(new_data)
        new_data = np.reshape(new_data, (1, 1, 5))
        prediction = model.prediction(new_data)
        print(prediction)
        data[start - look_back + days + 1][0][-1] = prediction
        prediction = scaler.inverse_transform(prediction)
        predictedvalues[start - 1 + days] = prediction


dataset = scaler.inverse_transform(dataset)
plt.plot(dataset, "green")
plt.plot(predictedvalues, "red")
plt.grid(True)
plt.xlable("Time")
plt.ylable("price")
plt.title("Stock prediction HDFC")
plt.show()
