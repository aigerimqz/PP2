import pygame
import datetime

pygame.init()
main_clock = pygame.image.load("img/main-clock.png")

# main_clock = pygame.transform.scale(main_clock, (800, 800))
screen = pygame.display.set_mode((main_clock.get_size()))


def blitRotate(scr, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    scr.blit(rotated_image, rotated_image_rect)

s_hand = pygame.image.load("img/right-hand.png")
m_hand = pygame.image.load("img/left-hand.png")
sw, sh = s_hand.get_size()
mw, mh = m_hand.get_size()
done = False

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pos = (screen.get_width()/2, screen.get_height()/2)
    screen.blit(main_clock, (0, 0))  
    scnd = datetime.datetime.now().second
    print(scnd)
    mnt = datetime.datetime.now().minute
    s_angle = 450 - (scnd * 6)
    m_angle = 450 - (mnt * 6)
    blitRotate(screen, s_hand, pos, (sw/2, sh/2), s_angle)
    blitRotate(screen, m_hand, pos, (mw/2, mh/2), m_angle)
    
    pygame.display.flip()
