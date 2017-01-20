import regex as re

f = open('C:/Users/jzhou/Desktop/AoC/Puzzleinputs/AoC9_input.txt')
puzzleinput = f.read()
f.close()

print(len(puzzleinput))

h = 'la(5x3)(5x5)Tomfsd(2x1)Hoshtrhgfdbhs(10x10)dgfsdgfsdfsrrtfhj'

def determine_length(inpt):
    result = ''
    while re.search('\(\d+x\d+\)', inpt):
        marker = re.search('\(\d+x\d+\)', inpt) #the matchobject that returns the first pattern match
        markerText = marker[0] #the string of the matchobject
        depth, repetitions = int(markerText[1:markerText.find('x')]), int(markerText[markerText.find('x') + 1:markerText.find(')')]) #to find the depth and # of repetitions of the next repetition
        toDuplicate = inpt[marker.end():marker.end() + depth]
        duplication = toDuplicate * repetitions
        result, inpt = result + inpt[:marker.start()] + duplication, inpt[marker.end() + depth:]
        #print(result)
        #print(inpt)
    result += inpt
    return len(result)

print(determine_length(h))
