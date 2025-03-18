import time

import pygame

screen = pygame.display.set_mode((750, 500))

piece_image = pygame.image.load('wieza_hanoi_piece.png')
piece_image = pygame.transform.scale(piece_image, (49, 10))

mouse_image = pygame.image.load('mouse_thingy.png')
mouse_image = pygame.transform.scale(mouse_image, (9, 9))


pole_positions = [140, 356, 610]


poles = [[], [], []]

mouse_thingy_taken = False


class GamePiece(pygame.sprite.Sprite):
	def __init__(self, image, size, top, pos):
		super(GamePiece, self).__init__()
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (width * size, height * 5))
		self.image.set_colorkey((1, 1, 1), 1)
		self.rect = self.image.get_rect()
		self.lifted = False
		self.current_pos = 0
		self.rect.x = 140 - self.rect.width/2
		self.rect.y = 310
		self.size = size

	def update(self):
		screen.blit(self.image, self.rect)
		if self.lifted:
			if pygame.key.get_pressed()[pygame.K_RIGHT]:
				self.current_pos = (self.current_pos + 1) % 3
				self.rect.x = pole_positions[self.current_pos] - self.rect.width / 2
			if pygame.key.get_pressed()[pygame.K_LEFT]:
				self.current_pos = (self.current_pos - 1) % 3
				self.rect.x = pole_positions[self.current_pos] - self.rect.width / 2


def update_all_pieces():
	for p in game_pieces:
		p.rect.y = -50 + 50 * (len(game_pieces) - poles[p.current_pos].index(p)) + 210


class MouseThingy(pygame.sprite.Sprite):
	def __init__(self, image):
		super(MouseThingy, self).__init__()
		width = image.get_width()
		height = image.get_height()
		self.mouse_current_pos = 0
		self.image = pygame.transform.scale(image, (width * 5, height * 5))
		self.image.set_colorkey((0, 0, 0), 1)
		self.rect = self.image.get_rect()
		self.rect.x = pole_positions[self.mouse_current_pos] - self.rect.width/2
		self.taken = False
		self.lifted_piece = 0

	def update(self):
		screen.blit(self.image, self.rect)
		if pygame.key.get_pressed()[pygame.K_LEFT]:
			self.mouse_current_pos = (self.mouse_current_pos - 1) % 3
			self.rect.x = pole_positions[self.mouse_current_pos] - self.rect.width/2
			time.sleep(0.2)

		elif pygame.key.get_pressed()[pygame.K_RIGHT]:
			self.mouse_current_pos = (self.mouse_current_pos + 1) % 3
			self.rect.x = pole_positions[self.mouse_current_pos] - self.rect.width/2
			time.sleep(0.2)

		if pygame.key.get_pressed()[pygame.K_SPACE]:
			if not self.taken:
				if len(poles[self.mouse_current_pos]) > 0:
					self.lifted_piece = poles[self.mouse_current_pos][-1]
					self.lifted_piece.rect.y = 50
					self.lifted_piece.lifted = True
					poles[self.mouse_current_pos].remove(self.lifted_piece)
					self.taken = True
				time.sleep(0.2)

			elif self.taken:
				if (len(poles[self.mouse_current_pos]) > 0 and poles[self.mouse_current_pos][-1].size > self.lifted_piece.size) or len(poles[self.mouse_current_pos]) ==  0:
					self.lifted_piece.rect.y = 310
					self.lifted_piece.lifted = False
					poles[self.mouse_current_pos].append(self.lifted_piece)
					self.lifted_piece.current_pos = self.mouse_current_pos
					self.taken = False
					update_all_pieces()

					if len(poles[self.mouse_current_pos]) == 3 and not self.mouse_current_pos == 0:
						print('Win')
				time.sleep(0.2)


background = pygame.image.load('wieza_hanoi_stand.png')
background = pygame.transform.scale(background, (750, 500))

game_pieces = pygame.sprite.Group()

pole1_pieces = []
pole2_pieces = []
pole3_pieces = []


game_piece1 = GamePiece(piece_image, 5, False, 3)
game_piece2 = GamePiece(piece_image, 4, False, 2)
game_piece3 = GamePiece(piece_image, 3, True, 1)


game_pieces.add(game_piece1)
game_pieces.add(game_piece2)
game_pieces.add(game_piece3)


poles[0].append(game_piece1)
poles[0].append(game_piece2)
poles[0].append(game_piece3)


mouse_thingy = MouseThingy(mouse_image)
clock = pygame.time.Clock()
gameOn = True

update_all_pieces()
while gameOn:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOn = False

	screen.blit(background, (0, 0))
	for p in game_pieces:
		p.update()
	mouse_thingy.update()
	pygame.display.flip()

