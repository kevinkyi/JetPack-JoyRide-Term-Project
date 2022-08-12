#from/influenced by jetpack joyride
from cmu_112_graphics import*
import random, time 

class missile(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.randomMissile1 = random.randint(50,430)
        self.randomMissile2 = random.randint(50,430)
        self.randomMissile3 = random.randint(50,430)

    def hardMissileY(self, characterY):
        hardYpos = int(characterY)
        return hardYpos     

    def easyMissileY(self):
        return random.randint(30,450)
      
def appStarted(app):
    ### Code for the game screen ###
    s1 = 'https://s3.amazonaws.com/gameartpartnersimagehost/'
    s2 = 'wp-content/uploads/2017/12/Flat_Game_Background_2.jpg'
    url = 'https://i.redd.it/4hurq0y5yms11.png'
    app.backgroundStrip = app.loadImage(url)
    app.gameStarted = False
    app.gameOver = False
    app.score = 0
    app.time = time.time()
    app.time2 = time.time()
    app.timeLaser = time.time()
    app.timeCoin = time.time()
    app.timeCoin2 = time.time()

    app.speedMultiplier = 1
    
    #scrolling iamage vars
    app.imageX = 540
    app.rightSideOfImage = 270

    #square character
    app.characterMove = 0
    app.gravity = 20
    app.topOfRectangle = app.height - 60
    app.bottomOfRectangle = app.height - 10

    #barry character flying

    app.flyingUrl = 'barryflying[1997].png'
    app.flyingSprite = app.loadImage(app.flyingUrl)
    app.flyingImage = app.flyingSprite.resize((85,85))
    #canvas.create_image(x,y,image=ImageTk.PhotoImage(sprite))

    #barry running character(sprite sheet)
    app.runningUrl = 'BarryFullSpriteSheet[1996].png'
    app.spritestrip = app.loadImage(app.runningUrl)
    
    app.sprite= [ ]

    for i in range(4):
        sprite = app.spritestrip.crop((153.5*i, 0, 152*(i+1), 146))
        app.runningImage = sprite.resize((100,100))      

        app.sprite.append(app.runningImage)
    app.spriteCounter = 0

    #code for missiles(using squares)
    app.randomMissile1 = random.randint(50,430)
    app.randomMissile2 = random.randint(50,430)
    app.randomMissile3 = random.randint(50,430)
    app.easyMissileY = random.randint(60,420)

    app.missileDifficulty = "easy difficulty"
    app.missileLaunch = False
    app.missileFired = 0
    app.missilesLaunched = 5
    app.missileDelay = 10
    app.missileYValue = 0
    app.hardMissileY = 200 #grabbing random y value for hard missile
    app.startingMissile = False
    app.easyMissileLaunch = False
  
    app.easyMissilesLaunched = 3

    app.missileUrl = "missileLaunch.png"
    app.missileFile = app.loadImage(app.missileUrl)
    app.missileImage = app.missileFile.resize((180,180))

    #code for lasers(using lines)
    app.laserDifficulty = "easy" 
    app.laserPlaced = False
    app.secondLaserPlaced = False
    app.laserMove = 0 
    app.laserMove2 = 0
    app.randomLaserPlacement = random.randint(120,370)
    app.randomLaserPlacement2 = random.randint(120,370)
    app.randomLaserLength = random.randint(70, 130)
    app.randomHorizontalLaserLength = random.randint(50, 150)
    app.laserLaunch = False 
    app.randomLaser = random.randint(1,3)
    app.randomLaser2 = random.randint(1,3)

    app.verticalLaserUrl = "verticalLaser.png"
    app.verticalLaser = app.loadImage(app.verticalLaserUrl)
    app.verticalLaserImage = app.verticalLaser.resize((550,550))

    app.horizontalLaserUrl = "horizontalLaser.png"
    app.horizontalLaser = app.loadImage(app.horizontalLaserUrl)
    app.horizontalLaserImage = app.horizontalLaser.resize((550,550))

    #code for coin algorithm
    app.coinDuplicate = False
    app.coinScore = 0
    app.coinPlaced = False
    app.coinMove = 0 
    app.randomCoinPlacement = random.randint(50, 430)
    app.characterPos = []
    app.obstaclePos = []

    app.laserY = 0
    app.laserRandomY = 0
    app.laserY2 = 0
    app.laserRandomY2 = 0
    app.missileY = 0
    
    app.coinX = app.width - 50
    app.coinY = 200


    ### Code for the starting and difficulty screen ###
    app.difficulty = "hard difficulty"
    app.mode = "startingScreen"
    #variables for the start screen
    url = 'starting screen.jpg'
    app.screen = app.loadImage(url)
    app.startingScreen = app.screen.resize((1075,480))
    app.will = False
    

    #variables for the difficulty changing screen
    hardDifficultyUrl = 'Barry(hard difficulty picture).jpg'
    app.hardDifficultyImage = app.loadImage(hardDifficultyUrl)
    app.hardImage = app.hardDifficultyImage.resize((575,535))

    easyDifficultyUrl = 'Barry(easy difficulty picture).png'
    app.easyDifficultyImage = app.loadImage(easyDifficultyUrl)
    app.easyImage = app.easyDifficultyImage.resize((575,535))

    #lighter barry images 

    lighterHardUrl = 'Barry(Lighter Hard Image).jpg'
    app.lighterHard = app.loadImage(lighterHardUrl)
    app.lighterHardImage = app.lighterHard.resize((575,535))

    lighterEasyUrl = 'Barry(Lighter Easy Image).png'
    app.lighterEasy = app.loadImage(lighterEasyUrl)
    app.lighterEasyImage = app.lighterEasy.resize((575,535))

    #changes contract of Barry images
    app.mouseLeftSide = False
    app.mouseRightSide = False

    ### Code for the end screen ###
    app.currentScore = 0 
    app.bestScore = 0
    app.winnerCheck = False
    app.winnerMessage = "Congratulations you have hit a high score!!!"
    app.returnButton = False

    app.endScreenImage = app.loadImage("endScreen.jpg")

    #code for game lives 
    app.lives = 3
    app.missileImpact = True
    app.laserImpact = True
    app.laserImpact2 = True
    
    app.heartImageLoad = app.loadImage("heartImage.png")
    app.heartImage = app.heartImageLoad.resize((100,100))


def gameScreen_pathFindingAlgorithm(app,characterPos,obstaclePos):
    hemisphere = "upper"
    obstacleNum = len(obstaclePos)
    distanceBetweenObstacles = 0
    maxY = 0
    # 3 obstacles 
    largestY = 0 
    smallestY = 0
    middleY = 0

    if characterPos[1] < 240:
        hemisphere = "upper"
    if characterPos[1] >= 240:
        hemisphere = "lower"

    if obstacleNum == 1:
        if characterPos[1] - obstaclePos[0][1] < 30 and hemisphere == 'upper':
            return obstaclePos[0][1] - 50

        if characterPos[1] - obstaclePos[0][1] < 30 and hemisphere == 'lower':
            if characterPos[1] == 420:
                return app.height - 150
            return obstaclePos[0][1] + 50
    
    if obstacleNum == 2:
        distanceBetweenObstacles = (obstaclePos[0][1] + obstaclePos[1][1])//2
        if distanceBetweenObstacles > characterPos[1]:
            if hemisphere == "upper":
                return max(obstaclePos[0][1], obstaclePos[1][1]) - (distanceBetweenObstacles/3)
            if hemisphere == "lower":
                return min(obstaclePos[0][1], obstaclePos[1][1]) + (distanceBetweenObstacles/3)


    if obstacleNum == 3: 
        largestY, smallestY = max(int(obstaclePos[0][1]), int(obstaclePos[1][1]), 
                        int(obstaclePos[2][1])), min(int(obstaclePos[0][1]), 
                        int(obstaclePos[1][1]), int(obstaclePos[2][1]))
        for i in range(len(obstaclePos)):
            if obstaclePos[i][1] != largestY and obstaclePos[i][1] != smallestY:
                middleY = obstaclePos[i][1]
        
        if largestY - middleY > middleY - smallestY:
            return largestY - ((largestY - middleY)/2)

        elif middleY - smallestY > largestY - middleY:
            return middleY - ((middleY - smallestY)/2)

        elif characterPos[1] > largestY or characterPos[1] < smallestY: 
            return characterPos[1]

        else:
            return smallestY + 100
                
    else:
        return 200         


def gameScreen_hardMissileImpact(app):
    L1 = [app.width - 925, app.topOfRectangle - 35, app.width-870,app.topOfRectangle +35]
    L2 = [app.width - 80 - app.missileFired, app.hardMissileY - 15, 
    app.width - 20 - app.missileFired, app.hardMissileY +15]
    if L1[0] <= L2[0] <= L1[2]:

        #if (L1[0] >= L2[2] or L1[3] <= L2[1] or L1[2] <= L2[0] or L1[1] >= L2[3]):
        if L1[1] <= L2[1] <= L1[3] or L1[1] <= L2[3] <= L1[3]:
            return True
        else:
            return False

    return False


def gameScreen_easyMissileImpact(app):
    L1 = [app.width - 925, app.topOfRectangle - 35, app.width-870,app.topOfRectangle +35]
    L2 = [app.width - 80 - app.missileFired, app.easyMissileY - 15, 
    app.width - 20 - app.missileFired, app.easyMissileY +15]
    if L1[0] <= L2[0] <= L1[2]:

        #if (L1[0] >= L2[2] or L1[3] <= L2[1] or L1[2] <= L2[0] or L1[1] >= L2[3]):
        if L1[1] <= L2[1] <= L1[3] or L1[1] <= L2[3] <= L1[3]:
            return True
        else:
            return False

    return False


def gameScreen_LaserImpact(app):
    L1 = [app.width - 925, app.topOfRectangle - 35, app.width-870,app.topOfRectangle +35]
    L2 = [app.width - 55 - app.laserMove, app.height - app.randomLaserPlacement -140,
                app.width - 35 - app.laserMove, app.height - app.randomLaserPlacement]
    L3 =[app.width - app.laserMove - 95, app.height - app.randomLaserPlacement - 80, 
                app.width + 5 - app.laserMove, app.height - app.randomLaserPlacement - 60]
    if app.laserPlaced:
        if app.randomLaser == 1 or app.randomLaser == 2:
            if L1[0] <= L2[0] <= L1[2]:

                if L1[1] <= L2[1] <= L1[3] or L1[1] <= L2[3] <= L1[3]:
                    return True
                else:
                    return False

        if app.randomLaser == 3:
            if L1[0] <= L3[0] <= L1[2]:

                if L1[1] <= L3[1] <= L1[3] or L1[1] <= L3[3] <= L1[3]:
                    return True
                else:
                    return False

def gameScreen_secondLaserImpact(app):
    L1 = [app.width - 925, app.topOfRectangle - 35, app.width-870,app.topOfRectangle +35]
    L2 = [app.width - 55 - app.laserMove2, app.height - app.randomLaserPlacement2 -140,
                app.width - 35 - app.laserMove2, app.height - app.randomLaserPlacement2]
    L3 =[app.width - app.laserMove2 - 95, app.height - app.randomLaserPlacement2 - 80, 
                app.width + 5 - app.laserMove2, app.height - app.randomLaserPlacement2 - 60]
    if app.laserPlaced:
        if app.randomLaser2 == 1 or app.randomLaser2 == 2:
            if L1[0] <= L2[0] <= L1[2]:

                if L1[1] <= L2[1] <= L1[3] or L1[1] <= L2[3] <= L1[3]:
                    return True
                else:
                    return False

        if app.randomLaser2 == 3:
            if L1[0] <= L3[0] <= L1[2]:

                if L1[1] <= L3[1] <= L1[3] or L1[1] <= L3[3] <= L1[3]:
                    return True
                else:
                    return False
 
def gameScreen_coinImpact(app):
    L1 = [app.width - 925, app.topOfRectangle - 35, app.width-870,app.topOfRectangle +35]
    L2 = [app.coinX - app.coinMove, app.coinY, app.coinX + 40 - app.coinMove, 
          app.coinY + 40]
    if app.coinPlaced:
        if L1[0] <= L2[0] <= L1[2]:

            if L1[1] <= L2[1] <= L1[3] or L1[1] <= L2[3] <= L1[3]:
                return True
            else:
                return False


def gameScreen_timerFired(app):
    #Side scrolling timer fired
    app.imageX -= 5 * app.speedMultiplier
    app.speedMultiplier *= 1.001

    if app.imageX < 0:
        app.imageX = 540
    
    if not app.gameOver:
        app.score += 10

    #timer fired for barry flying(constant gravity)
    if app.bottomOfRectangle != app.height - 10: #and app.topOfRectangle != 0:
        app.bottomOfRectangle = app.bottomOfRectangle + app.gravity
        app.topOfRectangle = app.topOfRectangle + app.gravity

    #timerFired for Barry running sprite
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprite)

