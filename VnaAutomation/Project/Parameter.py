from VnaAutomation.Base.Abbreviated import Abbreviated
from VnaAutomation.Project.Option import Option

OPTION = "option"


class Parameter(Abbreviated):
    """
    Project parameter. Contains option values.
    """

    def __init__(self):
        super().__init__()
        self._options: list[Option] = []

    def parseDict(self, values: dict) -> None:
        super().parseDict(values)

        #TODO: Add "option" to force_list setting
        if OPTION in values:
            options = values[OPTION]
            for value in options:
                option = Option()
                option.parseDict(value)
                self.appendOption(option)

    def options(self) -> list[Option]:
        return self._options

    def appendOption(self, option: Option) -> None:
        self._options.append(option)

