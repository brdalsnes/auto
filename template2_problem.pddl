(define 
	(problem boxes_problem)
	(:domain boxes_domain)
	(:objects 

		waypoint1 waypoint2 - waypoint
		rob - robot
	)
	
	(:init

		(atrobot waypoint2)
		(red red_box)
		(green green_box)
		(grey grey_box)	
		(dropped green_box)
		(dropped grey_box)
		(dropped red_box)
	)
	
	(:goal
		(and
		(atrobot waypoint2)
		)	
	)
)

