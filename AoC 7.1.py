import re

f = open('C:/Users/jzhou/Desktop/AoC/AoC7_input.txt')
puzzleinput = f.read()
f.close()

testinput = """rhamaeovmbheijj[hkwbkqzlcscwjkyjul]ajsxfuemamuqcjccbcpoop
gdlrknrmexvaypu[crqappbbcaplkkzb]vhvkjyadjsryysvj[nbvypeadikilcwg]jwxlimrgakadpxu[dgoanojvdvwfabtt]yqsalmulblolkgsheo
dqpthtgufgzjojuvzvm[eejdhpcqyiydwod]iingwezvcbtowwzc[uzlxaqenhgsebqskn]wcucfmnlarrvdceuxqc[dkwcsxeitcobaylhbvc]klxammurpqgmpsxsr
gmmfbtpprishiujnpdi[wedykxqyntvrkfdzom]uidgvubnregvorgnhm"""

test = 'rhamaeovmbheijj[hkwbkqzlcscwjkyjul]ajsxfuemamuqcjccbcpoop'

def contains_abba(string):
    abba_start = re.search('(\w)(\w)\\2\\1',string)
    print(abba_start)
    try:
        abba = string[abba_start:abba_start+4]
        print(abba)
        if abba[0] != abba[1]:
            return True
    except:
        return False

def TLScount(inpt):
    result = 0
    IPs = inpt.split()
    for IP in IPs:
        valid = True
        hypernet_strings = re.findall('(?<=\[)\w+(?=\])',IP)
        for string in hypernet_strings:
            if contains_abba(string):
                valid = False
                break
        if contains_abba(IP) and valid == True:
            result += 1
            print(hypernet_strings)
            print(IP)
    return result

print(contains_abba(test))
#print(TLScount(testinput))
