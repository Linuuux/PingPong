from pygame import *
from random import randint
font.init()

window = display.set_mode((700, 500))
display.set_caption('pingpong')
background = transform.scale(image.load('pong.jpg'), (700, 500))
kills = 0
death = 0
player = transform.scale(image.load('platform.png'), (225, 225))
enemy = transform.scale(image.load('platform.png'), (225, 225))
ball = transform.scale(image.load('ball.png'), (225, 225))
speed_x = 3
speed_y = 3
lose_txt = font.SysFont('verdana', 70).render('GAME OVER', True, (240, 0, 0))
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

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        self.rect.x += speed_x
        self.rect.y += speed_y
        if sprite.collide_rect(self, player):
            speed_y *= -1
            speed_x *= 1
        if sprite.collide_rect(self, enemy):
            speed_y *= -1
            speed_x *= 1
        if self.rect.x >= 660:
            speed_y *= 1
            speed_x *= -1
        if self.rect.x <= 0:
            speed_y *= 1
            speed_x *= -1




player = Player(250, 450, 125, 30, 'platform.png', 7)
enemy = Enemy(250, 30, 125, 30, 'platform.png', 7)
ball = Ball(250, 200, 40, 40, 'ball.png', 0)

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
        if ball.rect.y >= 460:
            finish = True
            window.blit(lose_txt, (200, 200))
        if ball.rect.y <= 0:
            finish = True
            window.blit(lose_txt, (200, 200))
    clock.tick(FPS)
    display.update()
