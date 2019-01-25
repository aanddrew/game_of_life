import pygame

size = 10

#A cell represents one element of the game of life, either alive or dead.
class Cell:
	#yellow is alive
	yellow = (255,255,0)
	#gray is dead
	gray = (128,128,128)

	def __init__(self, xIn, yIn):
		self.x = xIn
		self.y = yIn
		self.alive = False

	def draw(self, screen):
		color = self.gray
		if self.alive == True:
			color = self.yellow
		pygame.draw.rect(screen, color, 
						 pygame.Rect(self.x,self.y, size, size))

	def in_cell(self, xTest, yTest):
		return ((self.x +size >= xTest and self.y +size >= yTest) and
				 (self.x <= xTest and self.y <= yTest))

	def swap_status(self):
		self.alive = not self.alive

	pass