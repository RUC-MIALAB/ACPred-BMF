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
#######标准化
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from tensorflow.keras.layers import LSTM,Dense,Activation,Dropout,Bidirectional
from tensorflow.keras import Sequential
from keras.models import *


def read_fasta(input): #用def定义函数read_fasta()，并向函数传递参数用变量input接收
    with open(input,'r') as f: # 打开文件
        fasta = []# 定义一个空的字典
        for line in f:
            line = line.strip() # 去除末尾换行符
            if line[0] == '>':
                header = line[1:]
            else:
                sequence = line
                fasta.append(sequence)
    return fasta
########################################用写好的函数读取文件

import sys
input_fasta = sys.argv[1] # file type: fasta
output_dir = sys.argv[2]  # file dir
filename = sys.argv[3] #file name


#fa = read_fasta('./main_ts.fasta')
#fa = read_fasta('./ACP164.fasta')
fa = read_fasta(input_fasta)

####转为DataFrame
df=pd.DataFrame(pd.Series(fa),columns=['seq'])
df=df.reset_index().rename(columns={'index':'id'})
#df['leixing']=np.where(df['id'].apply(lambda x: '|1'in x),1,0)
df.head()


#f=open('./amino acids_1.csv')
# f = open(input_csv)
feature_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)),'amino_acids_1.csv')
pp_aa=pd.read_csv(feature_csv,encoding='gbk')
pp_aa.head()
embed=pd.get_dummies(pp_aa.iloc[:,1:12])
stdScale=StandardScaler().fit(embed.iloc[:,0:6])
#minmaxScale=preprocessing.MinMaxScaler().fit(embde.iloc[:,0:6])
embed.head()
embed.iloc[:,0:6]=stdScale.transform(embed.iloc[:,0:6])
embed.head()

##混合性质
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

###构造符合LSTM的数据格式
###其中bb[i,j,:]为第i+1个序列第j+1个氨基酸
x=np.array(x_code).reshape(bb.shape[0],max_num,single_n)
#x_test1=np.array(x_code1).reshape(cc.shape[0],max_num,single_n)
#y=df['leixing']
#y_test1=main_ts['leixing']
#x_quanc=x[:,:,0:26]

#####################model prediction
##载入模型
main_h5 = os.path.join(os.path.dirname(os.path.abspath(__file__)),'main.h5')
main_model=load_model(main_h5)

prediction=pd.DataFrame(0,columns = ['index','sequence','prediction'],
                                   index=range(df.shape[0]))
y_pred=main_model.predict(x)
y_pred_xgb= np.argmax(y_pred, axis=1)
prediction['sequence']=df['seq']
prediction['prediction']=y_pred_xgb
prediction['index'] = prediction.index
# print(prediction)
#prediction.to_csv('main_model_prediction.csv')

output_path = output_dir + "/" + filename + "_main_prediction.csv"
prediction.to_csv(output_path,index=False)
