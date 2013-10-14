function q12()

n=1;
for i=2:50000
	n=n+i;
	primeFactor=factor( n );
	uni=unique(primeFactor);
	
	num=1 ;
	for j=1:size(uni,2);
		num = num * (size(find(primeFactor==uni(j)),2)+1);
	end
	
	if num > 500
		break;
    end
end

num
n

return;
