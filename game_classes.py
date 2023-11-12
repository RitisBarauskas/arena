from dataclasses import dataclass


@dataclass
class Thing:
    """Создает объект инвентаря."""
    title: str
    defense_percentage: int
    attack: int
    health_point: int


@dataclass
class Person:
    """
    Создает персонажа.

    """
    health: int


@dataclass
class Paladin(Person):
    """Создает персонажа типа: Plaldin"""
    ...

@dataclass
class Warrior(Person):
    """Создает персонажа типа: Warrior"""
    ...

