# Importing pgzero constants
import pgzero.screen
import pgzero.keyboard

# Local imports
from gamestate import GameState
from robot import Robot
from platforms import Platform_Cluster

# Defining needed variables
screen: pgzero.screen.Screen
keyboard: pgzero.keyboard.Keyboard

# Setting window size
WIDTH = 300
HEIGHT = 300

center = (WIDTH/2, HEIGHT/2)

# Creating actors
state = GameState(300, 0, 1500)
robot = Robot(10, 200, center)
cluster = Platform_Cluster(state)

tmp_draw = None


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
	screen.draw.text(str(state.scroll), (WIDTH/2, 50))
	robot.draw()
	cluster.draw_all(screen)

def update(dt):
	# I wish it could be passed in the constructor
	state.check_keyboard(keyboard, dt)
	#robot.update(dt)
	cluster.update(dt)

