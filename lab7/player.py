import pygame

pygame.init()
icon = pygame.image.load("img/iconplayer.png")
pygame.display.set_icon(icon)
w, h = 500, 500
pygame.display.set_caption("MUSIC PLAYER APP")
screen = pygame.display.set_mode((w, h))
bg = pygame.image.load("img/bgplayer.jpg")
bg = pygame.transform.scale(bg, (w, h))
# play = pygame.draw
music_list = ["music/1.mp3", "music/2.mp3", "music/3.mp3", "music/4.mp3", "music/5.mp3"]
MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)
def play_music(i):
    global music_list
    pygame.mixer.music.load(music_list[i])
    pygame.mixer.music.play()

def play_btn(p):
    pygame.draw.circle(screen, (255, 255, 255), (w/2, h/2), 30)
    if p == True:
        pygame.draw.polygon(screen, (0, 0, 0), ((w/2 - 10, h/2 - 15), (w/2 - 10, h/2 + 15), (w/2 + 16, h/2)))
    else:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(w/2 - 10, h/2 - 12.5, 5, 25))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(w/2 + 5, h/2 - 12.5, 5, 25))
    
def next_btn(color):
    pygame.draw.polygon(screen, color, ((w/2 + 60, h/2 - 15), (w/2 + 60, h/2 + 15), (w/2 + 86, h/2)))
    pygame.draw.rect(screen, color, pygame.Rect(w/2 + 85, h/2 - 15, 5, 30))

def prev_btn(color):
    pygame.draw.polygon(screen, color, ((w/2 - 60, h/2 - 15), (w/2 - 60, h/2 + 15), (w/2 - 86, h/2)))
    pygame.draw.rect(screen, color, pygame.Rect(w/2 - 90, h/2 - 15, 5, 30))
i = 0
play_music(i)
font = pygame.font.Font("font/Montserrat-Regular.ttf", 40)
font2 = pygame.font.Font("font/Montserrat-SemiBold.ttf", 15)
text = font.render("music player", "White", False)
instruction = '''press 'key space' ----> to stop music 
press 'key return(enter)' ----> to play music
press 'key right' ----> to play next music
press 'key left' ----> to play previous music
'''
instr_lst = instruction.split("\n")
def text_ins():
    y = 370
    pygame.draw.rect(screen, (107, 90, 166), pygame.Rect(40, y, 340, 85))
 
    for line in instr_lst:
        instruct = font2.render(line, (0, 0, 0), False)
        screen.blit(instruct, (50, y))
        y += 20


p = False
done = False
while not done:
    screen.blit(bg, (0, 0))
    screen.blit(text, (120, 100))
    text_ins()
    play_btn(p)
    next_btn((0, 0, 0))
    prev_btn((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            exit()
        elif event.type == MUSIC_END:
            i += 1
            if i == len(music_list):
                i = 0
            play_music(i)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p = False
                i -= 1
                if i == - len(music_list):
                    i = 0
                play_music(i)
            elif event.key == pygame.K_RIGHT:
                p = False
                i += 1
                if i == len(music_list):
                    i = 0
                play_music(i)
            elif event.key == pygame.K_SPACE:
                p = True
                pygame.mixer.music.pause()
                
                
            elif event.key == pygame.K_RETURN:
                p = False
                pygame.mixer.music.unpause()
                
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_LEFT]:
        prev_btn((255, 255, 255))
    elif pressed[pygame.K_RIGHT]:
        next_btn((255, 255, 255))
    pygame.display.flip()
    