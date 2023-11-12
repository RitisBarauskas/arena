from dataclasses import asdict, dataclass


@dataclass
class Person:
    """
    Создает персонажа.

    """

    name: str
    health: int
    default_attack: int
    default_deffent: int

    def set_things(self, things):
        """Принимает список вещей."""
        for thing in things:
            self._count_buff(**asdict(thing))

    def _count_buff(self):
        """Обновление свойств персонажа"""
        


    def attack_damage(self):
        """Вычитает жизни на основе атаки."""
        pass
