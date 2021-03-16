# Making Initial Imports
import pygame

# Forming the hitboxes class.
# This is used for a simple & effective form of Wall Hitbox Detection.
class Hitboxes:

    # The program mostly uses pygame.Rect() for calculating Hitboxes.
    def __init__(self, x_cord, y_cord, width, height):
        # The left side is the X coord and the top side is the Y coord
        self.x_cord = x_cord
        self.width = width
        self.y_cord = y_cord
        self.height = height
        self.rect = pygame.Rect(x_cord, y_cord, width, height)

    def return_cords(self):
        return(self.x_cord, self.y_cord, self.width, self.height)

    """ COLLISION TESTS """
    # Make a way for Collision Tests to be appendable to a
    # This is wall Test 2.0! It tests for a character hitting a wall.
    # If the character hits a wall, then it would stop moving in that direction.
    def wallTest(self, character):
        # This combines the character & platform's widths & heights for simplicity.
        characterRight = character.boundaries.width + character.boundaries.x_cord
        platformRight = self.width + self.x_cord
        characterBottom = character.boundaries.y_cord + character.boundaries.height
        platformBottom = self.y_cord + self.height

        # There is a Bug where the player is almost always gravity_pull+1 * 2 pixels below a platform (I blame gravity)
        # This forces them off a platform. To solve it, I subtracted gravity_pull+ 1 * 2 from the characterBottom
        # for more accurate checks.

        # First test determines if the character is to the left of the platform.
        # print(f"CHARBOTTOM: {characterBottom}, PLATFORMBOTTOM: {platformBottom}, PLATFORMTOP: {self.y_cord}, \
        # CHARTOP: {character.boundaries.y_cord + 1.8}")
        if character.boundaries.x_cord < self.x_cord and characterBottom - 1.8 >= self.y_cord:
            character.boundaries.x_cord = self.x_cord - character.boundaries.width
            return True
        # Second test determines if the character is to the right of the platform and not under or over it.
        elif characterRight > platformRight and characterBottom - 1.8 >= self.y_cord:
            character.boundaries.x_cord = platformRight
            return True
        return False

    # bonkTest ensures Maximal Player Head Bonkage will playing! (It prevents them from bonking their head into walls).d
    def bonkTest(self, character):
        characterBottom = character.boundaries.y_cord + character.boundaries.height
        platformBottom = self.y_cord + self.height
        if characterBottom > platformBottom:
            character.boundaries.y_cord = platformBottom
            return True

    # This is floor Test 2.0! We don't talk about 1.0.
    def floorTest(self, character):
        # This updates the character's rectangle and compares it to the platform,
        # Resulting in this test which checks if the player is on a platform.
        character.rect = pygame.Rect(character.boundaries.return_cords())
        if self.inRect(character):
            # This tests to see if the character is entering the platform from the left or right.
            if self.wallTest(character):
                return
            if self.bonkTest(character):
                return
            character.canJump = True
            character.boundaries.y_cord = self.y_cord - character.boundaries.height
            return False

    # This is used for things other than wall collision.
    def inRect(self, character):
        if self.rect.colliderect(pygame.Rect(character.boundaries.return_cords())):
            return True


