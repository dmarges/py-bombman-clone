#A Game written by Donnie Marges
import pygame
import settings as gs
from assets import Assets
from game import Game

class BomberMan:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((gs.SCREENWIDTH, gs.SCREENHEIGHT))
    pygame.display.set_caption("Bomber Man")

    self.ASSETS = Assets()
    self.FPS = pygame.time.Clock()
    self.GAME = Game(self, self.ASSETS)

    self.run = True

  def input(self):
     self.GAME.input()

  def update(self):
      self.FPS.tick(gs.FPS)
      self.GAME.update()
  
  def draw(self, window):
      window.fill(gs.BLACK)
      self.GAME.draw(window)
      pygame.display.update()

  def start(self):
      while self.run == True:
          self.input()
          self.update()
          self.draw(self.screen)

if __name__ == "__main__":
    game = BomberMan()
    game.start()
    pygame.quit()