#life checker
    if app.lives == 0:
        app.mode = "endScreen"
        app.gameOver = True

    
#hard missile timer delay
    if app.gameStarted:
        if app.difficulty == "hard difficulty":
            if time.time() - app.time > 13:
                app.startingMissile = False
                app.missileLaunch = False
            if time.time() - app.time > 15:
                app.missileImpact = True
                app.startingMissile = True
            if time.time() - app.time > 25:
                app.hardMissileY = missile.hardMissileY(app, app.topOfRectangle)
                app.missileLaunch = True
                app.time = time.time()
                app.missileFired = 0
            if gameScreen_hardMissileImpact(app):
                if app.missileImpact:
                    app.lives -= 1
                    app.missileImpact = False
      
    
#easy missile timer delay
    if app.gameStarted:
        if app.difficulty == "easy difficulty":
            if 1 < time.time() - app.time2 < 2:
                app.missileImpact = True

            if time.time() - app.time2 > 5:
                app.easyMissileLaunch = True

            if time.time() - app.time2 > 10:
                app.missileLaunch = True

            if time.time() - app.time2 > 25:
                app.missileLaunch = False
                app.easyMissileLaunch = False
                app.time2 = time.time()
                app.missileFired = 0
                app.easyMissileY = random.randint(70,410)
            if gameScreen_easyMissileImpact(app):
                if app.missileImpact:
                    app.lives -= 1
                    app.missileImpact = False

