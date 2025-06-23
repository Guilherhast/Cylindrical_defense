class Scroll:
	# Change in x since last update
	__delta = 0
	__direction = 0

	## Getter functions

	### Get te value of x delta
	def get_delta(self):
		return self.__delta

	### Get scroll displacement
	def get_displacement(self):
		return self.__displacement

	def get_scrollable_width(self):
		return self.scrollable_width

	## Constructor
	def __init__(self, speed, displacement, scrollable_width):
		self.speed = speed
		self.__displacement = displacement
		self.scrollable_width = scrollable_width

	## Calculation functions
	### Calc constrained movement
	def constrain_scroll(self, value):
		return min(self.scrollable_width, max(0, value))

	### Calc delta in left direction
	def calc_scroll_left(self, dt):
		return max(-self.speed * dt, - self.__displacement)

	### Calc delta in right direction
	def calc_scroll_right(self, dt):
		return min(self.speed * dt, self.scrollable_width - self.__displacement)

	## Scroll functions
	### Scroll right
	def scroll_right(self, _):
		self.__direction -= 1

	### Scroll left
	def scroll_left(self, _):
		self.__direction += 1

	### Update scroll
	def update(self, dt):
		new_scroll = self.constrain_scroll(self.__displacement + self.__direction * self.speed * dt)
		self.__delta = self.__displacement - new_scroll
		self.__displacement = new_scroll
		#### Clean movement direction
		self.__direction = 0

