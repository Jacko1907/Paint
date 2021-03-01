import pygame
from brushes import *
pygame.init()

size = (700, 900)
bg_color = (225, 229, 235)
screen = pygame.display.set_mode(size)
screen.fill(bg_color)
pygame.display.flip()
pygame.display.set_caption("Jack's Paint")



BRUSH_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]



Brush1 = normalBrush(BRUSH_COLORS[1], 10, 0)
SquareBrush1 = squareBrush(BRUSH_COLORS[1], 10)
Eraser1 = Eraser(10)
currentbrush = Brush1


run = True
while run:
    pygame.time.delay(100)


    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            # Check if up arrow is pressed, if it is it will increase the size. 
            if event.key == pygame.K_UP:
                currentbrush.setRadius(currentbrush.radius + 5)
                print(f'Set {currentbrush.name} to {currentbrush.radius}')


            # Check if down arrow is pressed, if it is it will decrease the size. 
            if event.key == pygame.K_DOWN:
                currentbrush.setRadius(currentbrush.radius - 5)
                print(f'Set {currentbrush.name} to {currentbrush.radius}')


            # Check if 1 is pressed, if it is it will change to the standard brush   
            if event.key == pygame.K_1:
                currentbrush = Brush1
                print("switched to the brush")


            # Check if 2 is pressed, if it is it will change to the square brush   
            if event.key == pygame.K_2:
                currentbrush = SquareBrush1
                print("switched to the square brush")

            
            # Check if 3 is pressed, if it is it will change to the eraser   
            if event.key == pygame.K_3:
                currentbrush = Eraser1
                print("switched to the rubber")


            # Check if left arrow is pressed, if it is it will change color
            if event.key == pygame.K_LEFT:
                if currentbrush.name == "Rubber":
                    print("You are on a rubber")
                else:
                    currentcolour = BRUSH_COLORS.index(currentbrush.color)
                    if currentcolour == 0:
                        print("You are already on the first color")
                    else:
                        currentbrush.setColor(BRUSH_COLORS[currentcolour - 1])

             # Check if right arrow is pressed, if it is it will change color
            if event.key == pygame.K_RIGHT:
                if currentbrush.name == "Rubber":
                    print("You are on a rubber")
                else:
                    currentcolour = BRUSH_COLORS.index(currentbrush.color)
                    if currentcolour == len(BRUSH_COLORS) - 1:
                        print("You are already on the last color")
                    else:
                        currentbrush.setColor(BRUSH_COLORS[currentcolour + 1])

            
             # Check if left ctrl is pressed, if it is it will save the image
            if event.key == pygame.K_LCTRL:
                option = input("What would you like to save the image as? If you name it as an existing image, it will overwrite it: ")
                pygame.image.save(screen, f'drawings/{option}.jpg')
                print("success")





    pos = pygame.mouse.get_pos()
   
        
   


    button = pygame.mouse.get_pressed()
    if button[0] == True: 
        currentbrush.draw(screen, pos)
        pygame.display.flip()



pygame.quit()