#easy laser time delay
    if app.gameStarted: 
        if app.difficulty == "easy difficulty":
            if time.time() - app.timeLaser > 5:
                app.laserPlaced = True
            if time.time() - app.timeLaser > 20:
                app.laserPlaced = False
                app.timeLaser = time.time()
                app.laserMove = 0
                app.randomLaserPlacement = random.randint(120,370)
                app.randomLaser = random.randint(1,3)
            if gameScreen_LaserImpact(app):
                if app.laserImpact:
                    app.lives -= 1
                    app.laserImpact = False

#hard laser delay
    if app.gameStarted:
        if app.difficulty == "hard difficulty":
            if 2 > time.time() - app.timeLaser > 1:
                app.laserImpact = True
                app.laserImpact2 = True

            if time.time() - app.timeLaser > 5:
                app.laserPlaced = True

            if time.time() - app.timeLaser > 10:
                app.secondLaserPlaced = True

            if time.time() - app.timeLaser > 25:
                app.laserPlaced = False
                app.secondLaserPlaced = False
                app.timeLaser = time.time()
                app.laserMove = 0
                app.laserMove2 = 0
                app.randomLaserPlacement = random.randint(120,370)
                app.randomLaser = random.randint(1,3)

                app.randomLaserPlacement2 = random.randint(120,370)
                app.randomLaser2 = random.randint(1,3)

            if gameScreen_LaserImpact(app):
                if app.laserImpact:
                    app.lives -= 1
                    app.laserImpact = False
                    print(app.lives)

            if gameScreen_secondLaserImpact(app):
                if app.laserImpact2:
                    app.lives -= 1
                    app.laserImpact2 = False

