import pygame
import Objects

# There used to be ~50 lines of information relevant to the project (sources, ideas, etc.)
# I moved it out of here while I was refactoring in order to save space.

""" URGENTS! """
# Start making background, I'm tired of looking at yellow.
# Fix Issue with ground2 not registering player
# Refactor code so that it is better overall.


""" ROOMS & STAGES """

class Node:

    def __init__(self, roomNum, traps, walls):
        self.roomNum = roomNum
        # Both trapList and wallList should be LISTS!
        self.trapList = traps
        self.wallList = walls


# This is a linked list that points to another room. Whenever the player enters a loading zone, it should tell
# the roomList to load the next room. Right now it isn't implemented.

class roomList:

    def __init__(self, value=0):
        self.start = None
        self.currentRoom = None

    # This originates from our Linked List project from Janurary, but with some tweaks & changes. Okay, a
    # large amount of changes & modifications.

    def add(self, key, traps, walls):
        new_node = Node(key, traps, walls)
        if self.start == None:
            self.start = new_node
            # This new value
            self.currentRoom = self.start
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
            return (None)
        if self.start == None:
            return (None)
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
            pygame.draw.rect(window, "Brown", i.boundaries.rect)

    # This function checks Collision.
    # It also passes down a value that helps with gravity.
    def checkCollision(self, character):
        # there is a glitch here where the game doesn't load the last wall in this list. Fix it!
        for i in self.currentRoom.wallList:
            i.boundaries.floorTest(character)


    def returnTestWall(self):
        return self.currentRoom.wallList[0]

# Note: You're not supposed to change the name of STAGE1. It's capitalized.
STAGE1 = roomList()

# I still have to initialize data, this just makes it easier to store & access the data.
# Also reasons.
ground = Objects.Walls(100, 400, 800, 100)
# For SOME reason, ground2 isn't doing wall collision correctly. This needs to be fixed.
ground2 = Objects.Walls(200, 200, 200, 145)
ground3 = Objects.Walls(100, 800, 800, 100)
ground4 = Objects.Walls(50, 100, 200, 145)
ground5 = Objects.Walls(40, 30, 20, 10)
ground6 = Objects.Walls(700, 700, 20, 10)
ground7 = Objects.Walls(800,750,23,45)
ground8 = Objects.Walls(900, 900, 200, 200)

STAGE1.add(1, [], [ground, ground2, ground3, ground4, ground5, ground6])
STAGE1.get(1)