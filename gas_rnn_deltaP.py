# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 18:55:20 2020

@author: hsegh
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time as tm

import tensorflow as tf

from tensorflow import keras

class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

def noise(x):
    return np.sin(x*np.pi)

def gauss_noise(train_data,last):
    noise=np.random.normal(0,0.1,[len(train_data),last])
    for i in range(len(train_data)):
        for j in range(last):
            train_data[i][j] += noise[i][j]
    return train_data

def arqScatter(arq):
    plt.scatter([i[0] for i in arq],[j[1] for j in arq],c=[k[-1] for k in arq],cmap="Set1")
    plt.xlabel("Time")
    plt.ylabel("Presssure")
    plt.show() 

def modelGraphs(hist):
    
    #Loss function graphs
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.plot(hist['epoch'][Patience:], hist['loss'][Patience:],label='Train Loss Function')
    plt.plot(hist['epoch'][Patience:], hist['val_loss'][Patience:],label = 'Val Loss Functionr')
    plt.legend()
    
    #Mean absolute error graphs
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [MPG]')
    plt.plot(hist['epoch'][Patience:], hist['mae'][Patience:],label='Train Error')
    plt.plot(hist['epoch'][Patience:], hist['val_mae'][Patience:],label = 'Val Error')
    plt.legend()
    
    #Mean square error graphs
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error [$MPG^2$]')
    plt.plot(hist['epoch'][Patience:], hist['mse'][Patience:],label='Train Error')
    plt.plot(hist['epoch'][Patience:], hist['val_mse'][Patience:],label = 'Val Error')
    plt.legend()
    
    plt.show()
    print(np.mean(np.abs(target)))

def resultGraphs(prediction):
    plt.scatter([i[0] for i in time[last+2:]],[j for j in prediction],c="red")
    plt.scatter([i[0] for i in time[last+2:]],[j for j in target],c="blue")
    plt.xlabel("Time")
    plt.ylabel("Pressure")
    plt.show()
    plt.scatter([i[0] for i in prediction],[j for j in target],c=[k[0][-1] for k in train_data_norm],cmap="Set1")
    plt.xlabel("Prediction")
    plt.ylabel("Target")
    plt.plot([-5,5],[-5,5],c="purple")
    plt.grid(True)
    plt.show()

def preprocess(arq):
    data=[]
    label=[]
    for i in range(0,arq.shape[0]-last-2):
        data.append([])
        for j in range(last):
            data[-1].append([])
            data[-1][-1].append(arq[i+j+2][0]) #appending time
            #data[-1][-1].append(arq[i+j,1]) #appending pressure
            data[-1][-1].append(arq[i+j+1,1]-arq[i+j,1])
            data[-1][-1].append(arq[i+j+2,-1]) #appending flow rate
            
        #label.append(arq[i+last,1]) #appending pressure target
        label.append(arq[i+last+1,1]-arq[i+last,1])
        
    data=np.array(data)
    label=np.array(label)
    
    return data,label
#--------------------------------
t0 =tm.perf_counter()
last=3

seed=1
tf.random.set_seed(seed)
np.random.seed(seed)

time=pd.read_csv("data/time.txt",sep=" ")
time=time.to_numpy()

#a=pd.read_csv("data/gas_primeiro_caso_variavel.txt",sep=" ")
#a=pd.read_csv("data/gas_segundo_caso_variavel.txt",sep=" ")
a=pd.read_csv("data/gas_terceiro_caso_variavel.txt",sep=" ")
#a=pd.read_csv("data/gas_quarto_caso_variavel.txt",sep=" ")

a=a.to_numpy()
arqScatter(a)

deltaT=True
if(deltaT==True):
    for i in range(1,len(a)):
        a[-i][0]=np.abs(a[-i][0]-a[-i-1][0]) #replacing timestamps with time delta
    
data_df=pd.DataFrame(a)
data_df=data_df.describe()
data_stats=data_df.to_numpy()

train_data,target=preprocess(a)
for i in range(0,len(a[0])):
    a[:,i]=(a[:,i]-data_stats[1,i])/data_stats[2,i] #standarization
    #a[:,i]=a[:,i]/data_stats[-1,i] #normalization
    