#coin algorithm
    if app.gameStarted: 
        if app.difficulty == "hard difficulty":
            if time.time() - app.timeCoin > 26:
                app.laserY = app.laserMove
                app.laserRandomY = app.randomLaserPlacement

                app.laserY2 = app.laserMove2
                app.laserRandomY2 = app.randomLaserPlacement2

                app.missileY = app.missileFired 
                app.coinDuplicate = True
            if time.time() - app.timeCoin > 27:
                app.characterPos = [app.width-900, app.topOfRectangle]
                app.obstaclePos = []
                if app.laserPlaced: 
                    app.obstaclePos += [[app.width - 30 - app.laserY, 
                    app.height - app.laserRandomY]]
                        
                if app.secondLaserPlaced:
                    app.obstaclePos += [[app.width - 30 - app.laserY2, 
                    app.height - app.laserRandomY2]]

                if app.missileLaunch:
                    app.obstaclePos += [[app.width - 30 - app.missileY, app.hardMissileY]]
                    
                app.coinPlaced = True
                app.timeCoin = time.time()
                app.coinY = gameScreen_pathFindingAlgorithm(app, app.characterPos, app.obstaclePos)
                print(app.characterPos)
                print(app.obstaclePos)
            if time.time() - app.timeCoin2 > 37:
                
                app.coinMove = 0
                app.coinPlaced = False
                app.timeCoin2 = time.time()

            if gameScreen_coinImpact(app):
                if app.coinDuplicate:
                    app.coinScore += 1
                    app.coinDuplicate = False
                    print(f"your coin score is {app.coinScore}")



