# File to define classes for the platforms
## Imports
from random import random
from math import floor
from actors.scrollable import ScrollableActor

## Images thanks to
### https://www.gameart2d.com/free-sci-fi-platformer-tileset.html

## Class to manage a single platform
class Platform(ScrollableActor):
	### Create a platform using the platform image
	def __init__(self, pos):
		super().__init__('scifi/box.png', pos)

## Class to manage platform groups
class PlatformGroup():
	### Create an instance to manage a platform group
	def __init__(self, state, screen): #DEBUG Remove screen
		self.__screen = screen
		self.__state = state
		self.create_group()

	### Random y position
	def __random_y(self):
		level = 1 + floor(random() * 3)
		return  self.__screen.surface.get_height() - 60 * level

	### Scroll all platforms to left
	def __scroll(self, delta):
		for plt in self.__group:
			plt.scroll(delta)

	### Create a group of platforms
	def create_group(self):
		positions = [ self.__random_y() for i in range(15) ]
		positions.insert(0, 240)
		self.__group = [
					Platform((150 + 100*i, y))
					#Platform((150 + 100*i, 240))
					for i,y in enumerate(positions)
				]

	### Draw all platforms
	def draw(self):
		for i,plt in enumerate(self.__group):
			text_pos = (plt.pos[0], plt.pos[1] + 30)
			self.__screen.draw.text(str(i), text_pos)
			plt.draw()

	### Update all platforms from group
	def update(self, _):
		delta = self.__state.get_delta()
		self.__scroll(delta)

	### Check if point collide with any of the platforms
	def collidepoint(self, point):
		return any(g.collidepoint(point) for g in self.__group)
