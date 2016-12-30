import re

f = open('C:/Users/jzhou/Desktop/AoC/AoC7_input.txt')
puzzleinput = f.read()
f.close()

def contains_abba(string): #to verify that a string contains an abba pattern
    abba = re.search('(\w)(\w)\\2\\1',string)
    if abba != None:
        abba = abba.group(0)
        if abba[0] != abba[1]:
            return True
    return False

def TLScount(inpt):
    result = 0
    IPs = inpt.split()
    for IP in IPs:
        valid = True #valid gauges whether or not a hypernet string in the input contains an abba or not
        hypernet_strings = re.findall('(?<=\[)\w+(?=\])',IP) #negative lookahead and lookbehind regex statement
        for string in hypernet_strings:
            if contains_abba(string):
                valid = False
                break #all it takes it one hypernet abba to spoil the barrel
        if contains_abba(IP) and valid == True:
            result += 1
    return result

print(TLScount(puzzleinput))
