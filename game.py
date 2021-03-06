import time

import pygame, sys, random, copy

pygame.init()

screen_width= 1100
screen_length = 600

window = pygame.display.set_mode((screen_width,screen_length))

clock = pygame.time.Clock()

pygame.display.set_caption("Goblin Frenzy")

background = pygame.image.load('Graphics/battleback1.png')

character_width = 36
character_height = 48


walkRight = [pygame.transform.scale(pygame.image.load('Graphics/right4.png'), (character_width, character_height)),
             pygame.transform.scale(pygame.image.load('Graphics/right5.png'), (character_width, character_height)),
             pygame.transform.scale(pygame.image.load('Graphics/right6.png'), (character_width, character_height))]

walkLeft  = [pygame.transform.scale(pygame.image.load('Graphics/left4.png'), (character_width, character_height)),
             pygame.transform.scale(pygame.image.load('Graphics/left5.png'), (character_width, character_height)),
             pygame.transform.scale(pygame.image.load('Graphics/left6.png'), (character_width, character_height))]

walkUp =  [pygame.transform.scale(pygame.image.load('Graphics/up1.png'), (character_width, character_height)),
           pygame.transform.scale(pygame.image.load('Graphics/up2.png'), (character_width, character_height)),
           pygame.transform.scale(pygame.image.load('Graphics/up3.png'), (character_width, character_height))]

walkDown = [pygame.transform.scale(pygame.image.load('Graphics/down1.png'), (character_width, character_height)),
            pygame.transform.scale(pygame.image.load('Graphics/down2.png'), (character_width, character_height)),
            pygame.transform.scale(pygame.image.load('Graphics/down3.png'), (character_width, character_height))]

standing = pygame.transform.scale(pygame.image.load('Graphics/Standing.png'), (character_width, character_height))
standingRight = pygame.transform.scale(pygame.image.load('Graphics/right2.png'), (character_width, character_height))
standingLeft = pygame.transform.scale(pygame.image.load('Graphics/left2.png'), (character_width, character_height))

attackingStanceRight = [pygame.transform.scale(pygame.image.load('Graphics/attackRight1.png'), (character_width, character_height)),
                        pygame.transform.scale(pygame.image.load('Graphics/attackRight2.png'), (character_width, character_height)),
                        pygame.transform.scale(pygame.image.load('Graphics/attackRight3.png'), (character_width, character_height))]

attackingStanceLeft = [pygame.transform.scale(pygame.image.load('Graphics/attackLeft1.png'), (character_width, character_height)),
                       pygame.transform.scale(pygame.image.load('Graphics/attackLeft2.png'), (character_width, character_height)),
                       pygame.transform.scale(pygame.image.load('Graphics/attackLeft3.png'), (character_width, character_height))]

attackingStanceUp = [pygame.transform.scale(pygame.image.load('Graphics/attackUp1.png'), (character_width, character_height)),
                        pygame.transform.scale(pygame.image.load('Graphics/attackUp2.png'), (character_width, character_height)),
                        pygame.transform.scale(pygame.image.load('Graphics/attackUp3.png'), (character_width, character_height))]

attackingStanceDown = [pygame.transform.scale(pygame.image.load('Graphics/attackDown1.png'), (character_width, character_height)),
                       pygame.transform.scale(pygame.image.load('Graphics/attackDown2.png'), (character_width, character_height)),
                       pygame.transform.scale(pygame.image.load('Graphics/attackDown3.png'), (character_width, character_height))]



x = 350 #
y = screen_length - (screen_length/2.5) # default position we want our object to start at

walkUpEnemy =  [pygame.transform.scale(pygame.image.load('Graphics/GoblinDown1.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/GoblinDown2.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/GoblinDown3.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/GoblinDown4.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/GoblinDown5.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/GoblinDown6.png'), (1.8 * character_width, 1.2 * character_height))]

walkLeftEnemy= [pygame.transform.scale(pygame.image.load('Graphics/tile033.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/tile034.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/tile035.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/tile036.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/tile037.png'), (1.8 * character_width, 1.2 * character_height)),
                pygame.transform.scale(pygame.image.load('Graphics/tile038.png'), (1.8 * character_width, 1.2 * character_height))]

