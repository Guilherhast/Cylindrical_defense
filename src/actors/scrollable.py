# Imports
from pgzero.actor import Actor

class ScrollableActor(Actor):
	def __init__(self, img, pos):
		super().__init__(img, pos)

	def scroll(self, delta):
			new_pos = (self.pos[0] + delta, self.pos[1])
			self.pos = new_pos


