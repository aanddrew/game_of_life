import Cell
import Button
import pygame
import random

pygame.display.init()
# pygame.time.init()
# pygame.init()

disp_width = 1024
disp_height = 768
dimensions = (disp_width, disp_height)
white = (255,255,255)
green = (  0,255,0  )
red   = (255,0  ,0  )

clock = pygame.time.Clock()
display = pygame.display.set_mode(dimensions)

middle = disp_width/2

button_go   = Button.Button(middle + 95,disp_height-75,green)
button_stop = Button.Button(middle + 25,disp_height-75,red  )
button_rand = Button.Button(middle - 75,disp_height-75,white, 'dice.png')
button_reset= Button.Button(middle- 145,disp_height-75,white, 'reset.png')

buttons = []
buttons.append(button_go)
buttons.append(button_stop)
buttons.append(button_reset)
buttons.append(button_rand)

#this to become a 2d array
#cells[rows][cols]
cells = []
def create_cells():
	del cells[:]
	effective_size = Cell.size + 1
	numRows = (disp_height-100)/(effective_size)
	numCols = disp_width/(effective_size)

	for r in range(0, numRows):
		cols = []
		for c in range(0, numCols):
			temp_cell = Cell.Cell(c*effective_size, r*effective_size)
			cols.append(temp_cell)

		cells.append(cols)

def randomize():
	for row in cells:
		for c in row:
			x = random.randint(0,4)
			if x == 1:
				c.swap_status()

def draw_buttons():
	#draw the go button in green
	for b in buttons:
		b.draw(display)

def setup():
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				return False

			if event.type == pygame.MOUSEBUTTONDOWN:
				mousex = pygame.mouse.get_pos()[0]
				mousey = pygame.mouse.get_pos()[1]
				for row in cells:
					for c in row:
						if c.in_cell(mousex, mousey):
							c.swap_status()
				if button_go.in_button(mousex,mousey):
					done = True
				elif button_rand.in_button(mousex,mousey):
					randomize()
				elif button_reset.in_button(mousex,mousey):
					create_cells()

			if event.type == pygame.MOUSEMOTION:
				mousex = pygame.mouse.get_pos()[0]
				mousey = pygame.mouse.get_pos()[1]
				for b in buttons:
					if b.in_button(mousex, mousey):
						b.darken()
					else:
						b.lighten()


		display.fill(white)
		
		for row in cells:
			for c in row:
				c.draw(display)

		draw_buttons()

		pygame.display.update()
	return True

def play_round():
	flags =[]
	for row in range(1, len(cells)-1):
		flags.append([])
		for col in range(1, len(cells[0])-1):
			live_neighbors = 0
			if cells[row-1][col-1].alive == True:
				live_neighbors += 1
			if cells[row-1][col  ].alive == True:
				live_neighbors += 1
			if cells[row-1][col+1].alive == True:
				live_neighbors += 1
			if cells[row  ][col-1].alive == True:
				live_neighbors += 1
			if cells[row  ][col+1].alive == True:
				live_neighbors += 1
			if cells[row+1][col-1].alive == True:
				live_neighbors += 1
			if cells[row+1][col  ].alive == True:
				live_neighbors += 1
			if cells[row+1][col+1].alive == True:
				live_neighbors += 1

			if cells[row][col].alive == True:
				if live_neighbors < 2:
					# cells[row][col].alive == False
					flags[row-1].append(False)
				elif live_neighbors > 3:
					# cells[row][col].alive == False
					flags[row-1].append(False)
				else:
					flags[row-1].append(True)
			else:
				if live_neighbors == 3:
					# cells[row][col].alive = True
					flags[row-1].append(True)
				else:
					flags[row-1].append(False)

	for row in range(0, len(flags)):
		for col in range(0, len(flags[0])):
			cells[row][col].alive = flags[row-1][col-1]


def play():
	done = False
	while not done:
		play_round()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				return False
			if event.type == pygame.MOUSEBUTTONDOWN:
				mousex = pygame.mouse.get_pos()[0]
				mousey = pygame.mouse.get_pos()[1]
				if button_stop.in_button(mousex,mousey):
					done = True

			if event.type == pygame.MOUSEMOTION:
				mousex = pygame.mouse.get_pos()[0]
				mousey = pygame.mouse.get_pos()[1]
				for b in buttons:
					if b.in_button(mousex, mousey):
						b.darken()
					else:
						b.lighten()
		display.fill(white)
		
		for row in cells:
			for c in row:
				c.draw(display)

		clock.tick(10)
		draw_buttons()
		pygame.display.update()
	return True

	


def main():
	create_cells()
	playing = True
	while playing:
		playing = setup()
		if playing:
			playing = play()


main()
pygame.quit()
quit()