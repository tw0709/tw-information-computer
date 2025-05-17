import pygame
SCREEN_WIDTH=600
SCREEN_HEIGHT=700
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
pygame.init()
pygame.display.set_caption("Drawing")
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock=pygame.time.Clock()
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(WHITE)
    pygame.draw.line(screen,RED,[50,50],[500,50],10)
    pygame.draw.line(screen,GREEN,[50,100],[500,100],10)
    pygame.draw.line(screen,BLUE,[50,150],[500,150],10)
    pygame.draw.rect(screen,RED,[50,200,150,150],4)
    pygame.draw.polygon(screen,GREEN,[[350,200],[250,350],[450,350]],4)
    pygame.draw.circle(screen,BLUE,[150,450],60,4)
    pygame.draw.ellipse(screen,BLUE,[250,400,200,100],0)
    font=pygame.font.SysFont('FixedSys',40,True,False)
    text=font.render("Hello world!",True,BLACK)
    screen.blit(text,[200,600])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()