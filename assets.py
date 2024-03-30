import pygame
import settings as gs

class Assets:
    def __init__(self):
        self.spritesheet = self.load_spritesheet("images", "spritesheet.png", 192 * 4, 272 * 4)
        self.player_char = self.load_sprite_range(gs.PLAYER, self.spritesheet)


    def load_spritesheet(self, path, filename, width, height):
        image = pygame.image.load(f"{path}/{filename}").convert_alpha()
        image = pygame.transform.scale(image, (width, height))
        return image

    def load_sprites(self, spritesheet, x_pos, y_pos, width, height):
        #Create empty surface
        image = pygame.Surface((width, height))

        #Fill with black
        image.fill((0, 0, 1))

        #Blit sprite on to surface
        image.blit(spritesheet, (0, 0), (x_pos, y_pos, width, height))

        #Convert black to transparent
        image.set_colorkey(gs.BLACK)

        return image

    def load_sprite_range(self, image_dict, spritesheet, row=gs.SIZE, col=gs.SIZE, width=gs.SIZE, height=gs.SIZE, resize=False):
        animation_images = {}

        for animation in image_dict.keys():
            animation_images[animation] = []

            for coord in image_dict[animation]:
                image = self.load_sprites(spritesheet, coord[1] * col, coord[0] * row, width, height)

                if resize:
                    image = pygame.transform.scale(image, (32, 32))

                animation_images[animation].append(image)

        return animation_images