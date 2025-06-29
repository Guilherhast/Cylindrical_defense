# File with the main function of the game

## Imports
### Importing pgzero constants
import pgzero.screen
import pgzero.keyboard

### Import system objects
from Game.controller import Controller
from Game.manager import Manager

### Import actor objects
from actors.scroll import Scroll
from actors.robot import Robot
from actors.platforms import PlatformGroup

from actors import bullet
from actors import ballon

## Defining object types
screen: pgzero.screen.Screen
keyboard: pgzero.keyboard.Keyboard

## Setting constants
WIDTH = 300
HEIGHT = 300

screen_size = (WIDTH, HEIGHT)

### Scroll variables
scroll_speed = -300
scroll_max = 1500
scroll_displacement = 0

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
	'left': lambda game, dt: game.scroll.scroll_left(dt),
	'right': lambda game, dt: game.scroll.scroll_right(dt),
	'up': lambda game, dt: game.robot.jump(dt),
	'space': lambda game, _: game.robot.shoot(),
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
	game.controller = Controller(game, keyboard, actions)
	game.scroll = Scroll(scroll_speed, scroll_displacement, scroll_max)
	game.platform_group = PlatformGroup(game.scroll, screen)
	#### General objects
	game.destroyables = bullet.DestroyableList(game.scroll)
	scope = bullet.Scope(-50, scroll_max + WIDTH, 0, HEIGHT)
	#### Robot objects
	bullet_factory = bullet.Bullet.create_factory('robot/objects/bullet_001.png', 100,  scope, game.scroll)
	cannon = bullet.Cannon(bullet_factory, [20, 2], .8, game.destroyables)
	game.robot = Robot(10, 200, screen_size, game.platform_group, cannon)
	#### Ballon objects
	# Fixme change for level manager
	ballon_factory = ballon.Balloon.create_ballon_factory(1, scope, game.scroll)
	game.spawner = ballon.BallonSpawner(ballon_factory, 10, game.destroyables, HEIGHT)



### Loop update interaction
def loop(game, dt):
	game.controller.update(dt)
	game.scroll.update(dt)
	game.robot.update(dt)
	game.platform_group.update(dt)
	game.destroyables.update(dt)
	game.spawner.update(dt)

### Draw
def update_screen(game):
	screen.fill(get_color())
	screen.draw.text(str(game.scroll.get_displacement()), (WIDTH/2, 50)) # Debug
	screen.draw.text(str(screen.surface.get_height()), (WIDTH/2, 90)) # Debug

	game.robot.draw()
	game.platform_group.draw()
	game.destroyables.draw()

## Variable to hold the game
game = Manager(start, loop, update_screen)

## Main pgzero functions
### Frist update
def update(dt):
	game.update(dt)

### Draw after update
def draw():
	game.draw()
