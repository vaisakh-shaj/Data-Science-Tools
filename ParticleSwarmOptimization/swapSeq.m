function ss= swapSeq(p1,p2)
k=1;
n=size(p1,2)
for i=1:n
    if(p1==p2)
        break;
    else
        if(p1(i)==p2(i))
            continue;
        else
        pos=find(p2==p1(i));
        ss(k,:)=[i,pos]
        k=k+1;
        temp=p2(i);
        p2(i)=p2(pos);
        p2(pos)=temp;
        end
    end
end