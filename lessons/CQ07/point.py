"""Challenge Question 07: Point Class!"""

from __future__ import annotations

__author__ = "730578454"


class Point:
    """Defines the Point class."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Points x and y."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates the point by a scale factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Making a new and mutated point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
