# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:51:02 2018

@author: vaisakhs

Tsne Plot for any data(sparse/non-sparse) 
USAGE:
    from plot_tsne import plotTsne
"""
import numpy as np
from time import time
import matplotlib.pyplot as plt
from matplotlib import offsetbox
from sklearn import (manifold, datasets, decomposition, ensemble,
                     discriminant_analysis, random_projection)
import scipy as sc




class plotTsne():
    '''
    Superclass for plotting Tsne given the data and labels
    DATA MEMBERS
        - X: input data in numpy format
        - y: corresponding labels for labelling
        - isSparse: Boolean
    MEMBER FUNCTIONS
        - plot: do preprocessing on X and do tsne embedding to 2D space, calls plot_embedding
        - plot_embedding: Worker function for plotting figure    
    
    '''
    def __init__(self,X,y,isSparse=True):
          self.X = X
          self.y = y
          self.isSparse = isSparse
          

    # Scale and visualize the embedding vectors
    def plot_embedding(self,X,y,title=None):
        """
        INPUTS
        - X: input data in numpy format
        - y: corresponding labels for labelling
        
        OUTPUTS
        - plt: 2D pyplot object with colored clusters
      
        """
        x_min, x_max = np.min(X, 0), np.max(X, 0)
        X = (X - x_min) / (x_max - x_min)
    
        plt.figure()
        ax = plt.subplot(111)
        for i in range(X.shape[0]):
            plt.text(X[i, 0], X[i, 1], str(y[i]),
                     color=plt.cm.Set1(y[i] / 10.),
                     fontdict={'weight': 'bold', 'size': 9})
    
        
        plt.xticks([]), plt.yticks([])
        if title is not None:
            plt.title(title)
        return plt
            
            
    # t-SNE embedding of the digits dataset
    def plot(self):
        '''
        Plot the tsne after doing a isSparse test and preprocessing accordingly
        '''
        if self.isSparse==True:
            pca = decomposition.TruncatedSVD(n_components=50,random_state=0)
            X = pca.fit_transform(self.X)
        else:
            X=self.X
        print("Computing t-SNE embedding")
        t0 = time()
        tsne = manifold.TSNE(n_components=2, n_iter=600,learning_rate=500, random_state=0)
        X_tsne = tsne.fit_transform(X)
        print("Hello")
        plt = self.plot_embedding(X_tsne,self.y,
                       "t-SNE embedding of the Malware And CleanWare (time %.2fs)" %
                       (time() - t0))
        
        plt.show()