#obstacle scrolling
    if app.gameStarted:
        if app.missileLaunch:
            app.missileFired += 15 * app.speedMultiplier #change according to side scrolling 
            
        if app.laserPlaced:
            app.laserMove += 15 * app.speedMultiplier #change this according to side scrolling
        if app.secondLaserPlaced:
            app.laserMove2 += 15 * app.speedMultiplier

        if app.coinPlaced:
            app.coinMove += 15 * app.speedMultiplier
    
def gameScreen_keyPressed(app, event):
    if event.key == "r":
        appStarted(app)
    
    if event.key == "q":
        app.mode = "endScreen"

    if event.key == "Space":
        app.topOfRectangle -= 20
        app.bottomOfRectangle -= 20 
    
        if app.topOfRectangle == 0:
            app.topOfRectangle += 20
            app.bottomOfRectangle += 20

    #practice coin placement
    if event.key == "c":
        app.coinPlaced = True

    if app.coinPlaced:
        if event.key == "x":
            app.coinMove += 10
    


def gameScreen_redrawAll(app,canvas):
    canvas.create_image(app.imageX, 
    app.rightSideOfImage,image =ImageTk.PhotoImage(app.backgroundStrip))


    #creating background side scroller   
    canvas.create_image(app.imageX, 
    app.rightSideOfImage,image =ImageTk.PhotoImage(app.backgroundStrip))

    canvas.create_image(app.imageX + app.width, 
    app.rightSideOfImage,image =ImageTk.PhotoImage(app.backgroundStrip))

    #barry running sprite image
    if app.topOfRectangle == app.height - 60:
        sprite = app.sprite[app.spriteCounter]
        canvas.create_image(app.width - 900, app.height - 70,
        image=ImageTk.PhotoImage(sprite))

    #barry flying image
    else:
        canvas.create_image(app.width - 900, app.topOfRectangle,
        image=ImageTk.PhotoImage(app.flyingImage))

    #drawing missiles
    if app.difficulty == "hard difficulty" and app.startingMissile:

        if app.missileLaunch:

            canvas.create_image(app.width - 30 - app.missileFired, 
            app.hardMissileY, image=ImageTk.PhotoImage(app.missileImage))
        else:
            canvas.create_rectangle(app.width - 20, app.topOfRectangle, 
            app.width - 10, app.topOfRectangle - 30, fill = "red")
            
            canvas.create_rectangle(app.width - 20, app.topOfRectangle + 5, 
            app.width - 10, app.topOfRectangle + 15, fill = "red")
        

    elif app.difficulty == "easy difficulty" and app.easyMissileLaunch == True:

            if app.missileLaunch:
              
                canvas.create_image(app.width - 30 - app.missileFired, 
                app.easyMissileY, image=ImageTk.PhotoImage(app.missileImage))

            if app.missileLaunch == False:
                canvas.create_rectangle(app.width - 20, 
                app.easyMissileY, 
                app.width - 10, app.easyMissileY -30, fill = "red")
            
                canvas.create_rectangle(app.width - 20, 
                app.easyMissileY + 5, 
                app.width - 10, app.easyMissileY +15, fill = "red")


    #drawing laser (first vertical, second horizontal) 
    if app.difficulty == "easy difficulty":
        if app.laserPlaced:
            if app.randomLaser == 1 or app.randomLaser == 2:
            
                canvas.create_image(app.width - 30 - app.laserMove, 
                app.height - app.randomLaserPlacement, image=ImageTk.PhotoImage(app.verticalLaserImage))
        
            if app.randomLaser  == 3:
                canvas.create_image(app.width - 30 - app.laserMove, 
                app.height - app.randomLaserPlacement, image=ImageTk.PhotoImage(app.horizontalLaserImage))

    if app.difficulty == "hard difficulty":
        if app.laserPlaced:
            if app.randomLaser == 1 or app.randomLaser == 2:

                canvas.create_image(app.width - 30 - app.laserMove, 
                app.height - app.randomLaserPlacement, image=ImageTk.PhotoImage(app.verticalLaserImage))

            if app.randomLaser  == 3:
                canvas.create_image(app.width - 30 - app.laserMove, 
                app.height - app.randomLaserPlacement, image=ImageTk.PhotoImage(app.horizontalLaserImage))

        if app.secondLaserPlaced:
            if app.randomLaser2 == 1 or app.randomLaser2 == 2:
            
                canvas.create_image(app.width - 30 - app.laserMove2, 
                app.height - app.randomLaserPlacement2, image=ImageTk.PhotoImage(app.verticalLaserImage))

            if app.randomLaser2  == 3:
                canvas.create_image(app.width - 30 - app.laserMove2, 
                app.height - app.randomLaserPlacement2, image=ImageTk.PhotoImage(app.horizontalLaserImage))

    #drawing coin
    if app.coinPlaced:
        canvas.create_oval(app.coinX - app.coinMove, 
        app.coinY, app.coinX + 40 - app.coinMove, 
        app.coinY + 40, fill = "gold")

        canvas.create_text(app.coinX + 20 - app.coinMove, app.coinY + 20, text = "$", fill = "black",
        font = "Times 17 italic bold")


    #creating score 
    canvas.create_text(70, 30, text = f"Score: {app.score}",
        font = "Times 17 italic bold", fill = "gold")

    #creating lives
    canvas.create_text(200, 30, text = "Lives:",
        font = "Times 17 italic bold", fill = "gold")

    #canvas.create_image(app.imageX, 
    #app.rightSideOfImage,image =ImageTk.PhotoImage(app.heartImage))
    if app.lives == 3:
        canvas.create_image(250, 
        30,image =ImageTk.PhotoImage(app.heartImage))
        canvas.create_image(280, 
        30,image =ImageTk.PhotoImage(app.heartImage))
        canvas.create_image(310, 
        30,image =ImageTk.PhotoImage(app.heartImage))
    if app.lives == 2:
        canvas.create_image(250, 
        30,image =ImageTk.PhotoImage(app.heartImage))
        canvas.create_image(280, 
        30,image =ImageTk.PhotoImage(app.heartImage))
    if app.lives == 1:
        canvas.create_image(250, 
        30,image =ImageTk.PhotoImage(app.heartImage))

