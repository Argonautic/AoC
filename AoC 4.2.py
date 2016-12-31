import re #really enjoying regex's. I don't really have to use it here but for rn it's just mad fun
import collections

f = open("C:/Python27/Jon's Code/AoC4_input.txt")
puzzleinput = f.read()
f.close()

def decrypt(room_codes):
	next_room_startpoint = room_codes.find(']')
	while next_room_startpoint != -1: #keep's going until the last bracket
		current_room_code = room_codes[:next_room_startpoint] #the string of the current room name, sector ID, and checksum
		sectorID_search = re.search('\d',current_room_code) #to locate the index of the start of the sector ID
		sectorID = int(current_room_code[sectorID_search.start():sectorID_search.start()+3]) #the entire sector ID as an int
		raw_letters = current_room_code[:sectorID_search.start()-1] #the string of the encrypted room name
		rooms.append(shift(raw_letters,sectorID))
		shifted = (shift(raw_letters,sectorID))
		if "north" in shifted:
			print(shifted,sectorID)
		room_codes = room_codes[next_room_startpoint+1:] #room code begins at the end of this current room
		next_room_startpoint = room_codes.find(']') #prep the next iteration


def shift(letters,depth):
	result = ''
	depth = depth % 26
	for letter in letters:
		if letter == '-':
			result += ' '
			continue
		shifted_letter = ord(letter)+depth
		if shifted_letter > 122:
			shifted_letter = chr((shifted_letter%122) + 96)
		else:
			shifted_letter = chr(shifted_letter)
		result += shifted_letter
	return result

print(decrypt(puzzleinput))