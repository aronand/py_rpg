from attrs import define


@define
class Item:
    name: str
    description: str
