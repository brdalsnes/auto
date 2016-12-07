#!/usr/bin/env python
import sys
import os
import rospy
from pddl_reader import get_commands
from get_speech import get_speech
from std_msgs.msg import String
#from move_to_goal import move_to_goal

waypoint1 = (0, 10) #Example coords
waypoint2 = (20, 30)

waypoints = {'wp1' : (0,0), 'wp2' : (0,0), 'wp3' : (0,0), 'wp4' : (0,0)}
def talker():
    rospy.init_node('talker', anonymous=True)

    #Get commands from input
    all_commands = get_commands(str(sys.argv[1]))

    #Sound test
    os.system("mpg123 initialize.mp3")

    for command in all_commands:
        first_command = command.split()
        command_words = first_command[0].split('_')


        if command_words[0] == 'move':
            if command_words[2].endswith('1'):
                #move_to_goal(waypoint1[0], waypoint11], 'waypoint1')
                rospy.loginfo('waypoint1') #remove
            elif command_words[2].endswith('2'):
                #move_to_goal(waypoint2[0], waypoint2[1], 'waypoint2')
                rospy.loginfo('waypoint2') #remove
        else:
            if command_words[0] == 'pick':
                text = "Could you please pick up the " + command_words[1] + " box and put it on top of me?"
            elif command_words[0] == 'drop':
                text = "Could you please put the " + command_words[1] + " box down on the floor?"

            rospy.loginfo(text)

            speech_string = ""
            while speech_string != "yes":
                speech_string = get_speech()
                rospy.loginfo("You said: " + speech_string)

    os.system("mpg123 task_complete.mp3")
    rospy.loginfo('Task complete!\n')

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass