f = open('AoC6_input.txt')
puzzleinput = f.read()
f.close

import collections

def repair(inpt):
    result = ''
    index = 0
    rows = inpt.split()
    column_message = ''
    while index < len(rows[0]):
        for row in rows:
            column_message += row[index]
        frequencies = collections.Counter(column_message)
        highest_frequency = max(frequencies, key=frequencies.get)
        result += highest_frequency
        index += 1
        column_message = ''
    return result

print(repair(puzzleinput))
