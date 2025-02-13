import pygame

screen = pygame.display.set_mode((750, 500))

piece_image = pygame.image.load('wieza_hanoi_piece.png')
piece_image = pygame.transform.scale(piece_image, (49, 10))

mouse_image = pygame.image.load('mouse_thingy.png')
mouse_image = pygame.transform.scale(mouse_image, (9, 9))


pole_positions = [140, 356, 610]


class GamePiece(pygame.sprite.Sprite):
	def __init__(self, image, size):
		super(GamePiece, self).__init__()
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (width * size, height * size))
		self.image.set_colorkey((1, 1, 1), 1)
		self.rect = self.image.get_rect()
		self.lifted = False
		self.current_pos = 0
		self.rect.x = 140 - self.rect.width/2
		self.rect.y = 310
		pole1_pieces.append(size)

	def update(self):
		screen.blit(self.image, self.rect)
		if pygame.key.get_pressed()[pygame.K_SPACE]:
				if self.lifted:
					self.lifted = False
					self.rect.y = 310
				else:
					if mouse_current_pos == self.current_pos:
						self.lifted = True
						self.rect.y = 50
		if self.lifted:
			if pygame.key.get_pressed()[pygame.K_RIGHT]:
				self.current_pos = (self.current_pos + 1) % 3
				self.rect.x = pole_positions[self.current_pos] - self.rect.width / 2
			if pygame.key.get_pressed()[pygame.K_LEFT]:
				self.current_pos = (self.current_pos - 1) % 3
				self.rect.x = pole_positions[self.current_pos] - self.rect.width / 2


mouse_current_pos = 0


class MouseThingy(pygame.sprite.Sprite):
	def __init__(self, image):
		super(MouseThingy, self).__init__()
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (width * 5, height * 5))
		self.image.set_colorkey((0, 0, 0), 1)
		self.rect = self.image.get_rect()
		self.rect.x = pole_positions[mouse_current_pos] - self.rect.width/2

	def update(self):
		global mouse_current_pos
		screen.blit(self.image, self.rect)
		if pygame.key.get_pressed()[pygame.K_LEFT]:
			mouse_current_pos = (mouse_current_pos - 1) % 3
			self.rect.x = pole_positions[mouse_current_pos] - self.rect.width/2
		elif pygame.key.get_pressed()[pygame.K_RIGHT]:
			mouse_current_pos = (mouse_current_pos + 1) % 3
			self.rect.x = pole_positions[mouse_current_pos] - self.rect.width/2


background = pygame.image.load('wieza_hanoi_stand.png')
background = pygame.transform.scale(background, (750, 500))

game_pieces = pygame.sprite.Group()

pole1_pieces = []
pole2_pieces = []
pole3_pieces = []

game_piece1 = GamePiece(piece_image, 5)
# game_piece2 = GamePiece(piece_image, 4)
# game_piece3 = GamePiece(piece_image, 3)

game_pieces.add(game_piece1)
# game_pieces.add(game_piece2)
# game_pieces.add(game_piece3)

mouse_thingy = MouseThingy(mouse_image)
clock = pygame.time.Clock()
gameOn = True
while gameOn:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOn = False

	screen.blit(background, (0, 0))
	for p in game_pieces:
		p.update()
	mouse_thingy.update()
	pygame.display.flip()
	clock.tick(5)
