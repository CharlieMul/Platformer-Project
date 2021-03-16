import Rooms
import Objects
import pygame

# RoomList stores the data for all of the rooms.

STAGE1 = Rooms.roomList()
# ROOMS are organized by...

# 1. What is in the room
# 2. The declaration of the room

# These walls are used often, so they are here for easy reference.
leftWall = Objects.Walls(0, 0, 80, 1000)
rightWall = Objects.Walls(1120, 0, 80, 1000)
lowGround = Objects.Walls(0, 800, 200, 100)

# For putting a door alongside the right wall, it's x cord needs to be 1051

# =========
""" 1 - 5 """
# =========

""" R1 """
r1ground1 = Objects.Walls(0, 800, 1200, 300)

r1loading_zone = Objects.Boundaries(1051, 682, 2, [100, 700])
r1decoration1 = Objects.Decorations(450, 600, pygame.image.load("Billboard_Tutorial.png"))

STAGE1.add(1, [r1decoration1], [leftWall, rightWall, r1ground1], [r1loading_zone], [200, 800], "Brown")

""" R2 """
r2ground1 = Objects.Walls(450, 800, 200, 100)
r2ground2 = Objects.Walls(920, 800, 200, 100)

r2loading_zone = Objects.Boundaries(1051, 682, 3, [100, 700])

STAGE1.add(2, [], [leftWall, rightWall, lowGround, r2ground1, r2ground2], [r2loading_zone], [100, 700], "Brown")

""" R3 """
r3ground1 = Objects.Walls(350, 700, 100, 40)
r3ground2 = Objects.Walls(550, 600, 200, 40)
r3ground3 = Objects.Walls(920, 500, 200, 100)

r3loading_zone = Objects.Boundaries(1051, 382, 4, [100, 700])

STAGE1.add(3, [], [leftWall, rightWall, lowGround, r3ground1, r3ground2, r3ground3], [r3loading_zone], [100, 700]
           , "Brown")

""" R4 """
r4ground1 = Objects.Walls(50, 600, 500, 40)
r4ground2 = Objects.Walls(500, 800, 35, 35)
r4ground3 = Objects.Walls(900, 800, 300, 35)

r4loading_zone = Objects.Boundaries(1051, 682, 5, [100, 700])
r4decoration1 = Objects.Decorations(150, 400, pygame.image.load("Billboard_Jump.png"))

STAGE1.add(4, [r4decoration1], [leftWall, rightWall, lowGround, r4ground1, r4ground2, r4ground3], [r4loading_zone], [100, 700]
           , "Brown")

""" R5 """
# Reuses ground2
r5ground1 = Objects.Walls(350, 700, 100, 40)
r5ground2 = Objects.Walls(550, 600, 200, 40)
r5ground3 = Objects.Walls(1020, 600, 100, 100)
r5ground4 = Objects.Walls(300, 400, 900, 40)

r5loading_zone = Objects.Boundaries(1051, 482, 6, [100, 700])

STAGE1.add(5, [], [leftWall, rightWall, lowGround, r5ground1, r5ground2, r5ground3, r5ground4], [r5loading_zone],
           [100, 700], "Brown")


# STAGE1.add(#, [], [], [], [100, 700], "Dark Orange")
# ==========
""" 6 - 10 """
# ==========

""" R6 """
r6ground1 = Objects.Walls(0, 800, 400, 400)
r6ground2 = Objects.Walls(700, 800, 500, 400)
r6ground3 = Objects.Walls(920, 400, 280, 500)

r6spring1 = Objects.Springs(820, 765)

r6loading_zone = Objects.Boundaries(1051, 282, 7, [100, 700])

STAGE1.add(6, [r6spring1], [r6ground1, r6ground2, r6ground3], [r6loading_zone], [100, 700], "Dark Orange")

""" R7 """
r7ground1 = Objects.Walls(400, 700, 1000, 300)
r7ground2 = Objects.Walls(650, 435, 170, 410)
r7ground3 = Objects.Walls(925, 345, 170, 410)

