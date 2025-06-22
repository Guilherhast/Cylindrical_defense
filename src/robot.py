# Imports
from pgzero.actor import Actor

# Images thanks to
# https://www.gameart2d.com/the-robot---free-sprites.html

class Robot(Actor):
	__fall_speed = 0
	def __init__(self, gravity, terminal_speed, pos):
		self.terminal_speed = terminal_speed
		self.gravity = gravity
		super().__init__('robot/runshoot_1.png', pos)

	def update(self, dt):
		self.__fall_speed = min(
					self.__fall_speed + dt*self.gravity,
					self.terminal_speed
				)
		self.pos = (self.pos[0], self.pos[1] + self.__fall_speed)
		pass
