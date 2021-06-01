import pygame

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("WUMPUS")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# player
player_sprite = pygame.image.load('characters/knight.png')
player_sprite = pygame.transform.scale(player_sprite, (60,60))
player_x = width/2
player_y = 10

#calls player onto the screen
def player():
    screen.blit(player_sprite, (player_x,player_y))




running = True
while running: #anything running throughout the game MUST be put inside here
## the code below allows us to quit using the cross in the top right
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    screen.fill((128,128,128))
    player()
    pygame.display.update() #updates screen constantly



    