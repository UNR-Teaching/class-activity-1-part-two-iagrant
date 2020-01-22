#!/usr/bin/env python3

import car
import bike
import wheel

def main():
    carWheel = wheel.wheel("car wheel 1","car",27)
    bikeWheel = wheel.wheel("bike wheel 1","bike",27)
    notCar = car.car("Pinto","Red",carWheel)
    notBike = bike.bike("Pinto","Red",bikeWheel)
    print(notCar)
    print(notBike)

main()
