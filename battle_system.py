from constants import *
import pygame


class Battle_system(pygame.sprite.Sprite):

    def __init__(self, player, enemy):
        super().__init__()
        self.player = player
        self.enemy = enemy
        self.x, self.y = GAME_WIDTH // 2, GAME_HEIGHT // 2
        self.width, self.height = GAME_WIDTH // 4, GAME_HEIGHT // 3
        self.image = pygame.Surface((self.width, self.height))
        # self.image = self.get_image_from_sprite_sheet(0, self.y_sprite_sheet_index)
        self.color = (255, 255, 255)
        self.image.fill(self.color)
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)

        self.margin = 10
        self.menu_item_size = (self.width - self.margin * 2, BLOCK_SIZE)


        self.font = pygame.font.SysFont("Arial", 40)





        self.menu = [
            {
                "name": "Attack!",
                "action": self.attack(),
                "pos": (self.margin, 64 + self.margin * 1)
            },

            {
                "name": "Magic",
                "action": self.magic(),
                "pos": (self.margin, 128 + self.margin * 2)
            },

            {
                "name": "Item",
                "action": self.item(),
                "pos": (self.margin, 192 + self.margin * 3)
            },
        ]

        self.menu_index = 0
        self.draw_menu()



    def update(self):
        pass




    def attack(self):
        pass
    def magic(self):
        pass
    def item(self):
        pass

    # def update(self):
    #     pass

    def draw_menu(self):
        # self.textSurf = self.font.render("Hello World", True, (0, 0, 255))
        # self.image.blit(self.textSurf, (0, 0))
        for index, item in enumerate(self.menu):
            print(self.menu_index)

            button_image = pygame.Surface(self.menu_item_size)

            if self.menu_index % len(self.menu) == index:
                color = (150, 0, 150)
                text_color = (250, 250, 250)
            else:
                color = (100, 0, 100)
                text_color = (200, 200, 200)
            rect = pygame.Rect(button_image.get_rect())
            # image = get_image_from_sprite_sheet(0, y_sprite_sheet_index)

            button_image.fill(color)

            rect.topleft = item["pos"]
            ts = self.font.render(item["name"], True, text_color)
            pygame.draw.rect(button_image, BLACK, rect, 5)
            button_image.blit(ts, ((rect.width // 2) - (len(item["name"] * 40) // 2), 0))
            self.image.blit(button_image, item["pos"])


    def check_keys(self, key):


        if key == pygame.K_UP:
            print("up")
            self.menu_index -= 1
            self.draw_menu()

        if key == pygame.K_DOWN:
            print("down")
            self.menu_index += 1
            self.draw_menu()

        if key == pygame.K_RIGHT:
            print("right")

        if key == pygame.K_LEFT:
            print("left")
