"""For Advent of Code day 7, question 2. Take as an input a string of IP addresses seperated by lines. Returns as an output the 
number of IP addresses that support SSL (different from real life SSL). An IP addresses supports SSL if there is an ABA pattern 
within a supernet sequence (sequence not surrounded by brackets) and a matching BAB pattern within a hypernet sequence (sequence 
that is surrounded by brackets). BAB sequences are palindromes of ABA sequences, and within an ABA, the A character must be 
different from the B character."""

import regex as re #regex allows for an overlapping findall where regular re doesn't

f = open('C:/Users/jzhou/Desktop/AoC/AoC7_input.txt')
puzzleinput = f.read()
f.close()


def SSLcount(inpt): #main function. Blackboxed to be as understandable as possible
    result = 0
    IPs = inpt.split()
    for IP in IPs:
        nets = re.split('(\[\w+\])',IP) #to split IPs by supernet/hypernet sequences
        supernet_strings, hypernet_strings = categorize_nets(nets) #to gather all supernet & hypernet strings in respective lists
        supernet_ABAs, hypernet_ABAs = find_ABAs(supernet_strings), find_ABAs(hypernet_strings) #to find all ABA patterns
        if palindrome_exists(supernet_ABAs, hypernet_ABAs): #to see if any supernet ABA has a matching hyper BAB
            result += 1
    return(result)


def categorize_nets(nets): #put supernet & hypernet strings in respective lists
    supernet_strings = []
    hypernet_strings = []
    for string in nets:
        if '[' in string:
            hypernet_strings.append(string)
        else:
            supernet_strings.append(string)
    return supernet_strings, hypernet_strings


def aba_check(string): #to verify that a string contains an aba pattern
    aba_list = re.findall('(\w)(\w)\\1', string, overlapped = True)
    if aba_list != None:
        for aba in aba_list:
            if aba[0] == aba[1]:
                aba_list.remove(aba)
        if aba_list:
            return aba_list
    return None


def find_ABAs(net_strings): #to find all ABAs within hypernet & supernet strings
    ABAs = []
    for sequence in net_strings:
        if aba_check(sequence):
            ABAs.extend(aba_check(sequence))
    return ABAs


def palindrome_exists(a,b): #to deduce if any supernet ABA has a corresponding hypernet BAB
    for sequence1 in a:
        for sequence2 in b:
            if sequence1[0] == sequence2[1] and sequence1[1] == sequence2[0]:
                return True
    return False

print(SSLcount(puzzleinput))
