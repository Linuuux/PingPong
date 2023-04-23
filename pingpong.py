import pygame
from random import randint

window = display.set_mode((700, 500))
display.set_caption('pingpong')
background = transform.scale(image.load('pong.jpg'), (700, 500))
kills = 0
death = 0
player = transform.scale(image.load('platform.png'), (225, 225))
enemy = transform.scale(image.load('platform.png'), (225, 225))
ball = transform.scale(image.load('ball.png'), (225, 225))
clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, img, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 570:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT] and self.rect.x < 570:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        
        
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


player = Player(250, 450, 125, 30, 'platform.png', 7)
enemy = Enemy(250, 30, 125, 30, 'platform.png', 7)
ball = Ball(250, 225, 50, 50, 'ball.png', 7)

game = True
finish = False

while game:
    for e in event.get():
        if e.type ==  QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        player.reset()
        player.update()
        enemy.reset()
        enemy.update()
        ball.reset()
        ball.update()
    clock.tick(FPS)
    display.update()