from VnaAutomation.Project.Parameter import Parameter

PARAMETER = "parameter"


class ParameterManager:
    def __init__(self):
        self._parameters: list[Parameter] = []

    def parseDict(self, values: dict) -> None:
        #TODO: Add "parameter" to force_list setting
        if PARAMETER in values:
            parameters = values[PARAMETER]
            for value in parameters:
                parameter = Parameter()
                parameter.parseDict(value)

                self.appendParameter(parameter)

    def parameters(self) -> list[Parameter]:
        return self._parameters

    def appendParameter(self, parameter: Parameter) -> None:
        self._parameters.append(parameter)
