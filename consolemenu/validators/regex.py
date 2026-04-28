from re import match

from consolemenu.validators.base import BaseValidator


class RegexValidator(BaseValidator):

    def __init__(self, pattern):
        super(RegexValidator, self).__init__()
        self.__pattern = pattern

    @property
    def pattern(self):
        pass

    def validate(self, input_string):
        """
        Validate input_string against a regex pattern

        :return: True if match / False otherwise
        """
        pass
