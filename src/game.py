# File with the main function of the game

## Imports
### Importing pgzero constants
import pgzero.screen
import pgzero.keyboard

### Game system imports
from gamemanager import GameManager
from gamecontroller import GameController

### Game object imports
from gamestate import GameState
from robot import Robot
from platforms import PlatformGroup

## Defining object types
screen: pgzero.screen.Screen
keyboard: pgzero.keyboard.Keyboard

## Setting constants
WIDTH = 300
HEIGHT = 300

screen_size = (WIDTH, HEIGHT)

### Background Settings
color = {
			'red': 0,
			'green': 0,
			'blue': 128
		}

#### Turn color into a tuple
def get_color():
	return (
			color['red'],
			color['green'],
			color['blue'],
		)

## Declare actions for the each key
actions = {
	'left': lambda game, dt: game.state.scroll_left(dt),
	'right': lambda game, dt: game.state.scroll_right(dt),
	'up': lambda game, dt: game.robot.jump(dt),
}

## Update functions
'''
All this business is avoid passing to many aruments
Also to avoid passing constants several times
I wont teach it to students
Unless they ask
'''

### First update interaction
def start(game, _):
	game.controller = GameController(game, keyboard, actions)
	game.state = GameState(300, 0, 1500, keyboard)
	game.platform_group = PlatformGroup(game.state, screen)
	game.robot = Robot(10, 200, screen_size, game.platform_group)

### Loop update interaction
def loop(game, dt):
	game.controller.update(dt)
	game.state.update(dt)
	game.robot.update(dt)
	game.platform_group.update(dt)

### Draw
def update_screen(game):
	screen.fill(get_color())
	screen.draw.text(str(game.state.get_scroll()), (WIDTH/2, 50))
	game.robot.draw()
	game.platform_group.draw()

## Variable to hold the game
game = GameManager(start, loop, update_screen)

## Main pgzero functions
### Frist update
def update(dt):
	game.update(dt)

### Draw after update
def draw():
	game.draw()
