from core import Node
from core import KinematicBody

import pyray


class Character(KinematicBody):
    __slots__ = "__character_name", "__level", "__max_stamina", "__cur_stamina"

    def __init__(self, node_name: str = "Character",
                 parent: Node | None = None,
                 character_name: str = "",
                 position: pyray.Vector2 = pyray.Vector2(0, 0)) -> None:
        super().__init__(node_name=node_name, parent=parent, position=position)
        self.__character_name = character_name
        self.__level: int = 1
        self.__max_stamina: int = 100
        self.__cur_stamina: int = self.__max_stamina

    @property
    def character_name(self) -> str:  # can't use name, as this clashes with Node.name
        return self.__character_name

    @property
    def level(self) -> int:
        return self.__level

    @property
    def max_stamina(self) -> int:
        return self.__max_stamina

    @property
    def cur_stamina(self) -> int:
        return self.__cur_stamina

    @cur_stamina.setter
    def cur_stamina(self, value: int) -> None:
        if value > self.__max_stamina:
            # TODO: Possibly raise an exception?
            return
        if type(value) is not int:
            # TODO: Possibly raise an exception?
            return
        if value < 0:
            value = 0
        self.__cur_stamina = value

    @property
    def is_dead(self) -> bool:
        return self.__cur_stamina <= 0

    def level_up(self) -> None:
        self.__level += 1
        self.__max_stamina = int(1.1 * self.__max_stamina)

    def update(self) -> None:
        # We need to call the KinematicBody's update as we are inheriting it
        # TODO: Maybe split the actual movement logic and move it here?
        super().update()
