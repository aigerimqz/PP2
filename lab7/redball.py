import pygame, time
pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
icon = pygame.image.load("img/redball.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("RED BALL")
done = False
x, y = w/2, h/2
clock = pygame.time.Clock()
FPS = 60

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            exit()
        
            
    screen.fill((255, 255, 255))
    redball = pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if redball.top <= 0:
            y = 25
        else:
            y -= 20
    
    elif pressed[pygame.K_DOWN]:
        if redball.bottom >= h:
            y = h - 25
        else:
            y += 20
        
    elif pressed[pygame.K_LEFT]:
        if redball.left <= 0:
            x = 25
        else:   
            x -= 20
        
    elif pressed[pygame.K_RIGHT]:
        if redball.right >= w:
            x = w - 25
        else:
            x += 20
      
    

    

    clock.tick(FPS)
    pygame.display.flip()
    