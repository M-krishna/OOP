"""
Observer pattern example
"""

import time
from abc import ABC, abstractmethod

# Create Interface(ABC) for Observer
class Observer(ABC):

    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        pass


# Create Interface(ABC) for Subject
class Subject(ABC):

    @abstractmethod
    def registerObserver(self, observer: Observer):
        pass

    @abstractmethod
    def removeObserver(self, observer: Observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

# Create Interface(ABC) for Display
class DisplayElement(ABC):

    @abstractmethod
    def display(self):
        pass



# Create concrete implementation for the Subject
class WeatherData(Subject):

    _temp: float
    _humidity: float
    _pressure: float

    def __init__(self):
        self.observers = []


    def registerObserver(self, observer: Observer):
        self.observers.append(observer)

    def removeObserver(self, observer: Observer):
        self.observers.remove(ob)

    def notifyObservers(self):
        for ob in self.observers:
            ob.update(self._temp, self._humidity, self._pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temp: float, humidity: float, pressure: float):
        print("Setting new measurements...")
        self._temp = temp
        self._humidity = humidity
        self._pressure = pressure

        self.measurementsChanged()

# Create concrete implementation for the Observers and DisplayElement
class CurrentConditionsDisplay(Observer, DisplayElement):

    _temp: float
    _humidity: float
    _weatherData: WeatherData

    def __init__(self, weatherData: WeatherData):
       self._weatherData = weatherData
       weatherData.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self._temp = temp
        self._humidity = humidity
        self._pressure = pressure
        self.display()


    def display(self):
        print("Current conditions: ", self._temp, self._humidity)


class StatisticsDisplay(Observer, DisplayElement):

    _temp: float
    _humidity: float
    _weatherData: WeatherData

    def __init__(self, weatherData: WeatherData):
        self._weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self._temp = temp
        self._humidity = humidity
        self._pressure = pressure
        self.display()

    def display(self):
        print("Statistics display: ", self._temp, self._humidity, self._pressure)



weatherData = WeatherData()
current_conditions_display = CurrentConditionsDisplay(weatherData)
print("Setting new measurements in 3 seconds")
time.sleep(3)
weatherData.setMeasurements(1.1, 2.2, 3.3)

print()
print("Setting new measurements in 3 seconds")
time.sleep(3)
statistics_display = StatisticsDisplay(weatherData)
weatherData.setMeasurements(2.134, 3.123, 7.65)
