"""
Module that contains the configuration parameters for
the application
"""
import yaml

class Config():
    """
    Config class that contains all the config information for the app.

    Attributes
    ----------
    filename : str, default=configs/app.yml
    """

    def __init__(self, file="../configs/app.yml"):
        """
        Constructor of the class: read and load the YAML file passed or in alternative
        the default one.

        Raises
        ------
        yaml.YAMLError
            If there is an error in the YAML unmarshalling.
        FileNotFoundError
            If no such file or directory for file parameter
        """
        self.app_config = {}
        # load the config
        with open(file, "r") as stream:
              try:
                  self.app_config = yaml.safe_load(stream)
              except yaml.YAMLError as ex:
                  return ex
