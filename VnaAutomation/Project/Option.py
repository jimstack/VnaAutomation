from VnaAutomation.Base.Abbreviated import Abbreviated


class Option(Abbreviated):
    """
    Option for a project parameter. Initial implementation only includes name and abbreviation.
    The name will be used in any user interactions while the abbreviation will be used in file name creation.
    """

    def __init__(self):
        super().__init__()
