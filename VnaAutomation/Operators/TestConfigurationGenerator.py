from collections import OrderedDict

from VnaAutomation.Project.Project import Project
from VnaAutomation.Project.Parameter import Parameter
from VnaAutomation.Project.Option import Option
from VnaAutomation.Project.TestConfiguration import TestConfiguration


class TestConfigurationGenerator:
    def __init__(self):
        pass

    @staticmethod
    def apply(project: Project) -> list[TestConfiguration]:
        configurations: list[TestConfiguration] = []
        selectedOptions: OrderedDict[Parameter, Option] = OrderedDict()
        parameters: list[Parameter] = project.parameterManager().parameters()

        TestConfigurationGenerator._buildConfigurations(configurations, selectedOptions, parameters)

        return configurations

    @staticmethod
    def _buildConfigurations(configurations: list[TestConfiguration],
                             selectedOptions: OrderedDict[Parameter, Option],
                             remainingParameters: list[Parameter]) -> None:

        # Make a copy of the incoming lists, so when we return to this point from a deeper call
        # we still have all the parameters we need to work with.
        parameters: list[Parameter] = remainingParameters.copy()

        parameter: Parameter = parameters.pop(0)    # Remove the first parameter from the list
        options: list[Option] = parameter.options()
        for option in options:
            # Add the option to the selection
            selectedOptions[parameter] = option

            if parameters:
                # There are still parameters in the list, keep building
                TestConfigurationGenerator._buildConfigurations(configurations, selectedOptions, parameters)
            else:
                # There are no more parameters. Create a configuration
                configurations.append(TestConfiguration(selectedOptions))

            # Return the selected options to their original state for further processing
            selectedOptions.pop(parameter)

