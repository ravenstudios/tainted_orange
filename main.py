from constants import *
import pygame
import player
import enemy
import battle_system

pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

enemy = enemy.Enemy(700, 100)
player = player.Player(100, 600)
battle_system = battle_system.Battle_system(player, enemy)
all_group = pygame.sprite.Group()
all_group.add(player)
all_group.add(enemy)
all_group.add(battle_system)



def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                battle_system.check_keys(event.key)
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background

    all_group.draw(surface)
    pygame.display.flip()



def update():
    all_group.update()
    pass



if __name__ == "__main__":
    main()
