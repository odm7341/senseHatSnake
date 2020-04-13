from sense_hat import SenseHat
from random import randrange
from time import sleep



class Game:
	def __init__(self):
		# init snake with no body pieces
		self.valid = True
		self.snake = Snake(0, 0, 0)
		self.food = Food(5, 5, self)
		self.snake.giveFood(self.food)
		self.score = 0


	def isValid(self):
		if(self.snake.isValid()):
			return True
		print(self.score)
		sense.show_message("Score:" + str(self.score), text_colour=[0, 255, 0])
		return False

	def run(self):
		sleep(.3)
		self.snake.move()

	def foodEaten(self):
		self.score += 1
		newX = randrange(0, 8)
		newY = randrange(0, 8)
		while (self.snake.isHere(newX, newY)):
			newX = randrange(0, 8)
			newY = randrange(0, 8)
		self.food = Food(newX, newY, self)
		self.snake.addTail()
		self.snake.giveFood(self.food)

	def up(self):
		self.snake.setVertd(-1)

	def down(self):
		self.snake.setVertd(1)
		
	def left(self):
		self.snake.setHord(-1)
		
	def right(self):
		self.snake.setHord(1)
		
class Food:
	def __init__(self, x, y, game):
		self.x = x
		self.y = y
		self.game = game
		self.c = (255,0,0)
		sense.set_pixel(self.x, self.y, self.c)

	def isHere(self, x, y):
		if (x == self.x and y == self.y):
			sense.set_pixel(self.x, self.y, (0,0,0))
			self.game.foodEaten()
			return True
		return False




class Body:
	def __init__(self, front):
		self.front = front
		self.x = front.getX()
		self.y = front.getY()
		self.c = (0,255,0)
		self.tail = None

	def move(self):
		#print(self.tail)
		if (self.tail != None):
			self.tail.move()
		if (self.tail == None):
			sense.set_pixel(self.x, self.y, (0,0,0))
		self.x = self.front.getX()
		self.y = self.front.getY()
		sense.set_pixel(self.x, self.y, self.c)

	def isHere(self, x, y):
		if (x == self.x and y == self.y):
			return True
		if (self.tail):
			return self.tail.isHere(x, y)
		return False

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def addTail(self):
		#print("add")
		if (self.tail == None):
			self.tail = Body(self)
			return
		self.tail.addTail()


class Snake(Body):
	def __init__(self, tailSize, x, y):
		self.tailSize = tailSize
		self.tail = None
		self.x = x
		self.y = y
		self.c = (160,255,160)
		self.valid = True
		self.hd = 0
		self.vd = 1
		self.food = None
		sense.set_pixel(self.x, self.y, self.c)

	def isValid(self):
		return self.valid

	def giveFood(self, food):
		self.food = food;

	def move(self):
		nextX = self.x + self.hd
		nextY = self.y + self.vd
		if(self.food):
			self.food.isHere(nextX, nextY)
		if (nextX not in range(0,8) or nextY not in range(0, 8)):
			self.valid = False
			return
		if (self.tail):
			if (self.tail.isHere(nextX, nextY)):
				self.valid = False
				return
			self.tail.move()
		if (self.tail == None):
			sense.set_pixel(self.x, self.y, (0,0,0))
		self.x += self.hd
		self.y += self.vd
		sense.set_pixel(self.x, self.y, self.c)
		# print(self.x)

	def setVertd(self, dir):
		if (self.vd == 0):
			self.vd = dir
			self.hd = 0

	def setHord(self, dir):
		if (self.hd == 0):
			self.hd = dir
			self.vd = 0



if __name__ == "__main__":
	sense = SenseHat()
	sense.clear()

	#while True:
	
	game = Game()

	sense.stick.direction_up = game.up
	sense.stick.direction_down = game.down
	sense.stick.direction_left = game.left
	sense.stick.direction_right = game.right

	while game.isValid():
		game.run()
	#sense.show_message("GAME OVER", text_colour=[255, 0, 0])



