# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import warnings
import os
warnings.filterwarnings('ignore')
#######Standardization
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from tensorflow.keras.layers import LSTM,Dense,Activation,Dropout,Bidirectional
from tensorflow.keras import Sequential
from keras.models import *


def read_fasta(input): #Define a function read_fasta() using def and pass the parameter using the variable input.
    with open(input,'r') as f: # open file
        fasta = []# Define an empty dictionary
        for line in f:
            line = line.strip() # Remove the trailing newline character.
            if line[0] == '>':
                header = line[1:]
            else:
                sequence = line
                fasta.append(sequence)
    return fasta
######################################## Read the file using the written function

import sys
input_fasta = sys.argv[1] # file type: fasta
output_dir = sys.argv[2]  # file dir
filename = sys.argv[3] #file name


fa = read_fasta(input_fasta)

####Convert to DataFrame
df=pd.DataFrame(pd.Series(fa),columns=['seq'])
df=df.reset_index().rename(columns={'index':'id'})
#df['leixing']=np.where(df['id'].apply(lambda x: '|1'in x),1,0)
df.head()


feature_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)),'amino_acids_1.csv')
pp_aa=pd.read_csv(feature_csv,encoding='gbk')
pp_aa.head()
embed=pd.get_dummies(pp_aa.iloc[:,1:12])
stdScale=StandardScaler().fit(embed.iloc[:,0:6])
#minmaxScale=preprocessing.MinMaxScaler().fit(embde.iloc[:,0:6])
embed.head()
embed.iloc[:,0:6]=stdScale.transform(embed.iloc[:,0:6])
embed.head()

##mixed nature
def encode(x,encode_len,mask):
    seq_encode=list()
    acid=['G','A','V','L','I','F','W','Y','D','H','N','E','K','Q','M','R','S','T','C','P']
    if len(x)>=encode_len:
        for i in range(encode_len):
            m=[0]*36           
            for j in range(20):
                if x[i]==acid[j]:
                    m=embed.iloc[j,:]
            m=list(m)
            seq_encode.append(m)
    else:
        for i in range(len(x)):
            m=[0]*36
            for j in range(20):
                if x[i]==acid[j]:
                    m=embed.iloc[j,:]
            m=list(m)
            seq_encode.append(m)
        for j in range(encode_len-len(x)):
            seq_encode.append([mask]*36)
            #bit_opf.append([0]*30)
    return(seq_encode) 
    
single_n=36
mask_value=100
bb=df['seq']
bb=pd.DataFrame(bb)
#max_num=np.max(bb.seq.apply(lambda x:len(x)))
max_num=50
bb['encode']=bb.seq.apply(lambda x:encode(x,encode_len=max_num,mask=mask_value))
#print(bb)
x_code=list()
for i in range(bb.shape[0]):
    x_code+=bb.iloc[i,1]

###Construct data format suitable for LSTM
###Where bb[i, j, :] represents the (j+1)-th amino acid of the (i+1)-th sequence
x=np.array(x_code).reshape(bb.shape[0],max_num,single_n)
#x_test1=np.array(x_code1).reshape(cc.shape[0],max_num,single_n)
#y=df['leixing']
#y_test1=main_ts['leixing']
#x_quanc=x[:,:,0:26]

#####################model prediction
##load model
main_h5 = os.path.join(os.path.dirname(os.path.abspath(__file__)),'main.h5')
main_model=load_model(main_h5)

prediction=pd.DataFrame(0,columns = ['index','sequence','prediction'],
                                   index=range(df.shape[0]))
y_pred=main_model.predict(x)
y_pred_xgb= np.argmax(y_pred, axis=1)
prediction['sequence']=df['seq']
prediction['prediction']=y_pred_xgb
prediction['index'] = prediction.index

output_path = output_dir + "/" + filename + "_main_prediction.csv"
prediction.to_csv(output_path,index=False)
