import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_position = (0, 0)
        mouse_position = (0, 0)
        mole_positionx= 0
        mole_positiony = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = tuple(ti // 32 for ti in event.pos)
                    mole_position = tuple(ti // 32 for ti in mole_position)
                    if mouse_position == mole_position:
                        mole_position = (random.randrange(0, 640, 32), random.randrange(0, 512, 32))

            screen.fill("light green")
            for i in range(0, 641, 32):
                pygame.draw.line(screen, 'dark blue', (i, 0), (i, 512) )
            for j in range(0, 513, 32):
                pygame.draw.line(screen, 'dark blue', (0, j), (640, j))
            screen.blit(mole_image, mole_image.get_rect(topleft= mole_position))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
