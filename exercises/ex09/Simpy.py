"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730466997"


class Simpy:
    """List of values stored in a class."""
    values: list[float]

    def __init__(self, values: list[float] = []):
        """Initiates Simpy."""
        self.values = values

    def __str__(self):
        """Represents class object as a string."""
        return f"Simpy({self.values})"

    def fill(self, value: float, amount: int) -> None:
        """Fills values in Simpy with amount and value provided."""
        replacement: list[float] = []
        i: int = 0
        while i < amount:
            replacement.append(value)
            i += 1
        self.values = replacement

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills values with a range of values."""
        assert step != 0.0
        replacement: list[float] = []
        i: float = start
        while i != stop:
            replacement.append(i)
            i += step
        self.values = replacement

    def sum(self) -> float:
        """Returns sum of values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds two Simpys or two floats."""
        new: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                new.values.append(self.values[i] + rhs.values[i])
        else:
            for i in range(0, len(self.values)):
                new.values.append(self.values[i] + rhs)
        return new

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Puts a Simpy to the power of another or a float."""
        new: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                new.values.append(self.values[i] ** rhs.values[i])
        else:
            for i in range(0, len(self.values)):
                new.values.append(self.values[i] ** rhs)
        return new

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns bools of if values in a Simpy equal values in another or a float."""
        bools: list[bool] = []
        if isinstance(rhs, Simpy):
            for i in range(0, len(self.values)):
                if self.values[i] == rhs.values[i]:
                    bools.append(True)
                else:
                    bools.append(False)
        else:
            for i in range(0, len(self.values)):
                if self.values[i] == rhs:
                    bools.append(True)
                else:
                    bools.append(False)
        return bools

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns bools of if values in a Simpy equal values in another or a float."""
        bools: list[bool] = []
        if isinstance(rhs, Simpy):
            for i in range(0, len(self.values)):
                if self.values[i] > rhs.values[i]:
                    bools.append(True)
                else:
                    bools.append(False)
        else:
            for i in range(0, len(self.values)):
                if self.values[i] > rhs:
                    bools.append(True)
                else:
                    bools.append(False)
        return bools

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adds the ability to use subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            new: Simpy = Simpy([])
            for i in range(0, len(rhs)):
                if rhs[i]:
                    new.values.append(self.values[i])
            return new