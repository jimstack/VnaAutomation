NAME = "@name"


class Named:
    """An object that has an associated name."""

    def __init__(self):
        self._name: str = ""

    def parseDict(self, values: dict) -> None:
        if NAME in values:
            self.setName(values[NAME])

    def name(self) -> str:
        return self._name

    def setName(self, name: str) -> None:
        self._name = name
