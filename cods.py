#здесь я буду кодить совю игру илья пинг понг
#здесь я буду кодить совю игру илья пинг понг
from pygame import *


class GameSprite(sprite.Sprite):
    # Конструктор
    def __init__(self, img, x, y, speed):
        self.image = transform.scale(image.load(img), (65, 65))
        self.speed = speed
        # Для контроля столкновений
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class p2(GameSprite):
    def update(self):
        kjin = key.get_pressed()
        
        if kjin[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if kjin[K_s] and self.rect.y < h - 70:
            self.rect.y -= self.speed

class p1(GameSprite):
    def update(self):
        kjin = key.get_pressed()
        
        if kjin[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if kjin[K_DOWN] and self.rect.y < h - 70:
            self.rect.y -= self.speed





P2 = p2("raketka.jpg", 30, 30, 5)
P1 = p1("raketka.jpg", 500, 30, 5)

game = True
clock = time.Clock()
FPS = 120


mixer.init()
mixer.music.load("freebeat.mp3")
mixer.music.play()

font.init()
font = font.Font(None, 70)
win1 = font.render("P1 WIN", True, (75, 0, 130))
win2 = font.render("P2 WIN", True, (75, 0, 130))



w, h = 700, 500
window = display.set_mode((w,h))
display.set_caption("Labirint")
bg = transform.scale(image.load("gamadril.jpg"), (w,h))






# Игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(bg, (0,0))
    

    

    
    display.update()
    clock.tick(FPS)
