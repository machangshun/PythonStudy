import abc
class Enemy(object):
    @abc.abstractclassmethod
    def getScore(self):
        pass