import tcod
import tcod.event as tcv
import constants

# Movement
def draw_all(map,map_console,entities,fov):
	for y in constants.DrawOrder:
		for x in entities:
			if fov[x.x][x.y] == True:
				if x.draw_order == y:
					draw_e(map_console,x)
			elif (map.t_[x.x][x.y].explored == True and (x.draw_order == constants.DrawOrder.FLOOR)):
				draw_e(map_console,x,True)
	
def clear_all(map_console,entities):
	for x in entities:
		clear_e(map_console,x)

def draw_s(menu_console,menu_selection):
	tcod.console_set_default_foreground(menu_console, constants.COLORS[14])
	menu_console.put_char(2, constants.SETTINGS[menu_selection]["yval"], 16, tcod.BKGND_DEFAULT)

def clear_s(menu_console,menu_selection):
	menu_console.put_char(2, constants.SETTINGS[menu_selection]["yval"], ord(" "), tcod.BKGND_DEFAULT)

def draw_e(map_console,x,out_of_sight=False):
	if out_of_sight:
		tcod.console_set_default_foreground(map_console,constants.COLORS[8])
	else:
		tcod.console_set_default_foreground(map_console,constants.COLORS[x.fg])
	map_console.put_char(x.x, x.y, x.char, x.bg)
	
def clear_e(map_console,x):
	map_console.put_char(x.x, x.y, ord(" "), tcod.BKGND_DEFAULT)

def draw_map(map,map_console,fov):
	map.walls_and_pits()
	for y in range(map_console.height):
		for x in range(map_console.width):
			if fov[x][y] == True:
				tcod.console_set_default_foreground(map_console,map.t_[x][y].fg)
				tcod.console_set_default_background(map_console,map.t_[x][y].bg)
				map_console.put_char(x, y, map.t_[x][y].char, tcod.BKGND_DEFAULT)
				map_console.bg[x,y] = map.t_[x][y].bg
				map_console.fg[x,y] = map.t_[x][y].fg
			elif (fov[x][y] == False) and map.t_[x][y].explored == True:
				map_console.put_char(x, y, map.t_[x][y].char, tcod.BKGND_DEFAULT)
				map_console.bg[x,y] = (map.t_[x][y].bg[0]*.4,map.t_[x][y].bg[1]*.4,map.t_[x][y].bg[2]*.4)
				map_console.fg[x,y] = (map.t_[x][y].fg[0]*.4,map.t_[x][y].fg[1]*.4,map.t_[x][y].fg[2]*.4)
				
def draw_con(main_console,map_console,xpos,ypos):
	map_console.blit(
		main_console,
		xpos,ypos, #dest
		0,0, #src
		map_console.width,map_console.height, #w&h
		1.0,1.0, #fg,bg alpha
		None
		)
		
def console_borders(z,x0,y0,x1,y1):
	for x in range(x0+1,x1):
		z.put_char(x, y0, constants.LINES["top-bottom"], tcod.BKGND_DEFAULT)
		z.put_char(x, y1, constants.LINES["top-bottom"], tcod.BKGND_DEFAULT)
	for y in range(y0+1,y1):
		z.put_char(x0, y, constants.LINES["left-right"], tcod.BKGND_DEFAULT)
		z.put_char(x1, y, constants.LINES["left-right"], tcod.BKGND_DEFAULT)
	z.put_char(x0, y0, constants.LINES["top-left"], tcod.BKGND_DEFAULT)
	z.put_char(x1, y0, constants.LINES["top-right"], tcod.BKGND_DEFAULT)
	z.put_char(x0, y1, constants.LINES["bottom-left"], tcod.BKGND_DEFAULT)
	z.put_char(x1, y1, constants.LINES["bottom-right"], tcod.BKGND_DEFAULT)
	return

def messageprint(z,s,m):
	z.clear(32,constants.COLORS[15],constants.COLORS[0])
	m.append(s)
	for x in range(0,z.height):
		if m[len(m)-1-x] != "":
			z.print(0,z.height-1-x,"> " + m[len(m)-1-x],constants.COLORS[15],constants.COLORS[0],tcod.BKGND_DEFAULT,tcod.LEFT)
	print(s)

#message construction for basic actions

def construct_message(
	self,		#entity acting
	other,		#entity acted on
	verb_2p,	#2nd-person verb (w/ spaces)
	verb_3p,	#3rd-person verb (w/ spaces)
	act_ext="", #extended description e.g. "for 10 [damage/healing/etc]"
	val_ins=0,	#value to insert e.g. the 10
	unit="",	#unit for value (e.g. "HP" for healing)
	s_end=".",	#ends sentence
	shortmsg=False
	):

	if (self == other and self == "You"):
		return ""

	if self.dispname == "You":
		msg = "You" + verb_2p
	else:
		if self.dispname == "":
			msg = "The " + self.faction.name + verb_3p
		else:
			msg = self.dispname + verb_3p
	if shortmsg == False:
		if other.dispname =="":
			msg += "the " + self.faction.name
		else:
			msg += other.dispname
		if act_ext != "":
			msg += act_ext + str(val_ins) + unit
	msg +=s_end
	return msg