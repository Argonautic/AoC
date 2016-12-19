import re #really enjoying regex's. I don't really have to use it here but for rn it's just mad fun
import collections
import urllib.request
with urllib.request.urlopen('http://adventofcode.com/2016/day/4/input') as response:
   html = response.read()

def prep(puzzleinput):
    puzzleinput += ' '
    return puzzleinput
    dsdsasad

def sectorID_sum(room_codes):
    room_codes += ' '
    result = 0
    next_room_startpoint = room_codes.find(']') + 1
    current_room_code = room_codes[:next_room_startpoint]
    sectorID_search = re.search('\d',current_room_code) #to find index of the first digit of the sector ID
    sectorID = current_room_code[sectorID_search.start():sectorID_search.start()+3]
    raw_letters = current_room_code[:sectorID_search.start()]
    letters = raw_letters.replace('-','')
    checksum = current_room_code[room_codes.find('[')+1:next_room_startpoint-1]
    #while next_room_startpoint != -1:
if is_real(letters,checksum):
            result = sectorID
        
            #room_codes = room_codes[next_room_startpoint:]
            #next_room_startpoint = room_codes.find(']') + 1

def is_real(letters,checksum):
    most_frequent_letters = []
    for code in checksum:
        frequencies = collections.Counter(letters)
        highest_frequency = max(frequencies.values())
        for letter in checksum:
            if frequencies[letter] == highest_frequency:
                most_frequent_letters.append(letter)
        if most_frequent_letters:
            if min(most_frequent_letters) != code:
                return False
        else:
            return False
        most_frequent_letters = []
        letters = letters.replace(code,'')
    return True

print(sectorID_sum(prep(puzzleinput)))

#print(is_real('nzydfxpcrclopqwzhpcqtylyntyr','oshgk'))
#print(is_real('aaaaabbbzyx','abxyz'))
