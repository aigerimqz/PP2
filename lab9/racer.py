import pygame, random, time, sys  #libraries
from pygame.locals import *
pygame.init()

#i changed structure of code, because wanted to make code shorter and organised

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
# coinimg = pygame.image.load("images/coin.png")
# coinimg = pygame.transform.scale(coinimg, (50, 50))


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


#three types of enemies as dictionary
enemies_data = ({"path": "Enemy.png"},
                {"path": "enemy_2.png"},
                {"path": "enemy3.png"})
enemies_list = [pygame.image.load("images/" + data["path"]).convert_alpha() for data in enemies_data] #making them as list

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


#types of three coins as dictionary
coins_data = ({"path": "coin.png", "score": 100},
              {"path": "coin2.png", "score" : 50},
              {"path": "coin3.png", "score": 10})
coins_list = [pygame.image.load("images/" + data["path"]).convert_alpha() for data in coins_data] #as list


#generaing numbers for random x 
def generatenum():
    global w
    enemyx = random.randint(30, w - 30)
    coinx = random.randint(30, w - 30)
    if (abs(enemyx - coinx) >= 30):
        return enemyx, coinx
    else:
        return generatenum()



#function which makes coin
def makeCoin(group, direction):
    i = random.randint(0, len(coins_list) - 1) #random type of coin
    x = direction #takes from parameter

    speed = 4 #initial speed
    return Coin(x, speed, coins_list[i], coins_data[i]["score"], group) #returns class with included parameters




speed_enemy = 4 #enemys speed


#function which makes enemy
def makeEnemy1(group, cnt, speed):
    l = [80, 320] #fro first and third line
    i = random.randint(0, len(coins_list) - 1) #generates random
    if cnt % 2 == 0:
        x = random.choice(l) #random choise between list l
    elif cnt % 2 == 1: 
        x = 200
    
    
    # x = random.choice(l)
    speed = speed + random.choice([0.5, 1]) #speed randomly generates
    return Enemy(x, speed, enemies_list[i], group) #return class with included parameters


game_score = 0 #initial game score
all_sprites = pygame.sprite.Group() #makes group of sprites
all_sprites.add(p) #adds player sprite to gruop



#if player collides with coin
def collideCoins():
    global game_score
    for coin in coins:
        all_sprites.add(coin)
        if p.rect.colliderect(coin.rect):
            coincollect.play()
            game_score += coin.score #adds score to total
            print("Current score", game_score)
            coin.kill() #collided coin disappears



#if player is getting closer to enemy, enemy makes sound like "beeeep"
def dangerrr():
    for enemy in enemies:
        all_sprites.add(enemy)
        if abs(p.rect.centerx - enemy.rect.centerx) <= 1: #if thier difference less than 1
            beep.play() #play beep sound



#if player collides with enemy
def collideEnemy():
    for enemy in enemies:
        all_sprites.add(enemy)
        if p.rect.colliderect(enemy.rect):
            crash.play() #play sound
            losegame() #function losing game activates



#when player collides with enemy
def losegame():
    time.sleep(0.5) #waiting 0,5

    screen.fill(red) #background color is red, because user lost the game
    driving.stop() #sound of engine of car stops
    pygame.mixer.music.stop() #bg music stops
    # #some texts
    screen.blit(game_over, (30, 250))
    screen.blit(total, (30, 400))
    screen.blit(scores, (150, 400))
    pygame.display.update()
    for entity in all_sprites:
        entity.kill() #deletes all sprites
    
    time.sleep(2)
    pygame.quit()
    exit()

coins = pygame.sprite.Group() #collecting coin sprites together
enemies = pygame.sprite.Group() #collecting enemy sprites together


speed = 5 #initial speed 
gen = generatenum() #generating num for x

makeCoin(coins, gen[1]) #making first coin
makeEnemy1(enemies, 0, speed_enemy) #making first enemy


# USEREVENT for increasing speed of enemies by time
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

#USEREVENT for increasing speed of enemy by time
enemy1 = pygame.USEREVENT + 1
pygame.time.set_timer(enemy1, 800) #increases speed after every 0.8 second





cnt = 0 #counting every enemy
#loop
while not done:
    gen = generatenum()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #setting for exiting game
            done = True
            pygame.quit()
            exit()
        if event.type == inc_speed:
            if game_score >= 200 and game_score <= 500: 
                speed_enemy = random.choice([5.5, 6])
            if game_score > 500: 
                speed_enemy = random.choice([7.5, 8])
        if event.type == enemy1: #making coin and enemy by time
            cnt += 1
            makeCoin(coins, gen[1])
            makeEnemy1(enemies, cnt, speed_enemy)
            
        
    
    #pressed key for moving player 
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: #when pressing key K_LEFT then player moves to the right
        p.rect.x -= speed
        if p.rect.x < 0:
            p.rect.x = 0
    elif pressed[pygame.K_RIGHT]: #when pressing key K_RIGHT then player moves to the right
        p.rect.x += speed
        if p.rect.x > w - p.rect.width:
            p.rect.x = w - p.rect.width


    

    # activaing fucntions
    dangerrr()
    collideCoins()
    collideEnemy()
    #adding background image and image of coin to score pad, then amount of scores on the screen
    screen.blit(background, (0, 0))
    coins.draw(screen)
    enemies.draw(screen)
    screen.blit(p.image, p.rect)
    

    # screen.blit(coinimg, (w - 50, 2))
    scores = font_small.render(str(game_score), True, black)
    screen.blit(scores, (w - 90, 15))
    




    #If user earns certain score to win the game
    if game_score >= 1000: #I chose score as 1000
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


        
        
    pygame.display.update() #updates the screen
    FramePerSec.tick(FPS) #frames per second
    coins.update(h) #sends the h to coins
    enemies.update(h) #send the h to the coins