# Forming the player class. This handles the player's movement, values, & (for now) their hitboxes.
class Player:

    # Initializes hitboxes & the image that represents the player.
    def __init__(self, x_cord, y_cord, width, height, image):
        self.boundaries = Hitboxes(x_cord, y_cord, width, height)
        self.image = image
        # This value determines how much the player's X_Cord is increased by movement.
        self.SPEED = 1.2
        self.Xmomentum = 0
        self.Ymomentum = 0
        self.canJump = True
        self.isDead = False

    # Returns values for drawing the player onto the screen.
    def drawPlayer(self):
        return(self.image, self.boundaries.return_cords())

    def _teleport(self):
        # THIS IS A DEV COMMAND. THE PLAYER IS NOT SUPPOSED TO ACCESS THIS.
        self.boundaries.x_cord = int(input("Input new X coordinate\n>> "))
        self.boundaries.y_cord = int(input("Input new Y coordinate\n>> "))

    def y_cordMovement(self, gravitationalPull):
        if self.Ymomentum < 0:
            self.Ymomentum += .15
        # This is less responsive as an Else Statement.
        if self.Ymomentum > 0:
            # This makes sure the player can't jump while falling & prevents them from gaining too much
            # Downwards momentum (Velocity).
            self.canJump = False
            self.Ymomentum = 0
        self.boundaries.y_cord += self.Ymomentum

    # This handles the player's X momentum & movement.
    def cordMovement(self, event):
        # Runs a test to check and see if a key is being held
        if event.key == pygame.K_a:
            # Move Left
            self.Xmomentum -= self.SPEED
        elif event.key == pygame.K_d:
            # Move Right
            self.Xmomentum += self.SPEED
        elif event.key == pygame.K_v:
            self._teleport()
        elif event.key == pygame.K_SPACE:
            # self.boundaries.y_cord -= 60
            if self.canJump and self.Ymomentum >= 0:
                self.Ymomentum = -8
                self.canJump = False

# Maybe this could help prevent the issue.
# if event.type == pygame.KEYUP and character.isDead:
#   skip on subtracting or adding SPEED

    # This disables a keypress if the key is no longer being pressed. Yes, it is necessarily.
    def x_cordMovementDisable(self, event):
        # Runs a test to check and see if a key is no longer being held
        if event.key == pygame.K_a:
            # Move Left
            self.Xmomentum += self.SPEED
        elif event.key == pygame.K_d:
            # Move Right
            self.Xmomentum -= self.SPEED
        elif event.key == pygame.K_SPACE:
            self.canJump = False

    def outOfBounds(self, SCREEN_HEIGHT, SCREEN_WIDTH):
        characterRight = self.boundaries.x_cord + self.boundaries.width
        if self.boundaries.y_cord > SCREEN_HEIGHT or self.boundaries.x_cord < 0 or characterRight > SCREEN_WIDTH:
            return True


""" OBJECTS """
# This class stores the data for Walls & and sets up their rectangle for collision.
class Walls:

    # Initializes hitboxes & the image that represents the player.
    def __init__(self, x_cord, y_cord, width, height):
        self.boundaries = Hitboxes(x_cord, y_cord, width, height)

# This class stores the data for boundaries & loading zones.
class Boundaries:

    # Initializes hitboxes & the image that represents the player.
    def __init__(self, x_cord, y_cord, next, new_cords):
        self.boundaries = Hitboxes(x_cord, y_cord, 69, 118)
        self.image = pygame.image.load("Door.png")
        # Next is the next Node
        self.next = next
        # new_cords is the cords the player starts in the next room.
        self.new_cords = new_cords

""" TRAPS """
# This class modifies the character's jump, letting them jump in mid-air.
class Batteries:
    def __init__(self, x_cord, y_cord):
        self.image = pygame.image.load("Battery.png")
        self.boundaries = Hitboxes(x_cord, y_cord, 80, 90)

    def inBoundary(self, character):
        character.canJump = True

class Springs:
    def __init__(self, x_cord, y_cord):
        self.image = pygame.image.load("Spring.png")
        self.boundaries = Hitboxes(x_cord, y_cord, 80, 35)

    def inBoundary(self, character):
        character.Ymomentum = -12
        character.canJump = True

class Spikes:
    def __init__(self, x_cord, y_cord):
        self.image = pygame.image.load("Spikes.png")
        self.boundaries = Hitboxes(x_cord, y_cord, 100, 35)

    def inBoundary(self, character):
        character.isDead = True

# This prints the image onto the screen. Be mindful of the image's Width & Height!
class Decorations:
    def __init__(self, x_cord, y_cord, image):
        self.boundaries = Hitboxes(x_cord, y_cord, 300, 200)
        self.image = image
        # BillBoards are 300x200

    def inBoundary(self, character):
        # I only have it here so I don't have to run a separate check to see if there are decorations in a room.
        pass
