maxiter=100
for iter=1:maxiter
    iter;
    c=[0 0 0];
    w1=0.95-(0.95)*((iter)/maxiter);
    w2=.05+.95*((iter)/maxiter);
    w3=.05+.95*((iter)/maxiter);
    c=[0 0 0];
        x=fortune_wheel([w1,w2,w3])
        c(x)=1;
        c;
end