commands = []
with open ('input') as input:
	for line in input:
		#Remove parentheses
		line = line[1:-2]

		commands.append(line)

print(commands)