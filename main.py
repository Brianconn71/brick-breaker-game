import pygame

width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaker Game")

frames = 60

def draw(win):
    win.fill("white")
    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(frames)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                Break
        draw(win)
    
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()