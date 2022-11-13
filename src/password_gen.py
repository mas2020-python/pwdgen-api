
import random
import string
from utils import config


class PwdGenerator():
    """
    Generator class that is responsible to generate the random password.
    Attributes
    ----------

    """
    length = config.app_config["password_config"]["default_length"]
    numbers_flag = config.app_config["password_config"]["default_params"]["numbers_flag"]
    lowercase_flag = config.app_config["password_config"]["default_params"]["lowercase_flag"]
    uppercase_flag = config.app_config["password_config"]["default_params"]["uppercase_flag"]
    special_flag = config.app_config["password_config"]["default_params"]["special_flag"]

    def __init__(self, file="configs/app.yml"):
        """
        Constructor of the class.

        Raises
        ------
        ...
        """
        self.password = ""
        pass

    def generate(self, length=length, numbers_flag=numbers_flag, lowercase_flag=lowercase_flag,
                 uppercase_flag=uppercase_flag, special_flag=special_flag) -> str:
        """
        Generate the pwd and returns it to the caller.

        Parameters
        ----------
        length : str,         default config file configuration
          The desired pwd length
        numbers_flag : bool,  default config file configuration
          If consider numbers in the pwd generation
        lowercase_flag : bool,  default config file configuration
          If consider lowercase chars in the pwd generation
        uppercase_flag : bool,  default config file configuration
          If consider uppercase chars in the pwd generation
        special_flag : bool,  default config file configuration
          If consider special chars in the pwd generation

        Returns
        -------
        pwd : str
          The generated password

        Raises
        ------
        Exception
          The message reports what is the reason of the failure
        ...
        """
        print(f"the lenght={length}, numbers_flag={numbers_flag}, lowercase_flag={lowercase_flag}, uppercase_char{uppercase_flag}, special_flag={special_flag}")
        lowercases_chars, numbers, uppercases_chars, special_chars = "", "", "", ""
        # controls the pwd semantically (raise an exception in case of any error)
        elems, ts = self.__checks(length, numbers_flag, lowercase_flag,
                                  uppercase_flag, special_flag)
        # numbers of chars that compose each set of chars
        chars_length = length // elems
        remaining = length

        # it always generates a pwd with some characters (fdaieoifhawero)
        while remaining > 0:
            if lowercase_flag:
                lowercases_chars += self.__generate_flag(
                    chars_length if chars_length < remaining else remaining, string.ascii_lowercase)
                remaining -= chars_length
                print(f'the lowercases_chars is {lowercases_chars}')
            if numbers_flag:
                numbers += self.__generate_flag(
                    chars_length if chars_length < remaining else remaining, "01233456789")
                remaining -= chars_length
                print(f'the numbers are {numbers}')
            if uppercase_flag:
                uppercases_chars += self.__generate_flag(chars_length if chars_length < remaining else remaining,
                                                         string.ascii_uppercase)
                remaining -= chars_length
                print(f'the uppercase_flag are {uppercases_chars}')
            if special_flag:
                special_chars += self.__generate_flag(chars_length if chars_length < remaining else remaining,
                                                      "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
                remaining -= chars_length
                print(f'the special_chars are {special_chars}')

        # shuffle the final string
        password = self.__shuffle(
            length, lowercases_chars+numbers+uppercases_chars+special_chars)
        print(f'the final pws is >> {password} <<, length: {len(password)}')
        return password

    def __checks(self, length, numbers_flag, lowercase_flag,
                 uppercase_flag, special_flag):
        """
        Method to check the parameter for building the pwd
        """
        elems = 0
        if lowercase_flag:
            elems += 1
        if numbers_flag:
            elems += 1
        if uppercase_flag:
            elems += 1
        if special_flag:
            elems += 1
        # max length exceed
        if length > config.app_config["password_config"]["max_length"]:
            raise Exception(
                f'the given length ({length}) exceeds the max length of {config.app_config["password_config"]["max_length"]}')
        if elems == 0:
            raise Exception(
                'all the arguments passed to the API are False, it is not possible to generate a pwd. Set at least one parameter to True.')
        if length <= 0:
            raise Exception('the password length must be greater than 0')
        return elems, 100

    def __generate_flag(self, number: int, chars: list):
        """
        Generates a numbers or random chars and returns to the caller

        Parameters
        ----------
        number : int
          How many characters to generate
        chars : list
          List of characters to randomly pick up

        Returns
        -------
        chars_back : list
          The picked up characters
        """
        chars_back: list = []
        for i in range(0, number):
            chars_back.append(chars[random.randint(0, len(chars) - 1)])

        return ''.join(chars_back)

    def __shuffle(self, length: int, pwd: string):
        """
        Shuffle a password completing the length in case is needed.
        """
        final_pwd = ''.join(random.sample(pwd, len(pwd)))
        if length > len(final_pwd):
            lowercases = self.__generate_flag(
                length - len(final_pwd), string.ascii_lowercase)
            final_pwd += lowercases
        return final_pwd
