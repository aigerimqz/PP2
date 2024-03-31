import pygame, random, sys
pygame.init()




#size of screen and setting screen
w, h = 1200, 800
screen = pygame.display.set_mode((w, h))


#colors
white = (255, 255, 255)
black = (0, 0, 0)
# gray = (65, 65, 65)
# gold = (215, 255, 0)


#paddle settings
p_w = 300 #width of paddle
p_h = 30 #height of paddle

pad_speed = 20 #speed of paddle
x, y = w//2 - p_w//2, h - p_h//2 - 20 #coordinate of paddle direction

#why function, because to change size of the paddle in any condition, i need parameter to add. It's easier to me to use function
def pad(x, y, p_w, p_h):
    return pygame.Rect((x, y), (p_w, p_h)) 

paddle = pad(x, y, p_w, p_h)
#ball
radius = 15
ball_speed = 7
ball_rect = int(radius * 2 ** 0.5) #because we took ball as outside of the rectangle, and to find the width of the rectangle, we need such this formula sqrt(r^2 + r^2) = r*sqrt(2)
# ball_rect = int(radius * 2)
ball = pygame.Rect(random.randrange(ball_rect, w - ball_rect), h // 2, ball_rect, ball_rect) #why random, because ball should appear in random place when game starts
dx, dy = 1, -1 #cooficient to change direction of ball, for example to up or to bottom to left or to right in some conditions

#unbeakable blocks
stone_block = pygame.image.load("images/stone_block.jpg") #i chose unbreakable block as stone, so loaded stone image
stone_block = pygame.transform.scale(stone_block, (100, 50)) # transforming image to needed size
unbreak_block_list = [pygame.Rect(200 + 400 * i, 340 + 70 * j, 100, 50) for i in range(3) for j in range(1)] #we have 3 unbreakable blocks



#blocks
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)] #there is 40 blocks we generated it with loop 
color_list = [(random.randrange(1, 256), random.randrange(1, 256), random.randrange(1, 256)) for i in range(10) for j in range(4)] #for those blocks we need to add random colors


#bonus blocks
gold_block = pygame.image.load("images/goldblock.webp") #bonus block! I chose bonus block as gold brick, so this is image of gold brick
gold_block = pygame.transform.scale(gold_block, (100, 50)) #transforming to needed size
bonus_list = random.choices(block_list, k = 2) #in this case, I chose bonus block randomly between block_list, after that bonus blocks will appear randomly and it makes game more interesting and harder



#collision function
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left #when ball hits rectangle from left side
    else:
        delta_x = rect.right - ball.left #when ball hits rectangle from right side
    if dy > 0:
        delta_y = ball.bottom - rect.top #when ball hits rectangle from top

    else:
        delta_y = rect.bottom - ball.top #when ball hits rectangle from bottom
    
    if abs(delta_x - delta_y) < 10: #it's condition when ball hits rectangle from corner side
        dx, dy = -dx, -dy
    elif delta_x > delta_y: #when x side is greater, then y side will move in opposite direction
        dy = -dy
    elif delta_y > delta_x: #when y side is greater, then x side will move in opposite direction
        dx = -dx

    return dx, dy


#user events to change smth by time
increase_speed = pygame.USEREVENT + 1
pygame.time.set_timer(increase_speed, 1000) #increases speed after every 1 second

shrink_pad = pygame.USEREVENT + 1
pygame.time.set_timer(shrink_pad, 1000) #shrinks paddle after every 1 second


#design part
score = 0
font2 = pygame.font.SysFont("OCR A Extended", 30)
scoreText = font2.render(f"Score: {score}", True, black) #score text
scoreRect = scoreText.get_rect()
scoreRect.center = (100, 20)


font = pygame.font.SysFont("OCR A Extended", 70)

pygame.display.set_caption("ARKANOID") #caption of the game
icon = pygame.image.load("images/arkanoid_icon.png")
pygame.display.set_icon(icon)

win = font.render("WIN!", True, black) #win text
game_over = font.render("GAME OVER", True, white) #game over text


