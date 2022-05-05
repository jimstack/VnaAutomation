from VnaAutomation.Base.Abbreviated import Abbreviated
from VnaAutomation.Project.ParameterManager import ParameterManager

PARAMETER_MANAGER = "parameterManager"


class Project(Abbreviated):
    def __init__(self):
        super().__init__()

        self._parameterManager: ParameterManager = ParameterManager()

    def parseDict(self, values: dict) -> None:
        super().parseDict(values)

        parameterManagerData = values[PARAMETER_MANAGER]
        self._parameterManager.parseDict(parameterManagerData)

    def parameterManager(self) -> ParameterManager:
        return self._parameterManager
