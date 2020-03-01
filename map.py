import constants
from random import randint
import copy

class Tile:

	def __init__(self,block_m,block_s=None,char=0,fg=15,bg=0):
		self.block_m = block_m
		if block_s is None:
			block_s = block_m
		self.block_s = block_s
		self.char = char
		self.fg = constants.COLORS[fg]
		self.bg =  constants.COLORS[bg]
		self.explored = False

def newtile(terrain):
	return Tile(
		terrain["block_m"],
		terrain["block_s"],
		terrain["char"],
		terrain["fg"],
		terrain["bg"]
		)

class Map:

	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.t_ = self.t_init()
		
	def t_init(self):
		tiles = [[newtile(constants.TERRAIN["ground"]) for y in range(self.height)] for x in range(self.width)]
		
		for y in range(self.height):
			for x in range(self.width):
				tiles[x][y] = newtile(constants.TERRAIN["ground"])

		for y in range(self.height):
			for x in range(self.width):
				if y==0 or x==0 or (y==self.height-1) or (x==self.width-1):
					tiles[x][y] = newtile(constants.TERRAIN["fence"])
		return tiles

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
		
		self.draw_square(hx,hy,hw,hh,"wall","floor")

def rand_square(x0,x1,y0,y1,w0,w1,h0,h1):

	rand_s_x, rand_s_y = randint(x0,x1), randint(y0,y1)
	rand_s_w, rand_s_h = randint(w0,w1), randint(h0,h1)
	
	return rand_s_x, rand_s_y, rand_s_w, rand_s_h
	
def make_map(map):
	x0,x1 = 5, 5
	y0,y1 = 7, 7
	w0,w1 = 5, 7
	h0,h1 = 5, 7
	rand_s_x, rand_s_y, rand_s_w, rand_s_h = rand_square(x0,x1,y0,y1,w0,w1,h0,h1)
	map.draw_house(rand_s_x, rand_s_y, rand_s_w, rand_s_h)
	
	return