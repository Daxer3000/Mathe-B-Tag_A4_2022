def get_all_numbers(volume_n = 1999, volume_m = 4):
	list_m = [0, volume_m]
	list_n = [0]
	n = 0
	n_ = volume_n
	m = 0
	m_ = volume_m
	
	# n -m*k
	while n_ > 0 :
		if n_ not in list_n:
		 	list_n.append(n_)
		n_ -= volume_m
	# m*k
	while n < volume_n :
		if n not in list_n:
			list_n.append(n)
		n += volume_m 
	list_n.sort()		
	print("Every n:  ", list_n,"'\n"+"'\n"+"Every m:  ", list_m)
run = get_all_numbers() 
		 
	