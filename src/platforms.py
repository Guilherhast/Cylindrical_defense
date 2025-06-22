# Imports
from pgzero.actor import Actor
from scrollable import ScrollableActor

# Images thanks to
# https://www.gameart2d.com/free-sci-fi-platformer-tileset.html

class Platform(ScrollableActor):
	def __init__(self, pos):
		super().__init__('scifi/box.png', pos)

class Platform_Cluster():
	def __init__(self, state):
		self.scroll = state.scroll
		self.state = state
		self.create_cluster()
		self.old_scroll = state.scroll

	def create_cluster(self):
		self.cluster = [
					Platform((50 + 100*i, 220))
					for i in range(20)
				]

	def draw_all(self, screen):
		for i,plt in enumerate(self.cluster):
			text_pos = (plt.pos[0], plt.pos[1] + 30)
			screen.draw.text(str(i), text_pos)
			plt.draw()

	def update(self, dt):
		delta = self.scroll  - self.state.scroll
		self.scroll  = self.state.scroll
		for plt in self.cluster:
			plt.scroll(delta)

	def scroll(self, delta):
		for plt in self.cluster:
			plt.scroll(delta)





