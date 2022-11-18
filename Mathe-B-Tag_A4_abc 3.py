def get_all_numbers(volume_n = 2022, volume_m =7):
	list_m = [0, volume_m]
	list_n = [0]
	end = False
	not_calculated = 0
	count = 0
	while end == False: 
		n = 0
		n_ = volume_n
		m = 0
		m_ = volume_m	
		# n -m*k
		while n_ > 0 and count ==0 :
			if n_ not in list_n:
				list_n.append(n_)
				n_ -= volume_m
		# m*k
		while n < volume_n :
			if not_calculated != 0:
				if not_calculated not in list_n:
					list_n.append(not_calculated)
				n += not_calculated
				not_calculated = 0	
			else:	
				if n not in list_n:
					list_n.append(n)
				n += volume_m 
		list_n.sort()
		m_num = volume_m - (volume_n - list_n[-2])
		m_num2 = list_n[1]
		if m_num in list_m:
			pass
		else:
			list_m.append(m_num)
		if m_num2 in list_m:
			pass
		else:		
			list_m.append(m_num2)
		end = True
		for i in list_m:
			if i not in list_n:
				list_n.append(i)
				not_calculated = i
				end = False
		print(not_calculated)	
		list_m.sort()
		list_n.sort()
		if count > 0:
			volume_n - list_n[-2]	
		count += 1
			
	print("Every n:  ", list_n,"'\n"+"'\n"+"Every m:  ", list_m)
run = get_all_numbers() 
		 
	