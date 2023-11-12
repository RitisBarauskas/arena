from dataclasses import dataclass


@dataclass
class Person:
    """
    Создает персонажа.

    """

    name: str
    health: int
    default_attack: int
    default_deffent: int
