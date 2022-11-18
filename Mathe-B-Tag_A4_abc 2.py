def get_all_numbers(volume_n = 2022, volume_m = 7):
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
	m_num = volume_m - (volume_n - list_n[-2])
	m_num2 = list_n[1]
	if m_num == m_num2:
		list_m.append(m_num)
	else:
		list_m.append(m_num)
		list_m.append(m_num2)
	list_m.sort()		
	print("Every n:  ", list_n,"'\n"+"'\n"+"Every m:  ", list_m)
run = get_all_numbers() 
		 
	