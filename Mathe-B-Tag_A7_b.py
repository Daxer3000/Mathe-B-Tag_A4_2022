###  Da Pi irratioal ist, ist nur eine annährungsweise Kalkulation zur Zahl 1 hin möglich. ###


from math import pi
def get_all_numbers(max_volume_n = 5, max_volume_m = pi):
	list_of_m_volumes = [0,max_volume_m]
	list_of_n_volumes = [0, max_volume_n]
	end = False
	not_calculated = 0
	count = 0
	while end == False: 
		momentary_volume_n_from_empty = 0
		momentary_volume_n_from_full = max_volume_n
		momentary_volume_m_from_empty = 0
		momentary_volume_m_from_full = max_volume_m	
		# n -m*k
		while momentary_volume_n_from_full > 0 and count == 0 :
			if momentary_volume_n_from_full not in list_of_n_volumes:
				list_of_n_volumes.append(momentary_volume_n_from_full)
			momentary_volume_n_from_full -= max_volume_m
		# m*k
		while (momentary_volume_n_from_empty + max_volume_m)< max_volume_n :
			if not_calculated != 0:
				if not_calculated not in list_of_n_volumes :
					list_of_n_volumes .append(not_calculated)
				momentary_volume_n_from_empty += not_calculated
				not_calculated = 0	
			else:	
				if momentary_volume_n_from_empty not in list_of_n_volumes :
					list_of_n_volumes .append(momentary_volume_n_from_empty)
				momentary_volume_n_from_empty += max_volume_m 
		list_of_n_volumes.append(momentary_volume_n_from_empty)	

		residue_of_container_m_from_cyle_n_empty_to_full = max_volume_m - (max_volume_n - momentary_volume_n_from_empty)

		if residue_of_container_m_from_cyle_n_empty_to_full in list_of_m_volumes :
			pass
		else:
			list_of_m_volumes.append(residue_of_container_m_from_cyle_n_empty_to_full)

		end = True

		if residue_of_container_m_from_cyle_n_empty_to_full not in list_of_n_volumes:
			list_of_n_volumes.append(residue_of_container_m_from_cyle_n_empty_to_full)
			not_calculated = residue_of_container_m_from_cyle_n_empty_to_full
			end = False	
		count += 1
		if count > 1000: # Stopp der Kalkulation 
			break
	list_of_m_volumes.sort()
	list_of_n_volumes.sort()
	print("\n \n \n \n" +"Nearly every possible volume of container n:  ", list_of_n_volumes,"\n \n \n \n"+"Nearly every possible volume of container m:  ", list_of_m_volumes)
run = get_all_numbers() 
		 
