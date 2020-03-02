import tcod, tcod.event
from controls import key_input
import entity as ec
import render as re
import constants as cx
import map
import menu

def main():
	
	screen_width = 80
	screen_height = 45
	map_w = 60
	map_h = 40
	
	level_map = map.Map(map_w,map_h)
	
	map.make_map(level_map)
	
	player = ec.Entity(3,2,cx.CHARS["person"],15,0,10,10,cx.Faction.Ally,cx.DrawOrder.PLAYER,True,"You")
	
	#npc = ec.Entity(int(level_map.width*3/4),int(level_map.height*1/4),cx.CHARS["person"],14,0,10,10,cx.Faction.Ally,cx.DrawOrder.NPC,True,"")

	#ene = ec.Entity(int(level_map.width*4/5),int(level_map.height*3/5),cx.CHARS["person"],10,0,10,10,cx.Faction.Enemy,cx.DrawOrder.NPC,True,"Mortimer")
	
	entities = [player,
	#npc,ene
	]
	
	key = tcod.Key()
	mouse = tcod.Mouse()
	
	tcod.console_set_custom_font(cx.FONT_FILE[cx.SETTINGS[1]["sel"]],
		tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_ASCII_INROW,
		32,16
		)
	main_console = tcod.console_init_root(screen_width, screen_height, "D@N ROGUE", False, 3, "F", True)
	
	map_console = tcod.console.Console(map_w, map_h, "F", None)
	menu_console = tcod.console.Console(30, 19, "F", None)
	
	message_console = tcod.console.Console(map_console.width,main_console.height-map_console.height)
	
	status_console = tcod.console.Console(main_console.width-map_console.width,main_console.height)
	
	messages = []
	for x in range(0,message_console.height):
		messages.append("")
	
	menu.menu_print(menu_console)
	
	re.console_borders(menu_console,0,0,menu_console.width-1,menu_console.height-1)
	
	fg_sh = 15
	bg_sh = 0
	
	while True:
	
		fov = player.fov(level_map,entities)
		re.draw_map(level_map, map_console, fov)
		re.draw_all(level_map,map_console,entities,fov)
		re.draw_con(main_console,map_console,status_console.width,0)
		re.draw_con(main_console,message_console,status_console.width,main_console.height-message_console.height)
		tcod.console_flush()
		re.clear_all(map_console,entities)
		for event in tcod.event.wait():
			if event.type == "KEYDOWN":
				action = key_input(event.sym)
				move = False
				exit = False
				pause = False
				move = action.get('move')
				exit = action.get('exit')
				pause = action.get('pause')
				if move:
					dx,dy = move
					player.move(dx,dy,level_map,entities,message_console,messages)
				if exit:
					return True
				if pause:
					menu.menu(main_console,menu_console)
			elif event.type == "WINDOWCLOSE":
				return True

if __name__ == "__main__":
	main()