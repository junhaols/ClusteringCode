function LJH_CreatGifti(Vector,VertIndex,OutPut)
data=zeros(32492,1);

if size(Vector,1)<size(Vector,2)
    Vector=Vector';
end

if size(VertIndex,1)<size(VertIndex,2)
    VertIndex=VertIndex';
end

if min(VertIndex)>32492
    VertIndex=VertIndex-32492;
end

data(VertIndex)=Vector;

gii=gifti;
gii.cdata=data;
save_surf(gii,OutPut)