#code for the startscreen

def startingScreen_mousePressed(app,event):
    #button for the game screen
    if 300 < event.x < 420 and 300 < event.y < 380: 
        #reset all timers when game starts3
        app.gameStarted = True
        app.time = time.time()
        app.time2 = time.time()
        app.timeLaser = time.time()
        app.timeCoin = time.time()
        app.timeCoin2 = time.time()

        app.mode = "gameScreen"

    #button for the difficulty changing screen
    if 150 < event.x < 270 and 300 < event.y < 380: 
        app.mode = "difficultyScreen"

def startingScreen_redrawAll(app,canvas):
    canvas.create_image(535, 240,
        image=ImageTk.PhotoImage(app.startingScreen))

    #this is to the difficuly screen
    canvas.create_rectangle(150,300, 270, 380, fill = 'lightGreen')
    canvas.create_text(210,335,font = "Times 17 italic bold",
    text = "Difficulty", fill = "Dark Blue")
    if app.will:
        canvas.create_rectangle(300,320, 420, 380, fill = 'magenta')

    #this is to the start of the game screen
    canvas.create_rectangle(300,300, 420, 380, fill = 'lightGreen')
    canvas.create_text(360,335,font = "Times 17 italic bold",
    text = "Start Game", fill = "Dark Blue")
    

