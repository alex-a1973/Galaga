from graphics import *
from Player import *
from Bullets import *
from Enemy import *

def main():
    #"win" is the variable that creates the game window.
    win = GraphWin("Galaga", 800, 600)
    win.setBackground("black")

    #"thePlayer" is an object that calls all the info within the "Player" class, the "Player" class creates the ship with the "win" variable being sent into the parameter within the "Player" class called "gameWindow"
    thePlayer = Player(win)

    #"blueEnemy", "redEnemy", "greenEnemy" are variables that are being put into the "EnemyList" list, and within the list are objects that call the "Enemy" class with the parameters "gameWindow", "x", "y", "color"
    blueEnemy = "Images/blueGalagaenemy.png"
    redEnemy = "Images/redGalagaenemy.png"
    greenEnemy = "Images/greenGalagaenemy.png"

    #the numbers are the "x" and "y" coordinates for each of the enemies, and the "color" of enemies referenced back the the variables before
    EnemyList = [ Enemy(win, 400, 300, blueEnemy), Enemy(win, 430, 300, blueEnemy), Enemy(win, 460, 300, blueEnemy), Enemy(win, 490, 300, blueEnemy), Enemy(win, 370, 300, blueEnemy), Enemy(win, 340, 300, blueEnemy), Enemy(win, 310, 300, blueEnemy), Enemy(win, 400, 270, blueEnemy), Enemy(win, 430, 270, blueEnemy), Enemy(win, 460, 270, blueEnemy), Enemy(win, 490, 270, blueEnemy), Enemy(win, 370, 270, blueEnemy), Enemy(win, 340, 270, blueEnemy), Enemy(win, 310, 270, blueEnemy), Enemy(win, 400, 240, redEnemy), Enemy(win, 430, 240, redEnemy), Enemy(win, 460, 240, redEnemy), Enemy(win, 490, 240, redEnemy), Enemy(win, 370, 240, redEnemy), Enemy(win, 340, 240, redEnemy), Enemy(win, 310, 240, redEnemy), Enemy(win, 400, 210, greenEnemy), Enemy(win, 440, 210, greenEnemy), Enemy(win, 360, 210, greenEnemy) ]
    enemyDirectionX = 2
    enemyDirectionY = 2
    enemyDistanceX = 300
    
    bulletList = [Bullets(win), Bullets(win)]
    bulletListSpeed = [0, 0]

    livesText = Text(Point(700, 50), "Lives: ")
    livesText.setTextColor("white")
    livesText.draw(win)
    numberofLives = Text(Point(750, 50), "3")
    numberofLives.setTextColor("white")
    numberofLives.draw(win)

    win.getMouse()
    while thePlayer.getLives() > 0:
        playerInput = win.checkKey()
        thePlayer.playerControls(playerInput)

#'playerInput' checks if the user presses 'w' and if the user does the bullet shows at the x-coord of the ship
        if (playerInput == "w" and bulletList[0].getBulletPosX() == -10):
            bulletList[0].showBullet(thePlayer.getShipPositionX())
            bulletListSpeed[0] = -4.0
        elif (playerInput == "w" and bulletList[1].getBulletPosX() == -10):
            bulletList[1].showBullet(thePlayer.getShipPositionX())
            bulletListSpeed[1] = -4.0

#'for i in range(2):' counts to 0, 1 and is used as a variable to group both objects within 'bulletList' to move the bullet if the y-coord of the bullet is greater than 0 and if its less than 0 it resets its position
        for i in range(2):
            if (bulletList[i].getBulletPosY() > 0):
                bulletList[i].bulletMovement(bulletListSpeed[i])
            else:
                bulletList[i].resetBullet()
                bulletListSpeed[i] = 0

#this creates boundaries that count by adding 'enemyDistanceX' and 'enemyDirectionX' until 'enemyDistanceX' greater than 500 then moves in the opposite direction in X direction
        if enemyDistanceX > 500:
            enemyDirectionX = -1
        if enemyDistanceX < 100:
            enemyDirectionX = 1
        enemyDistanceX += enemyDirectionX

#sentry variable 'x' for all the items in 'EnemyList' moves all the enemies
        for x in EnemyList:
            x.enemyShipMove(enemyDirectionX, enemyDirectionY)

#sentry variables 'y' and 'x' for 'bulletList' and 'EnemyList', creating hit boxes for all the items within the lists and if hitboxes collide 'enemyShipRemove' undraws and moves the hit enemy as well as the bullet
        for y in bulletList:
            for x in EnemyList:
                if (y.getBulletPosX() > x.getenemyShipPosX() - 5) and (y.getBulletPosX() < x.getenemyShipPosX() + 5):
                    if (y.getBulletPosY() > x.getenemyShipPosY() - 5) and (y.getBulletPosY() < x.getenemyShipPosY() + 5):
                        x.enemyShipRemove(win)
                        y.resetBullet()

#creates 'enemyship' hitbox and 'ship' hitbox and if 'enemyship' hitbox lands within 'ship' hitbox, the 'ship' lives will be lowered by one and moved. 'numberofLives' text changes due to the 'lives' method
                if (x.getenemyShipPosX() - 5 > thePlayer.getShipPositionX() - 10) and (x.getenemyShipPosX() + 5 < thePlayer.getShipPositionX() + 10):
                    if (x.getenemyShipPosY() - 5 > thePlayer.getShipPositionY() - 10) and (x.getenemyShipPosY() + 5 < thePlayer.getShipPositionY() + 10):
                        thePlayer.ShipRemove(win)
                        thePlayer.ship.move(-thePlayer.getShipPositionX() + 200, 0)

                        numberofLives.setText(thePlayer.lives)

        if (thePlayer.getLives() == 0):
            gameOver = Text(Point(400, 300), "GAME OVER")
            gameOver.setTextColor("white")
            gameOver.draw(win)
           
main()