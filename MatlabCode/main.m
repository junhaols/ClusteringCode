%% creat clustering-label.func.gii
clear
addpath(genpath('/Users/Junhao/data/Project/LJHProject/ClusteringCode/'))
ClusteringLabel='/Users/Junhao/data/Project/LJHProject/Clustering/result/NGSR_Result/Pos/100307_Pos_Clustering_3Type.label.mat';
OrigVertIndex='/Users/Junhao/data/Project/LJHProject/Clustering/result/NGSR_Result/Pos/100307_PT_HS.VertIndex.mat';
OutFile='/Users/Junhao/data/Project/LJHProject/Clustering/result/NGSR_Result/Pos/100307_Pos_Clustering_3Class.func.gii';
Gifti_Clusteringlabel(ClusteringLabel,OrigVertIndex,OutFile);


keyName={'L-PT','L-HS'};
SubDir='/Users/Junhao/data/Project/LJHProject/Clustering/HCP_vert_FC';
Subject='100307'
GSType='GSR'
FC_Flag='Pos'
[FirstGradient,VertIndex,TargetMask]=Main_Gradient(SubDir,Subject,keyName,GSType,FC_Flag);