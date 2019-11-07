import abc
class Enemy(object):
    @abc.abstractmethod
    def getScore(self):
        pass