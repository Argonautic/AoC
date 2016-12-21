puzzleinput = 'wtnhxymk'

import hashlib

def brute_force(ID):
	password = ''
	index = 0
	while len(password) < 8:
		current_hash = hashlib.md5((ID + str(index)).encode()).hexdigest()
		if current_hash[:5] == '00000':
			password += current_hash[5]
		index += 1
	return password

print(brute_force(puzzleinput))
