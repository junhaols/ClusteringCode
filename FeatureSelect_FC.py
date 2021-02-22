#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:58:11 2021

@author: Junhao
"""
import numpy as np
import scipy.io as sio
##############################################################################
## All FC are selected. (Feature-1)

# The basic function for interation
def FC_FileMat(filename,array_ori):
    # FC matrix
    newfc=sio.loadmat(filename)['FC']
    new_array=np.concatenate((array_ori,newfc),axis=0)
    # seedIndex  
    return new_array

def FC_FileMatAppend(file_li):  # file_li:A list to store all the file path.
   
    if isinstance(file_li,list):
        arr_ori=sio.loadmat(file_li[0])['FC']
        print('list files to input!')
        for filename in file_li[1:]:
            arr_ori=FC_FileMat(filename,arr_ori)
        return arr_ori
    elif isinstance(file_li,str):
        arr_ori=sio.loadmat(file_li)['FC']
        
        return arr_ori

##############################################################################
## All the seed index are selected
# basic fun to extract seed Index from input file

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

##############################################################################
## Only the positive FC are selected.(Feature-2)

def FC_Matrix_Pos_2Files(files_FC):
    if len(files_FC)==1:
        FC=sio.loadmat(files_FC[0])['FC']
        FC_mean=np.mean(FC,0)
        FC_pos_index=np.where(FC_mean>0)
        PreData_pos=FC[:,FC_pos_index]
        return PreData_pos
    else:
        # the first file
        FC0=sio.loadmat(files_FC[0])['FC']
        FC0_mean=np.mean(FC0,0)
        FC0_pos_index=np.where(FC0_mean>0)
        PreData0_pos=FC[:,FC0_pos_index]
        
        for file in files_FC[1:]:
            FC=sio.loadmat(file)['FC']
            FC_mean=np.mean(FC,0)
            FC_pos_index=np.where(FC_mean>0)
            PreData_pos=FC[:,FC0_pos_index]
            index_pos=np.intersect1d(FC0_pos_index,FC_pos_index) #intersextld:both in x and y
            FCData=np.row_stack((FC,FC0)); # Store all the FC-data
            
            
            
            
            
            
            
            

    
    

    for file in files_FC:
        print(file)
        FC=sio.loadmat(file)['FC']
        FC_mean=np.mean(FC,0)
   

    ## read mat 
    LPT_FC = sio.loadmat(files_FC[0])
    LHS_FC=sio.loadmat(files_FC[1])
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



















