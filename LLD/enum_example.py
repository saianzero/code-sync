# https://algomaster.io/practice/low-level-design/design-traffic-light

# Implement Color as an Enum above TrafficLight.
# Required members: RED, GREEN, YELLOW.
# Each member must expose:
# - duration (an int property)
# - next() -> Color
# TrafficLight is complete; do not modify it.

"""
As a general rule, you should always read a member's value using the public property .value. 
However, _value_ becomes critical when you want to override a member's value dynamically during enum creation.

If you try to assign a value to self.value inside an enum's __init__ or __new__ method, Python will raise an AttributeError because .value is protected against modification. To bypass this and manually bind custom or transformed values, you must modify self._value_ instead.

Color.RED
# Color.RED

Color.RED.name
# "RED"

Color.RED.value
# "red"

Color.RED.duration
# 30

"""
from enum import Enum

class Color(Enum): # name = value
    RED = ("red", 30)
    GREEN = ("green", 25)
    YELLOW = ("yellow", 5)

    def __init__(self, value: str, duration: int):
        self._value_ = value 
        self.duration = duration
    
    def next(self):
        if self == Color.RED:
            return Color.GREEN
        elif self == Color.GREEN:
            return Color.YELLOW
        else:
            return Color.RED

class TrafficLight:

    def __init__(self, startColor: str):
        self._current = Color.RED
        for color in Color:
            if color.name.lower() == startColor.lower():
                self._current = color
                break

    def getColor(self) -> str:
        return self._current.name

    def getDuration(self) -> int:
        return self._current.duration

    def next(self) -> str:
        self._current = self._current.next()
        return self._current.name

    def describe(self) -> str:
        return "%s (%ds)" % (self._current.name, self._current.duration)