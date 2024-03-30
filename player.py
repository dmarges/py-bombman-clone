import pygame
import settings as gs

class Player(pygame.sprite.Sprite):
    def __init__(self, game, image_dict):
        super().__init__()
        self.GAME = game

        #character pos
        self.x = 0
        self.y = 0

        #attrs
        self.alive = True
        self.speed = 3

        #actions
        self.action = "walk_left"

        #display
        self.index = 0
        self.anim_time = 50
        self.anim_time_set = pygame.time.get_ticks()
        self.image_dict = image_dict
        self.image = self.image_dict[self.action][self.index]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.GAME.MAIN.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.GAME.MAIN.run = False

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.move("walk_right")
        elif keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.move("walk_left")
        elif keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            self.move("walk_up")
        elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            self.move("walk_down")


    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, self.rect)
        pygame.draw.rect(window, gs.RED, self.rect)

    def animate(self, action):
        if pygame.time.get_ticks() - self.anim_time_set >= self.anim_time:
            self.index += 1

            if self.index == len(self.image_dict[action]):
                self.index = 0

            self.image = self.image_dict[action][self.index]
            self.anim_time_set = pygame.time.get_ticks()

    def move(self, action):
        #Don't move if Player is dead
        if not self.alive:
            return

        if action != self.action:
            self.action = action
            self.index = 0

        direction = {"walk_left": -self.speed, "walk_right": self.speed, "walk_up": -self.speed, "walk_down": self.speed}

        #Change player coords
        if action == "walk_left" or action == "walk_right":
            self.x += direction[action]
        elif action == "walk_up" or action == "walk_down":
            self.y += direction[action]

        self.animate(action)

        #Update player rect
        self.rect.topleft = (self.x, self.y)