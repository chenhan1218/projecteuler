function q50()
p=primes(1000000);

num=0;
ans=0;

for i=1:size(p,2)
	if i+num-1 > size(p,2)
		break;
	end
	
	s=sum( p(i:i+num-1) );
	for j=i+num:size(p,2)
		s=s+p(j);
		
		if s >= 1000000
			break;
		end
		
		if j-i+1 > num && isprime(s)
			num=j-i+1;
            p(i:i+num-1)
			ans=s
		end
	end
end

ans