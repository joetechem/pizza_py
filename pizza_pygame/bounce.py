import sys, pygame

# initialize pygame
pygame.init()

# window size
size = width, height = 600, 700

# set speed
speed = [1, 1]
speed2 = [1, 2]

# create a variable color
color = (230, 202, 154)

# tell Python the type of screen
screen = pygame.display.set_mode(size)

# set variable for image
# and tell Python the file name to get
first_pizza = pygame.image.load("images/pizza1.png")
second_pizza = pygame.image.load("images/pizza2.png")

# set variable 
ballrect1 = first_pizza.get_rect()

ballrect2 = second_pizza.get_rect()

# setup the loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect1 = ballrect1.move(speed)
    if ballrect1.left < 0 or ballrect1.right > width:
        speed[0] = -speed[0]
    if ballrect1.top < 0 or ballrect1.bottom > height:
        speed[1] = -speed[1]

    ballrect2 = ballrect2.move(speed2)
    if ballrect2.left < 0 or ballrect2.right > width:
        speed2[0] = -speed2[0]
    if ballrect2.top < 0 or ballrect2.bottom > height:
        speed2[1] = -speed2[1]

    # fill the background with the color specified earlier
    screen.fill(color)
    # draw image file to screen
    screen.blit(first_pizza, ballrect1)
    screen.blit(second_pizza, ballrect2)
    pygame.display.flip()
