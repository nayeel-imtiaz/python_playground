"""
Nayeel Imtiaz
10-12-26

Parking Lot coding implementation from UML diagram
- Given a UML diagram with more substantial abstractions
and separation of responsibilities, code up a working
implementation and test it (30 minutes).

Timeline:

Reflection:

"""

from typing import Protocol
from abc import abstractmethod
from enum import Enum
from time import time


class VehicleSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Vehicle(Protocol):
    @abstractmethod
    def getLicensePlate(self) -> str:
        ...

    @abstractmethod
    def getSize(self) -> VehicleSize:
        ...


class ParkingSpot(Protocol):
    @abstractmethod
    def isAvailable(self) -> bool:
        ...

    @abstractmethod
    def occupy(self, vehicle: Vehicle) -> None:
        ...

    @abstractmethod
    def vacate(self) -> None:
        ...

    @abstractmethod
    def getSpotNumber(self) -> int:
        ...

    @abstractmethod
    def getSize(self) -> VehicleSize:
        ...


class Car(Vehicle):
    def __init__(self, licensePlate: str):
        self._licensePlate = licensePlate
        self._size = VehicleSize.MEDIUM

    def getLicensePlate(self) -> str:
        return self._licensePlate

    def getSize(self) -> VehicleSize:
        return self._size


class Motorcycle(Vehicle):
    def __init__(self, licensePlate: str):
        self._licensePlate = licensePlate
        self._size = VehicleSize.SMALL

    def getLicensePlate(self) -> str:
        return self._licensePlate

    def getSize(self) -> VehicleSize:
        return self._size


class Truck(Vehicle):
    def __init__(self, licensePlate: str):
        self._licensePlate = licensePlate
        self._size = VehicleSize.LARGE

    def getLicensePlate(self) -> str:
        return self._licensePlate

    def getSize(self) -> VehicleSize:
        return self._size


class Ticket:
    ticketCounter = 1

    def __init__(self, vehicle: Vehicle, parkingSpot: ParkingSpot):
        self._ticketId = Ticket.ticketCounter
        self._vehicle = vehicle
        self._parkingSpot = parkingSpot
        self._entryTime = time()
        self._exitTime = None
        Ticket.ticketCounter += 1

    def calculateParkingDuration(self) -> int:
        # return answer in seconds
        self._exitTime = time()
        return int(self._exitTime - self._entryTime)


class ParkingManager:
    pass


class FareCalculator:
    pass


class FareStrategy(Protocol):
    @abstractmethod
    def calculateFare(ticket: Ticket) -> int:
        ...


class BaseFareStrategy(FareStrategy):
    pass


class PeakHoursFareStrategy(FareStrategy):
    pass


class CompactSpot(ParkingSpot):
    pass


class OversizedSpot(ParkingSpot):
    pass


class RegularSpot(ParkingSpot):
    pass


class ParkingLot:
    def __init__(self, parkingManager: ParkingManager, fareCalculator: FareCalculator):
        self._parkingManager = parkingManager
        self._fareCalculator = fareCalculator

    def enterVehichle(self, vehicle: Vehicle) -> Vehicle:
        pass

    def leaveVehicle(self, Ticket) -> None:
        pass


def main():
    pass


if __name__ == '__main__':
    main()