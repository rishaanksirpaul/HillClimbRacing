import pygame,os
import sys
fps = 30
fpscontroller = pygame.time.Clock()
pygame.display.set_caption('Hill Climb Racing')
# pygame.display.set_caption(title, icontitle=None)
width = 700
height = 500
game_window = pygame.display.set_mode((width,height))

keepPlaying = True

pygame.init()

desertBg = pygame.image.load('background/desertbg.png')
desertBg = pygame.transform.scale(desertBg,(width,height))

def load_image(name,sizeX = -1, sizeY = -1, colorKey = None):
   
    image = pygame.image.load(name)
   
    if sizeX != -1 or sizeY != -1:
        image = pygame.transform.scale(image,(sizeX,sizeY))

    return image


class Coin:
    pass

# class petrol:
#     pass

orc_width = 0
orc_height = height-90

girl_width = 0
girl_height = height-90

t_width = 0
t_height = height-90



current_direction = 'FORWARD'
next_direction = current_direction

current_rotation = 0

orc_car = load_image('images/o_Body.png',100,40)
orcwheel = load_image('images/o_Wheel.png',30,30)
orchead = load_image('images/o_head.png',30,30)
orchead = pygame.transform.scale(orchead, (80, 80))
orcheadplay = pygame.transform.scale(orchead, (50, 50))

girlcar = load_image('images/G_Body.png',100,40)
girlwheel = load_image('images/G_Wheel.png',30,30)
girlhead = load_image('images/G_Head.png',30,30)
girlhead = pygame.transform.scale(girlhead,(80 ,80))
girlheadplay = pygame.transform.scale(girlhead,(50 ,50))

tcar = load_image('images/t_Body.png',100,40)
twheel = load_image('images/t_Wheel.png',30,30)
thead = load_image('images/t_Head.png',30,30)
thead = pygame.transform.scale(thead,(80,80))
theadplay = pygame.transform.scale(thead,(50,50))

graveyard = load_image('background/GraveyardBackground.png')
graveyardBG =  pygame.transform.scale(graveyard,(width,height))
graveyard = pygame.transform.scale(graveyard,(150,100))
sunny = load_image('background/sunnybg.png')
sunnyBG = pygame.transform.scale(sunny,(width,height))
sunny = pygame.transform.scale(sunny,(150,100))
winter = load_image('background/winterbg.png')
winterBG = pygame.transform.scale(winter,(width,height))
winter = pygame.transform.scale(winter,(150,100))

start = load_image('images/Start.png', sizeX= 200, sizeY= 100)
exit = load_image('images/Exit.png', sizeX= 200, sizeY= 100)

road = load_image('background/road.png')
blue = pygame.Color(0,0,200)

tick = load_image('images/tick.png' , sizeX = 80,sizeY= 80)

red = pygame.Color(255,0,0)

def levels_selected(level = "", character = ""):
    # Rectangles are needed for clickable objects
    rectA = pygame.Rect((100,100),(150,100))
    rectB = pygame.Rect((300, 100),(150,100))
    rectC = pygame.Rect((500,100),(150,100))

    rectD = pygame.Rect((100,200),(150,100))
    rectE = pygame.Rect((300,200),(150,100))
    rectF = pygame.Rect((500,200),(150,100))

    rectG = pygame.Rect((150,320),(200,100))
    rectH = pygame.Rect((400,320),(200,100))

    my_font = pygame.font.SysFont('arial' , 50)
    topText = my_font.render('Please select a character and a level', True, red)
    rect = topText.get_rect()
    rect.midtop = (350,30)
    game_window.blit(topText, rect)
  

    game_window.blit(orchead, (rectA.x,rectA.y))
    game_window.blit(girlhead,(rectB.x,rectB.y))
    game_window.blit(thead,(rectC.x,rectC.y))

    game_window.blit(graveyard,(rectD.x,rectD.y))
    game_window.blit(sunny,(rectE.x,rectE.y))
    game_window.blit(winter,(rectF.x,rectF.y))

    game_window.blit(start,(rectG.x,rectG.y))
    game_window.blit(exit,(rectH.x,rectH.y))
    
    running = True

    while running:
        
        mx,my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    next_direction = 'FORWARD'
                if event.key == pygame.K_LEFT:
                    next_direction = 'BACKWARDS'
                # current_rotation += 13
            if event.type == pygame.QUIT:
                 #pygame.quit()
                 #sys.exit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rectA.collidepoint((mx,my)):
                    character = "orc"
                                
                if rectB.collidepoint((mx,my)):
                    character = "girl"
                   #rectB.fill(blue)
                if rectC.collidepoint((mx,my)):
                    character = "t"
                    # rectC.fill(blue)
                    
                if rectD.collidepoint((mx,my)):
                    level = "graveyard"
                    # rectD.fill(blue)

                if rectE.collidepoint((mx,my)):
                    level = "sunny"
                    # rectE.fill(blue)

                if rectF.collidepoint((mx,my)):
                    level = "winter"
                    # rectF.fill(blue)
                if rectG.collidepoint((mx,my)):
                    if character != "" and level != "":

                        running = False
                        keepPlaying = True
                if rectH.collidepoint((mx,my)):
                    pygame.quit()
                    sys.exit()
                
                # if character == 'orc':
                #         game_window.blit(orchead, (rectA.x,rectA.y))
                # else:
                #     character = "orc"
                #     game_window.blit(tick,(rectA.x,rectA.y))
        
    print("I am out of running loop...")
    return (level,character)




while keepPlaying:
    game_window.blit(desertBg, (0,0))
    values = levels_selected()
    level,character = values
    print(level,character)
    if level == 'graveyard':
        game_window.blit(graveyardBG,(0,0))
        game_window.blit(road,(0,height-50))
    if level == 'sunny':
        game_window.blit(sunnyBG,(0,0))
        game_window.blit(road,(0,height-50))
    if level == 'winter':
        game_window.blit(winterBG,(0,0))
        game_window.blit(road,(0,height-50))

    if character == 'orc':
        game_window.blit(orc_car,(orc_width,orc_height))
        game_window.blit(orcwheel,(orc_width+10,orc_height + 20))
        game_window.blit(orcwheel,(orc_width+60,orc_height + 20))
        game_window.blit(orcheadplay,(orc_width+10,orc_height-40))
    
    if character == 'girl':
        game_window.blit(girlcar,(girl_width,girl_height))
        game_window.blit(girlwheel,(girl_width+10,girl_height + 20))
        game_window.blit(girlwheel,(girl_width+60,girl_height + 20))
        game_window.blit(girlheadplay,(girl_width+10,girl_height-40)) 
        

    if character == 't':
        game_window.blit(tcar,(t_width,t_height))
        game_window.blit(twheel,(t_width+10,t_height + 20))
        game_window.blit(twheel,(t_width+60,t_height + 20))
        game_window.blit(theadplay,(t_width+10,t_height-40))

    

    fpscontroller.tick(fps)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_direction = 'FORWARD'
            if event.key == pygame.K_LEFT:
                next_direction = 'BACKWARDS'

    
    if next_direction == 'FORWARD':
        print("FORWARD")
        orc_width += 1
        current_rotation -= 13
    elif next_direction == 'BACKWARDS':
        print("BACKWARD")
        orc_width -= 0.5
        current_rotation += 13

        
    pygame.transform.rotate(orcwheel,current_rotation)
    
