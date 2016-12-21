puzzleinput = 'wtnhxymk'

import hashlib

def good_position(string):
	try:
		int(string)
		if int(string) < 8:
			return True
		else:
			return False
	except ValueError:
		return False

def brute_force(ID):
	password = ''
	password_placeholder = ['','','','','','','',''] 
	index = 0
	while '' in password_placeholder:
		current_hash = hashlib.md5((ID + str(index)).encode()).hexdigest()
		if current_hash[:5] == '00000' and good_position(current_hash[5]) and password_placeholder[int(current_hash[5])] == '':
			password_placeholder[int(current_hash[5])] = current_hash[6]
		index += 1
	while password_placeholder:
		password += password_placeholder.pop(0)
	return password

print(brute_force(puzzleinput))
