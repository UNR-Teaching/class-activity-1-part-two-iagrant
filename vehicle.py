#!/usr/bin/env python3

from abc import ABC,abstractmethod

class vehicle(ABC):
    def __init__(self,name,color,wheel):
        self.name = name
        self.color = color
        self.wheel = wheel
    def makeSound():
        pass
