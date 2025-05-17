import pygame
import os
current_path=os.path.dirname(__file__)
assets_path=os.path.join(current_path,"assets")
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
GRAY=(200,200,200)
pygame.init()
pygame.display.set_caption("Keyboard")
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock=pygame.time.Clock()
done=False
keyboard_image=pygame.image.load(os.path.join(assets_path,"keyboard.png"))
keyboard_x=SCREEN_WIDTH/2
keyboard_y=SCREEN_HEIGHT/2
keyboard_dx=0
keyboard_dy=0

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                keyboard_dx=-3
            if event.key==pygame.K_RIGHT:
                keyboard_dx=3
            if event.key==pygame.K_UP:
                keyboard_dy=-3
            if event.key==pygame.K_DOWN:
                keyboard_dy=3
            #p107 키가 놓일 경우 부터터
    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()