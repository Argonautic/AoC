import regex as re

f = open('C:/Users/jzhou/Desktop/AoC/AoC8_input.txt')
puzzleinput = f.read()
f.close()

def make_screen(rows, columns):
    board = []
    row = ['.'] * columns
    for n in range(rows):
        new_row = row[:]
        board.append(new_row)
    return board

puzzlescreen = make_screen(6, 50)

test1 = 'rect 3x2'
test2 = 'rotate row y=1 by 3'
test3 = 'rotate column x=1 by 2'
test4 = '123456'

def decipher(inpt, screen):
    sequence = re.findall('\w+ [a-z0-9= ]+', inpt) #works because + and * are greedy. Adding \n to the inside of the brakcet would match the whole puzzleinput
    for instructions in sequence:
        if instructions.startswith('rect'):
            screen = turn_on_pixels(instructions, screen)
        elif instructions.startswith('rotate row'):
            screen = rotate_row(instructions, screen)
        else:
            screen = rotate_column(instructions, screen)
    return countpixels(screen)


def turn_on_pixels(instructions, screen):
    rect_area = instructions[instructions.find('rect') + 5:]
    size_values = rect_area.split('x')
    for i in range(int(size_values[1])):
        for n in range(int(size_values[0])):
            screen[i][n] = '#'
    return screen


def rotate_row(instructions, screen):
    row = int(re.search('(?<=y=)\d+', instructions).group()) #lookbehind assertion for y= and returns the corresponding number
    depth = int(re.search('\d+$', instructions).group()) #Perhaps there's a more universally understood way to do this operation?
    screen[row] = screen[row][-depth:] + screen[row][:-depth]
    return screen


def rotate_column(instructions, screen):
    result = screen[:]
    column = int(re.search('(?<=x=)\d+', instructions).group())
    depth = int(re.search('\d+$', instructions).group())
    for i in range(len(screen)):
        result[(i + depth) % 6][column] = screen[i][column]
        #for row in result:
        #    print(row)
        #for row1 in screen:
        #    print(screen)

#print(turn_on_pixels(test1, puzzlescreen))
puzzlescreen = turn_on_pixels(test1, puzzlescreen)
#for row1 in puzzlescreen:
#    print(row1)
#print(rotate_row(test2, puzzlescreen))
print(rotate_column(test3, puzzlescreen))
#print(decipher(puzzleinput, puzzlescreen))
