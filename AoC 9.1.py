import regex as re

f = open("C:/Users/Jonathan/Documents/Programming/Advent of Code/AoC9_input.txt")
puzzleinput = f.read()
f.close()

def determine_length(inpt): #determines the length of the decompressed file
    result = ''
    while re.search('\(\d+x\d+\)', inpt):
        marker = re.search('\(\d+x\d+\)', inpt) #the matchobject that returns the first pattern match
        markerText = marker[0] #the string of the matchobject
        depth, repetitions = int(markerText[1:markerText.find('x')]), int(markerText[markerText.find('x') + 1:markerText.find(')')]) #to find the depth and # of repetitions of the next repetition
        toDuplicate = inpt[marker.end():marker.end() + depth] #the string to duplicate
        duplication = toDuplicate * repetitions
        result, inpt = result + inpt[:marker.start()] + duplication, inpt[marker.end() + depth:] #to prepare the input for the next iteration
    if not ' ' in inpt: #to add in any leftover characters not caught by a compressor, and that isn't whitespace
        result += inpt
    return len(result)
