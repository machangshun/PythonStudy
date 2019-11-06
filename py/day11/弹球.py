import pygame,sys
class Ball(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600),0,0)
        self.x = 25
        self.y = 25
        self.xStep = 1
        self.yStep = 1
    def main(self):
        pygame.display.set_caption("弹球")
        while True:
            self.screen.fill((255,255,255))
            self.action()
            self.paint()
            pygame.display.update()

    def action(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.x += self.xStep
        self.y += self.yStep
    def paint(self):
        pygame.draw.circle(self.screen,(0,0,0),(self.x,self.y),25,0)

if __name__ == '__main__':
    ball = Ball()
    ball.main()