# Connor Stidham
# Slide and Catch 2
# 6-7
# Slide and Catch game showcasing simpleGE and pygame capabilities 


import pygame, simpleGE, random

class Apple(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("apple.png")
        self.position = (320, 400)
        self.setSize(35,35)
        self.minSpeed = 5
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
class Basket(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("basketR.png")
        self.moveSpeed = 10
        self.position = (320, 350)
        self.lBasket = "basketL.png"
        self.rBasket = "basketR.png"

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
            self.setImage(self.lBasket)
            currentPosition = self.position
            self.position = currentPosition
        if self.isKeyPressed(pygame.K_RIGHT):
            self.setImage(self.rBasket)
            self.x += self.moveSpeed
            currentPosition = self.position
            self.position = currentPosition

class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)

class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("orchard.png")
        
        self.sndApple = simpleGE.Sound("sound.mp3")
        self.numApples = 5
        self.score = 0
        self.lblScore = LblScore()
        self.lblScore.fgColor = ((0xFF,0x00,0x00))
        self.lblScore.bgColor = ((0x80,0xFF,0x80))
        
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.lblTime = LblTime()
        self.lblTime.fgColor = ((0xFF,0x00,0x00))
        self.lblTime.bgColor = ((0x80,0xFF,0x80))
        
        self.basket = Basket(self)
        
        self.apples = []
        for i in range(self.numApples):
            self.apples.append(Apple(self))
        
        self.sprites = [self.basket,
                        self.apples,
                        self.lblScore,
                        self.lblTime]
        
    def process(self):
        for apple in self.apples:
            if apple.collidesWith(self.basket):
                apple.reset()
                self.sndApple.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()
                
class Instructions(simpleGE.Scene):
    def __init__(self, prevScore):
        super().__init__()
        
        self.prevScore = prevScore
 
        self.setImage("orchard.png")
        self.response = "Quit"
        
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
        "It's harvest season!",
        "See how many apples you can collect",
        "in 10 seconds!"
            ]
        
        self.directions.center = (320, 150)
        self.directions.size = (450, 150)
        self.directions.fgColor = ((0xFF,0x00,0x00))
        self.directions.bgColor = ((0x80,0xFF,0x80))
        
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        self.btnPlay.fgColor = ((0xFF,0x00,0x00))
        self.btnPlay.bgColor = ((0x80,0xFF,0x80))
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 400)
        self.btnQuit.fgColor = ((0xFF,0x00,0x00))
        self.btnQuit.bgColor = ((0x80,0xFF,0x80))
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "HighScore: 0"
        self.lblScore.center = (320, 400)
        self.lblScore.fgColor = ((0xFF,0x00,0x00))
        self.lblScore.bgColor = ((0x80,0xFF,0x80))

        self.lblScore.text = f"Last Score: {self.prevScore}"
        
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
        
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
            
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        
def main():
    
    keepGoing = True
    lastScore = 0
    
    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            lastScore = game.score
        
        
        else:
            keepGoing = False
            
    
if __name__ == "__main__":
    main()