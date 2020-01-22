#!/usr/bin/env python3

from vehicle import vehicle
from abc import ABC,abstractmethod

class bike(vehicle):
    def __init__(self,name,color,wheel):
        super().__init__(name,color,wheel)
    def wheelie(length):
        for i in range(0,length):
            print("WEEE!")
    def makeSound():
        print("BRRRING BRRRING")
