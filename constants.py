from enum import Enum
import math

class Faction(Enum):
	Ally = 0
	Enemy = 1

class DrawOrder(Enum):
	FLOOR = 0
	NPC = 1
	PLAYER = 2

THETAS = []

for theta in range(1080):
	theta = math.radians(float(theta/3))
	xd_d = float(math.cos(theta))
	yd_d = float(math.sin(theta))
	THETAS.append((xd_d,yd_d))
		
LINES = {
	"top-left" : 201,
	"bottom-right" : 188,
	"top-right" : 187,
	"left-right" : 186,
	"bottom-left" : 200,
	"top-bottom" : 205
	}

SETTINGS = [
	{
		"name" : "Control Scheme",
		"yval" : 3,
		"sel" : 0,
		"desc" : "INPUT_SEL"
	},
	{
		"name" : "Font",
		"yval" : 12,
		"sel" : 0,
		"desc" : "FONT_SEL"
	},
	{
		"name" : "Continue Playing [Esc]",
		"yval" : 15,
		"sel" : 0,
		"desc" : "NO_SEL"
	},
	{
		"name" : "Save and Quit",
		"yval" : 17,
		"sel" : 0,
		"desc" : "NO_SEL"
	}
	]

DESC = {
	"INPUT_SEL" : [
	"\nMOVE:     REST: 5,. \n"\
	"7 8 9               \n"\
	" \|/                \n"\
	"4-@-6               \n"\
	" /|\                \n"\
	"1 2 3               ",
	"\nMOVE:     REST: S,. \n"\
	"Q W E               \n"\
	" \|/                \n"\
	"A-@-D               \n"\
	" /|\                \n"\
	"Z X C               ",
	"\nMOVE:     REST: .   \n"\
	"Y K U               \n"\
	" \|/                \n"\
	"H-@-L               \n"\
	" /|\                \n"\
	"B J N               "
	],
	"FONT_SEL" : [
	"16x16 Stable         ",
	"16x16 Working Set    ",
	"16x16 \"Alpha\"        ",
	],
	"NO_SEL" : []
}

walldraw = []
for x in range(0,16):
	walldraw.append(x+256)
	
pitdraw = []
for x in range(0,5):
	pitdraw.append(x+288)

FONT_FILE = [
	"uc-tiles-16x16-stable.png",
	"uc-tiles-16x16-working.png",
	"uc-tiles-16x16-alpha.png",
	]

TERRAIN = {
	"wall": {
		"block_m" : True,
		"block_s" : True,
		"char" : 178,
		"fg" : "wall-fg",
		"bg" : "wall-bg",
		"type" : "wall",
		"falloff-exp" : float(2.0)
		},
	"solidwall": {
		"block_m" : True,
		"block_s" : True,
		"char" : 178,
		"fg" : "wall-fg",
		"bg" : "wall-bg",
		"type" : "solidwall",
		"falloff-exp" : float(2.0)
		},
	"floor" : {
		"block_m" : False,
		"block_s" : False,
		"char" : 273,
		"fg" : "floor-fg",
		"bg" : "floor-bg",
		"type" : "floor",
		"falloff-exp" : float(2.0)
		},
	"pit" : {
		"block_m" : True,
		"block_s" : False,
		"char" : 352,
		"fg" : "pit-fg",
		"bg" : "pit-bg",
		"type" : "pit",
		"falloff-exp" : float(1.25)
		},
	"nav" : {
		"block_m" : False,
		"block_s" : False,
		"char" : ord(" "),
		"fg" : "black",
		"bg" : "black",
		"type" : "nav",
		"falloff-exp" : float(1.0)
		},
	}