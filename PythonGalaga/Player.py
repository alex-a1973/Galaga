from graphics import *

class Player():
    def __init__(self, gameWindow):
        self.ship = Image(Point(400, 550), "Images/Galagaship.png")
        self.ship.draw(gameWindow)
        self.speed = 5
        self.lives = 3

#controls for the 'ship', 'playerInput' = window.checkKey from 'main' function being sent to this method. Works if the 'ship' stays within the x-coords 200-600
    def playerControls(self, playerInput):
        shipPosition = self.ship.getAnchor()

        if playerInput == "d":
            if shipPosition.getX() < 600:
                self.ship.move(self.speed, 0)
        if playerInput == "a":
            if shipPosition.getX() > 200:
                self.ship.move(-self.speed, 0)

#gets x-coord of 'ship'
    def getShipPositionX(self):
        return self.ship.getAnchor().getX()

#gets y-coord of 'ship'
    def getShipPositionY(self):
        return self.ship.getAnchor().getY()

    def getLives(self):
        return self.lives

#'self.lives - 1' = self.lives
    def ShipRemove(self, gameWindow):
        self.lives -= 1
