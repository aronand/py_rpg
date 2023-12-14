from functools import singledispatchmethod
from typing import Iterator

from item import Item


class ItemRepository:
    __slots__ = ["__items"]

    class ItemNotFoundException(Exception):
        pass

    def __init__(self) -> None:
        self.__items: list[Item] = []

    def __getitem__(self, idx: int) -> Item:
        return self.__items[idx]

    def __iter__(self) -> Iterator[Item]:
        return iter(self.__items)

    def __len__(self) -> int:
        return len(self.__items)

    def add_item(self, item: Item) -> None:
        """
        Adds an Item object into the ItemRepository.
        """
        self.__items.append(item)

    def create_item(self, *args) -> None:
        """
        Creates an Item object in the repository with the given args.
        
        See Item for more information on the args.
        """
        self.__items.append(Item(*args))

    @singledispatchmethod
    def remove_item(self, arg) -> Item:
        """
        Remove an item from the ItemRepository based on the type of arg.
        """
        raise NotImplementedError

    @remove_item.register
    def _(self, arg: int) -> Item:
        """
        Removes the item at the given index from the ItemRepository.

        :returns: Item object at given index
        :raises IndexError: If index is out of range
        """
        return self.__items.pop(arg)

    @remove_item.register
    def _(self, arg: str) -> Item:
        """
        Removes the item with the given name from the ItemRepository.

        Note that only the first item with a matching name will be removed.
        Name is case-sensitive.

        :returns: Item object with the given name
        :raises ItemRepository.ItemNotFoundException: If an Item with a
        matching name is not found.
        """
        for idx, item in enumerate(self.__items):
            if item.name != arg:
                continue
            return self.remove_item(idx)

        raise ItemRepository.ItemNotFoundException()
