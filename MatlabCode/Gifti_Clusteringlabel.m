function Gifti_Clusteringlabel(ClusteringLabel,OrigVertIndex,OutFile)
%Clustering_label=load('/Users/Junhao/data/Project/LJHProject/Clustering/result/NGSR_Result/100307_Clustering_3Type.label.mat')
addpath(genpath('/Users/Junhao/data/ToolBox/LJHCode/fibre_tri_Code/function_final/gifti-1.6/'))

Clustering_label=load(ClusteringLabel)
%Clustering_label=load('/Users/Junhao/data/Project/LJHProject/Clustering/result/NGSR_Result/100307_Clustering_3Type.label.mat')
Orig_vertIndex=load(OrigVertIndex)

VertIndex=Orig_vertIndex.VertIndex;
ClusterLabel=(Clustering_label.Clustering_labels)';
ClusteringResult(:,1)=VertIndex;
ClusteringResult(:,2)=ClusterLabel;


label=gifti
label.cdata=zeros(32492,1);
data=zeros(32492,1);
data(ClusteringResult(:,1),:)=ClusteringResult(:,2);
label.cdata=data;
%save_surf(label,'ClusteringResult_cluster.label.func.gii');
save_surf(label,OutFile);
