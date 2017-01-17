puzzledescription = 'http://adventofcode.com/2016/day/8'

import regex as re
import copy #so I can do deepcopies


f = open('C:/Users/jzhou/Desktop/AoC/AoC8_input.txt')
puzzleinput = f.read()
f.close()


def make_screen(rows, columns): #creates a rows by columns sized screen, with each row as a nested list. All pixels in the screen start off as '.'
    board = []
    row = ['.'] * columns
    for n in range(rows):
        new_row = list(row)
        board.append(new_row)
    return board


puzzlescreen = make_screen(6, 50)


def pixel_count(inpt, screen): #to count the number of pixels in the input screen after going through all the input actions
    sequence = re.findall('\w+ [a-z0-9= ]+', inpt) #works because + and * are greedy. Adding \n to the inside of the brakcet would match the whole puzzleinput
    for instructions in sequence:
        if instructions.startswith('rect'):
            screen = turn_on_pixels(instructions, screen) #replaces all '.'s with '#'s in an n x n rectangle
        elif instructions.startswith('rotate row'):
            screen = rotate_row(instructions, screen) #rotates a certain row by a certain depth
        else:
            screen = rotate_column(instructions, screen) #rotates a certain column by a certain depth
    return countpixels(screen)


def turn_on_pixels(instructions, screen):
    rect_area = instructions[instructions.find('rect') + 5:]
    size_values = rect_area.split('x')
    for i in range(int(size_values[1])):
        for n in range(int(size_values[0])):
            screen[i][n] = '#'
    return screen


def rotate_row(instructions, screen): #rotates to the right the row at index row, by depth amount. Rotations that exceed the end of the index overlap to the front
    row = int(re.search('(?<=y=)\d+', instructions).group()) #lookbehind assertion for y= and returns the corresponding number
    depth = int(re.search('\d+$', instructions).group()) #Perhaps there's a more universally understood way to do this operation?
    screen[row] = screen[row][-depth:] + screen[row][:-depth]
    return screen


def rotate_column(instructions, screen): #rotates down the column at index column, by depth amount. rotations that exceed below the bottom list go to the top
    result = copy.deepcopy(screen) #to make a non aliased copy of the screen
    column = int(re.search('(?<=x=)\d+', instructions).group()) #to find the correct column to rotate
    depth = int(re.search('\d+$', instructions).group()) #how much to rotate that column
    for i in range(len(screen)):
        result[(i + depth) % 6][column] = screen[i][column]
    return result


def countpixels(screen): #count the number of pixels that are '#'
    result = 0
    for row in screen:
        for pixel in row:
            if pixel == '#':
                result +=1
    return result


print(pixel_count(puzzleinput, puzzlescreen))
