#!/usr/bin/env python
import sys
import rospy
from pddl_reader import get_commands
from std_msgs.msg import String
import pyttsx
#from move_to_goal import move_to_goal

roomA = (0, 10) #Example coords
roomB = (20, 30)

engine = pyttsx.init()
engine.setProperty('rate', 120)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id) #English

def talker():
    #Get commands from input
    all_commands = get_commands(str(sys.argv[1]))

    #probably remove
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)

    for command in all_commands:
        command_words = command.split()

        if command_words[0] == 'move':
            if command_words[2] == 'rooma':
                #move_to_goal(roomA[0], roomA[1])
                rospy.loginfo('move') #remove
            elif command_words[2] == 'roomb':
                #move_to_goal(roomB[0], roomA[1])
                rospy.loginfo('move') #remove
                
        else:
            text = command_words[0].capitalize() + " " + command_words[1] + ". Press enter when action is complete."
            #Speech
            engine.say(text)
            engine.runAndWait()

            rospy.loginfo(text)
            raw_input('')

    rospy.loginfo('Task complete!\n')

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass