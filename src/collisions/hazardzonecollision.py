'''
Created on June 29, 2009

@author: William Madison
'''

from src.collisions.basecollision import BaseCollision

class HazardZoneCollision(BaseCollision):

  def __init__(self, entFrog):
    self.frogCollidedWith = entFrog

  def handleCollision(self):
    '''
      This is the function responsible for providing the 
      means of handling a collision of between a Car and a Frog.
    '''
    #self.FrogCollidedWith.resetToStartingPosition()
    print "I'm melting...melting..."

  @property
  def FrogCollidedWith(self):
    return self.frogCollidedWith
