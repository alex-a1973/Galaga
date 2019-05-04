from graphics import *

class Enemy():
    def __init__(self, gameWindow, x, y, color):
        self.enemyship = Image(Point(x, y), color)
        self.enemyship.draw(gameWindow)

    def enemyShipMove(self, directionX, directionY):
        self.enemyship.move(directionX, directionY)
        if self.enemyship.getAnchor().getY() > 610:
            self.enemyship.move(0, -620)
        
    def getenemyShipPosX(self):
        return self.enemyship.getAnchor().getX()

    def getenemyShipPosY(self):
        return self.enemyship.getAnchor().getY()

    def enemyShipRemove(self, gameWindow):
        self.enemyship.undraw()
        self.enemyship.move(-self.getenemyShipPosX(), -self.getenemyShipPosY())
