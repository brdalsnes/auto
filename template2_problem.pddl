(define 
	(problem boxes_problem)
	(:domain boxes_domain)
	(:objects 

		green_box red_box grey_box  - box

		waypoint1 waypoint2 - waypoint
		rob - robot
	)
	
	(:init

		(atrobot waypoint1)
		(red red_box)
		(green green_box)
		(grey grey_box)	

		

		(at green_box waypoint1)(at red_box waypoint1)(at grey_box waypoint1)
		(dropped green_box)
		(dropped grey_box)
		(dropped red_box)

		

	)
	
	(:goal
		(and

		

		(at green_box waypoint2)(at red_box waypoint2)(at grey_box waypoint2)
		(atrobot waypoint2)
		)	
	)
)


