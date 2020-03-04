import constants
from random import randint
import copy
import drawval

class Tile:

	def __init__(self,block_m,block_s,char,fg,bg,type,falloff_exp):
		self.block_m = block_m
		if block_s is None:
			block_s = block_m
		self.block_s = block_s
		self.char = char
		self.fg = drawval.COLORS[fg]
		self.bg = drawval.COLORS[bg]
		self.explored = False
		self.type = type
		self.falloff_exp = falloff_exp

def newtile(terrain):
	return Tile(
		terrain["block_m"],
		terrain["block_s"],
		terrain["char"],
		terrain["fg"],
		terrain["bg"],
		terrain["type"],
		terrain["falloff-exp"]
		)

class Map:

	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.t_ = self.t_init()
		
	def t_init(self):
		tiles = [[newtile(constants.TERRAIN["wall"]) for y in range(self.height)] for x in range(self.width)]

		map_debug = 0
		
		for y in range(self.height):
			for x in range(self.width):
				tiles[x][y] = newtile(constants.TERRAIN["floor"])

		for y in range(self.height):
			for x in range(self.width):
				if y==1 or x==1 or (y==self.height-2) or (x==self.width-2):
					tiles[x][y] = newtile(constants.TERRAIN["wall"])
				if y==0 or x==0 or (y==self.height-1) or (x==self.width-1):
					tiles[x][y] = newtile(constants.TERRAIN["solidwall"])

		if map_debug == 1:
			for y in range(self.height):
				for x in range(self.width):
					tiles[x][y].explored = True
		return tiles

	def walls_around(self,x,y):
		for z in range(0,9):
			x2 = (x-1)+(z%3)
			y2 = (y-1)+(z//3)
			if x2 > -1 and x2 < self.width and y2 > -1 and y2 < self.height:
				if self.t_[x2][y2].type != "wall" and self.t_[x2][y2].type != "solidwall":
					return
		self.t_[x][y] = newtile(constants.TERRAIN["solidwall"])
		
	def walls_and_pits(self):
	
		for y in range(self.height):
			for x in range(self.width):
				if self.t_[x][y].type == "wall":
					self.walls_around(x,y)
	
		for y in range(self.height):
			for x in range(self.width):
				if self.t_[x][y].type == "wall":
					z_tmp = 0
					z_tmp += self.char_update_val(x,y-1,1,"wall")
					z_tmp += self.char_update_val(x,y+1,2,"wall")
					z_tmp += self.char_update_val(x+1,y,4,"wall")
					z_tmp += self.char_update_val(x-1,y,8,"wall")
					self.t_[x][y].char = constants.walldraw[z_tmp]
				if self.t_[x][y].type == "pit":
					z_tmp = 0
					z_tmp += self.char_update_val(x,y-1,1,"pit")
					z_tmp += self.char_update_val(x-1,y,2,"pit")
					if z_tmp == 0:
						z_tmp += self.char_update_val(x-1,y-1,4,"pit")
					self.t_[x][y].char = constants.pitdraw[z_tmp]

	def char_update_val(self,x,y,v,type):
		if ((x < 0) or (x > (self.width -1))):
			return 0
		elif ((y < 0) or (y > (self.height -1))):
			return 0
		else:
			if ((type == "pit") and (self.t_[x][y].type != type)):
				return v
			elif ((type != "pit") and (self.t_[x][y].type == type)):
				return v
			else:
				return 0

	def line_from(self,x0,x1,y0,y1,line_type):
		if x0 == x1:
			self.line_v(y0,y1,x0,line_type)
		elif y0 == y1:
			self.line_h(x0,x1,y0,line_type)

	def line_h(self,x0,x1,y,line_type):
		for x in range(x0,x1+1):
			self.t_[x][y] = newtile(constants.TERRAIN[line_type])
			
	def line_v(self,y0,y1,x,line_type):
		for y in range(y0,y1+1):
			self.t_[x][y] = newtile(constants.TERRAIN[line_type])

	def draw_square(self,x0,y0,w,h,line_type="wall",fill_type=""):
		if fill_type != "":
			for x in range(x0,x0+w+1):
				self.line_from(x,x,y0,y0+h,fill_type)
		self.line_from(x0,x0+w,y0,y0,line_type)
		self.line_from(x0,x0+w,y0+h,y0+h,line_type)
		self.line_from(x0,x0,y0,y0+h,line_type)
		self.line_from(x0+w,x0+w,y0,y0+h,line_type)

	def draw_house(self,hx,hy,hw,hh):
		
		self.draw_square(hx,hy,hw,hh,"wall","wall")

def rand_square(x0,x1,y0,y1,w0,w1,h0,h1):

	rand_s_x, rand_s_y = randint(x0,x1), randint(y0,y1)
	rand_s_w, rand_s_h = randint(w0,w1), randint(h0,h1)
	
	return rand_s_x, rand_s_y, rand_s_w, rand_s_h
	
def make_map(map):
	x0,x1 = 5, 5
	y0,y1 = 7, 7
	w0,w1 = 5, 7
	h0,h1 = 5, 7
	#rand_s_x, rand_s_y, rand_s_w, rand_s_h = rand_square(x0,x1,y0,y1,w0,w1,h0,h1)
	#map.draw_house(rand_s_x, rand_s_y, rand_s_w, rand_s_h)
	
	xw = 4
	rw = 6
	xh = 4
	rh = 6
	for y in range(rh+2,map.height-rh,xh+rh):
		for x in range(rw+2,map.width-rw,xw+rw):
			map.draw_square(x,y,xw-1,xh-1,"wall","wall")
			zrand = randint(0,3)
			zh = 6
			zw = 6
			map.draw_square(x-rw,y,rw-1,xh-1,"wall","wall")
			map.draw_square(x+xw,y,rw-1,xh-1,"wall","wall")
			map.draw_square(x,y-rh,xw-1,rh-1,"wall","wall")
			map.draw_square(x,y+xh,xw-1,rh-1,"wall","wall")
			if zrand != 0: #right
				zzrand = randint(x+xw+1,x+xw+rw-3)
				map.line_from(zzrand,zzrand,y,y+xh,"floor")
			if zrand != 1: #left
				zzrand = randint(x-rw+1,x-2)
				map.line_from(zzrand,zzrand,y,y+xh,"floor")
			if zrand != 2: #up
				zzrand = randint(y-rh+1,y-2)
				map.line_from(x,x+xw,zzrand,zzrand,"floor")
			if zrand != 3: #down
				zzrand = randint(y+xh+1,y+xh+rh-3)
				map.line_from(x,x+xw,zzrand,zzrand,"floor")

	for y in range(2,map.height-rh,xh+rh):
		for x in range(2,map.width-rw,xw+rw):
			zzrand = randint(0,8)
			if (zzrand % 3) == 1:
				map.t_[x][y] = newtile(constants.TERRAIN["wall"])
				map.t_[x+5][y] = newtile(constants.TERRAIN["wall"])
				map.t_[x][y+5] = newtile(constants.TERRAIN["wall"])
				map.t_[x+5][y+5] = newtile(constants.TERRAIN["wall"])
			if zzrand == 1:
				map.draw_square(x+1,y+1,3,3,"pit","wall")
			if zzrand == 2:
				map.draw_square(x+1,y+1,3,3,"pit","wall")
			if zzrand == 3:
				map.draw_square(x+2,y+2,1,1,"wall","solidwall")
			if zzrand == 4:
				map.draw_square(x+1,y+1,3,3,"pit","pit")
			if zzrand == 5:
				map.draw_square(x+1,y+1,3,3,"wall","floor")
			if zzrand == 6:
				for c in range(0,8):
					zrand2 = randint(1,4)
					zrand3= randint(1,4)
					map.t_[x+zrand2][y+zrand3] = newtile(constants.TERRAIN["pit"])
			if zzrand == 7:
				for c in range(0,8):
					zrand2 = randint(1,4)
					zrand3= randint(1,4)
					map.t_[x+zrand2][y+zrand3] = newtile(constants.TERRAIN["wall"])
			if zzrand == 8:
				for c in range(0,8):
					zrand2 = randint(1,4)
					zrand3 = randint(1,4)
					zrand4 = randint(0,1)
					if zrand4 == 0:
						map.t_[x+zrand2][y+zrand3] = newtile(constants.TERRAIN["wall"])
					else:
						map.t_[x+zrand2][y+zrand3] = newtile(constants.TERRAIN["pit"])

	map.walls_and_pits()
	
	return