import constants as cx
import render as re
import math

class Entity:

	def __init__(self,
			x,y,
			char_input = 2,
			fg = 15,bg = 0,
			hp = 10,speed = 10,
			faction = cx.Faction.Enemy,
			draw_order = cx.DrawOrder.NPC,
			block_m = True,
			dispname = ""):
		self.x = x
		self.y = y
		self.char = char_input
		self.fg = fg
		self.bg = bg
		self.stats = Stats(hp,speed)
		self.block_m = block_m
		self.block_s = False
		self.faction = faction
		self.dispname = dispname
		self.draw_order = draw_order
		self.sightrange = 10

	def move(self,dx,dy,map,entities,message_console,messages):
		if (self.x+dx > -1 and self.x+dx < map.width and self.y+dy > -1 and self.y+dy < map.height):
			
			target_entity = blocking_entity(entities,self.x+dx,self.y+dy)
			if target_entity is not None:
				if target_entity.faction == self.faction:
					self.talk(target_entity,message_console,messages)
				elif target_entity.faction != self.faction:
					self.attack(target_entity,message_console,messages)
			elif map.t_[self.x+dx][self.y+dy].block_m:
				re.messageprint(message_console,"You're blocked in that direction!",messages)
			else:
				self.x+=dx
				self.y+=dy

	def talk(self,other,message_console,messages):

		message = re.construct_message(self,other," talk to ", " talks to ")
		if message != "":
			re.messageprint(message_console,message,messages)
	
	def attack(self,other,message_console,messages):
	
		damage = self.stats.at - other.stats.df
		message = re.construct_message(self,other," attack ", " attacks "," for ",damage," HP")
		other.stats.hp -= damage
		if other.stats.hp < 1:
			message += " " + re.construct_message(other,other," die"," dies","",0,"","!",True)
			other.block_m = False
			other.char = ord("%")
			other.draw_order = cx.DrawOrder.FLOOR
		if message != "":
			re.messageprint(message_console,message,messages)
	
	def fov(self,map,entities):
	
		#fov = [[False for y in range(map.height)] for x in range(map.width)]
		fov = [[float(0.0) for y in range(map.height)] for x in range(map.width)]
		eblock = [[False for y in range(map.height)] for x in range(map.width)]
		
		for y in range(map.height):
			for x in range(map.width):
				fov[x][y] = False
				eblock[x][y] = False

		radius = self.sightrange
		
		for en in entities:
			if (en.block_s == True) and (e != self):
				eblock[en.x][en.y] = True

		for theta in range(len(cx.THETAS)):
			
			xd_i = float(self.x+0.5)
			yd_i = float(self.y+0.5)
			xd_d,yd_d = cx.THETAS[theta]
			fov[self.x][self.y] = 1
			map.t_[self.x][self.y].explored = True

			for r in range(radius):
				xd_i+=xd_d
				yd_i+=yd_d
				if (int(xd_i) < 0) or (int(yd_i) < 0) or (int(xd_i) > map.width-1) or (int(yd_i) > map.height-1):
					break
				if r == 0 or ((int(xd_i) == self.x) and (int(yd_i) == self.y)):
					fov[int(xd_i)][int(yd_i)] = float(1.0)
				else:
					falloff_mod = map.t_[int(xd_i)][int(yd_i)].falloff_exp
					fov[int(xd_i)][int(yd_i)] = float(-1.4*math.atan((r-2)/2)/math.pi+0.6)
				map.t_[int(xd_i)][int(yd_i)].explored = True
				if (map.t_[int(xd_i)][int(yd_i)].block_s == True) or (eblock[int(xd_i)][int(yd_i)] == True):
					break
		return fov
	
def blocking_entity(entities,x,y):
	for entity in entities:
		if ((entity.x == x) and (entity.y == y) and entity.block_m):
			return entity
	return None

class Stats:

	def __init__(self,hp,speed, at=3, df=0):
		self.hp = hp
		self.max_hp = hp
		self.speed = speed
		self.at = at
		self.df = df