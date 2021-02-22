#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:16:44 2020

@author: Junhao

"""


import sys
import glob
import scipy.io as sio
sys.path.append('/Users/Junhao/data/Project/LJHProject/ClusteringCode')
import FC_Matrix as FCG
import FC_Matrix_Pos_2Files as FCG2
import SpectralClustering as Clu

## GSR-All
#file=glob.glob('/Users/Junhao/data/Project/LJHProject/Clustering/HCP_vert_FC/*PT*.mat')
file=['/Users/Junhao/data/Project/LJHProject/Clustering/HCP_vert_FC/GSR/100307_FC_L-PT_surf_vert.mat','/Users/Junhao/data/Project/LJHProject/Clustering/HCP_vert_FC/GSR/100307_FC_L-HS_surf_vert.mat']

FCMatrix=FCG.FC_FileMatAppend(file)
labelIndex=FCG.FC_FileIndexMatAppend(file)
OutFile_label='/Users/Junhao/data/Project/LJHProject/Clustering/Result/GSR_Result/All/100307_PT_HS.VertIndex.mat'
sio.savemat(OutFile_label,{'VertIndex':labelIndex}) # plus 1 for

ClassNum=3

InputMatrix=FCMatrix
OutFile='/Users/Junhao/data/Project/LJHProject/Clustering/Result/GSR_Result/All/100307_All_Clustering_3Type.label.mat'

Clu.LJH_SpectralClustering(InputMatrix,OutFile,ClassNum) # default class=2

## GSR-Pos
labelIndex=FCG.FC_FileIndexMatAppend(file)
OutFile_label='/Users/Junhao/data/Project/LJHProject/Clustering/Result/GSR_Result/Pos/100307_PT_HS.VertIndex.mat'
sio.savemat(OutFile_label,{'VertIndex':labelIndex}) # plus 1 for
ClassNum=3
InputMatrix=FCG2.FC_Matrix_Pos_2Files(file)
OutFilePos='/Users/Junhao/data/Project/LJHProject/Clustering/Result/GSR_Result/Pos/100307_Pos_Clustering_3Type.label.mat'
Clu.LJH_SpectralClustering(InputMatrix,OutFilePos,ClassNum) # default class=2












## timeSeries

# import TimeSeries_Matrix as TM
# ciftiFile='/Users/Junhao/data/Project/LJHProject/Clustering/100307_Cifti/smooth_no_interp_wm_csf_gs_LR.dtseries.nii'
# labelFile='/Users/Junhao/data/Project/LJHProject/Clustering/HCP_label/HCP_100307.Rhemi_GZY.tex.gii'
# corticalMask='/Users/Junhao/data/Project/LJHProject/Clustering/CorticalVertIndex_RemoveNAN.mat'
# labelValue=100
# time1=TM.LJH_FileInputTimeSeries(ciftiFile,labelFile,corticalMask,labelValue)

