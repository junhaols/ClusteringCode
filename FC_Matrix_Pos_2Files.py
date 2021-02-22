#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 23:17:19 2020

@author: Junhao
"""
#from sklearn.cluster import SpectralClustering
import numpy as np
import scipy.io as scio
#import pandas as pd
#import nibabel as nib
#import glob
## demo
# X = np.array([[1, 1], [2, 1], [1, 0],
#               [4, 7], [3, 5], [3, 6]])
# clustering = SpectralClustering(n_clusters=2,
#         assign_labels="discretize",
#         random_state=0).fit(X)

#files_FC=glob.glob('/Users/Junhao/data/Project/Clustering/HCP_vert_FC/100307*L*.mat')

def FC_Matrix_Pos_2Files(files_FC):

    for file in files_FC:
        print(file)
   

    ## read mat 
    LPT_FC = scio.loadmat(files_FC[0])
    LHS_FC=scio.loadmat(files_FC[1])
    ##
    LPT_FC_data=LPT_FC['FC']
    LHS_FC_data=LHS_FC['FC'];
    PreData=np.row_stack((LPT_FC_data,LHS_FC_data));
    
    ## clustering orig-data
    # clustering1 = SpectralClustering(n_clusters=2,
    #         assign_labels="discretize",
    #         random_state=0).fit(PreData)
    # clustering1.labels_
    
    ##  select PT and HS postive FC-VERT，then clustering
    LPT_mean=np.mean(LPT_FC_data,0) # mean as column
    LHS_mean=np.mean(LHS_FC_data,0) 
    LPT_pos_index=np.where(LPT_mean>0)
    LHS_pos_index=np.where(LHS_mean>0)
    ##commom index
    index_pos=np.intersect1d(LPT_pos_index[0],LHS_pos_index[0]) #intersextld:both in x and y
    LPT_pos_data=LPT_FC_data[:,index_pos]
    LHS_pos_data=LHS_FC_data[:,index_pos]
    PreData_pos=np.row_stack((LPT_pos_data,LHS_pos_data));
    
    return PreData_pos

