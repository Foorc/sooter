from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption("шутер")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))

clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, image1, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image1), (65, 65))
        self.speed = speed    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 10)
        bullets.add(bullet)



lost = 0
font.init()
font1 = font.Font(None, 36)
jop = 0


class Enemy(GameSprite):
    
    def update(self):

        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -50
            self.rect.x = randint(1,560)
            self.speed = randint(1,5)

            global lost
            lost = lost + 1

class Bullet(GameSprite):

    def update(self):

        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


rocket = Player('rocket.png', 100, 400, 10)

ha = sprite.Group()
for i in range(6):
    ufo = Enemy("ufo.png", randint(1,560), -50, randint(1,5))
    ha.add(ufo)

gh = sprite.Group()
for i in range(4):
    asteroid = Enemy("asteroid.png", randint(1,560), -50, randint(1,5))
    gh.add(asteroid)

bullets = sprite.Group()



game = True
finish = False
while game:
    
    if not finish:
        
        window.blit(background, (0, 0 ))
        rocket.reset()
        rocket.update()
        gh.update()
        gh.draw(window)
        ha.update()
        ha.draw(window)
        bullets.draw(window)
        bullets.update()
        text_lose = font1 = SysFont('Arial', 40), ("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose,(15,15))
        gop = font1 = SysFont('Arial', 40), ("Счёт: " + str(jop), 1, (255, 255, 255))
        window.blit(gop,(15,50))
        if lost > 3:
            finish = True
            ho = font1 = font1 = SysFont('Arial', 40), ("Проигрыш", 1, (255, 255, 255))
            window.blit(ho,(300,300))
        if jop > 10:
            finish = True
            ho = font1 = SysFont('Arial', 40), ("Выигрыш", 1, (255, 255, 255))
            window.blit(ho,(300,300))
          
    jo = sprite.groupcollide(ha, bullets, True, True)
    for j in jo:
        jop += 1
        ufo = Enemy("ufo.png", randint(1,560), -50, randint(1,5))
        ha.add(ufo)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.fire()
    clock.tick(FPS)
    display.update() 