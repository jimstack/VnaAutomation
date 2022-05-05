import xmltodict
from VnaAutomation.Project.Project import Project
from VnaAutomation.Project.TestConfiguration import TestConfiguration
from VnaAutomation.Operators.TestConfigurationGenerator import TestConfigurationGenerator

ROOT = "root"
PROJECT = "project"


def main(fileName):
    project = Project()
    projectData = None

    with open(fileName, "rb") as inputFile:
        document = xmltodict.parse(inputFile, force_list={'parameter', 'option'})
        projectData = document[ROOT][PROJECT]

    if not projectData:
        return

    project.parseDict(projectData)

    configurations: list[TestConfiguration] = TestConfigurationGenerator.apply(project)
    for configuration in configurations:
        print(f"{project.name()}{configuration.getFileDescriptor()}")


if __name__ == "__main__":
    main("Data/SampleConfigs/Sample1.xml")
