from collections import OrderedDict
from VnaAutomation.Project.Option import Option
from VnaAutomation.Project.Parameter import Parameter


class TestConfiguration:
    def __init__(self, options: OrderedDict[Parameter, Option] = OrderedDict()):
        # Use an OrderedDict to honor insertion order
        self._options: OrderedDict[Parameter, Option] = OrderedDict(options)

    def appendOption(self, parameter: Parameter, option: Option) -> None:
        self._options[parameter] = option

    def getFileDescriptor(self) -> str:
        descriptor = ""
        for key, value in self._options.items():
            descriptor += "_"
            descriptor += key.abbreviation()
            descriptor += "-"
            descriptor += value.abbreviation()

        return descriptor
