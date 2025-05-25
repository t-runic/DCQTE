
import pygame, sys, random
from pygame.locals import *

pygame.init()

Display_Surface = pygame.display.set_mode((650, 500))

pygame.display.set_caption("Domain Clash Quick-Time-Event")

White = (255, 255, 255)
Black = (0, 0, 0)
Cyan = (159, 237, 237)
Red = (255, 60, 60)

FPS = 30
fpsClock = pygame.time.Clock()

input1 = True
input2 = False
input3 = False
input4 = False
input5 = False
input6 = False
inputscomplete = False
inputsfailed = False
newround = True
count = 0
score = 0
key_font = pygame.font.SysFont('Verdana', 40)
text_font = pygame.font.SysFont('Verdana', 20)

while True:

    Display_Surface.fill(Black)

    if input1 and not inputsfailed:
        pygame.draw.rect(Display_Surface, White, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (502, 215, 70, 70), 0)
    elif input1 and inputsfailed:
        pygame.draw.rect(Display_Surface, Red, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (502, 215, 70, 70), 0)
        if count > 5:
            input1 = False
            input2 = False
            input3 = False
            input4 = False
            input5 = False
            input6 = False
            inputscomplete = False
            inputsfailed = False
            score = 0
    elif input2 and not inputsfailed:
        pygame.draw.rect(Display_Surface, Cyan, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (502, 215, 70, 70), 0)
    elif input2 and inputsfailed:
        pygame.draw.rect(Display_Surface, Cyan, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Red, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (502, 215, 70, 70), 0)
        if count > 5:
            input1 = False
            input2 = False
            input3 = False
            input4 = False
            input5 = False
            input6 = False
            inputscomplete = False
            inputsfailed = False
            score = 0
    elif input3 and not inputsfailed:
        pygame.draw.rect(Display_Surface, Cyan, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (502, 215, 70, 70), 0)
    elif input3 and inputsfailed:
        pygame.draw.rect(Display_Surface, Cyan, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Red, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (502, 215, 70, 70), 0)
        if count > 5:
            input1 = False
            input2 = False
            input3 = False
            input4 = False
            input5 = False
            input6 = False
            inputscomplete = False
            inputsfailed = False
            score = 0
    elif input4 and not inputsfailed:
        pygame.draw.rect(Display_Surface, Cyan, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (502, 215, 70, 70), 0)
    elif input4 and inputsfailed:
        pygame.draw.rect(Display_Surface, Cyan, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Red, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (502, 215, 70, 70), 0)
        if count > 5:
            input1 = False
            input2 = False
            input3 = False
            input4 = False
            input5 = False
            input6 = False
            inputscomplete = False
            inputsfailed = False
            score = 0
    elif input5 and not inputsfailed:
        pygame.draw.rect(Display_Surface, Cyan, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (502, 215, 70, 70), 0)
    elif input5 and inputsfailed:
        pygame.draw.rect(Display_Surface, Cyan, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Red, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (502, 215, 70, 70), 0)
        if count > 5:
            input1 = False
            input2 = False
            input3 = False
            input4 = False
            input5 = False
            input6 = False
            inputscomplete = False
            inputsfailed = False
            score = 0
    elif input6 and not inputsfailed:
        pygame.draw.rect(Display_Surface, Cyan, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, White, (502, 215, 70, 70), 0)
    elif input6 and inputsfailed:
        pygame.draw.rect(Display_Surface, Cyan, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Red, (502, 215, 70, 70), 0)
        if count > 5:
            input1 = False
            input2 = False
            input3 = False
            input4 = False
            input5 = False
            input6 = False
            inputscomplete = False
            inputsfailed = False
            score = 0
    elif inputscomplete and count <= 5:
        pygame.draw.rect(Display_Surface, Cyan, (77, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (162, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (247, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (332, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (417, 215, 70, 70), 0)
        pygame.draw.rect(Display_Surface, Cyan, (502, 215, 70, 70), 0)
    else:
        input1 = True
        input2 = False
        input3 = False
        input4 = False
        input5 = False
        input6 = False
        inputscomplete = False
        inputsfailed = False
        newround = True
        count = 0

    if newround == True:
        newinput1 = random.choice(['W', 'E', 'R', 'T', 'Y', 'U', 'S', 'D', 'F', 'G', 'H', 'J', 'X', 'C', 'V', 'B', 'N', 'M'])
        newinput2temp = ['W', 'E', 'R', 'T', 'Y', 'U', 'S', 'D', 'F', 'G', 'H', 'J', 'X', 'C', 'V', 'B', 'N', 'M']
        newinput2temp.remove(newinput1)
        newinput2 = random.choice(newinput2temp)
        newinput3temp = ['W', 'E', 'R', 'T', 'Y', 'U', 'S', 'D', 'F', 'G', 'H', 'J', 'X', 'C', 'V', 'B', 'N', 'M']
        newinput3temp.remove(newinput2)
        newinput3 = random.choice(newinput3temp)
        newinput4temp = ['W', 'E', 'R', 'T', 'Y', 'U', 'S', 'D', 'F', 'G', 'H', 'J', 'X', 'C', 'V', 'B', 'N', 'M']
        newinput4temp.remove(newinput3)
        newinput4 = random.choice(newinput4temp)
        newinput5temp = ['W', 'E', 'R', 'T', 'Y', 'U', 'S', 'D', 'F', 'G', 'H', 'J', 'X', 'C', 'V', 'B', 'N', 'M']
        newinput5temp.remove(newinput4)
        newinput5 = random.choice(newinput5temp)
        newinput6temp = ['W', 'E', 'R', 'T', 'Y', 'U', 'S', 'D', 'F', 'G', 'H', 'J', 'X', 'C', 'V', 'B', 'N', 'M']
        newinput6temp.remove(newinput5)
        newinput6 = random.choice(newinput6temp)
        newround = False

    key1 = key_font.render(newinput1, True, Black)
    key2 = key_font.render(newinput2, True, Black)
    key3 = key_font.render(newinput3, True, Black)
    key4 = key_font.render(newinput4, True, Black)
    key5 = key_font.render(newinput5, True, Black)
    key6 = key_font.render(newinput6, True, Black)
    scoretext = text_font.render("Score: " + str(score), True, White)

    Display_Surface.blit(key1, (112 - key1.get_width() // 2, 250 - key1.get_height() // 2))
    Display_Surface.blit(key2, (197 - key2.get_width() // 2, 250 - key2.get_height() // 2))
    Display_Surface.blit(key3, (282 - key3.get_width() // 2, 250 - key3.get_height() // 2))
    Display_Surface.blit(key4, (367 - key4.get_width() // 2, 250 - key4.get_height() // 2))
    Display_Surface.blit(key5, (452 - key5.get_width() // 2, 250 - key5.get_height() // 2))
    Display_Surface.blit(key6, (537 - key6.get_width() // 2, 250 - key6.get_height() // 2))
    Display_Surface.blit(scoretext, (320 - scoretext.get_width() // 2, 450 - scoretext.get_height() // 2))

    for event in pygame.event.get():
        if input1 and inputsfailed == False and event.type == KEYDOWN:
            if newinput1 == 'W' and event.key == K_w:
                input1 = False
                input2 = True
            elif newinput1 == 'E' and event.key == K_e:
                input1 = False
                input2 = True
            elif newinput1 == 'R' and event.key == K_r:
                input1 = False
                input2 = True
            elif newinput1 == 'T' and event.key == K_t:
                input1 = False
                input2 = True
            elif newinput1 == 'Y' and event.key == K_y:
                input1 = False
                input2 = True
            elif newinput1 == 'U' and event.key == K_u:
                input1 = False
                input2 = True
            elif newinput1 == 'S' and event.key == K_s:
                input1 = False
                input2 = True
            elif newinput1 == 'D' and event.key == K_d:
                input1 = False
                input2 = True
            elif newinput1 == 'F' and event.key == K_f:
                input1 = False
                input2 = True
            elif newinput1 == 'G' and event.key == K_g:
                input1 = False
                input2 = True
            elif newinput1 == 'H' and event.key == K_h:
                input1 = False
                input2 = True
            elif newinput1 == 'J' and event.key == K_j:
                input1 = False
                input2 = True
            elif newinput1 == 'X' and event.key == K_x:
                input1 = False
                input2 = True
            elif newinput1 == 'C' and event.key == K_c:
                input1 = False
                input2 = True
            elif newinput1 == 'V' and event.key == K_v:
                input1 = False
                input2 = True
            elif newinput1 == 'B' and event.key == K_b:
                input1 = False
                input2 = True
            elif newinput1 == 'N' and event.key == K_n:
                input1 = False
                input2 = True
            elif newinput1 == 'M' and event.key == K_m:
                input1 = False
                input2 = True
            else:
                inputsfailed = True
        elif input2 and inputsfailed == False and event.type == KEYDOWN:
            if newinput2 == 'W' and event.key == K_w:
                input2 = False
                input3 = True
            elif newinput2 == 'E' and event.key == K_e:
                input2 = False
                input3 = True
            elif newinput2 == 'R' and event.key == K_r:
                input2 = False
                input3 = True
            elif newinput2 == 'T' and event.key == K_t:
                input2 = False
                input3 = True
            elif newinput2 == 'Y' and event.key == K_y:
                input2 = False
                input3 = True
            elif newinput2 == 'U' and event.key == K_u:
                input2 = False
                input3 = True
            elif newinput2 == 'S' and event.key == K_s:
                input2 = False
                input3 = True
            elif newinput2 == 'D' and event.key == K_d:
                input2 = False
                input3 = True
            elif newinput2 == 'F' and event.key == K_f:
                input2 = False
                input3 = True
            elif newinput2 == 'G' and event.key == K_g:
                input2 = False
                input3 = True
            elif newinput2 == 'H' and event.key == K_h:
                input2 = False
                input3 = True
            elif newinput2 == 'J' and event.key == K_j:
                input2 = False
                input3 = True
            elif newinput2 == 'X' and event.key == K_x:
                input2 = False
                input3 = True
            elif newinput2 == 'C' and event.key == K_c:
                input2 = False
                input3 = True
            elif newinput2 == 'V' and event.key == K_v:
                input2 = False
                input3 = True
            elif newinput2 == 'B' and event.key == K_b:
                input2 = False
                input3 = True
            elif newinput2 == 'N' and event.key == K_n:
                input2 = False
                input3 = True
            elif newinput2 == 'M' and event.key == K_m:
                input2 = False
                input3 = True
            else:
                inputsfailed = True
        elif input3 and inputsfailed == False and event.type == KEYDOWN:
            if newinput3 == 'W' and event.key == K_w:
                input3 = False
                input4 = True
            elif newinput3 == 'E' and event.key == K_e:
                input3 = False
                input4 = True
            elif newinput3 == 'R' and event.key == K_r:
                input3 = False
                input4 = True
            elif newinput3 == 'T' and event.key == K_t:
                input3 = False
                input4 = True
            elif newinput3 == 'Y' and event.key == K_y:
                input3 = False
                input4 = True
            elif newinput3 == 'U' and event.key == K_u:
                input3 = False
                input4 = True
            elif newinput3 == 'S' and event.key == K_s:
                input3 = False
                input4 = True
            elif newinput3 == 'D' and event.key == K_d:
                input3 = False
                input4 = True
            elif newinput3 == 'F' and event.key == K_f:
                input3 = False
                input4 = True
            elif newinput3 == 'G' and event.key == K_g:
                input3 = False
                input4 = True
            elif newinput3 == 'H' and event.key == K_h:
                input3 = False
                input4 = True
            elif newinput3 == 'J' and event.key == K_j:
                input3 = False
                input4 = True
            elif newinput3 == 'X' and event.key == K_x:
                input3 = False
                input4 = True
            elif newinput3 == 'C' and event.key == K_c:
                input3 = False
                input4 = True
            elif newinput3 == 'V' and event.key == K_v:
                input3 = False
                input4 = True
            elif newinput3 == 'B' and event.key == K_b:
                input3 = False
                input4 = True
            elif newinput3 == 'N' and event.key == K_n:
                input3 = False
                input4 = True
            elif newinput3 == 'M' and event.key == K_m:
                input3 = False
                input4 = True
            else:
                inputsfailed = True
        elif input4 and inputsfailed == False and event.type == KEYDOWN:
            if newinput4 == 'W' and event.key == K_w:
                input4 = False
                input5 = True
            elif newinput4 == 'E' and event.key == K_e:
                input4 = False
                input5 = True
            elif newinput4 == 'R' and event.key == K_r:
                input4 = False
                input5 = True
            elif newinput4 == 'T' and event.key == K_t:
                input4 = False
                input5 = True
            elif newinput4 == 'Y' and event.key == K_y:
                input4 = False
                input5 = True
            elif newinput4 == 'U' and event.key == K_u:
                input4 = False
                input5 = True
            elif newinput4 == 'S' and event.key == K_s:
                input4 = False
                input5 = True
            elif newinput4 == 'D' and event.key == K_d:
                input4 = False
                input5 = True
            elif newinput4 == 'F' and event.key == K_f:
                input4 = False
                input5 = True
            elif newinput4 == 'G' and event.key == K_g:
                input4 = False
                input5 = True
            elif newinput4 == 'H' and event.key == K_h:
                input4 = False
                input5 = True
            elif newinput4 == 'J' and event.key == K_j:
                input4 = False
                input5 = True
            elif newinput4 == 'X' and event.key == K_x:
                input4 = False
                input5 = True
            elif newinput4 == 'C' and event.key == K_c:
                input4 = False
                input5 = True
            elif newinput4 == 'V' and event.key == K_v:
                input4 = False
                input5 = True
            elif newinput4 == 'B' and event.key == K_b:
                input4 = False
                input5 = True
            elif newinput4 == 'N' and event.key == K_n:
                input4 = False
                input5 = True
            elif newinput4 == 'M' and event.key == K_m:
                input4 = False
                input5 = True
            else:
                inputsfailed = True
        elif input5 and inputsfailed == False and event.type == KEYDOWN:
            if newinput5 == 'W' and event.key == K_w:
                input5 = False
                input6 = True
            elif newinput5 == 'E' and event.key == K_e:
                input5 = False
                input6 = True
            elif newinput5 == 'R' and event.key == K_r:
                input5 = False
                input6 = True
            elif newinput5 == 'T' and event.key == K_t:
                input5 = False
                input6 = True
            elif newinput5 == 'Y' and event.key == K_y:
                input5 = False
                input6 = True
            elif newinput5 == 'U' and event.key == K_u:
                input5 = False
                input6 = True
            elif newinput5 == 'S' and event.key == K_s:
                input5 = False
                input6 = True
            elif newinput5 == 'D' and event.key == K_d:
                input5 = False
                input6 = True
            elif newinput5 == 'F' and event.key == K_f:
                input5 = False
                input6 = True
            elif newinput5 == 'G' and event.key == K_g:
                input5 = False
                input6 = True
            elif newinput5 == 'H' and event.key == K_h:
                input5 = False
                input6 = True
            elif newinput5 == 'J' and event.key == K_j:
                input5 = False
                input6 = True
            elif newinput5 == 'X' and event.key == K_x:
                input5 = False
                input6 = True
            elif newinput5 == 'C' and event.key == K_c:
                input5 = False
                input6 = True
            elif newinput5 == 'V' and event.key == K_v:
                input5 = False
                input6 = True
            elif newinput5 == 'B' and event.key == K_b:
                input5 = False
                input6 = True
            elif newinput5 == 'N' and event.key == K_n:
                input5 = False
                input6 = True
            elif newinput5 == 'M' and event.key == K_m:
                input5 = False
                input6 = True
            else:
                inputsfailed = True
        elif input6 and inputsfailed == False and event.type == KEYDOWN:
            if newinput6 == 'W' and event.key == K_w:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'E' and event.key == K_e:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'R' and event.key == K_r:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'T' and event.key == K_t:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'Y' and event.key == K_y:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'U' and event.key == K_u:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'S' and event.key == K_s:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'D' and event.key == K_d:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'F' and event.key == K_f:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'G' and event.key == K_g:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'H' and event.key == K_h:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'J' and event.key == K_j:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'X' and event.key == K_x:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'C' and event.key == K_c:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'V' and event.key == K_v:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'B' and event.key == K_b:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'N' and event.key == K_n:
                input6 = False
                inputscomplete = True
                score += 1
            elif newinput6 == 'M' and event.key == K_m:
                input6 = False
                inputscomplete = True
                score += 1
            else:
                inputsfailed = True

    if inputscomplete or inputsfailed:
        count += 1
            
    pygame.display.update()
    fpsClock.tick(FPS)
