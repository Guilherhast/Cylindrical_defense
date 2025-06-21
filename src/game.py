# Importing pgzero constants
import pgzero.screen

# Defining needed files
screen: pgzero.screen.Screen

# Setting window size
WIDTH = 300
HEIGHT = 300

# Background Settings
color = {
			'red': 0,
			'green': 0,
			'blue': 128
		}

def get_color():
	return (
			color['red'],
			color['green'],
			color['blue'],
		)

def draw():
	screen.fill(get_color())
