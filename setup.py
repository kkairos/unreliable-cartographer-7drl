from cx_Freeze import setup, Executable

import tcod, tcod.event
import entity as ec
import render as re
import constants as cx
import map
import menu

base = None

executables = [Executable("main.py",base=base)]

packages = [
	"idna",
	"tcod",
	"tcod.event",
	"copy",
	"random"
	]
options = {
	'build_exe': {
		'packages':packages
		}
	}
	
setup(
	name = "Dan Rogue",
	options = options,
	version = 'alpha 1',
	description = 'not great yet',
	executables = executables
)