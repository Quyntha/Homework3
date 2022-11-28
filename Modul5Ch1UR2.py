class Point():

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distance(self):
		return (self.x ** 2 + self.y ** 2) ** 0.5

p1 = Point(1, 1)


print(p1.distance())