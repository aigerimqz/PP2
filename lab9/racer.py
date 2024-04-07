import pygame, random, time, sys  #libraries
from pygame.locals import *
pygame.init()


#bool for loop
done = False

#FPS
FPS = 60
FramePerSec = pygame.time.Clock()


#colors
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)


#sizes of screen
w, h = 400, 600
# speed = 5
# score = 0

#fonts for texts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)
winner = font.render("Good job!", True, black)
total = font_small.render("Total score: ", True, black)


#sound effect
coincollect = pygame.mixer.Sound("sounds/coincollect.mp3")
crash = pygame.mixer.Sound("sounds/crash.wav")
beep = pygame.mixer.Sound("sounds/bebeep.mp3")
driving = pygame.mixer.Sound('sounds/driving.mp3')
driving.play(-1)
#background image and image of coin
background = pygame.image.load("images/AnimatedStreet.png")
coinimg = pygame.image.load("images/coin.png")
coinimg = pygame.transform.scale(coinimg, (50, 50))


#screen setting
screen = pygame.display.set_mode((w, h))

#caption setting and background music
icon = pygame.image.load("images/Player.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Car Adventure!")
pygame.mixer.music.load("sounds/background.wav")
pygame.mixer.music.play(-1) #plays while game stops



#class Player where some functions            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png") #image of player
        self.rect = self.image.get_rect() #rectangel of player
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]: #when user presses key K_LEFT, moves 5 pixels on left direction
                self.rect.move_ip(-5, 0)
        if self.rect.right < w:
            if pressed_keys[pygame.K_RIGHT]: #when user presses key K_RIGHT, moves 5 pixels on right direction
                self.rect.move_ip(5, 0)
    



#class Enemy where some functions
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf #image of enemy
        self.image = pygame.transform.scale(self.image, (48, 93))
        self.rect = self.image.get_rect(center = (x, 0)) #rectangle of enemy
        self.speed = speed
        self.add(group)
        self.x = x
    def update(self, *args):

        if (self.rect.y < args[0] - 20): #when bottom side of coin.rect touches a by y-axis, the coin disappears
            self.rect.y += self.speed
        else:
            self.kill()



enemies_data = ({"path": "Enemy.png"},
                {"path": "enemy_2.png"},
                {"path": "enemy3.png"})
enemies_list = [pygame.image.load("images/" + data["path"]).convert_alpha() for data in enemies_data]

#class Coin where some functions
class Coin(pygame.sprite.Sprite):
    
    def __init__(self, x, speed, surf, score, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf #image of coin
        self.image = pygame.transform.scale(self.image, (50, 50)) #transformed into one size
        self.rect = self.image.get_rect(center = (x, 0)) #rectangle of coin, appears in random places by x-axis
        self.speed = speed
        self.score = score
        self.point = x
        self.add(group)
    def update(self, *args):
        if (self.rect.y < args[0] - 20): #when bottom side of coin.rect touches a by y-axis, the coin disappears
            self.rect.y += self.speed
        else:
            self.kill()

p = Player()
# e1 = Enemy()
# coin = Coin()


coins_data = ({"path": "coin.png", "score": 100},
              {"path": "coin2.png", "score" : 50},
              {"path": "coin3.png", "score": 10})
coins_list = [pygame.image.load("images/" + data["path"]).convert_alpha() for data in coins_data]



def generatenum():
    global w
    enemyx = random.randint(30, w - 30)
    coinx = random.randint(30, w - 30)
    if (abs(enemyx - coinx) >= 30):
        return enemyx, coinx
    else:
        return generatenum()




def makeCoin(group, direction):
    i = random.randint(0, len(coins_list) - 1)
    x = direction

    speed = 4
    return Coin(x, speed, coins_list[i], coins_data[i]["score"], group)




speed_enemy = 4
def makeEnemy1(group, cnt, speed):
    l = [80, 320]
    i = random.randint(0, len(coins_list) - 1)
    if cnt % 2 == 0:
        x = random.choice(l)
    elif cnt % 2 == 1:
        x = 200
    
    
    # x = random.choice(l)
    speed = speed + random.choice([0.5, 1])
    return Enemy(x, speed, enemies_list[i], group)


game_score = 0
all_sprites = pygame.sprite.Group()
all_sprites.add(p)




def collideCoins():
    global game_score
    for coin in coins:
        all_sprites.add(coin)
        if p.rect.colliderect(coin.rect):
            coincollect.play()
            game_score += coin.score
            coin.kill()


def dangerrr():
    for enemy in enemies:
        all_sprites.add(enemy)
        if abs(p.rect.centerx - enemy.rect.centerx) <= 1:
            print(p.rect.centerx - enemy.rect.centerx)
            beep.play()


def collideEnemy():
    for enemy in enemies:
        all_sprites.add(enemy)
        if p.rect.colliderect(enemy.rect):
            crash.play()
            losegame()


# def collideCoinEnemy():
#     for enemy in enemies:
#         if enemy.rect.colliderect(coin.rect):
#             enemy.kill()
#             coin.kill()



def losegame():
    time.sleep(0.5)

    screen.fill(red) #background color is red, because user lost the game
    driving.stop()
    pygame.mixer.music.stop()
    # #some texts
    screen.blit(game_over, (30, 250))
    screen.blit(total, (30, 400))
    screen.blit(scores, (150, 400))
    pygame.display.update()
    for entity in all_sprites:
        entity.kill() #deletes all sprites
    
    time.sleep(3)
    pygame.quit()
    exit()
    # screen.fill(red)
    # for entity in all_sprites:
    #     entity.kill()
    
    # time.sleep(5)
    # exit()

coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()

list_x = []
list_xe = []

speed = 5
gen = generatenum()

makeCoin(coins, gen[1])
makeEnemy1(enemies, 0, speed_enemy)

# enemies = pygame.sprite.Group() #sprite group of class Enemy
# enemies.add(e1)
# coinscores = pygame.sprite.Group() #sprite group of class Coin
# coinscores.add(coin)
# all_sprites = pygame.sprite.Group() #all classes in this sprite group
# all_sprites.add(p1)
# all_sprites.add(e1)
# all_sprites.add(coin)
# player_enemy = pygame.sprite.Group() #sprite for player and enemy classes, because thier move() function doesn't have any parameter not like a coin class
# player_enemy.add(p1)
# player_enemy.add(e1)

# USEREVENT for increasing speed of enemies by time
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)
enemy1 = pygame.USEREVENT + 1
pygame.time.set_timer(enemy1, 2000) #increases speed after every 1 second

