"""
참고: 이 코드는 살짝 실패입니다다. 저작권 피하려고 사진 직접 만들었더니
크기때문에 크기가 너무 크게 나오더라고요. 그냥 그래도 사진은 잘 나옵니다.
"""
import pygame
import os
current_path=os.path.dirname(__file__)
assets_path=os.path.join(current_path,"assets")
background_image=pygame.image.load(os.path.join(assets_path,'terrain.png'))
mushroom_image_1=pygame.image.load(os.path.join(assets_path,'mushroom1.png'))
mushroom_image_2=pygame.image.load(os.path.join(assets_path,'mushroom2.png'))
mushroom_image_3=pygame.image.load(os.path.join(assets_path,'mushroom3.png'))
SCREEN_WIDTH=1080
SCREEN_HEIGHT=1080
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
LAND=(160,120,40)
pygame.init()
pygame.display.set_caption("Image")
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock=pygame.time.Clock()
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(LAND)
    screen.blit(background_image,background_image.get_rect())
    screen.blit(mushroom_image_1,[100,80])
    screen.blit(mushroom_image_2, [300,100])
    screen.blit(mushroom_image_3,[450,140])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()