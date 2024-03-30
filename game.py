import pygame
from player import Player
import settings as gs

class Game:
    def __init__(self, main, assets):
        self.MAIN = main
        self.ASSETS = assets
        self.player = Player(self)

    def input(self):
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         self.MAIN.run = False
        #     elif event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_ESCAPE:
        #             self.MAIN.run = False

        self.player.input()

    def update(self):
        self.player.update()

    def draw(self, window):
        self.player.draw(window)
