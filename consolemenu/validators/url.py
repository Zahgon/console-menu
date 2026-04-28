try:
    # python2
    from urlparse import urlparse
except Exception:
    # python3
    from urllib.parse import urlparse

from consolemenu.validators.base import BaseValidator


class UrlValidator(BaseValidator):

    def __init__(self):
        """
        URL Validator class
        """
        super(UrlValidator, self).__init__()

    def validate(self, input_string):
        """
        Validate url

        :return: True if match / False otherwise
        """
        pass
