from __future__ import print_function

import platform
import subprocess
import sys


class Screen(object):
    """
    Class representing a console screen.
    """

    def __init__(self):
        # TODO get actual screen size
        self.__height = 40
        self.__width = 80

    @property
    def screen_height(self):
        """
        int: The screen height in rows.
        """
        pass

    @property
    def screen_width(self):
        """
        int: The screen width in columns.
        """
        pass

    @staticmethod
    def clear():
        """
        Clear the screen.
        """
        pass

    @staticmethod
    def flush():
        """
        Flush any buffered standard output to screen.
        """
        pass

    def input(self, prompt=''):
        """
        Prompt the end user for input.

        Args:
            prompt (:obj:`str`, optional): The message to display as the prompt.

        Returns:
            The input provided by the user.
        """
        pass

    @staticmethod
    def printf(*args):
        """
        Print the specified arguments to the screen.

        Args:
            *args: Variable length argument list.
        """
        pass

    @staticmethod
    def println(*args):
        """
        Print the specified arguments to the screen, including an appended newline character.

        Args:
            *args: Variable length argument list.
        """
        pass
