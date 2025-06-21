# Imports
from pgzero.actor import Actor

# Images thanks to
# https://www.gameart2d.com/the-robot---free-sprites.html

class Robot(Actor):
	def __init__(self, pos):
		super().__init__('robot/runshoot_1.png', pos)