#code for the difficulty screen

def difficultyScreen_redrawAll(app,canvas):
    canvas.create_rectangle(300,320, 420, 380, fill = 'magenta')

    #creating the split screen for the different difficulties

    #left side image(easy)
    if app.mouseLeftSide:   
        canvas.create_image(app.width/2 + 275, 220,
        image=ImageTk.PhotoImage(app.lighterEasyImage))
    else:
        canvas.create_image(app.width/2 + 275, 220,
        image=ImageTk.PhotoImage(app.easyImage))

    #right side of image(hard)
    if app.mouseRightSide:
        canvas.create_image(app.width/2 - 300, 240,
        image=ImageTk.PhotoImage(app.lighterHardImage))
    else:
        canvas.create_image(app.width/2 - 300, 240,
        image=ImageTk.PhotoImage(app.hardImage))

    #text 
    canvas.create_text(575,60,font = "Times 30 italic bold",
    text = "Choose your difficulty", fill = "Magenta")

    canvas.create_text(270,240,font = "Times 30 italic bold",
    text = "Hard Difficulty", fill = "Magenta")

    canvas.create_text(810,240,font = "Times 30 italic bold",
    text = "Easy Difficulty", fill = "Magenta")


def difficultyScreen_mousePressed(app,event):
    if 537.5 < event.x < app.width:
        app.mouseLeftSide = True
        app.mode = "startingScreen"
        app.difficulty = "easy difficulty"

    elif app.mouseLeftSide and not 0 < event.x < 537.5:
        app.mouseLeftSide = False

    if 0 < event.x < 537.5:
        app.mouseRightSide = True
        app.mode = "startingScreen"
        app.difficulty = "hard difficulty"

    elif app.mouseRightSide and not 0 < event.x < 537.5:
        app.mouseRightSide = False

#code for the leaderboard/end screen
def endScreen_mousePressed(app,event):
    if 150 < event.x < 270 and 300 < event.y < 380:
        appStarted(app)
        app.mode = "startingScreen"

    if 350 < event.x < 470 and 300 < event.y < 380:
        exit()