walkDownEnemy = [pygame.transform.scale(pygame.image.load('Graphics/Goblinup1.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinup2.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinup3.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinup4.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinup5.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinup6.png'), (1.8 * character_width, 1.2 * character_height))]

walkRightEnemy= [pygame.transform.scale(pygame.image.load('Graphics/Goblinright1.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinright2.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinright3.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinright4.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinright5.png'), (1.8 * character_width, 1.2 * character_height)),
                 pygame.transform.scale(pygame.image.load('Graphics/Goblinright6.png'), (1.8 * character_width, 1.2 * character_height))]

enemyAttackRight = [pygame.transform.scale(pygame.image.load('Graphics/enemyAtackRight.png'), (1.8 * character_width, 1.2 * character_height)),
                    pygame.transform.scale(pygame.image.load('Graphics/enemyAtackRight2.png'), (1.8 * character_width, 1.2 * character_height)),
                    pygame.transform.scale(pygame.image.load('Graphics/enemyAtackRight3.png'), (1.8 * character_width, 1.2 * character_height))]

enemyAttackLeft = [pygame.transform.scale(pygame.image.load('Graphics/enemyAtackLeft.png'), (1.8 * character_width, 1.2 * character_height)),
                    pygame.transform.scale(pygame.image.load('Graphics/enemyAtackLeft2.png'), (1.8 * character_width, 1.2 * character_height)),
                    pygame.transform.scale(pygame.image.load('Graphics/enemyAtackLeft3.png'), (1.8 * character_width, 1.2 * character_height))]

enemyAttackUp = [pygame.transform.scale(pygame.image.load('Graphics/enemyAtackUp.png'), (1.8 * character_width, 1.2 * character_height)),
                    pygame.transform.scale(pygame.image.load('Graphics/enemyAtackUp2.png'), (1.8 * character_width, 1.2 * character_height)),
                    pygame.transform.scale(pygame.image.load('Graphics/enemyAtackUp3.png'), (1.8 * character_width, 1.2 * character_height))]

enemyAttackDown = [pygame.transform.scale(pygame.image.load('Graphics/enemyAtackDown.png'), (1.8 * character_width, 1.2 * character_height)),
                    pygame.transform.scale(pygame.image.load('Graphics/enemyAtackDown2.png'), (1.8 * character_width, 1.2 * character_height)),
                    pygame.transform.scale(pygame.image.load('Graphics/enemyAtackDown3.png'), (1.8 * character_width, 1.2 * character_height))]

hit = pygame.transform.scale(pygame.image.load('Graphics/explosion.png'), (character_width, character_height))

explosion  = [pygame.transform.scale(pygame.image.load('Graphics/tile000.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile001.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile002.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile003.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile004.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile005.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile006.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile007.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile008.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile009.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile010.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile011.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile012.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile013.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile014.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile015.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile016.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile017.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile018.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile019.png'), (character_width, character_height)),
              pygame.transform.scale(pygame.image.load('Graphics/tile020.png'), (character_width, character_height))]

potion =[pygame.transform.scale(pygame.image.load('Graphics/health1.png'), (character_width, character_width)),
         pygame.transform.scale(pygame.image.load('Graphics/health2.png'), (character_width, character_width)),
         pygame.transform.scale(pygame.image.load('Graphics/health3.png'), (character_width, character_width)),
         pygame.transform.scale(pygame.image.load('Graphics/health4.png'), (character_width, character_width)),
         pygame.transform.scale(pygame.image.load('Graphics/health5.png'), (character_width, character_width)),
         pygame.transform.scale(pygame.image.load('Graphics/health6.png'), (character_width, character_width)),
         pygame.transform.scale(pygame.image.load('Graphics/health7.png'), (character_width, character_width)),
         pygame.transform.scale(pygame.image.load('Graphics/health8.png'), (character_width, character_width))]

fontSettings = pygame.font.Font('freesansbold.ttf', 32)

