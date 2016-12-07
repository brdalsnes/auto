import sys
import os
import rospy
from pddl_reader import get_commands
from get_speech import get_speech
from std_msgs.msg import String
#from move_to_goal import move_to_goal


waypoints = {'waypoint1' : (0,0),
			 'waypoint2' : (0,0),
			 'waypoint3' : (0,0),
			 'waypoint4' : (0,0)
			 }
sounds = {  'pick_green_box' : 'pick_green.mp3',
			'pick_red_box' : 'pick_red.mp3',
			'pick_grey_box' : 'pick_grey.mp3',
			'pick_black_box' : 'pick_black.mp3',
			'drop_green_box' : 'drop_green.mp3',
			'drop_red_box' : 'drop_red.mp3',
			'drop_grey_box' : 'drop_grey.mp3',
			'drop_black_box' : 'drop_black.mp3',		
		}

def pick_best_plan():
	output_files = []

	for filename in os.listdir('/home/brd/AS/auto'): #Path to dir
		if filename.startswith('output.pddl'):
			output_files.append(filename)

	for filename in output_files:
		min_len = 999
		file_len = get_file_len(filename)
		if file_len < min_len:
			min_len = file_len
			min_file = filename

	return min_file


def get_file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def execute(robot_placement):
    rospy.init_node('talker', anonymous=True)

    #Get commands from input
    best_plan = pick_best_plan()
    all_commands = get_commands(best_plan)

    #Initialize
    os.system("mpg123 initialize.mp3")
    #move_to_goal(waypoints[robot_placement][0], waypoints[robot_placement][1])

    for commad in all_commands:
    	command_words = commad.split()

    	if command_words[0] == 'move' or command_words[0] == 'move_empty':
    		print('move') #Remove
    		#move_to_goal(waypoints[command_words[2]][0], waypoints[command_words[2]][1], command_words[2])

    	else:
    		sound_file = command_words[0] + "_" + command_words[1]
    		if command_words[1].startswith('b'): #Black box corner case
    			sound_file = sound_file[:-1]

    		os.system("mpg123 " + sounds[sound_file])

    	raw_input("") #Temp, replace with speech

    os.system("mpg123 task_complete.mp3")
    rospy.loginfo('Task complete!\n')

