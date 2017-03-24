#http://adventofcode.com/2016/day/12

f = open('C:/Users/Jonathan/Documents/Programming/Advent of Code/AoC12_input.txt')
puzzleinput = f.read()
f.close()

#PART ONE

registersDayOne = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

def processCode(inpt, registers):
	i = 0
	instructions = inpt.splitlines()
	while i < len(instructions):
		if instructions[i].startswith('cpy'):
			copy(instructions[i], registers)

		elif instructions[i].startswith('inc'):
			currentRegister = instructions[i][4:]
			registers[currentRegister] += 1

		elif instructions[i].startswith('dec'):
			currentRegister = instructions[i][4:]
			registers[currentRegister] -= 1
		
		else:
			jumpRange = jump(instructions[i], registers)
			i += jumpRange - 1	
		i += 1
	return registers

def copy(inpt, registers):
	instructionParts = inpt.split()
	toCopy, currentRegister = instructionParts[1], instructionParts[2]
	if toCopy.isdigit():
		registers[currentRegister] = int(toCopy)
	else:
		registers[currentRegister] = registers[toCopy]

def jump(inpt, registers):
	instructionParts = inpt.split()
	check, jumpRange = instructionParts[1], int(instructionParts[2])
	if not check.isdigit() and registers[check] == 0 or check == '0':
		jumpRange = 1
	return jumpRange 

#print(processCode(puzzleinput, registersDayOne))

#PART TWO

registersDayTwo = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
print(processCode(puzzleinput, registersDayTwo))