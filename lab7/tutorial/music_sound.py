import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load("sounds/jump.wav")
pygame.mixer.music.play()
done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
        if event.type == SONG_END:
             print("the song ended!")

    pygame.mixer.music.load("sounds/jump.wav")
    pygame.mixer.music.play(0)
    pygame.display.flip()