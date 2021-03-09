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

    # This is wall Test 2.0! It tests for a character hitting a wall.
    # If the character hits a wall, then it would stop moving in that direction.
    def wallTest(self, character):
        # This combines the character & platform's widths & heights for simplicity.
        characterRight = character.boundaries.width + character.boundaries.x_cord
        platformRight = self.width + self.x_cord
        characterBottom = character.boundaries.y_cord + character.boundaries.height
        print(character.boundaries.y_cord)

        # There is a Bug where the player is almost always 1.2 pixels below a platform (I blame gravity)
        # This forces them off a platform. To solve it, I subtracted 1.2 from the characterBottom for more
        # accurate checks.

        # First test determines if the character is to the left of the platform.
        if character.boundaries.x_cord < self.x_cord and characterBottom - 1.2 >= self.y_cord:
            character.boundaries.x_cord = self.x_cord - character.boundaries.width
            return True
        # Second test determines if the character is to the right of the platform.
        elif characterRight > platformRight and characterBottom - 1.2 >= self.y_cord:
            character.boundaries.x_cord = platformRight
            return True
        return False

    # This is floor Test 2.0! We don't talk about 1.0.
    def floorTest(self, character):
        # This updates the character's rectangle and compares it to the platform,
        # Resulting in this test which checks if the player is on a platform.
        character.rect = pygame.Rect(character.boundaries.return_cords())
        if self.rect.colliderect(character.rect):
            # This tests to see if the character is entering the platform from the left or right.
            if self.wallTest(character) == True:
                return
            character.boundaries.y_cord = self.y_cord - character.boundaries.height
            return False


# Forming the player class. This handles the player's movement, values, & (for now) their hitboxes.
class Player:

    # Initializes hitboxes & the image that represents the player.
    def __init__(self, x_cord, y_cord, width, height, image):
        self.boundaries = Hitboxes(x_cord, y_cord, width, height)
        self.image = image
        # This value determines how much the player's X_Cord is increased by movement.
        self.SPEED = .7
        self.Xmomentum = 0
        self.Ymomentum = 0
        self.rect = pygame.Rect(x_cord, y_cord, width, height)

    # Returns values for drawing the player onto the screen.
    def drawplayer(self):
        return(self.image, self.boundaries.return_cords())

    # This handles the player's X momentum & movement.
    def x_cordMovement(self, event):
        # Runs a test to check and see if a key is being held
        if event.key == pygame.K_w:
            # Vault
            print("IT'S ALIVE!")
        elif event.key == pygame.K_a:
            # Move Left
            self.Xmomentum -= self.SPEED
        elif event.key == pygame.K_d:
            # Move Right
            self.Xmomentum += self.SPEED
        elif event.key == pygame.K_s:
            # Changes Player to be smaller, more compressed.
            # Crouch
            pass
        elif event.key == pygame.K_SPACE:
            self.boundaries.y_cord -= 60

    # This disables a keypress if the key is no longer being pressed. Yes, it is necessarily.
    def x_cordMovementDisable(self, event):
        # Runs a test to check and see if a key is being held
        if event.key == pygame.K_w:
            # Vault
            print("IT'S ALIVE!")
        elif event.key == pygame.K_a:
            # Move Left
            self.Xmomentum += self.SPEED
        elif event.key == pygame.K_d:
            # Move Right
            self.Xmomentum -= self.SPEED
        elif event.key == pygame.K_s:
            # Changes Player to be smaller, more compressed.
            # Crouch
            pass
        elif event.key == pygame.K_SPACE:
            pass

# This class stores the data for Walls & and sets up their rectangle for collision.
class Walls:

    # Initializes hitboxes & the image that represents the player.
    def __init__(self, x_cord, y_cord, width, height):
        self.boundaries = Hitboxes(x_cord, y_cord, width, height)
