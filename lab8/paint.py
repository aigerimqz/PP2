import pygame
pygame.init()
w, y = 800, 500 #size of the screen
screen = pygame.display.set_mode((w, y)) #screen setting
drawshape = "" #name of the shape



#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
orange = (255, 128, 0)
pink = (255, 0, 127)
aqua = (0, 255, 255)



color = white #color by default is white in our case
colorname = "white"
eraser = False #by default eraser is not turned on yet
pygame.display.set_caption("PAINT") #name of our app
icon = pygame.image.load("images/paint.png")
pygame.display.set_icon(icon)


text_surface = pygame.Surface((350, 200)) #surface for our text bar
font = pygame.font.SysFont("Comic Sans MS", 20) #font 
font2 = pygame.font.SysFont("Comic Sans MS", 10) #font


#main information about game
info = "To choose shape: SHIFT + 'r' or 'c'(r - rect, c - circle)\n To choose color: CTRL + r/b/y/o/p/w/g/a first letters of colors\n To choose eraser: SHIFT + 'e'"
infotext = info.split("\n") #splitting this big text by \n
def infoprint(surf): #function to blit every way of the big text
    y = 120
    for i in infotext:
        text = font2.render(i, True, white)
        surf.blit(text, (20, y))
        y += 20


painting = False #painting by default is False, since we are not painting yet

done = False #boolean for loop


#loop
while not done:
    pressed = pygame.key.get_pressed() #when any key is pressed
    shift_held = pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT] #when pressed all key shift
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL] #when prssedall key control
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #quitting the game
            done = True
            exit()
        if event.type == pygame.KEYDOWN: #when some key is down
            if event.key == pygame.K_r and shift_held: #when key 'r' and pressing shift
                drawshape = 'rectangle' #then our chosen shape is rectangle
            elif event.key == pygame.K_c and shift_held: #when key 'c' and pressing shift
                drawshape = 'circle' #then our chosen shape is circle
            elif event.key == pygame.K_r and ctrl_held: #when key 'r' and pressing ctrl
                color = red #them our chosen color is red
                colorname = "red" 
            elif event.key == pygame.K_b and ctrl_held: #when key 'b' and pressing ctrl
                color = blue   #them our chosen color is blue
                colorname = "blue"
            elif event.key == pygame.K_g and ctrl_held:  #when key 'g' and pressing ctrl
                color = green  #them our chosen color is green
                colorname = "green"
            elif event.key == pygame.K_y and ctrl_held: #when key 'y' and pressing ctrl
                color = yellow  #them our chosen color is yellow
                colorname = "yellow"
            elif event.key == pygame.K_p and ctrl_held: #when key 'p' and pressing ctrl
                color = pink   #them our chosen color is pink
                colorname = "pink"
            elif event.key == pygame.K_a and ctrl_held: #when key 'a' and pressing ctrl
                color = aqua   #them our chosen color is aqua
                colorname = "aqua" 
            elif event.key == pygame.K_o and ctrl_held: #when key 'o' and pressing ctrl
                color = orange  #them our chosen color is orange
                colorname = "orange"
            elif event.key == pygame.K_w and ctrl_held: #when key 'w' and pressing ctrl
                color = white   #them our chosen color is white
                colorname = "white"


            #eraser
            elif event.key == pygame.K_e and shift_held: #when key 'e' and pressing shift
                color = black #similar with color of background, since its eraser
                colorname = "eraser"
                eraser = not eraser #mode
         
        if event.type == pygame.MOUSEBUTTONDOWN: #when we click the button of mouse
            if event.button == 1: #left button of mouse
                painting = True #then it's means that we are painting
        if event.type == pygame.MOUSEBUTTONUP: #when we not click the button og the mouse
            if event.button == 1:
                painting = False #then painting is False
    


    screen.blit(text_surface, (0, 0)) #adding surface for the text to the screen
    text_surface.fill(black) #filling it black
    pos = pygame.mouse.get_pos()  #getting the position of cursor when we clicked
    colortext = font.render(f"Chosen color: {colorname}", True, color) #name of chosen color
    text_surface.blit(colortext, (20, 20))
    shapetext = font.render(f"Chosen shape: {drawshape}", True, color) #name of chosen shape
    text_surface.blit(shapetext, (20, 50))
    infoprint(text_surface) #applying function
    

    if eraser: 
        mode = "ON" #if true
    else:
        mode = "OFF" #if false

    erasertext = font.render(f"Eraser is {mode}", True, white)   #mode of eraser as a text
    screen.blit(erasertext, (20, 80))  
    if painting == True: #when we are painting
        if drawshape == "rectangle": #if shape is rectangle then we draw the rectangle 
            pygame.draw.rect(screen, color, (pos[0], pos[1], 70, 70)) #using current color and position
        elif drawshape == "circle": #if shape is circle then we draw the circle
            pygame.draw.circle(screen, color, pos, 30) #using current color and position
    
    

    pygame.display.update() #updating the screen
