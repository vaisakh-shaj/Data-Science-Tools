function y=applySwap(x,v)
n=size(v,1)
for i=1:n
    s=v(i,:);
    temp=x(s(1));
    x(s(1))=x(s(2));
    x(s(2))=temp;
end
y=x;
end