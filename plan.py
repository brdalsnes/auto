import os
import rospy
import fileinput
import time
from get_speech import get_speech
from cabbage2 import *
from get_speech import *

FILE_PROBLEM = "template2_problem.pddl"
FILE_DOMAIN = "template2_domain.pddl"
robot_placement = ""

def reset_files():
	f = open("problem_start.pddl", 'r')
	text = f.read()
	f.close()
	f = open(FILE_PROBLEM, 'w')
	f.write(text)
	f.close()
	f = open("domain_start.pddl", 'r')
	text = f.read()
	f.close()
	f = open(FILE_DOMAIN, 'w')
	f.write(text)
	f.close()


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


def check_if_valid(ans_list, robot):
	if ans_list[0] == ans_list[2] != robot:
		return False
	if ans_list[1] == ans_list[2] != robot:
		return False
	return True

def generate_waypoints(number):
	string = "\n\t\t"
	for i in range(1, int(number)  + 1):
		string += "waypoint" + str(i) + " "
	string += "- waypoint\n"
	return string

def generate_robot_position(number):
	return "\n\t\t(atrobot waypoint" + str(number) + ")\n"

def generate_color_position(n_list):
	string = "\n\t\t(at green_box waypoint" + str(n_list[0])
	string += ")(at red_box waypoint" + str(n_list[1])
	string += ")(at grey_box waypoint" + str(n_list[2] + ")\n")
	return string

def generate_boxes(number):
	string = "\n\t\tgreen_box red_box grey_box "
	for i in range(1, int(number) + 1):
		string += "black_box" + str(i) + " "
	return string + " - box\n"

def generate_black_boxes(number):
	string = "\n\t\t"
	for i in range(1, int(number) + 1):
		string += "(dropped black_box" + str(i) +")"
	string += "\n"
	for i in range(1, int(number) + 1):
		string += "\t\t(black black_box" + str(i) +")"
	return string + "\n"

def generate_black_position(number_list):
	string ="\n\t\t"
	for i in range(0, len(number_list)):
		string += "(at black_box" + str(i+1) + " waypoint" + str(number_list[i]) + ")"
	return string + "\n"

def generate_domain(number):
	string = "(not(intrans green_box))(not(intrans red_box))(not(intrans grey_box))"
	for i in range(1, int(number) + 1):
		string += "(not(intrans black_box" + str(i) + "))"
	return string + ")\n"


def make_plan():
	reset_files()
	#Welcome

	#Waypoints
	os.system("mpg123 waypoints.mp3")
	ans = raw_input("How many? ")
	#ans = answer(['2', '3', '4']) #This format for speech instead of raw_input
	#Also have to convert 2 -> two somewhere
	place_in_file(FILE_PROBLEM, "(:objects", generate_waypoints(ans))


	#Place robot
	os.system("mpg123 place_robot.mp3")
	ans = raw_input("Where? ")
	robot_placement = ans
	place_in_file(FILE_PROBLEM, "(:init", generate_robot_position(ans))

	#Place boxes
	valid = False
	while not valid:
		ans_list = []
		#Green
		os.system("mpg123 place_green.mp3")
		ans = raw_input("Where?" )
		ans_list.append(ans)
		#Red
		os.system("mpg123 place_red.mp3")
		ans = raw_input("Where?" )
		ans_list.append(ans)
		#Grey
		os.system("mpg123 place_grey.mp3")
		ans = raw_input("Where?" )
		ans_list.append(ans)
		valid = check_if_valid(ans_list, robot_placement)
		if not valid:
			os.system("mpg123 invalid.mp3") #Not valid
	place_in_file(FILE_PROBLEM, "(grey grey_box)", generate_color_position(ans_list))

	#Goal boxes
	ans_list = []
	#Green
	os.system("mpg123 goal_green.mp3")
	ans = raw_input("Where?" )
	ans_list.append(ans)
	#Red
	os.system("mpg123 goal_red.mp3")
	ans = raw_input("Where?" )
	ans_list.append(ans)
	#Grey
	os.system("mpg123 goal_grey.mp3")
	ans = raw_input("Where?" )
	ans_list.append(ans)
	place_in_file(FILE_PROBLEM, "(and", generate_color_position(ans_list))

	#Black boxes
	#Number
	os.system("mpg123 number_black.mp3")
	ans = raw_input("How many? ")
	place_in_file(FILE_PROBLEM, "(:objects", generate_boxes(ans))
	place_in_file(FILE_PROBLEM, "(dropped red_box", generate_black_boxes(ans))
	domain_string = generate_domain(ans)
	place_in_file(FILE_DOMAIN, ":precondition (and(or(not(at green_box ?from))(not(at grey_box ?from)))(or(not(at red_box ?from))(not(at grey_box ?from)))(atrobot ?from) ", domain_string)
	place_in_file(FILE_DOMAIN, ":precondition (and (at ?what ?from)(atrobot ?from)", domain_string)

	#Start
	num_black_boxes = int(ans)
	ans_list = []
	for i in range(1, num_black_boxes + 1):
		os.system("mpg123 place_black.mp3")
		ans = raw_input("Where? ")
		ans_list.append(ans)
	place_in_file(FILE_PROBLEM, "(grey grey_box)", generate_black_position(ans_list))

	#Goal
	ans_list = []
	for i in range(1, num_black_boxes + 1):
		os.system("mpg123 goal_black.mp3")
		ans = raw_input("Where? ")
		ans_list.append(ans)
	place_in_file(FILE_PROBLEM, "(and", generate_black_position(ans_list))

	#Create plan
	os.system("mpg123 generating_plan.mp3")
	os.system("./plan " + FILE_DOMAIN + " " + FILE_PROBLEM + "output.pddl")
	time.sleep(10) #This isn't cheating, is it?
	os.system("mpg123 plan_complete.mp3") #Add something about picking best plan etc?
	time.sleep(1)

if __name__ == '__main__':
    try:
        make_plan()
        execute("waypoint" + robot_placement)
    except rospy.ROSInterruptException:
        pass


