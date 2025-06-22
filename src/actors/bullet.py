# File to define classes for bullet types
## Imports
from actors.scrollable import ScrollableActor

## Define a scope where an object can exist
class Scope():
	def __init__(self, x_start, x_end, y_start, y_end):
		self.__x_range = [x_start, x_end]
		self.__y_range = [y_start, y_end]

	def is_inside(self, point):
		return self.__x_range[0] <= point[0] <= self.__x_range[1] and self.__y_range[0] <= point[1] <= self.__y_range[1]

	def is_inside_x(self, x):
		return self.__x_range[0] <= x <= self.__x_range[1]

	def is_inside_y(self, y):
		return self.__y_range[0] <= y <= self.__y_range[1]

## Class to hold destroyable objects
class DestroyableList(list):
	def __init__(self, scroll,  *args):
		self.__scroll = scroll
		super().__init__(*args)

	def __scroll(self, delta):
		for item in self:
			item.scroll(delta)

	### Draw all items in the list
	def draw(self):
		for item in self:
			item.draw()

	### Update all items in the list
	def update(self, dt):
		delta = self.__scroll.get_delta()
		for item in self:
			item.update(dt)
			item.scroll(delta)
		self.filter()

	### Remove not destoryed items
	def filter(self):
		self[:] = [item for item in self if not item.is_destroyed()]
		return self

## Class to launch bullets
class Cannon():
	### Create a cannon using the cannon image
	def __init__(self, factory, gap, cool_down, destroyable_list, pos = [0,0]):
		self.destroyable_list = destroyable_list
		self.__factory = factory
		self.__bullet_gap = gap
		self.set_position(pos)
		self.__default_cool_down = cool_down
		self.__cool_down = cool_down

	def update(self, dt):
		# Check cooldown
		if self.__cool_down > 0:
			self.__cool_down = max(self.__cool_down - dt, 0)

	### Change cannon position
	def set_position(self, new_pos):
		self.__pos = new_pos
		self.__bullet_pos = (self.__pos[0] + self.__bullet_gap[0], self.__pos[1] + self.__bullet_gap[1])

	### Create a bullet and return it
	def shoot(self):
		# Check cooldown
		if self.__factory and self.__cool_down <= 0:
			self.destroyable_list.append(self.__factory(self.__bullet_pos))
			self.__cool_down = self.__default_cool_down

	def shoot_from(self, pos):
		self.set_position(pos)
		return self.shoot()

## Class to manage a single platform
class Bullet(ScrollableActor):
	### Create a platform using the platform image
	def __init__(self, image, pos, speed, scope, displacement = 0):
		super().__init__(image, pos)
		self.__displacement = pos[0] + displacement
		self.__is_destroyed = False
		self.__speed = speed
		self.__scope = scope

	### Create factory
	@staticmethod
	def create_factory(image, speed, scope, scroll=None):
		def factory(pos):
			disp = 0
			if scroll is not None:
				disp = scroll.get_displacement()
			return Bullet(image, pos, speed, scope, disp)
		return factory

	### Check if the bullet is destroyed
	def is_destroyed(self):
		return self.__is_destroyed

	### Get the position of the bullet
	def update(self, dt):
		if not self.is_destroyed():
			self.pos = (self.pos[0] + self.__speed * dt, self.pos[1])
			self.__displacement += self.__speed * dt
			if not self.__scope.is_inside_x(self.__displacement):
				self.destroy()

	### Destroy the bullet
	def destroy(self):
		self.__is_destroyed = True
