
### Da Pi irrational ist, ist eine genau Kalkulation bis zur Zahl 1 hin nur annährungsweise möglich ###

#import math.pi as pi
def get_all_numbers(volume_n = 5, volume_m =3.14159265359):
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
		while (n + volume_m)< volume_n :
			if not_calculated != 0:
				if not_calculated not in list_n:
					list_n.append(not_calculated)
				n += not_calculated
				not_calculated = 0	
			else:	
				if n not in list_n:
					list_n.append(n)
				n += volume_m 
		list_n.append(n)		
		#list_n.sort()
		m_num = volume_m - (volume_n - n)
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
		count += 1
		if count > 400: #Stopp der Kalkulation 
			break
	list_m.sort()
	list_n.sort()
	print("Every n:  ", list_n,"'\n"+"'\n"+"Every m:  ", list_m)
run = get_all_numbers() 
		 
	
