import tcod, tcod.event
import render as re
from controls import key_input
import constants as cx
import drawval
import map as mp

def menu_print(menu_console):

	menu_console.print(menu_console.width//2,1,"M A I N  M E N U",drawval.COLORS[15],drawval.COLORS[0],tcod.BKGND_DEFAULT,tcod.CENTER)
	
	for x in cx.SETTINGS:
		menu_console.print(4,x.get("yval"),x.get("name"),drawval.COLORS[15],drawval.COLORS[0],tcod.BKGND_DEFAULT,tcod.LEFT)
		if x.get("desc") != "NO_SEL":			
			y = cx.DESC[x.get("desc")]
			menu_console.print(4,x.get("yval")+1,y[x.get("sel")],drawval.COLORS[7],drawval.COLORS[0],tcod.BKGND_DEFAULT,tcod.LEFT)
	return

def menu(target_console,menu_console):

	menu_selection = 0
	while True:
		menu_print(menu_console)
		re.draw_s(menu_console,menu_selection)
		re.draw_con(target_console,menu_console,(target_console.width-menu_console.width)//2,(target_console.height-menu_console.height)//2-1)
		tcod.console_flush()
		re.clear_s(menu_console,menu_selection)
		for event in tcod.event.wait():
			if event.type == "KEYDOWN":
				action = key_input(event.sym)
				move = False
				exit = False
				pause = False
				pause = action.get('pause')
				exit = action.get('exit')
				move = action.get('move')
				if move:
					dx,dy = move
					if dx == 0:
						menu_selection = (menu_selection + dy) % len(cx.SETTINGS)
					tmp_sel = [cx.SETTINGS[1]["sel"]]
					if (dy == 0 and cx.SETTINGS[menu_selection]["sel"] != "NO_SEL"):
						cx.SETTINGS[menu_selection]["sel"] = (cx.SETTINGS[menu_selection]["sel"] + dx) % len(cx.DESC[cx.SETTINGS[menu_selection]["desc"]])
					if [cx.SETTINGS[1]["sel"]] != tmp_sel:
						temp_console = []
						for x_store in range(0,target_console.width):
							temp_console.append([])
							for y_store in range(0,target_console.height):
								temp_console[x_store].append([
								target_console.ch[x_store][y_store],
								(target_console.fg[x_store][y_store][0],target_console.fg[x_store][y_store][1],target_console.fg[x_store][y_store][2]),
								(target_console.bg[x_store][y_store][0],target_console.bg[x_store][y_store][1],target_console.bg[x_store][y_store][2])
								])
						tcod.console_set_custom_font(cx.FONT_FILE[cx.SETTINGS[1]["sel"]],tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_ASCII_INROW,32,16)
						target_console = tcod.console_init_root(target_console.width, target_console.height, "D@N ROGUE", False, 3, "F", True)
						for y_store in range(0,target_console.height):
							for x_store in range(0,target_console.width):
								target_console.ch[x_store][y_store] = temp_console[x_store][y_store][0]
								target_console.fg[x_store][y_store] = temp_console[x_store][y_store][1]
								target_console.bg[x_store][y_store] = temp_console[x_store][y_store][2]
				if exit or pause:
					return