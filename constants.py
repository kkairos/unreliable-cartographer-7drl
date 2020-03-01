from enum import Enum

class Faction(Enum):
	Ally = 0
	Enemy = 1

class DrawOrder(Enum):
	FLOOR = 0
	NPC = 1
	PLAYER = 2

COLORS = {
	15 : (255,255,255),
	14 : (255,255,84),
	13 : (255,84,255),
	12 : (255,84,84),
	11 : (84,255,255),
	10 : (84,255,84),
	9 : (84,84,255),
	8 : (84,84,84),
	7 : (168,168,168),
	6 : (168,84,0),
	5 : (168,0,168),
	4 : (168,0,0),
	3 : (0,168,168),
	2 : (0,168,0),
	1 : (0,0,168),
	0 : (0,0,0)
	}
	
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
	"Classic 437      ",
	#"Electrum-Thin 437",
	"Narrow 437       ",
	"Bubble 437       "
	],
	"NO_SEL" : []
}

FONT_FILE = [
	"font-8x14-classic.png",
	#"font-8x14-thin.png",
	"font-8x14-narrow.png",
	"font-8x14-bubble.png"
	]

TERRAIN = {
	"wall": {
		"block_m" : True,
		"block_s" : True,
		"char" : 178,
		"fg" : 7,
		"bg" : 0,
		"name" : "wall"
		},
	"floor" : {
		"block_m" : False,
		"block_s" : False,
		"char" : 249,
		"fg" : 7,
		"bg" : 0,
		"name" : "floor"
		},
	"fence" : {
		"block_m" : True,
		"block_s" : False,
		"char" : ord("#"),
		"fg" : 6,
		"bg" : 0,
		"name" : "floor"
		},
	"ground" : {
		"block_m" : False,
		"block_s" : False,
		"char" : ord(","),
		"fg" : 2,
		"bg" : 0,
		"name" : "floor"
		},
	"water" : {
		"block_m" : True,
		"block_s" : False,
		"char" : ord("~"),
		"fg" : 1,
		"bg" : 0,
		"name" : "floor"
		},
	"pit" : {
		"block_m" : True,
		"block_s" : False,
		"char" : ord(":"),
		"fg" : 8,
		"bg" : 0,
		"name" : "floor"
		}
	}