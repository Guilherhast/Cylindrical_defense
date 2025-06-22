class GameState:
	__delta = 0

	def __init__(self, speed, scroll, scrollable_width):
		self.speed = speed
		self.scroll = scroll
		self.scrollable_width = scrollable_width

	def get_delta(self):
		return self.__delta

	def calc_scroll_left(self, dt):
		return max(-self.speed * dt, -self.scroll)

	def calc_scroll_right(self, dt):
		return min(self.speed * dt, self.scrollable_width - self.scroll)

	def check_keyboard(self, kbd, dt):
		self.__delta = 0
		if kbd.left:
			self.__delta += self.calc_scroll_left(dt)
		if kbd.right:
			self.__delta += self.calc_scroll_right(dt)
		self.update_scroll(dt)

	def update_scroll(self, dt):
		self.scroll+= self.__delta
