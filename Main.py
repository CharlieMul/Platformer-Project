import pygame
import Objects
import RoomList
import Rooms

""" SCREEN INITIALIZATION """

# pygame.init() Initializes Pygame
pygame.init()

# 1200
SCREEN_WIDTH = 1200
# 1000
SCREEN_HEIGHT = 1000

# This Boolean Value is important to prevent a certain bug (No it isn't).
Gravity = True
GRAVITY_PULL = .8
# The Clock is needed for a stable frame-rate.
Clock = pygame.time.Clock()

# .display edits the main display window.
# This initializes the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Pygame")
background = pygame.image.load("Sunrise.jpg")

# Did you know geoffery used to be a giraffe?
# Geoffery was his name, and it stuck as the character's reference name.
geoffery_place = pygame.image.load("Robot_Character.png")
geoffery = Objects.Player(200, 800, 69, 118, geoffery_place)

""" MAIN LOOP """

keep_run = True
while keep_run:

    # I'm making this variable for simplicity.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_run = False
        # I had to make two separate movement functions. One for a & d keypresses, and one for other keypresses.
        # That way, horizontal movement would not be canceled by another key being pressed.
        elif event.type == pygame.KEYDOWN:
            geoffery.cordMovement(event)
            RoomList.STAGE1.roomChange = True
        elif event.type == pygame.KEYUP:
            RoomList.STAGE1.roomChange = True

            geoffery.x_cordMovementDisable(event)

    # This calculates the player's jumping.
    geoffery.y_cordMovement(GRAVITY_PULL)

    """ ORGANIZE THIS SECTION!!! """
    # Past here is the code that should always run.
    """ SCREEN UPDATING """

    # Calculates player x coordinate change based off of momentum.
    geoffery.boundaries.x_cord += geoffery.Xmomentum
    # Calculates player y coordinate using Gravity (And Vert. momentum in Objects.py
    geoffery.boundaries.y_cord += GRAVITY_PULL

    # Check to see if the player has died.
    if geoffery.outOfBounds(SCREEN_HEIGHT, SCREEN_WIDTH):
        geoffery.isDead = True

    # These check if the player is colliding with anything & draws all the objects in a room.
    RoomList.STAGE1.checkCollision(geoffery)
    RoomList.STAGE1.deathManager(geoffery)

    """ SCREEN UPDATING """
    # Drawing the background, objects, & player onto the screen.
    # This only happens if an event occurs.
    pygame.time.delay(1)
    if RoomList.STAGE1.roomChange == True:
        screen.blit(background, (0, 0))
        RoomList.STAGE1.drawData(screen)
        RoomList.STAGE1.roomChange = False
        print("EEE")

    screen.blit(geoffery.image, (geoffery.boundaries.x_cord, geoffery.boundaries.y_cord))
    pygame.display.update()


# NOTES FOR OPTIMIZATION UPDATE:
## 1. I don't need to draw objects every frame, just their collision.
## 2. Mess with .clock and make the game only update every x frames?