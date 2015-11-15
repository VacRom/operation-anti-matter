"""
 Sample use of drawing commands.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
 
# Import a library of functions called 'pygame'
import pygame
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
 
pi = 3.141592653
 
# Set the height and width of the screen
size = [800, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("draw module")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
 
    # Clear the screen and set the screen background
    screen.fill(black)


    # Draw a circle
    pygame.draw.circle(screen, blue, [150, 250], 40)
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()
