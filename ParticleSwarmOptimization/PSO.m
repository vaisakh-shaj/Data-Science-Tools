clc;clear;clear all;
m=load('gr17_d.txt');
N=size(m,1);
n=input('enter the number of particles');
vel=[];p=[];pos=[];
for i=1:n
    p(i,:)=randperm(N,N);
    vel{i}=swapSeq(randperm(N,N),p(i,:));
end
c1=1.5;c2=1.5;
Lbest=randperm(N,N);
Gbest=randperm(N,N);
for iter=1:10
    for i=1:n
        I=p(i,:);
        ic=cost(I,m);
        lbc=cost(Lbest,m);
        gbc=cost(Gbest,m);
        if(ic>lbc)
            Lbest=p(i,:);
        end
        if(ic>gbc)
            Gbest=p(i,:);
        end
        p3=edgeR(I,Lbest,m);
        p4=edgeR(I,Gbest,m);
        ssl=swapSeq(p3,I);
        ssg=swapSeq(p4,I);
        vel{i}=ADD(vel{i},mul(c1,ssl),mul(c2,ssg));
        pos(i,:)=applySwap(I,vel(:,:,i));
        vel{i}=swapSeq(pos(i,:),I);
    end
end