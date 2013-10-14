function q41()

num=sortrows(perms('1234567'));
for i=1:size(num,1)
	if isprime( str2num(num(end-i+1,:)) )
		num(end-i+1,:)
		break;
	end
end
