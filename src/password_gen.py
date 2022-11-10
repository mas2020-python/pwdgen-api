from utils import config


class PwdGenerator():
    """
    Generator class that is responsible to generate the random password.
    Attributes
    ----------

    """
    length = config.app_config["password_config"]["default_length"]
    numbers_flag = config.app_config["password_config"]["default_params"]["numbers_flag"]
    lowercase_chars = config.app_config["password_config"]["default_params"]["lowercase_chars"]
    uppercase_chars = config.app_config["password_config"]["default_params"]["uppercase_chars"]
    special_chars = config.app_config["password_config"]["default_params"]["special_chars"]

    def __init__(self, file="configs/app.yml"):
        """
        Constructor of the class.

        Raises
        ------
        ...
        """
        pass

    def generate(self, length=length, numbers_flag=numbers_flag, lowercase_chars=lowercase_chars,
                 uppercase_chars=uppercase_chars, special_chars=special_chars):
        """
        Generate the pwd and returns it to the caller.

        Parameters
        ----------
        length : str,         default config file configuration
        numbers_flag : bool,  default config file configuration

        Returns
        -------
        pwd : str
          The generated password
        Raises
        ------
        ...
        """
        print(f"the lenght={length}, numbers_flag={numbers_flag}, lowercase_chars={lowercase_chars}, uppercase_char{uppercase_chars}, special_chars={special_chars}")
        pass
