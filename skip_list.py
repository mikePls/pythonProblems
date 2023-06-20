import random
import math

class Node:
    def __init__(self, data, level=0):
        self.data = data
        self.next = [None] * level

    def __str__(self):
        return 'Node(%s%s)' %(self.data, len(self.next))

class SkipList(object):
    def __init__(self, max_level=8):
        self.max_level=max_level