def endScreen_redrawAll(app, canvas):
    #background image
    canvas.create_image(app.width/2 , app.height/2,
        image=ImageTk.PhotoImage(app.endScreenImage))
    

    if app.winnerCheck:
        canvas.create_text(575,60,font = "Times 30 italic bold",
    text = app.winnerMessage, fill = "Magenta") 

    #play again
    canvas.create_rectangle(150,300, 270, 380, fill = 'lightGreen')
    canvas.create_text(210,335,font = "Times 14 italic bold",
    text = "Return Home", fill = "Dark Blue")

    #quit game
    canvas.create_rectangle(350,300, 470, 380, fill = 'pink')
    canvas.create_text(410,335,font = "Times 14 italic bold",
    text = "Quit", fill = "Dark Blue")

    canvas.create_text(app.width//2,50,font = "Times 30 italic bold",
    text = "GAME OVER!!!", fill = "Black")

    canvas.create_text(app.width - 250, app.height - 230,
    font = "Times 17 italic bold", text = f"Score: {app.score}")

    canvas.create_text(app.width - 250, app.height - 205,
    font = "Times 17 italic bold", text = f"Coins Collected: {app.coinScore}")

runApp(width = 1075, height = 480)
     
#citations
#heavily inspired by HalfBrick studios "jetpack joyride"
#https://www.shutterstock.com/search/heart+cartoon

#https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wired.com%2F2011%2F09%2F
# jetpack-joyride%2F&psig=AOvVaw0ppbowGA2Of7u2GfjUA0ee&ust=1638479852496000&sour
# ce=images&cd=vfe&ved=0CAsQjRxqFwoTCPC5l6DDw_QCFQAAAAAdAAAAABAD

#https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.writeups.org%2Fwp-conten
# t%2Fuploads%2FBarry-Steakfries-Jetpack-Joyride-a.jpg&imgrefurl=https%3A%2F%2Fw
# ww.writeups.org%2Fbarry-steakfries-jetpack-joyride%2F&tbnid=0Nkv2W_yrkU_tM&vet
# =12ahUKEwiTu4e3w8P0AhWRb80KHQzmAPoQMygHegQIARBc..i&docid=bEOX8MUb7XvS0M&w=500&
# h=719&q=barry%20steakfries%20sad&ved=2ahUKEwiTu4e3w8P0AhWRb80KHQzmAPoQMygHegQI
# ARBc

#https://www.google.com/url?sa=i&url=https%3A%2F%2Fjetpackjoyride.fandom.com%2Fw
# iki%2FBarry_Steakfries%2FGallery&psig=AOvVaw0yWsfulAk95Y3QqJhO_b3o&ust=1638479
# 944986000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCMDjtMvDw_QCFQAAAAAdAAAAABAD

#https://www.google.com/imgres?imgurl=https%3A%2F%2Fimgix.kotaku.com.au%2Fconten
# t%2Fuploads%2Fsites%2F3%2F2013%2F09%2F01%2Fnzpefrlwsd4w8ekix0px.jpg%3Far%3D16%
# 253A9%26auto%3Dformat%26fit%3Dcrop%26q%3D80%26w%3D1280%26nrs%3D30&imgrefurl=ht
# tps%3A%2F%2Fwww.kotaku.com.au%2F2013%2F09%2Fthe-unknown-curse-of-the-immortal-
# barry-steakfries%2F&tbnid=IM7Sv28xvB8gXM&vet=12ahUKEwjArfLew8P0AhXZXs0KHdJzBrE
# QMygBegUIARCdAQ..i&docid=vw3rMGiPEdssaM&w=1280&h=720&itg=1&q=barry%20steakfrie
# s%20sad%20image&ved=2ahUKEwjArfLew8P0AhXZXs0KHdJzBrEQMygBegUIARCdAQ

#https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.wikia.nocookie.net%2F
# jetpackjoyride%2Fimages%2F2%2F23%2FNewZapper.png%2Frevision%2Flatest%3Fcb%3D20
# 151016122706&imgrefurl=https%3A%2F%2Fjetpackjoyride.fandom.com%2Fwiki%2FLaser&
# tbnid=STFFpmCHV486nM&vet=12ahUKEwjA1dHtw8P0AhXULM0KHSewDpIQMygAegUIARCjAQ..i&d
# ocid=OZL_qmYzAQegDM&w=217&h=227&itg=1&q=jetpack%20joyride%20laser%20image&ved=
# 2ahUKEwjA1dHtw8P0AhXULM0KHSewDpIQMygAegUIARCjAQ