r7spring1 = Objects.Springs(570, 665)
r7spring2 = Objects.Springs(820, 665)
r7spike1 = Objects.Spikes(650, 405)
r7spike2 = Objects.Spikes(720, 405)

r7loading_zone = Objects.Boundaries(1100, 582, 8, [100, 700])

STAGE1.add(7, [r7spring1, r7spring2, r7spike1, r7spike2], [lowGround, r7ground1, r7ground2, r7ground3],
           [r7loading_zone], [100, 700], "Dark Orange")
""" R8 """

r8ground1 = Objects.Walls(400, 800, 1000, 300)
r8ground2 = Objects.Walls(750, 435, 170, 410)
r8ground3 = Objects.Walls(1050, 382, 300, 100)
r8ground4 = Objects.Walls(600, 550, 200, 400)

r8spring1 = Objects.Springs(620, 515)
r8spring2 = Objects.Springs(420, 765)
r8spike1 = Objects.Spikes(750, 405)
r8spike2 = Objects.Spikes(820, 405)
r8spike3 = Objects.Spikes(1050, 355)
r8spike4 = Objects.Spikes(1100, 355)

r8loading_zone = Objects.Boundaries(1100, 682, 9, [100, 700])

STAGE1.add(8, [r8spring1, r8spring2, r8spike1, r8spike2, r8spike3, r8spike4],
           [lowGround, r8ground1, r8ground2, r8ground3, r8ground4], [r8loading_zone], [100, 700], "Dark Orange")

""" R9 """

r9ground1 = Objects.Walls(0, 550, 500, 50)
r9ground2 = Objects.Walls(500, 800, 40, 40)
r9ground3 = Objects.Walls(700, 700, 100, 100)
r9ground4 = Objects.Walls(1100, 400, 100, 100)

r9spring1 = Objects.Springs(720, 665)

r9loading_zone = Objects.Boundaries(1100, 282, 10, [100, 700])


STAGE1.add(9, [r9spring1], [lowGround, r9ground1, r9ground2, r9ground3, r9ground4],
           [r9loading_zone], [100, 700], "Dark Orange")
""" R10 """

r10ground1 = Objects.Walls(100, 550, 100, 300)
r10ground2 = Objects.Walls(300, 450, 100, 300)
r10ground3 = Objects.Walls(500, 350, 100, 300)
r10ground4 = Objects.Walls(750, 925, 100, 300)
r10ground5 = Objects.Walls(1000, 925, 100, 300)
r10ground6 = Objects.Walls(650, 950, 600, 200)
r10ground7 = Objects.Walls(800, 200, 150, 500)

r10spike1 = Objects.Spikes(650, 925)
r10spike2 = Objects.Spikes(850, 925)
r10spike3 = Objects.Spikes(900, 925)
r10spike4 = Objects.Spikes(1100, 925)
r10spring1 = Objects.Springs(1020, 890)

r10loading_zone = Objects.Boundaries(1060, 282, 11, [100, 550])

STAGE1.add(10, [r10spike1, r10spike2, r10spike3, r10spike4, r10spring1],
           [r10ground1, r10ground2, r10ground3, r10ground4, r10ground5, r10ground6, r10ground7],
           [r10loading_zone], [100, 550], "Dark Orange")


# STAGE1.add(#, [], [], [], [100, 700], "Dark Red")
# ===========
""" 11 - 15 """
# ===========
""" R11 """
r11ground1 = Objects.Walls(0, 600, 1200, 40)
r11ground2 = Objects.Walls(900, 800, 300, 100)

r11battery1 = Objects.Batteries(325, 800)
r11battery2 = Objects.Batteries(725, 800)
r11decoration1 = Objects.Decorations(450, 400, pygame.image.load("Billboard_Battery.png"))

r11loading_zone = Objects.Boundaries(1051, 682, 12, [100, 700])

STAGE1.add(11, [r11battery1, r11battery2, r11decoration1], [lowGround, r11ground1, r11ground2], [r11loading_zone], [100, 700]
           , "Dark Red")

