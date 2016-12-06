def get_commands(file):
	commands = []
	with open (file) as input:
		for line in input:
			#Remove parentheses
			line = line[1:-2]

			commands.append(line)

	return commands