width = character_width
height = character_height # size of object

class user():
    def __init__(self, x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 6
        self.isJump = False
        self.jumpDistance = 9 #
        self.jumpCount = 9 # THESE TWO NUMBERS MUST MATCH UP
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.madeFirstMove = False
        self.lastMove = None
        self.hitbox = (self.x, self.y + 2, width, height)
        self.attacking = False
        self.attackFrame = 0
        self.collision = False
        self.level = 1
        self.hitEnemy = False
        self.hitCoordinates = None
        self.health = 100

    def updateChar(self,window): # Animation

        if(self.attackFrame + 1 >= 10):
            self.attackFrame = 0
            self.attacking = False
        if(self.walkCount +1 >= 21):
            self.walkCount = 0
        if(self.left):
            if(self.attacking == True):
                window.blit(attackingStanceLeft[self.attackFrame//3], (self.x,self.y))
                self.attackFrame += 1
            else:
                window.blit(walkLeft[self.walkCount//7], (self.x,self.y))
                self.walkCount += 1
            self.lastMove = "left"

        elif(self.right):
            if(self.attacking == True):
                window.blit(attackingStanceRight[self.attackFrame//3], (self.x,self.y))
                self.attackFrame += 1
            else:
                window.blit(walkRight[player.walkCount//7], (self.x,self.y))
                self.walkCount += 1
            self.lastMove = "right"
        elif(self.down):
            if(self.attacking == True):
                window.blit(attackingStanceDown[self.attackFrame//3], (self.x,self.y))
                self.attackFrame += 1
            else:
                window.blit(walkDown[self.walkCount//7], (self.x,self.y))
                self.walkCount += 1
            self.lastMove = "down"

        elif(self.up):
            if(self.attacking == True):
                window.blit(attackingStanceUp[self.attackFrame//3], (self.x,self.y))
                self.attackFrame += 1
            else:
                window.blit(walkUp[self.walkCount//7], (self.x,self.y))
                self.walkCount += 1
            self.lastMove = "up"
        else:
            if(self.madeFirstMove == False):
                if(self.attacking == True):
                    window.blit(attackingStanceDown[self.attackFrame//3], (self.x,self.y))
                    self.attackFrame += 1
                else:
                    window.blit(standing, (self.x,self.y))
            else:

                if(self.lastMove == "left"):
                    if(self.attacking == True):
                        window.blit(attackingStanceLeft[self.attackFrame//3], (self.x,self.y))
                        self.attackFrame += 1
                    else:
                        window.blit(standingLeft, (self.x,self.y))

                elif(self.lastMove == "right"):
                    if(self.attacking == True):
                        window.blit(attackingStanceRight[self.attackFrame//3], (self.x,self.y))
                        self.attackFrame += 1
                    else:
                        window.blit(standingRight, (self.x,self.y))
                elif(self.lastMove == "up"):
                    if(self.attacking == True):
                        window.blit(attackingStanceUp[self.attackFrame//3], (self.x,self.y))
                        self.attackFrame += 1
                    else:
                        window.blit(walkUp[1], (self.x,self.y))
                else:
                    if(self.attacking == True):
                        window.blit(attackingStanceDown[self.attackFrame//3], (self.x,self.y))
                        self.attackFrame += 1
                    else:
                        window.blit(standing, (self.x,self.y))
        if(self.hitEnemy == True):
            window.blit(hit, self.hitCoordinates)
            self.hitEnemy = False
            self.hitCoordinates = None

        self.hitbox = (self.x, self.y + 2, width, height)
        #pygame.draw.rect(window, (255,0,0), self.hitbox,2)



class Enemy:
    def __init__(self, x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.maxDistance = 85
        self.directionCount = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.velocity = 1
        self.walkCount = 0
        self.hitbox = (self.x + 15, self.y , width + 5, height + 7)
        self.health = 100
        self.beenAttacked = False
        self.lastMove = None
        self.bounds = (self.x + 22, self.y +6 , width -10, height -10)
        self.dead = False
        self.explosionFrame = 0
        self.blastRadius = (self.x + 35, self.y + 28, width + 9, width + 9)
        self.distanceFromUser = [0,0]
        self.attacking = False
        self.cooldown = 0
        self.attackFrame = 0


    def updateMonster(self, window):

        if(self.explosionFrame + 1 >= 20):
            self.explosionFrame = 0
            self.dead = True
        if(self.health <= 0):
            window.blit(explosion[self.explosionFrame], (self.x,self.y))
            self.explosionFrame +=1
        else:
            if(self.walkCount +1 >= 72):
                self.walkCount = 0

            if(self.left):
                window.blit(walkLeftEnemy[self.walkCount//12], (self.x,self.y))
                self.walkCount += 1

            elif(self.right):
                window.blit(walkRightEnemy[self.walkCount//12], (self.x,self.y))
                self.walkCount += 1

            elif(self.down):
                window.blit(walkDownEnemy[self.walkCount//12], (self.x,self.y))
                self.walkCount += 1

            elif(self.up):
                window.blit(walkUpEnemy[self.walkCount//12], (self.x,self.y))
                self.walkCount += 1
            else:
                if(self.attackFrame + 1 >= 10):
                    self.attackFrame = 0
                if(self.lastMove == "left"):
                    window.blit(enemyAttackLeft[self.attackFrame//3], (self.x,self.y))
                    self.attackFrame +=1
                elif(self.lastMove == "right"):
                    window.blit(enemyAttackRight[self.attackFrame//3], (self.x,self.y))
                    self.attackFrame +=1
                elif(self.lastMove == "up"):
                    window.blit(enemyAttackUp[self.attackFrame//3], (self.x,self.y))
                    self.attackFrame +=1
                elif(self.lastMove == "down"):
                    window.blit(enemyAttackDown[self.attackFrame//3], (self.x,self.y))
                    self.attackFrame +=1


        self.hitbox = (self.x + 15, self.y, width + 5, height + 7)
        #pygame.draw.rect(window, (255,255,0), self.hitbox,2)
        self.bounds = (self.x + 10 , self.y  , width + 10, height  + 10)
        #pygame.draw.rect(window, (255,0,0), self.bounds,2)
        self.blastRadius = (self.x, self.y, width + 10, width + 10)
        #pygame.draw.circle(window, (0,0,255), (self.x + 35, self.y + 28), width + 9,  2)

class healthPotion:
    def __init__(self,x,y,width,length):
        self.x = x
        self.y = y
        self.range = (self.x,self.y, width,length)
        self.frame = 0
        self.width = width
        self.length = length

    def displayPotion(self,window):
        if(self.frame +1 >= 24):
            self.frame = 0
        window.blit(potion[self.frame//4],(self.x,self.y))
        self.frame +=1

        self.range = (self.x,self.y, self.width,self.length)
        #pygame.draw.rect(window,(0,0,255),self.range,2)





run = True

player = user(x,y,character_width, character_height)

Goblin = []

Goblin.append(Enemy(900, 350, 1.8*character_width, 1.2*character_height))
Goblin[0].left = True
Goblin[0].maxDistance += 20
Goblin[0].lastMove = "left"

Goblin.append(Enemy(200, 320, 1.8*character_width, 1.2*character_height))
Goblin[1].right = True
Goblin[0].maxDistance -= 20
Goblin[1].lastMove = "right"

oldGoblin = copy.deepcopy(Goblin)

potions = []

def displayLevel(x,y):
    level = fontSettings.render("Round: " + str(player.level), True, (255,0,0))
    window.blit(level, (x,y))

def displayHealth(x,y):
    if player.health<= 0:
        player.health = 0
    health = fontSettings.render("Health: " + str(player.health), True, (255,255,0))
    window.blit(health, (x,y))

def updateScreen():
    window.blit(background, (0,0))

    for i in range(len(Goblin)):
        Goblin[i].updateMonster(window)

    for i in range(len(potions)):
        potions[i].displayPotion(window)

    player.updateChar(window)



    displayLevel(900,50)
    displayHealth(75,50)

    pygame.display.update()




#GAME LOOP:
unwanted = []
while run:

    clock.tick(42)


    if(player.health <= 25):
        if(len(potions) == 0): # if there is not already a potion on the field
            y = random.randint(1,20)
            if(y >= 10):   # add a potion to a random part fo the field
                potions.append(healthPotion(500 + random.randint(-20,100), 280 + random.randint(-20,50), character_width, character_width))
            elif(y < 10 and y >= 6):
                potions.append(healthPotion(800 + random.randint(-20,100), 280 + random.randint(-20,50), character_width, character_width))
            else:
                potions.append(healthPotion(320 + random.randint(-20,100), 280 + random.randint(-20,50), character_width, character_width))
    else:
        if(len(potions) == 0):
            if(random.randint(1,(5000 - 5*player.level)) == 517): # randomly generate a potion regardless of health status
                                                                # odds of a random potion generation increase as the rounds do
                y = random.randint(1,20)
                if(y >= 10):   # add a potion to a random part fo the field
                    potions.append(healthPotion(500 + random.randint(-20,100), 280 + random.randint(-20,50), character_width, character_width))
                elif(y < 10 and y >= 6):
                    potions.append(healthPotion(800 + random.randint(-20,100), 280 + random.randint(-20,50), character_width, character_width))
                else:
                    potions.append(healthPotion(320 + random.randint(-20,100), 280 + random.randint(-20,50), character_width, character_width))

    if(len(potions) != 0):
        if(player.hitbox[0] + player.hitbox[2] >= potions[0].range[0]): # if player grabs a potion
            if(player.hitbox[0] - .1*player.hitbox[2] <= potions[0].range[0] + potions[0].range[2]):
                if(player.hitbox[1] - .1*player.hitbox[3] <= potions[0].range[1] + potions[0].range[3]):
                    if(player.hitbox[1] + player.hitbox[3] >= potions[0].range[1]):
                        del potions[0]
                        if(player.health + 35 < 100):
                            player.health += 35
                        else:
                            player.health = 100
    unwanted = []
    for i in range(len(Goblin)): # only display goblins that are still alive
        if(Goblin[i].dead):
            unwanted.append(i)

    sortedUnwanted = sorted(unwanted, reverse=True) # MUST be sorted or else there will be an idnex put of range error if 2 goblins are killed at once
    for i in range(len(unwanted)): # avoid memory leaks by deleting dead goblins instead of just removing them from the list
        del Goblin[sortedUnwanted[i]]

    switch = False # If one Goblin gets attacked they all chase you
    for i in range(len(Goblin)):
        if(Goblin[i].beenAttacked):
            switch = True

    if(switch) :
        for i in range(len(Goblin)):
            Goblin[i].beenAttacked = True


    if(len(Goblin) == 0): # New Level
        if(len(potions) != 0):
            del potions[0] # remove any potion on the field
        player.level += 1
        player.health = 100 # Reset health
        y = random.randint(1,20)
        if(y >= 10):   # Update spawning algorithm
            oldGoblin.append(Enemy(500 + random.randint(-20,100), 280 + random.randint(-20,100), 1.8*character_width, 1.2*character_height))
        elif(y < 10 and y >= 6):
            oldGoblin.append(Enemy(800 + random.randint(-20,100), 280 + random.randint(-20,100), 1.8*character_width, 1.2*character_height))
        else:
            oldGoblin.append(Enemy(320 + random.randint(-20,100), 280 + random.randint(-20,100), 1.8*character_width, 1.2*character_height))

        x = random.randint(1,4)
        if(x == 1):
            oldGoblin[-1].right = True
            oldGoblin[-1].lastMove = "right"
        elif(x ==2):
            oldGoblin[-1].left = True
            oldGoblin[-1].lastMove = "left"
        elif(x == 3):
            oldGoblin[-1].up = True
            oldGoblin[-1].lastMove = "up"
        else:
            oldGoblin[-1].down = True
            oldGoblin[-1].lastMove = "down"
        oldGoblin[-1].velocity += random.random()
        oldGoblin[-1].maxDistance += random.randint(-25,10)
        Goblin = copy.deepcopy(oldGoblin)


    for event in pygame.event.get():
        if event.type == pygame.QUIT: # allows you to exit
            run = False
        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_c): # if player attacks
                player.attacking = True
                for i in range(len(Goblin)):
                    if(player.hitbox[0] + player.hitbox[2] >= Goblin[i].hitbox[0]): # if player hits
                        if(player.hitbox[0] - .8*player.hitbox[2] <= Goblin[i].hitbox[0] + .3*Goblin[i].hitbox[2]):
                            if(player.hitbox[1] - player.hitbox[3] <= Goblin[i].hitbox[1] + .2*Goblin[i].hitbox[3]):
                                if(player.hitbox[1] + player.hitbox[3] >= Goblin[i].hitbox[1]):
                                    # Check direction
                                    if(player.x <= Goblin[i].hitbox[0] and player.lastMove == "right"):
                                        Goblin[i].beenAttacked = True
                                        Goblin[i].health -= 10
                                        player.hitEnemy = True
                                        player.hitCoordinates = (Goblin[i].x, Goblin[i].y)
                                        Goblin[i].lastMove = "left"

                                    elif(player.x > Goblin[i].hitbox[0] and player.lastMove == "left"):
                                        Goblin[i].beenAttacked = True
                                        Goblin[i].health -= 10
                                        player.hitEnemy = True
                                        player.hitCoordinates = (Goblin[i].x + 30, Goblin[i].y)
                                        Goblin[i].lastMove = "right"

                                    elif(player.y >= Goblin[i].hitbox[1] and player.lastMove == "up"):
                                        Goblin[i].beenAttacked = True
                                        Goblin[i].health -= 10
                                        player.hitEnemy = True
                                        player.hitCoordinates = (Goblin[i].x + 15, Goblin[i].y + 25)
                                        Goblin[i].lastMove = "down"

                                    elif(player.y < Goblin[i].hitbox[1]  and player.lastMove == "down"):
                                        Goblin[i].beenAttacked = True
                                        Goblin[i].health -= 10
                                        player.hitEnemy = True
                                        player.hitCoordinates = (Goblin[i].x + 15 , Goblin[i].y - 20)
                                        Goblin[i].lastMove = "up"





    keys = pygame.key.get_pressed() # gather user key info

    for i in range(len(Goblin)):
        if(Goblin[i].beenAttacked != True): # if goblin has not been attacked yet
            if(Goblin[i].left == True): # Goblin moves in a loop

                if(Goblin[i].directionCount == Goblin[i].maxDistance):
                    Goblin[i].left = False
                    Goblin[i].up = True
                    Goblin[i].directionCount = 0
                else:
                    Goblin[i].lastMove = "left"
                    Goblin[i].x -= Goblin[i].velocity
                    Goblin[i].directionCount += 1

            elif(Goblin[i].up == True):

                if(Goblin[i].directionCount == Goblin[i].maxDistance):
                    Goblin[i].up = False
                    Goblin[i].right = True
                    Goblin[i].directionCount = 0
                else:
                    Goblin[i].lastMove = "up"
                    Goblin[i].y -= Goblin[i].velocity
                    Goblin[i].directionCount += 1

            elif(Goblin[i].right == True):

                if(Goblin[i].directionCount == Goblin[i].maxDistance):
                    Goblin[i].right = False
                    Goblin[i].down = True
                    Goblin[i].directionCount = 0
                else:
                    Goblin[i].x += Goblin[i].velocity
                    Goblin[i].directionCount += 1
                    Goblin[i].lastMove = "right"
            else:

                if(Goblin[i].directionCount == Goblin[i].maxDistance):
                    Goblin[i].down = False
                    Goblin[i].left = True
                    Goblin[i].directionCount = 0
                else:
                    Goblin[i].lastMove = "down"
                    Goblin[i].y += Goblin[i].velocity
                    Goblin[i].directionCount += 1

        else: # After Goblin is attacked for the first time # Chase Player

            Goblin[i].left = False
            Goblin[i].right = False
            Goblin[i].up = False
            Goblin[i].down = False
            Goblin[i].attacking = False
            Goblin[i].distanceFromUser = [abs(Goblin[i].x - player.x), abs(Goblin[i].y - player.y)]

            if(player.x <= Goblin[i].x):
                if not (player.hitbox[0] + player.hitbox[2] >= Goblin[i].hitbox[0] and player.hitbox[0] - .8*player.hitbox[2] <= Goblin[i].hitbox[0] + .3*Goblin[i].hitbox[2]
                    and player.hitbox[1] - player.hitbox[3] <= Goblin[i].hitbox[1] + .2*Goblin[i].hitbox[3]
                    and player.hitbox[1] + player.hitbox[3] >= Goblin[i].hitbox[1]):
                            Goblin[i].left = True

            if(player.x > Goblin[i].x):
                if not (player.hitbox[0] + player.hitbox[2] >= Goblin[i].hitbox[0] and player.hitbox[0] - .8*player.hitbox[2] <= Goblin[i].hitbox[0] + .3*Goblin[i].hitbox[2]
                        and player.hitbox[1] - player.hitbox[3] <= Goblin[i].hitbox[1] + .2*Goblin[i].hitbox[3]
                        and player.hitbox[1] + player.hitbox[3] >= Goblin[i].hitbox[1]):
                            Goblin[i].right = True

            if(player.y >= Goblin[i].y):
                if not (player.hitbox[0] + player.hitbox[2] >= Goblin[i].hitbox[0] and player.hitbox[0] - .8*player.hitbox[2] <= Goblin[i].hitbox[0] + .3*Goblin[i].hitbox[2]
                        and player.hitbox[1] - player.hitbox[3] <= Goblin[i].hitbox[1] + .2*Goblin[i].hitbox[3]
                        and player.hitbox[1] + player.hitbox[3] >= Goblin[i].hitbox[1]):
                            Goblin[i].down = True

            if(player.y < Goblin[i].y):
                if not (player.hitbox[0] + player.hitbox[2] >= Goblin[i].hitbox[0] and player.hitbox[0] - .8*player.hitbox[2] <= Goblin[i].hitbox[0] + .3*Goblin[i].hitbox[2]
                        and player.hitbox[1] - player.hitbox[3] <= Goblin[i].hitbox[1] + .2*Goblin[i].hitbox[3]
                        and player.hitbox[1] + player.hitbox[3] >= Goblin[i].hitbox[1]):
                        Goblin[i].up = True

            if(Goblin[i].cooldown > 0):
                Goblin[i].cooldown -= 1

            if((Goblin[i].left == True or Goblin[i].right == True)  and (Goblin[i].up == True or Goblin[i].down == True)):
                if(Goblin[i].distanceFromUser[0] > Goblin[i].distanceFromUser[1] or Goblin[i].cooldown > 0):
                    if(Goblin[i].left == True):
                        Goblin[i].x -= Goblin[i].velocity
                        Goblin[i].lastMove = "left"

                    if(Goblin[i].right == True):
                        Goblin[i].x += Goblin[i].velocity
                        Goblin[i].lastMove = "right"
                elif(Goblin[i].distanceFromUser[0] < Goblin[i].distanceFromUser[1] and Goblin[i].cooldown == 0): # Go in the direction thats closest to user, dont go in two directions at onces (diagonal)
                    Goblin[i].left = False
                    Goblin[i].right = False
                    if(Goblin[i].down == True):
                        Goblin[i].y += Goblin[i].velocity
                        Goblin[i].lastMove = "down"
                    if(Goblin[i].up == True):
                        Goblin[i].y -= Goblin[i].velocity
                        Goblin[i].lastMove = "up"
                else: # If the goblins are equal distance x and y from you then they will rapidly oscillate towards the user
                    # to fix this I added a cooldown "timer"
                    # this also helps goblins from stacking on top of each other when attacking player
                    Goblin[i].cooldown = 15
                    if(Goblin[i].left == True):
                        Goblin[i].x -= Goblin[i].velocity
                        Goblin[i].lastMove = "left"

                    if(Goblin[i].right == True):
                        Goblin[i].x += Goblin[i].velocity
                        Goblin[i].lastMove = "right"


            else:
                if(Goblin[i].left):
                    Goblin[i].x -= Goblin[i].velocity
                    Goblin[i].lastMove = "left"
                elif(Goblin[i].right):
                    Goblin[i].x += Goblin[i].velocity
                    Goblin[i].lastMove = "right"
                elif(Goblin[i].up):
                    Goblin[i].y -= Goblin[i].velocity
                    Goblin[i].lastMove = "up"
                elif(Goblin[i].down):
                    Goblin[i].y += Goblin[i].velocity
                    Goblin[i].lastMove = "down"





    if(keys[pygame.K_LEFT] and player.x >= player.velocity + 40 ): # if not out of bounds, move
        player.x -= player.velocity
        player.left = True
        player.right = False
        player.up = False
        player.down = False
        player.madeFirstMove = True

    elif(keys[pygame.K_RIGHT] and player.x <= screen_width - (player.width-1) - player.velocity - 40):# if not out of bounds, move
        player.x += player.velocity
        player.right = True # for animation
        player.left = False #
        player.up = False
        player.down = False
        player.madeFirstMove = True

    elif(keys[pygame.K_UP] and player.y >= player.velocity + 190):# if not out of bounds, move
        player.y -= player.velocity
        player.right = False # for animation
        player.left = False #
        player.up = True
        player.down = False
        player.madeFirstMove = True

    elif(keys[pygame.K_DOWN] and player.y <= screen_length - (player.height + 2) - player.velocity - 140): # if not out of bounds, move
        if(player.isJump == False):
            player.y += player.velocity
            player.right = False # for animation
            player.left = False #
            player.up = False
            player.down = True
            player.madeFirstMove = True
    else: # if not out of bounds, move
        if(player.isJump == False):
            player.right = False #
            player.left = False # for animation
            player.up = False
            player.down = False
            player.walkCount = 0

    if(player.isJump == False): # "if not(isJump)", player jumps
        if(keys[pygame.K_SPACE]):
            player.isJump = True
            player.walkCount = 0

    else: # so we cannot jump twice in mid-air
    #if we uncomment this then we cannot jump and attack, I am still debating whether we should be able to
    # jump and attack at the same time:
        #player.attacking = False
        #player.attackFrame = 0

        if(player.jumpCount >= -player.jumpDistance): # jump algorithm

            if(player.jumpCount < 0):
                player.y += (player.jumpCount ** 2) / 2

            else:
                player.y -= (player.jumpCount ** 2) / 2

            player.jumpCount -= 1

        else: # restore default values
            player.isJump = False
            player.jumpCount = player.jumpDistance

# Player being attacked
    for i in range(len(Goblin)):
       if(player.hitbox[0] + player.hitbox[2] >= Goblin[i].bounds[0]
            and player.hitbox[0] - .7*player.hitbox[2] <= 1.1*Goblin[i].bounds[0]
            and player.hitbox[1] - .75*player.hitbox[3] <= 1.1*Goblin[i].bounds[1]
            and player.hitbox[1] + player.hitbox[3] >= Goblin[i].bounds[1]):
            if(Goblin[i].beenAttacked == True):
                if(random.randint(1,25) == 1): # theoretically 1/25 odds , balances the game at higher levels
                    player.health -= 2


    updateScreen()

    if(player.health <= 0): # Game over
        font = pygame.font.Font('freesansbold.ttf', 100)

        gameOver = font.render("GAME OVER", True, (255,0,0))
        madeIt = fontSettings.render("you made it to round " + str(player.level), True, (255,0,0))

        temp_surface = pygame.Surface(gameOver.get_size())
        temp_surface2 = pygame.Surface(madeIt.get_size())
        temp_surface.fill((255, 255, 255))
        temp_surface2.fill((255, 255, 255))

        window.blit(temp_surface, (250,250))
        window.blit(temp_surface2, (370,350))
        window.blit(gameOver,(250,250))
        window.blit(madeIt, (370,350))

        pygame.display.update()
        time.sleep(7)
        break

pygame.quit()

