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

    def set_things(things):
        """Принимает список вещей."""

    def attack_damage():
        """Вычитает жизни на основе атаки."""
        pass
