(define 
	(domain boxes_domain)

	(:requirements :strips :adl)

	(:types waypoint - object
		box - object
		robot - object	
	)
	
	(:predicates
		(at ?what - box ?where - waypoint)
		(atrobot ?where - waypoint)
		(intrans ?what - box)
		(green ?what - box)
		(red ?what - box)
		(grey ?what - box)
		(black ?what - box)
		(dropped ?what - box)
	)
	
	(:action move_empty
		:parameters (?from ?to - waypoint)
		:precondition (and(or(not(at green_box ?from))(not(at grey_box ?from)))(or(not(at red_box ?from))(not(at grey_box ?from)))(atrobot ?from) 
(not(intrans green_box))(not(intrans red_box))(not(intrans grey_box)))
		:effect (and(atrobot ?to)(not(atrobot ?from)))
	)
	
	(:action move
		:parameters (?what - box ?from ?to - waypoint)
		:precondition (and(intrans ?what)(atrobot ?from)(dropped ?what))
		:effect (and(atrobot ?to)(not(atrobot ?from))(not(dropped ?what)))
	
	)
	
	(:action pick
		:parameters (?what - box ?from - waypoint)
		:precondition (and (at ?what ?from)(atrobot ?from)
(not(intrans green_box))(not(intrans red_box))(not(intrans grey_box)))
		:effect (and 
		
				(when(and(green ?what)(or(not(at red_box ?from))(not(at grey_box ?from))))
				(and(intrans ?what)(not(at ?what ?from)))
				)
				
				(when(and(red ?what)(or(not(at green_box ?from))(not(at grey_box ?from))))
				(and(intrans ?what)(not(at ?what ?from)))
				)
				
				(when(and(grey ?what))
				(and(intrans ?what)(not(at ?what ?from)))
				)

				(when(and(black ?what)(or(not(at red_box ?from))(not(at grey_box ?from)))(or(not(at green_box ?from))(not(at grey_box ?from))))
				(and(intrans ?what)(not(at ?what ?from)))
				)
				
			)
	)

	(:action drop
		:parameters (?what - box ?to - waypoint)
		:precondition (and (intrans ?what)(atrobot ?to))
		:effect (and (at ?what ?to)(not(intrans ?what))(dropped ?what))
	)
	
)
