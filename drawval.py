from enum import Enum
import math

class Faction(Enum):
	Ally = 0
	Enemy = 1

class DrawOrder(Enum):
	FLOOR = 0
	NPC = 1
	PLAYER = 2

COLOR_BOOST = {
	#"warm" : [1.85, 1.35,1.00],	# multipliers for warm colors in r,g,b format
	#"cool" : [0.90,0.80,2],	# multipliers for cool colors in r,g,b format
	#"cool_darken" : 0.25		# multiplier to darken cool colors
    "warm" : [1.85, 1.35,1.00],	# multipliers for warm colors in r,g,b format
	"cool" : [0.60,0.70,1.8],	# multipliers for cool colors in r,g,b format
	"cool_darken" : 0.25		# multiplier to darken cool colors
	}

COLORS = {
	"wall-fg" : (180,140,120),
	"wall-bg" : (50,50,50),
	"floor-fg" : (42,42,42),
	"floor-bg" : (50,50,50),
	"pit-fg" : (42,42,42),
	"pit-bg" : (0,0,0),
	"black" : (0,0,0),
	15 : (255,255,255),
	14 : (255,255,84),
	13 : (255,84,255),
	12 : (255,84,84),
	11 : (84,255,255),
	10 : (84,255,84),
	9 : (84,84,255),
	8 : (84,84,84),
	7 : (168,168,168),

	"tilegrey" : (50,50,50),
	6 : (168,84,0),
	5 : (168,0,168),
	4 : (168,0,0),
	3 : (0,168,168),
	2 : (0,168,0),
	1 : (0,0,168),
	0 : (0,0,0),
	
	"darkgrey" : (42,42,42),
	
	-1 : (2,2,2)
	}
	
LINES = {
	"top-left" : 201,
	"bottom-right" : 188,
	"top-right" : 187,
	"left-right" : 186,
	"bottom-left" : 200,
	"top-bottom" : 205
	}

CHARS  ={
	"person" : 272
	}