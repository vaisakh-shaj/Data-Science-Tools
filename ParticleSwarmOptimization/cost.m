function c=cost(p,m)
n=size(p,2);
c=0;
for i=1:n
    if(i<n)
    c=c+m(p(i),p(i+1));
    else
        c=c+m(p(1),p(n));
    end
end
end