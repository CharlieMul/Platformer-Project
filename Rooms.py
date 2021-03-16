import pygame

""" ROOMS & STAGES """

class Node:

    def __init__(self, roomNum, traps, walls, transitions, respawnPoint, color):
        self.roomNum = roomNum
        # Lists that allow for multiple traps/walls/transitions per room.
        self.trapList = traps
        self.wallList = walls
        self.transitionList = transitions
        self.next = None
        self.respawnPoint = respawnPoint
        # Determines the color of the platforms.
        self.color = color

# This is a linked list that points to another room. Whenever the player enters a loading zone, it tells
# the roomList to load the next room.

class roomList:

    def __init__(self, value=0):
        self.start = None
        self.currentRoom = None
    
    # Adds a new room (Node) to the list of rooms.
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

    # Goes to find the next node & stores it as currentRoom.
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

    # This goes through the node stored in currentRoom and draws them on the screen.
    def drawData(self, window):
        for i in self.currentRoom.wallList:
            pygame.draw.rect(window, self.currentRoom.color, i.boundaries.rect)
        for i in self.currentRoom.transitionList:
            window.blit(i.image, (i.boundaries.x_cord, i.boundaries.y_cord))
        for i in self.currentRoom.trapList:
            window.blit(i.image, (i.boundaries.x_cord, i.boundaries.y_cord))

    # This function checks Collision.
    def checkCollision(self, character):
        # This loads the door to the next room.
        for i in self.currentRoom.transitionList:
            if i.boundaries.inRect(character):
                self.get(i.next)
                character.boundaries.x_cord = i.new_cords[0]
                character.boundaries.y_cord = i.new_cords[1]
                
        # Loading Platforms
        for i in self.currentRoom.wallList:
            i.boundaries.floorTest(character)

        # Loading traps
        for i in self.currentRoom.trapList:
            if i.boundaries.inRect(character):
                i.inBoundary(character)

    # Resets the player's position to a fixed point upon player death.
    def deathManager(self, character):
        if character.isDead:
            respawnCords = self.currentRoom.respawnPoint
            character.boundaries.x_cord = respawnCords[0]
            character.boundaries.y_cord = respawnCords[1]
            character.Ymomentum = 0
            character.isDead = False
