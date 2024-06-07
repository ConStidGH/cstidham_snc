# Connor Stidham
# Slide and Catch 1
# 6-7
# Slide and Catch game showcasing simpleGE and pygame capabilities 


import pygame, simpleGE

class Basket(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("basketR.png")
        self.setSize(175,150)
        self.position = (320, 350)
        self.moveSpeed = 10
        
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
            
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("orchard.png")
        self.basket = Basket(self)
        
        self.sprites = [self.basket]

def main():
        game = Game()
        game.start()

if __name__ == "__main__":
    main()