from VnaAutomation.Base.Named import Named

ABBREVIATION = "@abbreviation"


class Abbreviated(Named):
    """A named object that also has an associated abbreviation."""

    def __init__(self):
        super().__init__()
        self._abbreviation: str = ""

    def parseDict(self, values: dict) -> None:
        super().parseDict(values)

        if ABBREVIATION in values:
            self.setAbbreviation(values[ABBREVIATION])

    def abbreviation(self) -> str:
        return self._abbreviation

    def setAbbreviation(self, abbreviation: str) -> None:
        self._abbreviation = abbreviation
