# File where the main character is declared
# Imports
from pgzero.actor import Actor

## Class for actors that loop through the screen
class DoubleActor(Actor):
	def __init__(self, image, pos, gap):
		super().__init__(image, pos)
		self.__gap = gap
		self.__clone = Actor(image, pos)
		self.__update_clone_pos()

	def draw(self):
		self.__clone.draw()
		super().draw()

	def __update_clone_pos(self):
		self.__clone.pos = (
				self.pos[0] - self.__gap[0],
				self.pos[1] - self.__gap[1]
			)

	### Switch position with the clone
	def loop(self, _):
		self.pos = self.__clone.pos
		self.update(_)

	def update(self, _):
		self.__update_clone_pos()

