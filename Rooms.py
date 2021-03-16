import pygame

# There used to be ~50 lines of information relevant to the project (sources, ideas, etc.)
# I moved it out of here while I was refactoring in order to save space.

""" URGENTS! """
# Start making background, I'm tired of looking at yellow.
# Fix Issue with ground2 not registering player
# Refactor code so that it is better overall.


""" ROOMS & STAGES """

class Node:

    def __init__(self, roomNum, traps, walls, transitions, respawnPoint, color):
        self.roomNum = roomNum
        # Both trapList and wallList should be LISTS!
        self.trapList = traps
        self.wallList = walls
        self.transitionList = transitions
        self.next = None
        self.respawnPoint = respawnPoint
        # Determines the color of the platforms.
        self.color = color

# This is a linked list that points to another room. Whenever the player enters a loading zone, it should tell
# the roomList to load the next room. Right now it isn't implemented.

class roomList:

    def __init__(self, value=0):
        self.start = None
        self.currentRoom = None

    # This originates from our Linked List project from Janurary, but with some tweaks & changes. Okay, a
    # large amount of changes & modifications.

    def add(self, key, traps, walls, transitions, respawnPoint, color):
        new_node = Node(key, traps, walls, transitions, respawnPoint, color)
        if self.start == None:
            self.start = new_node
            # This new value
            self.currentRoom = self.start.roomNum
            return self.start
        current = self.start
        while current.next != None:
            current = current.next
        current.next = new_node
        return current.next

    # In the past, this got the value a node stored.
    # Now, it goes to find the node & stores it as currentRoom.
    def get(self, key):
        if key == None:
            return None
        current = self.start
        while current != None:
            if current.roomNum == key:
                self.currentRoom = current
                return None
            current = current.next
        return None

    def remove(self, key):
        if key == None:
            return None
        if self.start == None:
            return None
        if self.start.roomNum == key:
            temp = self.start.next
            self.start = temp
        current = self.start
        while current != None:
            if current.next.roomNum == key:
                removed = current.next
                current.next = current.next.next
                return ()
            current = current.next

    # Every Node has lists of data, namely the traps and walls.
    # This goes through the node stored in currentRoom and draws them on the screen.
    # Note: It only goes and calculates the walls/platforms.
    def drawData(self, window):
        for i in self.currentRoom.wallList:
            pygame.draw.rect(window, self.currentRoom.color, i.boundaries.rect)
        for i in self.currentRoom.transitionList:
            window.blit(i.image, (i.boundaries.x_cord, i.boundaries.y_cord))
        for i in self.currentRoom.trapList:
            window.blit(i.image, (i.boundaries.x_cord, i.boundaries.y_cord))

    # This function checks Collision.
    # It also passes down a value that helps with gravity.
    def checkCollision(self, character):
        # This loads the next room in the stage. This is first in order.
        for i in self.currentRoom.transitionList:
            if i.boundaries.inRect(character):
                self.get(i.next)
                character.boundaries.x_cord = i.new_cords[0]
                character.boundaries.y_cord = i.new_cords[1]

        # There might be a bug where the game doesn't load the last wall in this list. Fix it!
        for i in self.currentRoom.wallList:
            i.boundaries.floorTest(character)

        # Loading traps
        for i in self.currentRoom.trapList:
            if i.boundaries.inRect(character):
                i.inBoundary(character)

    def deathManager(self, character):
        if character.isDead:
            respawnCords = self.currentRoom.respawnPoint
            character.boundaries.x_cord = respawnCords[0]
            character.boundaries.y_cord = respawnCords[1]
            character.Ymomentum = 0
            character.isDead = False