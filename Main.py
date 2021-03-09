import pygame
import Objects
import Rooms

""" SCREEN INITIALIZATION """

# pygame.init() Initializes Pygame
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

# This Boolean Value is important to prevent a certain bug (No it isn't).
Gravity = True
GRAVITY_PULL = .4

# .display edits the main display window.
# This initializes the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Pygame")

# If this loop weren't here, then the screen would appear then disappear after the program ends.
# It also runs the game's main code continuously

# This initializes the main giraffe character.
giraffe_face = pygame.image.load("Robot_Character.png")
geoffery = Objects.Player(0, 0, 69, 118, giraffe_face)

"""
if isinstance(ground, Objects.Walls):
    print("It's a baby!")
"""


""" MAIN LOOP """

keep_run = True
while keep_run:
    # This loop uses an EVENT, or something the player does, to do Y.
    # Speciffically, it tests if the player is pressing an interaction key & deals with momentum.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_run = False

        # I had to make two separate movement functions. One for a & d keypresses, and one for other keypresses.
        # That way, horizontal movement would not be canceled by another key being pressed.
        elif event.type == pygame.KEYDOWN:
            geoffery.x_cordMovement(event)
        elif event.type == pygame.KEYUP:
            geoffery.x_cordMovementDisable(event)
            # I didn't feel like I'd overcomplicated things enough. Here you go :D


    """ ORGANIZE THIS SECTION!!! """
    # Past here is the code that should always run.
    """ SCREEN UPDATING """

    # Calculates player x coordinate change based off of momentum.
    geoffery.boundaries.x_cord += geoffery.Xmomentum
    # Calculates player y coordinate using Gravity (And Vert. momentum in the future)
    if Gravity == True:
        geoffery.boundaries.y_cord += GRAVITY_PULL

    # This checks if the player is colliding with anything & Draws all the objects in a room.
    Rooms.STAGE1.checkCollision(geoffery)

    # Drawing the background & player onto the screen.
    giraffePosition = geoffery.drawplayer()
    screen.fill((255, 200, 50))
    screen.blit(geoffery.image, (geoffery.boundaries.x_cord, geoffery.boundaries.y_cord))
    Rooms.STAGE1.drawData(screen)

    # Commented off text that, when active, shows values related to the player.
    """
    print(f"geofferyX: {geoffery.boundaries.x_cord}, geofferyY: {geoffery.boundaries.y_cord}, geofferyWIDTH: \
    {geoffery.boundaries.x_cord + geoffery.boundaries.width}, \
    geofferyHEIGHT: {geoffery.boundaries.y_cord + geoffery.boundaries.height}")
    """

    # To update the screen, use pygame.display.update()
    # This should be the LAST THING in the loop.
    pygame.display.update()