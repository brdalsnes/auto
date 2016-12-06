(define 
	(problem boxes_problem)
	(:domain boxes_domain)
	(:objects 
 
		#Insert waypoints in this line in the format        waypoint1 waypoint2 ... waypoint4 - waypoint
		#Insert boxes in this line in the format            green_box red_box grey_box black_box1 black_box2 ecc. - box
		rob - robot
	)
	
	(:init
		#Insert in this line the robot position in this format (atrobot waypoint#)
		(red red_box)
		(green green_box)
		(grey grey_box)	
		#Insert in this line the main boxes position in this format (at green_box waypoint#)(at red_box waypoint#)(at grey_box waypoint#)
		#Insert in this line the black boxes initial position in the same format of line above
		(dropped green_box)
		(dropped grey_box)
		(dropped red_box)
		#Insert in this line a string with this format (dropped black_box1)(dropped black_box2)ecc.
		#Insert in this line a string with this format (black black_box1)(black black_box2)ecc.
	)
	
	(:goal
		(and
		(atrobot waypoint2)
		#Insert in this line the main boxes final position in this format (at green_box waypoint#)(at red_box waypoint#)(at grey_box waypoint#)
		#Insert in this line the black boxes final position in the same format of the line above
		)	
	)
)


