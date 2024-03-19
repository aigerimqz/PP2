import pygame, datetime
pygame.init()
screen = pygame.display.set_mode((829, 836))
pygame.display.set_caption("Mickey Mouse Clock")
main_clock = pygame.image.load("img/main-clock.png").convert()
main_clock = pygame.transform.scale(main_clock, (829, 836))


def rot(scr, item, pos, expos, angle):
    itemrect = item.get_rect(topleft = (pos[0] - expos[0], pos[1] - expos[1]))
    c = pygame.math.Vector2(pos) - itemrect.center
    rotoffset = c.rotate(-angle)
    cntr = (pos[0] - rotoffset.x, pos[1] - rotoffset.y)
    rotitem = pygame.transform.rotate(item, angle)
    rotitemrect = rotitem.get_rect(center = cntr)
    scr.blit(rotitem, rotitemrect)
    


clock = pygame.time.Clock()

s_hand = pygame.image.load("img/right-hand.png")
m_hand = pygame.image.load("img/left-hand.png")
sw, sh = s_hand.get_size()
mw, mh = m_hand.get_size()
done = False



while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            exit()
    
    pos = (screen.get_width()/2, screen.get_height()/2)
    screen.blit(main_clock, (0, 0))  
    scnd = datetime.datetime.now().second
    mnt = datetime.datetime.now().minute
    s_angle = 439 - scnd * 6
    m_angle = 448 - mnt * 6
    print(scnd)
    rot(screen, s_hand, pos, (sw/2, sh/2), s_angle)
    rot(screen, m_hand, pos, (mw/2, mh/2), m_angle)

    
    
    pygame.display.flip()