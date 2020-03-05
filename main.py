import tcod, tcod.event
from controls import key_input
import entity as ec
import render as re
import constants as cx
import drawval
import map
import menu
from time import sleep

def new_level(map_w,map_h,entities):
	level_map = map.Map(map_w,map_h)
	map.make_map(level_map,entities)
	paper_map = map.Map(map_w,map_h)
	#paper_map.t_ = level_map.t_.copy
	for y in range(map_h):
		for x in range(map_w):
			z = level_map.t_[x][y].type
			paper_map.t_[x][y] = map.newtile(cx.TERRAIN[z])
			paper_map.t_[x][y].fg = drawval.COLORS["map-black"]
			paper_map.t_[x][y].bg = drawval.COLORS["map-white"]
			
		#	print(str(level_map.t_[x][y].char)+" " + str(paper_map.t_[x][y].char))
	
	paper_map.walls_and_pits()
			
	for y in range(map_h):
		for x in range(map_w):
			if paper_map.t_[x][y].type == "wall":
				paper_map.t_[x][y].char += 64
			if paper_map.t_[x][y].type == "pit":
				paper_map.t_[x][y].fg = drawval.COLORS["map-black"]
				paper_map.t_[x][y].bg = drawval.COLORS["map-white"]
				paper_map.t_[x][y].char += 64
			if paper_map.t_[x][y].type == "floor":
				paper_map.t_[x][y].char = 32
			if paper_map.t_[x][y].type == "solidwall":
				paper_map.t_[x][y].char = 32
				paper_map.t_[x][y].fg = drawval.COLORS["map-white"]
				paper_map.t_[x][y].bg = drawval.COLORS["map-white"]
			for entity in entities:
				if ((entity.x == x) and (entity.y == y) and entity.istrap):
					paper_map.t_[x][y].char = int(entity.char) + 64
					paper_map.t_[x][y].fg = drawval.COLORS["map-red"]
					paper_map.t_[x][y].type = "trap"
	paper_map.t_[paper_map.width//2][10].char = 338
	paper_map.t_[paper_map.width//2][10].fg = drawval.COLORS["map-red"]	
	paper_map.t_[paper_map.width-4][0].char = 338
	paper_map.t_[paper_map.width-4][0].fg = drawval.COLORS["map-red"]
	paper_map.t_[paper_map.width-3][0].char = 338
	paper_map.t_[paper_map.width-3][0].fg = drawval.COLORS["map-red"]
	paper_map.t_[paper_map.width-2][0].char = 338
	paper_map.t_[paper_map.width-2][0].fg = drawval.COLORS["map-red"]
	paper_map.t_[paper_map.width-1][0].char = 339
	paper_map.t_[paper_map.width-1][0].fg = drawval.COLORS["map-red"]
	
	return level_map, paper_map

def draw_loop(player, level_map, paper_map, map_console, main_console, message_console,status_console,entities):
	fov = player.fov(level_map,entities)
	re.draw_map(level_map, paper_map, map_console, fov)
	re.draw_all(level_map,map_console,entities,fov)
	re.draw_con(main_console,map_console,status_console.width,0)
	re.draw_con(main_console,message_console,status_console.width,main_console.height-message_console.height)
	tcod.console_flush()
	re.clear_all(level_map,map_console,entities)

def main():
	
	screen_width = 80
	screen_height = 45
	map_w = 60
	map_h = 40
	
	map_console_w = 60
	map_console_h = 40
	
	player = ec.Entity(4,2,drawval.CHARS["person"],15,0,10,10,cx.Faction.Ally,cx.DrawOrder.PLAYER,True,"You")
	entities = [player]

	level_map, paper_map = new_level(map_w,map_h,entities)

	player_state = 1	#alive
	key = tcod.Key()
	mouse = tcod.Mouse()
	
	tcod.console_set_custom_font(cx.FONT_FILE[cx.SETTINGS[1]["sel"]],
		tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_ASCII_INROW,
		32,16
		)
	main_console = tcod.console_init_root(screen_width, screen_height, "D@N ROGUE", False, 3, "F", True)
	
	map_console = tcod.console.Console(map_console_w, map_console_h, "F", None)
	menu_console = tcod.console.Console(30, 19, "F", None)
	
	message_console = tcod.console.Console(map_console.width,main_console.height-map_console.height)
	
	status_console = tcod.console.Console(main_console.width-map_console.width,main_console.height)
	
	messages = []
	for x in range(0,message_console.height):
		messages.append("")
	
	welcome_message = "Welcome to Unreliable Cartographer. This is a game about exploring a dungeon with a map of increasingly dubious accuracy and dodging traps along the way. Press [ENTER] to see controls. We hope you like it!"
	re.messageprint(message_console, welcome_message, messages )
	
	menu.menu_print(menu_console)
	
	re.console_borders(menu_console,0,0,menu_console.width-1,menu_console.height-1)
	
	fg_sh = 15
	bg_sh = 0

	fov = player.fov(level_map,entities)
	
	#re.console_borders(map_console,0,0,map_console.width-1,map_console.height-1)
	
#	move = False
#	exit = False
#	pause = action.get('pause')
	jump_trigger = False
	
	re.draw_paper_map(paper_map, map_console)
	
	while True:
	
		draw_loop(player, level_map, paper_map, map_console, main_console, message_console,status_console,entities)
		for event in tcod.event.wait():
			if event.type == "KEYDOWN":
				action = key_input(event.sym)
				
				#pause = False
				move = action.get('move')
				exit = action.get('exit')
				pause = action.get('pause')
				jump = action.get('jump')
				if player_state == 1:
					if move:
						dx,dy = move
						if not jump_trigger:
							player.move(dx,dy,level_map,entities,map_console,message_console,messages)
						elif jump_trigger:
							for z in range(0,2):
								if player.jump(dx,dy,level_map,entities,map_console,message_console,messages) == False:
									break
								else:
									draw_loop(player, level_map, paper_map, map_console, main_console, message_console,status_console,entities)
									sleep(0.0095)
							jump_trigger = False
					if level_map.t_[player.x][player.y].type == "pit":
						fov = player.fov(level_map,entities)
						
						for z in drawval.CHARS["person_fall"]:
							player.char = z
							draw_loop(player, level_map, paper_map, map_console, main_console, message_console,status_console,entities)
							sleep(0.005)
						player_state = 0
						entities.remove(player)
						re.messageprint(message_console,"Oh, dear! You've fallen down a pit!",messages)
					if jump:
						if not jump_trigger:
							re.messageprint(message_console, "Press [DIR] to jump 2 squares away in a direction, any other key to cancel.", messages )
							jump_trigger = True
						elif jump_trigger:		
							re.messageprint(message_console, "Jump cancelled.", messages )
							jump_trigger = False
				if exit:
					return True
				if pause:
					menu.menu(main_console,menu_console)
				
			elif event.type == "WINDOWCLOSE":
				return True

if __name__ == "__main__":
	main()