winrect = win.get_rect()
game_overrect = game_over.get_rect()
winrect.center = game_overrect.center = (w//2, h//2)


#sound effects
collision_sound = pygame.mixer.Sound("sounds/catch.mp3") #sound when hits the block
tapping = pygame.mixer.Sound("sounds/tap2.mp3") #sound when hits any side of screen or unbreakable block
bonus_earning = pygame.mixer.Sound("sounds/bonus.mp3") #sound when earns bonus


cnt = 0 #timer for timing bonus 

#fps
clock = pygame.time.Clock()
FPS = 60

#boolean to stop the loop
done = False




#loop
while not done:
    for event in pygame.event.get():
        if event.type == increase_speed:
            ball_speed += 0.5  #adds 0.5 to speed
        if event.type == shrink_pad:
            p_w -= 5 #minus from width of paddle to shrink
            paddle = pad(paddle.x, paddle.y, p_w, p_h) #new parameters of paddle
            
        if event.type == pygame.QUIT: #when quiting game
            done = True
            pygame.quit()
            exit()

    

    screen.fill(black) #filling to black
    

    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list) if block not in bonus_list] #drawing every block from block_list with its colors by using enumarate
    [screen.blit(stone_block, block) for block in unbreak_block_list] #adding stone block to screen
    [screen.blit(gold_block, block) for block in bonus_list] #adding gold block to screen
    pygame.draw.rect(screen ,white, paddle) #drawing paddle
    pygame.draw.circle(screen, white, ball.center, radius) #drawing our ball
    


    #ball movement
    ball.x += ball_speed * dx #moves by mean of dx
    ball.y += ball_speed * dy #moves by mean of dy


    if ball.centerx < radius or ball.centerx > w - radius: #to not going outside of screen
        tapping.play()
        dx = -dx
    if ball.centery < radius + 50: #to show ball full
        tapping.play()
        dy = -dy
    if ball.colliderect(paddle) and dy > 0: #if ball hits paddle and dy is positive
        tapping.play() #sound effect
        dx, dy = detect_collision(dx, dy, ball, paddle) #function 
    
    unbreak_collide = ball.collidelist(unbreak_block_list) #if ball hits the unbreakable block
    if unbreak_collide != -1:
        tapping.play() #sounf effect
        unbreak_rect = unbreak_block_list[-1]  
        dx, dy = detect_collision(dx, dy, ball, unbreak_rect) #applying function

    hit_index = ball.collidelist(block_list) #when ball hits block
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index) #popping from list
        hit_color = color_list.pop(hit_index) #popping its color
        dx, dy = detect_collision(dx, dy, ball, hit_rect) #appluing function
        score += 1 #adding score
        collision_sound.play() #sound effect

    scoreText = font2.render(f"Score: {score}", True, white) #text which shoes amount of scores
    screen.blit(scoreText, scoreRect)

    

    get_bonus = ball.collidelist(bonus_list) #when ball hits the bonus brick
    if get_bonus != -1:
        cnt = 0 #timer is 0 
        radius = 40 #radius of ball becomes bigger, since our bonus is big ball
        p_w = 1000 #width of paddle becomes longer
        paddle = pad(paddle.x, paddle.y, p_w, p_h) #new parameters of paddle
        hit_bonus = bonus_list.pop(get_bonus) #popping from list
        block_list.pop(get_bonus)
        dx, dy = detect_collision(dx, dy, ball, hit_bonus) #applying function
        bonus_earning.play() #sound effect
         
    if cnt > 300: #bonus only for 5 seconds
        radius = 15 #then raduis of the ball becomes smaller again
       

    if ball.bottom > h: #if ball goes away from screen, then you're loser
        tapping.stop()
        screen.fill(black) #filling black, since it's tragedy((((
        screen.blit(game_over, game_overrect)

    elif not len(block_list): #if you hit all of the blocks then you're WINNER!
        tapping.stop()
        screen.fill(white) #filling white, since it's happiness)))
        screen.blit(win, winrect)
        



    pressed = pygame.key.get_pressed() #when key is pressed
    if pressed[pygame.K_RIGHT] and paddle.right < w: #when pressing key K_RIGHT then paddle moves to the right
        paddle.right += pad_speed
    if pressed[pygame.K_LEFT] and paddle.left > 0: #when pressing key K_LEFT then paddle moves to the left
        paddle.left -= pad_speed

    cnt += 1 #counting the time to bonus timer 

    clock.tick(FPS) #applying fps
    pygame.display.update() #updating every time