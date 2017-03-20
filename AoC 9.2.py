import regex as re

f = open("C:/Users/Jonathan/Documents/Programming/Advent of Code/AoC9_input.txt")
puzzleinput = f.read()
f.close()

def decompressLen(inpt):
    marker = re.search('\((\d+)x(\d+)\)', inpt) #the matchobject that returns the first pattern match
    if marker == None:
        return len(inpt)
    end = marker.end()
    start = marker.start()
    print(inpt[start])
    depth, repetitions = int(marker.group(1)), int(marker.group(2)) #to find the depth and # of repetitions of the next repetition
    return len(inpt[:start]) + decompressLen(inpt[end:end + depth]) * repetitions + decompressLen(inpt[end + depth:])

test3 = "aa(8x2)(3x3)bbbcc"
"(3x3)bbb"
"bbb"
test2 = "aa(3x3)bbbcc"
test1 = "aabbbcc"

#print(decompressLen(puzzleinput))
print(decompressLen(test3))