# enemy2 = pygame.USEREVENT + 1
# pygame.time.set_timer(enemy2, 2000) #shrinks paddle after every 1 second

# enemy3 = pygame.USEREVENT + 1
# pygame.time.set_timer(enemy3, 1500) #shrinks paddle after every 1 second



cnt = 0
#loop
while not done:
    gen = generatenum()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #setting for exiting game
            done = True
            pygame.quit()
            exit()
        if event.type == inc_speed:
            if game_score == 200:
                speed_enemy += 1
            # speed += 1
        if event.type == enemy1: #increasing speed by the time
            cnt += 1
            makeCoin(coins, gen[1])
            makeEnemy1(enemies, cnt, speed_enemy)
            
        # if event.type == enemy2:
        #     makeEnemy2(enemies)

        # if event.type == enemy3:
        #     makeEnemy3(enemies)
    print(cnt)
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        p.rect.x -= speed
        if p.rect.x < 0:
            p.rect.x = 0
    elif pressed[pygame.K_RIGHT]:
        p.rect.x += speed
        if p.rect.x > w - p.rect.width:
            p.rect.x = w - p.rect.width


    

    # print(makeCoin().x)
    dangerrr()
    collideCoins()
    collideEnemy()
    # collideCoinEnemy()
    #adding background image and image of coin to score pad, then amount of scores on the screen
    screen.blit(background, (0, 0))
    coins.draw(screen)
    enemies.draw(screen)
    screen.blit(p.image, p.rect)
    

    screen.blit(coinimg, (w - 50, 2))
    scores = font_small.render(str(game_score), True, black)
    screen.blit(scores, (w - 90, 15))
    

    

    #Moving all sprites
    # for entity in all_sprites:
    #     screen.blit(entity.image, entity.rect)
    # for entity in player_enemy:
    #     entity.move()
    # for entity in coinscores:
    #     entity.move(600) #there is as parameter is 600, because initially, coin should appear before touching bottom of the screen



    #Collision detection with player and enemies
    # if pygame.sprite.spritecollideany(p1, enemies):
    #     pygame.mixer.Sound("sounds/crash.wav").play()
    #     time.sleep(0.5)

    #     screen.fill(red) #background color is red, because user lost the game

    #     #some texts
    #     screen.blit(game_over, (30, 250))
    #     screen.blit(total, (30, 400))
    #     screen.blit(scores, (150, 400))
    #     pygame.display.update()
    #     for entity in all_sprites:
    #         entity.kill() #deletes all sprites
        
    #     time.sleep(2)
    #     pygame.quit()
    #     exit()


    #If user earns certain score to win the game
    if game_score >= 1000: #I chose score as 20
        pygame.mixer.music.pause() #background music stops
        
        screen.fill(green) #screen is green, because user is winner
        #some texts
        screen.blit(winner, (30, 250)) 
        screen.blit(total, (30, 400))
        screen.blit(scores, (150, 400))
        
        pygame.display.update()
        
        pygame.mixer.Sound("sounds/victory.wav").play() #victory sound
        time.sleep(pygame.mixer.Sound("sounds/victory.wav").get_length()) #until victory sound ends
        for entity in all_sprites:
            entity.kill() #deletes all sprites

        time.sleep(2)
        pygame.quit()
        exit()



    # # Collision detection with player and coin
    # if p1.rect.colliderect(coin.rect): #when p1 and coin intersect with each other
    #     pygame.mixer.Sound("sounds/coincollect.mp3").play() #plays sound when car touches coin
    #     for entity in coinscores:
    #         entity.move(474)
    #     score += 1 #adding the score when there is collision
        
    # #Collision detection with enemy and coin, since they can encounter with each other or coin can appear on the enemy car, it's not beautiful 
    # if e1.rect.colliderect(coin.rect):
    #     for entity in coinscores:
    #         entity.move(0) #if enemy and coin intersect, coin disappear until showing on the screen
    
    
    # pos = pygame.mouse.get_pos()
    # print(pos)   

        
        
    pygame.display.update() #updates the screen
    FramePerSec.tick(FPS) #frames per second
    coins.update(h)
    enemies.update(h)

