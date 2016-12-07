import sys
import os
import rospy
from pddl_reader import get_commands
from get_speech import get_speech
from std_msgs.msg import String
#from move_to_goal import move_to_goal


waypoints = {'waypoint1' : (0,0), 'waypoint2' : (0,0), 'waypoint3' : (0,0), 'waypoint4' : (0,0)}
sounds = {  'pick_green_box' : 'file',
			'pick_red_box' : 'file',
			'pick_grey_box' : 'file',
			'pick_black_box' : 'file',
			'drop_green_box' : 'file',
			'drop_red_box' : 'file',
			'drop_grey_box' : 'file',
			'drop_black_box' : 'file',		
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


def execute():
    rospy.init_node('talker', anonymous=True)

    #Get commands from input
    best_plan = pick_best_plan()
    all_commands = get_commands(best_plan)

    #Sound test
    os.system("mpg123 initialize.mp3")

    for commad in all_commands:
    	command_words = commad.split()

    	if command_words[0] == 'move' or command_words[0] == 'move_empty':
    		print('move')
    		#move_to_goal(waypoints[command_words[2]][0], waypoints[command_words[2]][1], command_words[2])

    	else:
    		sound_file = command_words[0] + "_" + command_words[1]
    		if command_words[1].startswith('b'): #Black box corner case
    			sound_file = sound_file[:-1]

    		os.system("mpg123 " + sounds[sound_file])

    	raw_input = "" #Temp, replace with speech

    os.system("mpg123 task_complete.mp3")
    rospy.loginfo('Task complete!\n')