""" R12 """
r12ground1 = Objects.Walls(0, 800, 300, 800)
r12ground2 = Objects.Walls(0, 600, 1200, 40)
r12ground3 = Objects.Walls(900, 800, 300, 100)

r12battery1 = Objects.Batteries(725, 800)

r12loading_zone = Objects.Boundaries(1051, 682, 13, [100, 700])

STAGE1.add(12, [r12battery1], [r12ground1, r12ground2, r12ground3], [r12loading_zone], [100, 700]
           , "Dark Red")

""" R13 """
r13ground1 = Objects.Walls(0, 800, 150, 800)
r13ground2 = Objects.Walls(400, 400, 200, 800)
r13ground3 = Objects.Walls(800, 200, 150, 500)

r13spring1 = Objects.Springs(200, 765)
r13battery1 = Objects.Batteries(1045, 642)

r13loading_zone = Objects.Boundaries(1045, 482, 14, [20, 800])

STAGE1.add(13, [r13spring1, r13battery1], [r13ground1, r13ground2, r13ground3], [r13loading_zone], [20, 800], "Dark Red")

""" R14 """
r14ground1 = Objects.Walls(0, 200, 150, 800)
r14ground2 = Objects.Walls(0, 600, 950, 40)
r14ground3 = Objects.Walls(180, 900, 105, 100)

# Did someone say Spike?
# Really should have made a bigger spike for situations like this. Oh well.
r14spike1 = Objects.Spikes(150, 565)
r14spike2 = Objects.Spikes(250, 565)
r14spike3 = Objects.Spikes(350, 565)
r14spike4 = Objects.Spikes(450, 565)
r14spike5 = Objects.Spikes(550, 565)
r14spike6 = Objects.Spikes(650, 565)
r14spike7 = Objects.Spikes(750, 565)
r14spike8 = Objects.Spikes(850, 565)
r14battery1 = Objects.Batteries(1045, 642)
r14battery2 = Objects.Batteries(845, 842)
r14battery3 = Objects.Batteries(545, 842)

r14loading_zone = Objects.Boundaries(200, 782, 15, [20, 200])

STAGE1.add(14, [r14spike1, r14spike2, r14spike3, r14spike4, r14spike5, r14spike6, r14spike7, r14spike8, r14battery1,
                r14battery2, r14battery3], [r14ground1, r14ground2, r14ground3], [r14loading_zone],
           [20, 200], "Dark Red")

# FINAL ROOM
""" R15 """

r15ground1 = Objects.Walls(0, 800, 400, 300)
r15ground2 = Objects.Walls(600, 500, 100, 26)
r15ground3 = Objects.Walls(850, 250, 85, 300)
r15ground4 = Objects.Walls(1000, 650, 250, 100)
r15ground5 = Objects.Walls(0, 200, 40, 600)
r15ground6 = Objects.Walls(0, 200, 200, 100)

r15spring1 = Objects.Springs(300, 765)
r15spring2 = Objects.Springs(1100, 615)
r15battery1 = Objects.Batteries(645, 92)
r15battery2 = Objects.Batteries(345, 92)

r15loading_zone = Objects.Boundaries(50, 82, 16, [100, 700])

STAGE1.add(15, [r15spring1, r15spring2, r15battery1, r15battery2], [r15ground1, r15ground2, r15ground3, r15ground4,
                                                                    r15ground5, r15ground6], [r15loading_zone],
           [100, 700], "Dark Red")  # <--- I have no clue why it does this, it just DOES!

""" WIN ROOM """

r16ground1 = Objects.Walls(0, 800, 1200, 300)

r16decoration1 = Objects.Decorations(450, 600, pygame.image.load("Billboard_Win.png"))

STAGE1.add(16, [r16decoration1], [leftWall, rightWall, r16ground1], [], [200, 800], "Dark Red")


# This is for loading the most recent .get()!
# In other words, it's a dev shortcut.
STAGE1.get(1)


