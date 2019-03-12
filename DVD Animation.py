#Pygame Experimentation
import sys, pygame

pygame.init()   #Initialises pygame

size = width, height = 2100, 900  #Dimensions for screen in size variable
speed = [2,2]   #Sets speed of ball

black = 0, 0, 0     #RGB Value for Black

screen = pygame.display.set_mode(size)  #Setups a screen

ball = pygame.image.load("DVD_logo.svg.png")  #Defines ball variable to store the image of the ball
ballrect = ball.get_rect()

while True:     #Infinite Loop
    for event in pygame.event.get():    #Searches through the possible events in pygame events
        if event.type == pygame.QUIT: sys.exit()    #If the event type is quit then it terminates the execution

    ballrect = ballrect.move(speed)     #Moves the ball
    if ballrect.left < 0 or ballrect.right > width: #If the ball is beyound boundaries then it inverts the direction
        speed[0] = -speed[0]    
    elif ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
