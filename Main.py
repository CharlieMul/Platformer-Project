import pygame
import Objects
import RoomList

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

# .display edits the main display window.
# This initializes the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Pygame")
background = pygame.image.load("Sunrise.jpg")

# If this loop weren't here, then the screen would appear then disappear after the program ends.
# It also runs the game's main code continuously

# This initializes the main giraffe character.
geoffery_place = pygame.image.load("Robot_Character.png")
geoffery = Objects.Player(200, 800, 69, 118, geoffery_place)

"""
if isinstance(ground, Objects.Walls):
    print("It's a baby!")
"""


""" MAIN LOOP """

keep_run = True
while keep_run:
    # This loop uses an EVENT, or something the player does, to do Y.
    # Specifically, it tests if the player is pressing an interaction key & deals with momentum.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_run = False
        # This check prevents the player moving uncontrollably upon death.
        # I had to make two separate movement functions. One for a & d keypresses, and one for other keypresses.
        # That way, horizontal movement would not be canceled by another key being pressed.
        elif event.type == pygame.KEYDOWN:
            geoffery.cordMovement(event)
        elif event.type == pygame.KEYUP:
            geoffery.x_cordMovementDisable(event)

    # This calculates the player's jumping.
    geoffery.y_cordMovement(GRAVITY_PULL)

    """ ORGANIZE THIS SECTION!!! """
    # Past here is the code that should always run.
    """ SCREEN UPDATING """

    # Calculates player x coordinate change based off of momentum.
    geoffery.boundaries.x_cord += geoffery.Xmomentum
    # Calculates player y coordinate using Gravity (And Vert. momentum in the future)
    if geoffery.outOfBounds(SCREEN_HEIGHT, SCREEN_WIDTH):
        geoffery.isDead = True

    geoffery.boundaries.y_cord += GRAVITY_PULL

    # This checks if the player is colliding with anything & Draws all the objects in a room.
    RoomList.STAGE1.checkCollision(geoffery)
    RoomList.STAGE1.deathManager(geoffery)

    # Drawing the background & player onto the screen.
    giraffePosition = geoffery.drawPlayer()
    screen.blit(background, (0,0))
    screen.blit(geoffery.image, (geoffery.boundaries.x_cord, geoffery.boundaries.y_cord))
    RoomList.STAGE1.drawData(screen)

    # Commented off text that, when active, shows values related to the player.
    """
    print(f"geofferyX: {geoffery.boundaries.x_cord}, geofferyY: {geoffery.boundaries.y_cord}, geofferyWIDTH: \
    {geoffery.boundaries.x_cord + geoffery.boundaries.width}, \
    geofferyHEIGHT: {geoffery.boundaries.y_cord + geoffery.boundaries.height}")
    """

    # To update the screen, use pygame.display.update()
    # This should be the LAST THING in the loop.
    pygame.display.update()