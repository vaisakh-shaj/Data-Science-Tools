# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:11:21 2018

@author: vaisakhs

Returns training and testing numpy data that can be fed directly to a classifier
USAGE:
    from make_numpy_data import makeData
"""

import pandas as pd
import pickle
import numpy as np
from sklearn.metrics import accuracy_score
import sklearn.preprocessing as pp
from imblearn.over_sampling import SMOTE

class makeData():

    '''
    Superclass for cocatenating, normalizing, balancing and splitting data before classification
    DATA MEMBERS
        - D: list of tuples (X,y) where X is the input data(numpy array or list of numpy arrays)
             and y is the label(int)

             eg: In case of audio - list of numpy arrays
        - tt_ratio: ratio(train_data_size : test_data_size) , 0<tt_ratio<1

    MEMBER FUNCTIONS
        - balanceShuffleSplit: do SMOTE on data, shuffles and split according to tt_ratio
                               returns xTr,yTr,xTe,yTe
                               uses normalize
        - normalize: do normalization (customize it according to your wish - by default row wise l2 normalization)
                     uses makeSingleArray
        - makeSingleArray: Worker function for concatenating X's and y's in D


    '''

    def __init__(self,D,r):
        self.D=D
        self.tt_ratio = r

    # concatenate data and return a single numpy array for data and labels
    def makeSingleArray(self):
        X=[]
        X=np.array(X)
        X=X.reshape(0,39)
        y=[]
        y=np.array(y)
        for d in self.D:
            s=d[0].shape[0]
            for i in range(s):
                #print(x[i].shape)
                #print(X.shape)
                X=np.concatenate((X,d[0][i]))
                y=np.concatenate((y,np.ones(d[0][i].shape[0])*d[1]))
        return X,y


    # t-SNE embedding of the digits dataset
    def normalize(self):
        X,y=self.makeSingleArray()
        X=pp.normalize(X)
        return X,y

    def balanceShuffleSplit(self):
        X,y=self.normalize()
        sm=SMOTE()
        X_res,y_res=sm.fit_sample(X,y)
        arr=np.arange(X_res.shape[0])
        np.random.shuffle(arr)
        X_res=X_res[arr,:]
        y_res=y_res[arr]
        l=len(y_res)
        lTr=int(self.tt_ratio*l)
        xTr=X_res[:lTr,:]
        yTr=y_res[:lTr]
        xTe=X_res[lTr:,:]
        yTe=y_res[lTr:]
        return xTr,yTr,xTe,yTe
