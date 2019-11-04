import pygame,sys
class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600),0,0)
    def main(self):
        pygame.display.set_caption("game")
        while True:
            self.screen.fill((255,255,255))
            self.action()
            self.paint()
            pygame.display.update()
    def action(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def paint(self):
        pass



if __name__ == '__main__':
    game = Game()
    game.main()
