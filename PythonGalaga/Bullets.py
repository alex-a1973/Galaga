from graphics import *

class Bullets():
    def __init__(self, gameWindow):
        self.gameWindow = gameWindow
        self.bullet = Image(Point(-10, 555), "Images/missile.png")

#'bullet' is offscreen at x = -10, so plus 10 and the 'playerX' has the information 'thePlayer.getShipPositionX()'. Ultimately it just draws the 'bullet'
    def showBullet(self, playerX):
        self.bullet.move(playerX + 10, 0)
        self.bullet.draw(self.gameWindow)        
        
    def bulletMovement(self, bulletspeed):
        self.bullet.move(0, bulletspeed)

#gets y-coord of 'bullet'
    def getBulletPosY(self):
        return self.bullet.getAnchor().getY()

#gets x-coord of 'bullet'
    def getBulletPosX(self):
        return self.bullet.getAnchor().getX()

    def resetBullet(self):
        self.bullet.move(-self.getBulletPosX() - 10, 555 - self.getBulletPosY())
        self.bullet.undraw()