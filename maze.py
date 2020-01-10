import os
import random
import pygame
import time

def text_objects(text, font, color):
    surface = font.render(text, True, color)
    return surface, surface.get_rect()
def game_text(text, color, size):

    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((255,255,255))
        font = pygame.font.Font('lunchds.ttf', size)
        screen_text, surface_rect = text_objects(text,  font, color)
        surface_rect.center = ((592/2),(592/2))
        screen.blit(screen_text, surface_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        pause=False

#make player
class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom
#create walls
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

#caption
pygame.display.set_caption("MMME: Most Mediocre Maze Ever!")
screen = pygame.display.set_mode((592, 592))

clock = pygame.time.Clock()
walls = []
player = Player()

#maze layout
level = ['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X   X           X       X   X       X',
'X   X           X       X   X       X',
'X   X           X       X   X       X',
'X   X   XXXXX   X       X   X   X   X',
'X   X   X   X   X   X   X   X   X   X',
'X       X   X   X   X   X   X   X   X',
'X       X   X   X   X   X   X   X   X',
'X       X       X   X   X   X   X   X',
'X       X       X   X   X   X   X   X',
'XXXXXXXXX   XXXXX   X   X   X   X   X',
'X       X       X   X   X       X   X',
'X       X       X   X   X       X   X',
'X   X   XXXXX   X   X   XXXXXXXXX   X',
'X   X       X       X               X',
'X   X       X       X               X',
'X   X               X               X',
'X   X               X               X',
'X   XXXXXXXXXXXXXXXXX   XXXXXXXXXXXXX',
'X                   X       X       X',
'X                   X       X       X',
'X                   X       X       X',
'X   XXXXXXXXXXXXX   XXXXX   X   X   X',
'X       X       X           X   X   X',
'X       X       X           X   X   X',
'X       X       X           X   X   X',
'XXXXX   X   XXXXXXXXXXXXXXXXXXXXX   X',
'X       X               X           X',
'X       X               X           X',
'X       X               X           X',
'X   XXXXXXXXXXXXX   X   XXXXX   X   X',
'X               X   X   X       X   X',
'X               X   X   X       X   X',
'XXXXXXXXXXXXX   X   X   X   XXXXX   X',
'X                   X       X       X',
'X                   X       X      EX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
]
#X=wall, E=exit

x = y = 0
for row in level:
    for col in row:
        if col == "X":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0
#game function player and start time as variables
def game(t,player):
    running = True
    while running:

        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                quit()

        # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2, 0)
        if key[pygame.K_RIGHT]:
            player.move(2, 0)
        if key[pygame.K_UP]:
            player.move(0, -2)
        if key[pygame.K_DOWN]:
            player.move(0, 2)


        if player.rect.colliderect(end_rect):
            game_text("You escaped!",(0,0,0), 80)
            raise SystemExit
        # Draw the scene
        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        pygame.draw.rect(screen, (0, 255, 0), end_rect)
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        pygame.display.flip()
        t1=time.time()
        if t1-t>40:
            game_text("you took too long",(255,0,0), 50)
            game_text("try again",(255,0,0), 50)
            player=Player()
            game(t1,player)
#welcome message
game_text("Welcome!",(0,0,0), 115)
#initial time
t0=time.time()
#start game
game(t0,player)
#exit pygame
pygame.quit()
#quit window
quit()
