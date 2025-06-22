# File where the main character is declared
# Imports
#from pgzero.actor import Actor
from doubleactor import DoubleActor

## Images thanks to
#### https://www.gameart2d.com/the-robot---free-sprites.html

## Class for the main character
class Robot(DoubleActor):
	__height = 50
	__fall_speed = 0

	### Constructor
	def __init__(self, gravity, terminal_speed, screen_size, grounds):
		self.__terminal_speed = terminal_speed * 2
		self.__gravity = gravity * 100
		self.__jump_speed = 10 * self.__height

		self.__grounds = grounds
		self.__screen_size = screen_size

		pos = [x/2 for x in screen_size]
		gap = [0, screen_size[1]]
		super().__init__('robot/runshoot_1.png', pos, gap)

	### Check if the robot is touching the ground
	def __is_touching_ground(self):
		feet = (self.pos[0], self.pos[1]+self.__height/1.9)
		return self.__grounds is not None and self.__grounds.collidepoint(feet)

	def __is_out_of_screen(self):
		return self.pos[1] + self.__height/2 >= self.__screen_size[1]

	### Make sure the robot is bellow the terminal speed
	def __constrain_speed(self, speed):
		return min(speed, self.__terminal_speed)

	### Update the robot based on dt
	def update(self, dt):
		if self.__is_touching_ground():
			self.__fall_speed = min(0, self.__fall_speed)
		else:
			self.__fall_speed = self.__constrain_speed(self.__fall_speed+self.__gravity*dt)

		self.__fall(dt)

		if self.__is_out_of_screen():
			self.loop(dt)
		else:
			super().update(dt)

	### Fall based on gravity value and dt
	def __fall(self, dt):
		self.pos = (self.pos[0], self.pos[1] + self.__fall_speed * dt)

	### Jump
	def jump(self, _):
		if self.__is_touching_ground():
			self.__fall_speed = -self.__jump_speed


