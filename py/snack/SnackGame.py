import pygame,sys,random
from snack.Snack import Snack
class snackGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600),0,0)
        self.snack = Snack()
        self.eatX = random.randint(0,780)
        self.eatY = random.randint(0,580)
    def main(self):
        while True:
            self.screen.fill((255, 255, 255))
            self.action()
            self.paint()
            pygame.time.delay(10)
            pygame.display.update()
    def action(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.snack.dct = 1
                elif event.key == pygame.K_a:
                    self.snack.dct = 2
                elif event.key == pygame.K_w:
                    self.snack.dct = 3
                elif event.key == pygame.K_d:
                    self.snack.dct = 0
        self.stepAction()
        self.eatAction()
        self.outOfBounds()
    def outOfBounds(self):
        pass
    def eatAction(self):
        pass
    def stepAction(self):
        self.snack.step()
    def paint(self):
        self.painteat()
        pygame.draw.rect(self.screen,(0,255,0),(self.snack.x,self.snack.y,20,20),0)
    def painteat(self):
        pygame.draw.rect(self.screen,(255,0,0),(self.eatX,self.eatY,20,20), 0)




if __name__ == '__main__':
    game = snackGame()
    game.main()