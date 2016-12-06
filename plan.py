import os
import rospy
import fileinput
from get_speech import get_speech

def contains(accepted, string):
	for i in range(0, len(accepted)):
		if accepted[i] in string:
			return i
	return -1


def place_in_file(file_name, location, new_text):
	for line in fileinput.FileInput(file_name, inplace=1):
		if location in line:
			line = line.replace(line, line + new_text)
		print line,


def generate_waypoints(number):
	string = "\n\t\t"
	for i in range(1, int(number)  + 1):
		string += "waypoint" + str(i) + " "
	string += "- waypoint"
	return string


def make_plan():
	#Welcome

	#Waypoints
	os.system("mpg123 waypoints.mp3")
	ans = raw_input("How many? ")
	place_in_file("template2_problem.pddl", "(:objects", generate_waypoints(ans))



if __name__ == '__main__':
    try:
        make_plan()
    except rospy.ROSInterruptException:
        pass


