function q21()

a=0;
for i=2:10000
	if sumDivisors(sumDivisors(i))==i & sumDivisors(i)~=i
		a = a + i ;
		i
	end
end

a
return;


function ans=sumDivisors(n)
f=factor(n);
uf=unique(f);

ans=1;
for j=1:size(uf,2)
	ans=ans*(uf(j)^(sum(f==uf(j))+1)-1)/(uf(j)-1);
end

ans=ans-n;
