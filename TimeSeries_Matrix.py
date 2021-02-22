#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 13:46:08 2020

@author: Junhao
"""
import numpy as np
import scipy.io as sio
import pandas as pd
import nibabel as nib
import glob
import os
import sys
import glob
#file_li=glob.glob('/Users/Junhao/data/Project/LJHProject/Clustering/HCP_vert_FC/*.mat')


## basic fun to extract FC matrix from input file

# def FC_FileMat(filename,array_ori):
#     # FC matrix
#     newfc=sio.loadmat(filename)['FC']
#     new_array=np.concatenate((array_ori,newfc),axis=0)
#     # seedIndex
     
#     return new_array

# def FC_FileMatAppend(file_li):
   
#     if isinstance(file_li,list):
#         arr_ori=sio.loadmat(file_li[0])['FC']
#         print('list files to input!')
#         for filename in file_li[1:]:
#             arr_ori=FC_FileMat(filename,arr_ori)
#         return arr_ori
#     elif isinstance(file_li,str):
#         arr_ori=sio.loadmat(file_li)['FC']
        
#         return arr_ori



################################
        


def LJH_FileInputTimeSeries(ciftiFile,labelFile,corticalMask,labelValue):
    ## Time Series
    Img= nib.load(ciftiFile)
    Cifti=Img.dataobj
    data=Cifti[:] # It has removed 'NAN'  Cortical:59412,(0--59411)
    CorticalData=data[:,0:59412]
    CorticalData=CorticalData.T #Transpose
    
    ## Label File
    Label=nib.load(labelFile)
    labelData=Label.darrays[0].data; # darrays for label 
    labelData=np.around(labelData) # around label data

    
    ## mask_file=/Users/Junhao/data/Project/LJHProject/Clustering/CorticalVertIndex_RemoveNAN.mat
    mask=sio.loadmat(corticalMask) # a dict with key:brain_vert
    mask_data=mask['brain_vert']
    nan_index=mask['nan_index']
    new_nan_index= nan_index-1 # python vs. matlab 
    CorticalData_full=np.insert(CorticalData,new_nan_index[1:100],0,axis=0)
    
   
 ## label  
    index=np.where(labelData==labelValue) # orignal index of ROI
    #ROIdata=labelData[index,]
    mat_index=np.array(index,dtype=int)+1; # index is a tuple,converted to array
    vert_index_orig=np.where(mask_data==mat_index[0])
    for i in range(1,len(mat_index)):
        vert_index=np.where(mask_data==mat_index[i])
        vert_index_orig=np.concatenate(vert_index_orig,vert_index)
        
    #index_array=np.array(vert_index_orig) # convert a list to array
    index_array=vert_index_orig.T
    timeSeries=CorticalData[index_array] # select as rows
    
    return timeSeries,mat_index

