#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:00:10 2020

@author: Junhao
"""
#from sklearn.cluster import SpectralClustering
import numpy as np
import scipy.io as sio
#import pandas as pd
#import nibabel as nib
#import glob
#import os
#import sys
#import glob
#file_li=glob.glob('/Users/Junhao/data/Project/LJHProject/Clustering/HCP_vert_FC/*.mat')


## basic fun to extract FC matrix from input file

def FC_FileMat(filename,array_ori):
    # FC matrix
    newfc=sio.loadmat(filename)['FC']
    new_array=np.concatenate((array_ori,newfc),axis=0)
    # seedIndex
     
    return new_array

def FC_FileMatAppend(file_li):
   
    if isinstance(file_li,list):
        arr_ori=sio.loadmat(file_li[0])['FC']
        print('list files to input!')
        for filename in file_li[1:]:
            arr_ori=FC_FileMat(filename,arr_ori)
        return arr_ori
    elif isinstance(file_li,str):
        arr_ori=sio.loadmat(file_li)['FC']
        
        return arr_ori


## basic fun to extract seed Index from input file

def Seed_FileIndexMat(filename,array_ori):
  
    newindex=sio.loadmat(filename)['seedIndex']
    new_array=np.concatenate((array_ori,newindex),axis=0)
    # seedIndex
     
    return new_array

def FC_FileIndexMatAppend(file_li):
   
    if isinstance(file_li,list):
        arr_ori=sio.loadmat(file_li[0])['seedIndex']
        print('list files to input!')
        for filename in file_li[1:]:
            arr_ori=Seed_FileIndexMat(filename,arr_ori)
        return arr_ori
    elif isinstance(file_li,str):
        arr_ori=sio.loadmat(file_li)['seedIndex']
        return  arr_ori   

