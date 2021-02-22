#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:42:59 2020

@author: Junhao
"""
from sklearn.cluster import SpectralClustering
from sklearn import metrics
#import numpy as np
import scipy.io as sio
#import pandas as pd
#import nibabel as nib
#import glob
#import os
#import sys
#import glob

def LJH_SpectralClustering(InputMatrix,OutFile,ClassNum=2): # default class=2
    clustering = SpectralClustering(n_clusters=ClassNum,assign_labels="discretize",random_state=0).fit(InputMatrix)
    clustering.labels_
    #scio.savemat('/Users/Junhao/data/Project/Clustering/result/LPT_LHS_pos_clustering_label_2type.mat',{'Clustering_labels':clustering.labels_+1})
    sio.savemat(OutFile,{'Clustering_labels':clustering.labels_+1}) # plus 1 for matlab index
    return  clustering.labels_+1



def LJH_SpectralClustering_fit(InputMatrix,OutFile,ClassNum): # default class=2
    optimal_gamma=0.01
    max_CH_Score=0 # initial CH-SCORE
    optimal_n_cluster=2
    #ClassNum:tuple
    for index,Gamma in enumerate((0.001,0.01,0.1,1,10)):
        gamma=Gamma
        for index,k in enumerate(ClassNum):
            
            clustering = SpectralClustering(n_clusters=k,gamma=Gamma,assign_labels="discretize",random_state=0).fit(InputMatrix)
            clustering.labels_
            score=metrics.calinski_harabasz_score(InputMatrix,clustering.labels_)
            
            print ("Calinski-Harabasz Score with gamma=", gamma, "n_clusters=", k,"score:", score)
            #scio.savemat('/Users/Junhao/data/Project/Clustering/result/LPT_LHS_pos_clustering_label_2type.mat',{'Clustering_labels':clustering.labels_+1})
            #sio.savemat(OutFile,{'Clustering_labels':clustering.labels_+1}) # plus 1 for matlab index
            if score>max_CH_Score:
               max_CH_Score=score
               optimal_gamma=gamma
               optimal_n_cluster=k
    optimal_params=dict(gamma=optimal_gamma,n_cluster=optimal_n_cluster,CH_score=max_CH_Score)
    
    opt_clustering= SpectralClustering(n_clusters=optimal_n_cluster,gamma=optimal_gamma,assign_labels="discretize",random_state=0).fit(InputMatrix)
          
    sio.savemat(OutFile,{'Clustering_labels':opt_clustering.labels_+1,'OptParams':optimal_params}) # plus 1 for
    
    return  optimal_params,opt_clustering.labels_+1