train_data_norm,target_norm=preprocess(a)

train_split=280

index=list(range(len(train_data)))
np.random.shuffle(index)
train_index=index[0:train_split]
val_index=index[train_split:]

#------------ BUILDING THE NETWORK -------------------------------------------
print(train_data.shape)

layer_size=16

model = keras.Sequential()
model.add(keras.layers.GRU(layer_size, kernel_regularizer=keras.regularizers.l2(0.005),
                 activity_regularizer=keras.regularizers.l1(0.), batch_input_shape=(1, train_data_norm.shape[1], train_data_norm.shape[2])))
#model.add(keras.layers.Dense(layer_size, activation='relu'))
model.add(keras.layers.Dense(1,kernel_regularizer=keras.regularizers.l2(0.005),
                 activity_regularizer=keras.regularizers.l1(0.)))

model.compile(optimizer='adam',
              loss=tf.keras.losses.mse,
              metrics=['mae','mse','mape'])

EPOCHS = 1000
Patience=50
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=Patience)
history = model.fit(train_data_norm[train_index], target[train_index], epochs=EPOCHS,
                    validation_data=(train_data_norm[val_index], target[val_index]), 
                    verbose=0, callbacks=[PrintDot()])

#---------------- EVALUATING and TESTING -------------------------------------------------
hist = pd.DataFrame(history.history)

print("-/-")
hist['epoch'] = history.epoch
print(hist.tail(1))

modelGraphs(hist)

s=["data/gas_primeiro_caso_variavel.txt","data/gas_segundo_caso_variavel.txt","data/gas_quarto_caso_variavel.txt","data/gas_quinto_caso_variavel.txt","data/gas_terceiro_caso_variavel.txt"]
for k in range(len(s)):    
    a=pd.read_csv(s[k],sep=" ")    
    a=a.to_numpy()
    
    if(deltaT==True):
        for i in range(1,len(a)):
            a[-i][0]=np.abs(a[-i][0]-a[-i-1][0]) #replacing timestamps with time delta
    
    train_data,target=preprocess(a)
    
    for i in range(0,len(a[0])):
        a[:,i]=(a[:,i]-data_stats[1,i])/data_stats[2,i] #standarization
        #a[:,i]=a[:,i]/data_stats[-1,i] #normalization
        
    train_data_norm,target_norm=preprocess(a)
    prediction = model.predict(train_data_norm)
    resultGraphs(prediction)

#-------------------Predictions---------------------------
a=pd.read_csv("data/gas_quinto_caso_alterado.txt",sep=" ")
a=a.to_numpy()

if(deltaT==True):
    for i in range(1,len(a)):
        a[-i][0]=np.abs(a[-i][0]-a[-i-1][0]) #replacing timestamps with time delta

predict_data,predict_target=preprocess(a)
#predict data will contain the data resulting from the prediction
#we initialize it with the preprocess result of the case to be predicted
#test will be receive the normed values of each entry to be used as input
test=np.zeros(predict_data[0].shape)
r=0

for i in range(len(predict_data)-last):
    for j in range(len(predict_data[0][0])):
        test[:,j]=(predict_data[i,:,j]-data_stats[1,j])/data_stats[2,j]
        
    r=model.predict([np.array([test])])[0][0] #resulting pressure prediction
    
    i=i+1
    for j in range(last):
        #we feed the prediction result back into the predict data to be used in future iterations
        predict_data[i+j][-j-1][1]=r
            
plt.scatter([i[0][1] for i in predict_data[0:len(predict_data)]],[j for j in predict_target[0:len(predict_data)]],c=[k[0] for k in time[0:len(predict_data)]],cmap="Set1")
plt.xlabel("Prediction")
plt.ylabel("Target")
plt.plot([-5,5],[-5,5],c="purple")
plt.grid(True)
plt.show()

plt.scatter([i[0] for i in time[0:len(predict_data)]],[j[0][1] for j in predict_data[0:len(predict_data)]],c=[k[0] for k in time[0:len(predict_data)]],cmap="Set1")
plt.xlabel("Time")
plt.ylabel("Presssure")
plt.show()

t1=tm.perf_counter()
print("Time elapsed:",t1-t0)
