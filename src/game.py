# Importing pgzero constants
import pgzero.screen

# Local imports
from robot import Robot
from platforms import Platform_Cluster

# Defining needed variables
screen: pgzero.screen.Screen

# Setting window size
WIDTH = 300
HEIGHT = 300

# Creating actors
robot = Robot((WIDTH/2, HEIGHT/2))
cluster = Platform_Cluster()

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
	robot.draw()
	cluster.draw_all(screen)

