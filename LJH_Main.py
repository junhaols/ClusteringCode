#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 10:46:31 2020

@author: Junhao
"""
import sys
import glob
import scipy.io as sio
sys.path.append('/Users/Junhao/data/Project/LJHProject/ClusteringCode')
import FC_Matrix as FCG
import FC_Matrix_Pos_2Files as FCG2
import SpectralClustering as Clu
import os
import nibabel as nib
import numpy as np


## reading files

def SelectFiles(path,subj,GSType,types = ('*L-PT*', '*L-HS*')):
    # GSType:'GSR' or 'NGSR'
    # DateTypes:L-PT*', '*L-HS
    files=[]
    for mytype in types:
        filepath=path+GSType+'/'+subj+mytype
        files.extend(glob.glob(filepath))
    return files
    
def Run_Clustering(Files,FeatureType,ClassNum,ResultFolder,baseGifti,Hemi,Name):
    # FeatureFlag:'All','Pos'
    if FeatureType=='All':
       FCMatrix=FCG.FC_FileMatAppend(Files) # All FC
    elif FeatureType=='Pos':
       FCMatrix=FCG2.FC_Matrix_Pos_2Files(Files) # Positive FC
    else:
       print('FeatureType should be "All" or "Pos".')
       
    # Clustering 
    if not os.path.exists(ResultFolder):                   
       os.makedirs(ResultFolder)
    # Restore orignal label vert index
    labelIndex=FCG.FC_FileIndexMatAppend(Files)
    OutFile_label=ResultFolder+'/'+Name+'_VertIndex.mat'
    sio.savemat(OutFile_label,{'VertIndex':labelIndex}) # plus 1 for

    OutFile=ResultFolder+'/'+Name+'_Clustering.label.mat'
    ##### modified
    #Clustering_label=Clu.LJH_SpectralClustering(FCMatrix,OutFile,ClassNum)
    ####
    optimal_params,Clustering_label=Clu.LJH_SpectralClustering_fit(FCMatrix,OutFile,ClassNum)
    ## save as xxx.func.gii
  
    gii=nib.load(baseGifti)
    gii_new=gii
    #gii_new.darrays[0].data=np.zeros(32492,int) # 32492*0 matrix
    data_new=np.zeros(32492,int)
    # reshape 
    label_index_new=labelIndex.reshape(len(labelIndex),)
    # Hemi judging
    if Hemi=='L':
        print('Clustering whitin left hemisphere.')
    else:
        label_index_new=label_index_new-32492 # index-32492 for half hemi to view.
        print('Clustering whitin right hemisphere.')
        
       
    data_new[label_index_new-1]=Clustering_label  # python index should minus 1
    gii_new.darrays[0].data=data_new
    gii_out=ResultFolder+'/'+Name+'_'+str(optimal_params['n_cluster'])+'types'+'_Clustering.label.func.gii'
    nib.save(gii_new,gii_out)
    

 
    
def main(sub_path,subj,result_folder,basic_gii,Hemi,ClassNum,types):
    # Hemi:'L','R'
    #types = ('*L-PT*', '*L-HS*') 
    # 1.GSR+All
    GSType='GSR'
    FeatureType='All'
    #ClassNum=3
    ResultFolder1=os.path.join(result_folder,subj,GSType,FeatureType)
    Name=subj+'_',GSType+'_'+FeatureType+'_'+types[0][1:5]+'_'+types[1][1:5]
    Name=''.join(Name) # tuple to str
    files1=SelectFiles(sub_path,subj,GSType,types)
    Run_Clustering(files1,FeatureType,ClassNum,ResultFolder1,basic_gii,Hemi,Name)
    
    # 2.GSR+Pos
    GSType='GSR'
    FeatureType='Pos'
    #ClassNum=3
    ResultFolder2=os.path.join(result_folder,subj,GSType,FeatureType)
    Name=subj+'_',GSType+'_'+FeatureType+'_'+types[0][1:5]+'_'+types[1][1:5]
    Name=''.join(Name)
    files2=SelectFiles(sub_path,subj,GSType,types)
    Run_Clustering(files2,FeatureType,ClassNum,ResultFolder2,basic_gii,Hemi,Name)
    
    # 3.NGSR+All
    GSType='NGSR'
    FeatureType='All'
    #ClassNum=3
    ResultFolder3=os.path.join(result_folder,subj,GSType,FeatureType)
    Name=subj+'_',GSType+'_'+FeatureType+'_'+types[0][1:5]+'_'+types[1][1:5]
    Name=''.join(Name)
    files3=SelectFiles(sub_path,subj,GSType,types)
    Run_Clustering(files3,FeatureType,ClassNum,ResultFolder3,basic_gii,Hemi,Name)
    
    # 4.NGSR+Pos
    
    GSType='NGSR'
    FeatureType='Pos'
    #ClassNum=3
    ResultFolder4=os.path.join(result_folder,subj,GSType,FeatureType)
    Name=subj+'_',GSType+'_'+FeatureType+'_'+types[0][1:5]+'_'+types[1][1:5]
    Name=''.join(Name)
    files4=SelectFiles(sub_path,subj,GSType,types)
    Run_Clustering(files4,FeatureType,ClassNum,ResultFolder4,basic_gii,Hemi,Name)

if __name__ == '__main__':
    import time
    time_start=time.time()
    basic_gii='/Users/Junhao/data/Project/LJHProject/Clustering/HCP_label/HCP_100408.Lhemi_GZY.tex.gii'
    sub_path='/Users/Junhao/data/Project/LJHProject/Clustering/HCP_vert_FC/'  
    
    #########################
    types1 = ('*L-PT*', '*L-HS*')
    Hemi1='L'
    types2 = ('*R-PT*', '*R-HS*')
    Hemi2='R'
    ClassNum1=(2,3,4,5,6)
    ClassNum2=(2,3,4,5,6)
    #ClassNum2=2
    result_folder='/Users/Junhao/data/Project/LJHProject/Clustering/Result/Result_new'
    ########################
    subject=['100206','100307','100408']
    #subject=['100307']
    for subj in subject:
        main(sub_path,subj,result_folder,basic_gii,Hemi1,ClassNum1,types1)
        main(sub_path,subj,result_folder,basic_gii,Hemi1,ClassNum2,types1)
        main(sub_path,subj,result_folder,basic_gii,Hemi2,ClassNum1,types2)
        main(sub_path,subj,result_folder,basic_gii,Hemi2,ClassNum2,types2)
        
    print('finished!')
    time_end=time.time()
    print('time cost',time_end-time_start,'s')

# ## test    
# label='/Users/Junhao/data/Project/LJHProject/Clustering/HCP_label/HCP_100408.Lhemi_GZY.tex.gii'
# import nibabel as nib

# gii=nib.load(label)




    