'''
Created on Nov 26, 2016

@author: Thomas Lisankie
'''

class RVIndexPair(object):

    def __init__(self, index, RVBetweenPhonemes):
        self.indexes = []
        self.indexes.append(index)
        self.rhymeValueForSet = 0.0
        self.rhymeValueForSet = self.rhymeValueForSet + RVBetweenPhonemes
        self.childNode = None
        
    def addIndexes(self, indexesToAdd, RVBetweenPhonemes):
        for index in indexesToAdd:
            self.indexes.append(index)
            '''Indexes that are being compared for rhyme value
            differ between Java and Python versions for some
            reason.'''
        self.rhymeValueForSet = self.rhymeValueForSet + RVBetweenPhonemes
        
    def attachChildNode(self, childNode):
        self.childNode = childNode
        self.childNode.parentIndex = self
        