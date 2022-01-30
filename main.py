import pygame,os
import sys
fps = 60
fpscontroller = pygame.time.Clock()
pygame.display.set_caption('Hill Climb Racing')
# pygame.display.set_caption(title, icontitle=None)
width = 700
height = 500
game_window = pygame.display.set_mode((width,height))

keepPlaying = False

pygame.init()

desertBg = pygame.image.load('background/desertbg.png')
desertBg = pygame.transform.scale(desertBg,(width,height))

def load_image(name,sizeX = -1, sizeY = -1, colorKey = None):
   
    image = pygame.image.load(name)
   
    if sizeX != -1 or sizeY != -1:
        image = pygame.transform.scale(image,(sizeX,sizeY))

    return image



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
coin = load_image('images/coin.png', sizeX = 50, sizeY= 30)

road = load_image('background/road.png')
blue = pygame.Color(0,0,200)

tick = load_image('images/tick.png' , sizeX = 80,sizeY= 80)
wheelX = 0
wheelY = 0
wheelZ = 0
red = pygame.Color(255,0,0)
score = 0


def showScore():
    game_window.blit(coin,(20,20))
    score_font = pygame.font.SysFont('times new roman', 30)
    screen = score_font.render(f'X {score}',True,red)
    rect = screen.get_rect()
    rect.midtop = (100,20)
    game_window.blit(screen,rect)
    pygame.display.update()

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
    game_window.blit(desertBg, (0,0))
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
            
        fpscontroller.tick(fps)
        pygame.display.update()        
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
                        keepPlaying = True
                        return (level,character)
                        print("Keepplaying",keepPlaying)
                        running = False
                if rectH.collidepoint((mx,my)):
                    pygame.quit()
                    sys.exit()
                
                    
    return (level,character)

values = levels_selected()
keepPlaying = True
import random
coinPosition = [random.randrange(20,width,20),orc_height + 20]
coinPosition2 = [random.randrange(30,width,30),orc_height + 20]
rotation = 0

while keepPlaying:
    game_window.blit(desertBg, (0,0))
    level,character = values
    # print(level,character)
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
        wheelX = orc_width+60
        game_window.blit(orc_car,(orc_width,orc_height))
        game_window.blit(orcwheel,(orc_width + 10,orc_height + 20))
        game_window.blit(orcwheel,(wheelX,orc_height + 20))
        game_window.blit(orcheadplay,(orc_width+10,orc_height-40))
        

    
    if character == 'girl':
        wheelY = girl_width+60
        game_window.blit(girlcar,(girl_width,girl_height))
        game_window.blit(girlwheel,(girl_width+10,girl_height + 20))
        game_window.blit(girlwheel,(wheelY,girl_height + 20))
        game_window.blit(girlheadplay,(girl_width+10,girl_height-40)) 
        # character_width = girl_width
        

    if character == 't':
        wheelZ = t_width+60
        game_window.blit(tcar,(t_width,t_height))
        game_window.blit(twheel,(t_width+10,t_height + 20))
        game_window.blit(twheel,(wheelZ,t_height + 20))
        game_window.blit(theadplay,(t_width+10,t_height-40))
        # character_width = t_width

    game_window.blit(coin,(coinPosition[0],coinPosition[1]))
    game_window.blit(coin,(coinPosition2[0],coinPosition2[1]))

    showScore()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_direction = 'FORWARD'
                # print(character_width,"224")
            if event.key == pygame.K_LEFT:
                next_direction = 'BACKWARDS'

    
    if next_direction == 'FORWARD':
        # print("FORWARD")
        orc_width += 1      
    elif next_direction == 'BACKWARDS':
        # print("BACKWARD")
        orc_width-= 0.5

    if next_direction == 'FORWARD':
        # print("FORWARD")
        girl_width += 1      
    elif next_direction == 'BACKWARDS':
        # print("BACKWARD")
        girl_width-= 0.5

    if next_direction == 'FORWARD':
        # print("FORWARD")
        t_width += 1      
    elif next_direction == 'BACKWARDS':
        # print("BACKWARD")
        t_width -= 0.5
    
    if coinPosition[0] == wheelX or coinPosition[0] == wheelY or coinPosition[0] == wheelZ:
        score += 1
        coinPosition = [-100,-100]
        

    if coinPosition2[0] == wheelX or coinPosition2[0] == wheelY or coinPosition2[0] == wheelZ:
        score += 1
        coinPosition2 = [-100,-100]

    if wheelX >= width:
        orc_width = 0
        coinPosition = [random.randrange(20,width,20),orc_height + 20]
        coinPosition2 = [random.randrange(30,width,30),orc_height + 20]
    elif wheelY >= width:
        girl_width = 0
        coinPosition = [random.randrange(20,width,20),orc_height + 20]
        coinPosition2 = [random.randrange(30,width,30),orc_height + 20] 
    elif wheelZ >= width:
        t_width = 0
        coinPosition = [random.randrange(20,width,20),orc_height + 20]
        coinPosition2 = [random.randrange(30,width,30),orc_height + 20] 

    if wheelX <= 0:
        orc_width = 600

    if wheelY <= 0:
        girl_width = 600
        
    if wheelZ <= 0:
        t_width = 600
    fpscontroller.tick(fps)
    pygame.display.update()
