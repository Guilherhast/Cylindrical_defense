# Imports
from pgzero.actor import Actor

# Images thanks to
# https://www.gameart2d.com/free-sci-fi-platformer-tileset.html

class Platform(Actor):
	def __init__(self, pos):
		super().__init__('scifi/box.png', pos)

class Platform_Cluster(Actor):
	def __init__(self):
		self.create_cluster()

	def create_cluster(self):
		self.cluster = [
					Platform((50 + 100*i, 220))
					for i in range(15)
				]

	def draw_all(self, screen):
		for i,plt in enumerate(self.cluster):
			new_pos = (plt.pos[0], plt.pos[1] + 30)
			screen.draw.text(str(i), new_pos)
			plt.draw()

