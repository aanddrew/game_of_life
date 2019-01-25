import pygame

size = 50

class Button:

	def __init__(self, xIn, yIn, colorIn, imageIn = None):
		self.x = xIn
		self.y = yIn
		self.color = colorIn
		self.imageLoc = imageIn

		self.dark = False

		self.dark_surface = pygame.Surface((size,size))  # the size of your rect
		self.dark_surface.set_alpha(128)                # alpha level
		self.dark_surface.fill((0,0,0))           # this fills the entire surface

		if self.imageLoc is not None:
			self.image = pygame.image.load(self.imageLoc)

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, 
						 pygame.Rect(self.x,self.y, size, size))
		if self.imageLoc is not None:
			screen.blit(self.image, (self.x, self.y))

		if self.dark is True:
			screen.blit(self.dark_surface, (self.x, self.y))

	def in_button(self, xTest, yTest):
		return ((self.x +size >= xTest and self.y +size >= yTest) and
				 (self.x <= xTest and self.y <= yTest))

	def darken(self):
		self.dark = True

	def lighten(self):
		self.dark = False