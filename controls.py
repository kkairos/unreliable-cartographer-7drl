import tcod
import tcod.event as tcv
import constants

def key_input(sym):

	#moving
	
	if constants.SETTINGS[0]["sel"] == 0:
	
		if sym == tcv.K_HOME or sym == tcv.K_KP_7:
			return {'move': (-1, -1)}
			
		elif sym == tcv.K_UP or sym == tcv.K_KP_8:
			return {'move': (0, -1)}
		
		elif sym == tcv.K_PAGEUP or sym == tcv.K_KP_9:
			return {'move': (1, -1)}
		
		elif sym == tcv.K_LEFT or sym == tcv.K_KP_4:
			return {'move': (-1, 0)}
		
		elif sym in (tcv.K_PERIOD, tcv.K_KP_PERIOD, tcv.K_KP_5):
			return {'move': (0, 0)}
		
		elif sym == tcv.K_RIGHT or sym == tcv.K_KP_6:
			return {'move': (1, 0)}
		
		elif sym == tcv.K_END or sym == tcv.K_KP_1:
			return {'move': (-1, 1)}
		
		elif sym == tcv.K_DOWN or sym == tcv.K_KP_2:
			return {'move': (0, 1)}
		
		elif sym == tcv.K_PAGEDOWN or sym == tcv.K_KP_3:
			return {'move': (1, 1)}
	
	elif constants.SETTINGS[0]["sel"] == 1:
	
		if sym == tcv.K_HOME or sym == tcv.K_q:
			return {'move': (-1, -1)}
			
		elif sym == tcv.K_UP or sym == tcv.K_w:
			return {'move': (0, -1)}
		
		elif sym == tcv.K_PAGEUP or sym == tcv.K_e:
			return {'move': (1, -1)}
		
		elif sym == tcv.K_LEFT or sym == tcv.K_a:
			return {'move': (-1, 0)}
		
		elif sym in (tcv.K_PERIOD, tcv.K_KP_PERIOD, tcv.K_s):
			return {'move': (0, 0)}
		
		elif sym == tcv.K_RIGHT or sym == tcv.K_d:
			return {'move': (1, 0)}
		
		elif sym == tcv.K_END or sym == tcv.K_z:
			return {'move': (-1, 1)}
		
		elif sym == tcv.K_DOWN or sym == tcv.K_x:
			return {'move': (0, 1)}
		
		elif sym == tcv.K_PAGEDOWN or sym == tcv.K_c:
			return {'move': (1, 1)}
			
	elif constants.SETTINGS[0]["sel"] == 2:
	
		if sym == tcv.K_HOME or sym == tcv.K_y:
			return {'move': (-1, -1)}
			
		elif sym == tcv.K_UP or sym == tcv.K_k:
			return {'move': (0, -1)}
		
		elif sym == tcv.K_PAGEUP or sym == tcv.K_u:
			return {'move': (1, -1)}
		
		elif sym == tcv.K_LEFT or sym == tcv.K_h:
			return {'move': (-1, 0)}
		
		elif sym in (tcv.K_PERIOD, tcv.K_KP_PERIOD,):
			return {'move': (0, 0)}
		
		elif sym == tcv.K_RIGHT or sym == tcv.K_l:
			return {'move': (1, 0)}
		
		elif sym == tcv.K_END or sym == tcv.K_b:
			return {'move': (-1, 1)}
		
		elif sym == tcv.K_DOWN or sym == tcv.K_j:
			return {'move': (0, 1)}
		
		elif sym == tcv.K_PAGEDOWN or sym == tcv.K_n:
			return {'move': (1, 1)}
	
	#exiting
	
	if sym in (tcv.K_KP_ENTER, tcv.K_RETURN, tcv.K_RETURN2):
		return {'pause': True}
	
	if sym == tcv.K_ESCAPE:
		return {'exit': True}
		
	if sym == tcv.K_f:
		return {'jump': True}
	
	return {}