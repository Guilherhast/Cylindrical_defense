# File to define classes for ballons
from actors.bullet import Bullet, Cannon
from random import random
from math import floor

class Balloon(Bullet):
	### Create a platform using the platform image
	def __init__(self, level, scope, scrollable_width, displacement):
		self.__scrollable_width = scrollable_width
		self.__displacement = displacement
		super().__init__(
					self.__gen_img_name(level),
					self.__gen_random_position(),
					self.__gen_random_speed(level),
					scope,
					displacement
				)
		self.__health = floor((.5 + random()) * level)

	### Create factory
	@staticmethod
	def create_ballon_factory(level, scope, scroll):
		# Fixme change level to levelmanager
		def factory(pos):
			disp = 0
			scrollable_width = 0
			if scroll is not None:
				disp = scroll.get_displacement()
				scrollable_width = scroll.get_scrollable_width()
			return Balloon(
					level,
					scope,
					scrollable_width,
					disp
				)
		return factory

	### Generate a random speed based on the level
	def __gen_random_speed(self, level):
		return floor(- 20 * level + random() * 5 * level)

	def __gen_img_name(self, level):
		return f"ballons/ballon_{level}.png"

	def __gen_random_y(self):
		#FIXME magic number
		level = 3 + floor(random() * 10)
		return  300 - 20 * level

	def __gen_random_position(self):
		#FIXME magic number
		return ( 300 + self.__scrollable_width - self.__displacement, self.__gen_random_y())

class BallonSpawner(Cannon):
	### Create a cannon using the cannon image
	def __init__(self, factory, cool_down, destroyable_list, screen_height):
		pos = [0, screen_height/2]
		super().__init__(factory, [0,0], cool_down, destroyable_list, pos)

	def shoot(self):
		if self._factory and self._cool_down <= 0:
			self._destroyable_list.append(self._factory(self._pos))

	def __reset_cool_down(self):
		self._cool_down = self._default_cool_down * ( .7 + .5 * random())

	def __decrease_cool_down(self):
		self._default_cool_down *= .7

	def update(self, dt):
		self._cool_down -= dt
		if self._cool_down <= 0:
			self.shoot()
			self.__reset_cool_down()

