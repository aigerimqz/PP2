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
speed = 5
score = 0

#fonts for texts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)
winner = font.render("Good job!", True, black)
total = font_small.render("Total score: ", True, black)


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


#class Enemy where some functions
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Enemy.png") #image of enemy
        self.rect = self.image.get_rect() #rectangle of enemy
        self.rect.center = (random.randint(40, w - 40), 0) # rectangle center it's y-axis  is 0, because it starts from top of the screen

    def move(self):

        self.rect.move_ip(0, speed) #moves by y-axis
        if (self.rect.bottom > 600): #when touches 600 coordinates disappears
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0) #randomly coordinate for x-axis, for y-axis is 0 


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
    

#class Coin where some functions
class Coin(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/coin.png") #image of coin
        self.image = pygame.transform.scale(self.image, (50, 50)) #transformed into one size
        self.rect = self.image.get_rect() #rectangle of coin
        self.rect.center = (random.randint(30, 370), 0) #appears in random places by x-axis
    def move(self, a):
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > a): #when bottom side of coin.rect touches a by y-axis, the coin disappears
            # score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

p1 = Player()
e1 = Enemy()
coin = Coin()

enemies = pygame.sprite.Group() #sprite group of class Enemy
enemies.add(e1)
coinscores = pygame.sprite.Group() #sprite group of class Coin
coinscores.add(coin)
all_sprites = pygame.sprite.Group() #all classes in this sprite group
all_sprites.add(p1)
all_sprites.add(e1)
all_sprites.add(coin)
player_enemy = pygame.sprite.Group() #sprite for player and enemy classes, because thier move() function doesn't have any parameter not like a coin class
player_enemy.add(p1)
player_enemy.add(e1)



#USEREVENT for increasing speed of enemies by time
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)


#loop
while not done:
    for event in pygame.event.get():
        if event.type == inc_speed: #increasing speed by the time
            speed += 1
        if event.type == pygame.QUIT: #setting for exiting game
            done = True
            pygame.quit()
            exit()


    #adding background image and image of coin to score pad, then amount of scores on the screen
    screen.blit(background, (0, 0))
    screen.blit(coinimg, (w - 50, 2))
    scores = font_small.render(str(score), True, black)
    screen.blit(scores, (w - 70, 15))
    

    #Moving all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    for entity in player_enemy:
        entity.move()
    for entity in coinscores:
        entity.move(600) #there is as parameter is 600, because initially, coin should appear before touching bottom of the screen



    #Collision detection with player and enemies
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound("sounds/crash.wav").play()
        time.sleep(0.5)

        screen.fill(red) #background color is red, because user lost the game

        #some texts
        screen.blit(game_over, (30, 250))
        screen.blit(total, (30, 400))
        screen.blit(scores, (150, 400))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() #deletes all sprites
        
        time.sleep(2)
        pygame.quit()
        exit()


    #If user earns certain score to win the game
    if score == 20: #I chose score as 20
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



    # Collision detection with player and coin
    if p1.rect.colliderect(coin.rect): #when p1 and coin intersect with each other
        pygame.mixer.Sound("sounds/coincollect.mp3").play() #plays sound when car touches coin
        for entity in coinscores:
            entity.move(474)
        score += 1 #adding the score when there is collision
        
    #Collision detection with enemy and coin, since they can encounter with each other or coin can appear on the enemy car, it's not beautiful 
    if e1.rect.colliderect(coin.rect):
        for entity in coinscores:
            entity.move(0) #if enemy and coin intersect, coin disappear until showing on the screen
    
    
        

        
        
    pygame.display.update() #updates the screen
    FramePerSec.tick(FPS) #frames per second