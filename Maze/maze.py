from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y  
    def show(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

        if keys[K_RIGHT] and self.rect.x < lebar - 80:
            self.rect.x += self.speed
        
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < tinggi - 80:
            self.rect.y += self.speed
class enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= lebar - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface([self.width, self.height])
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def draw_wall(self):
        draw.rect(window,(self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))

lebar = 700
tinggi = 500

window = display.set_mode((lebar, tinggi))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (lebar, tinggi))

packman = player('hero.png', 5, tinggi - 80, 4)
monster = enemy('cyborg.png', lebar - 80, 280, 2)
final = GameSprite('treasure.png', lebar -120, tinggi -80, 0)
w1 = Wall(154,205,50,150,130,10,400)
w2 = Wall(154,205,50,300,0,10,400)
w3 = Wall(154,205,50,450,130,10,400)
game = True
clock = time.Clock()
finish = False

font.init()
font = font.SysFont('Times new roman',70)
win = font.render('YOU WIN!!!', True, (255,215,0))
lose = font.render ('YOU LOSE!!!', True, (180, 0, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True: 
        window.blit(background,(0,0))
        packman.show()
        packman.update()
        monster.show()
        monster.update()
        final.show()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        if sprite.collide_rect(packman, final):
            finish = True
            window.blit(win,(200,200))
            money.play()
        if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w3):
            finish = True
            window.blit(lose,(200,200))
            kick.play()

    display.update()
    clock.tick(60)