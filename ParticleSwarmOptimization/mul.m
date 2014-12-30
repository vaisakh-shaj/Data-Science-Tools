function V=mul(c,v)
if(c<1)
    n=floor(c*size(v,1));
    v=v(1:n,:)
else
    if(c>1)
        V=[];
        N=floor(c);
        for i=1:N
            V=[V;v];
        end
        C=c-N;
        n=floor(C*size(v));
        v=v(1:n,:);
        V=[V;v]
    else
        if(c==0)
            V=[];
        end
    end
end
end
