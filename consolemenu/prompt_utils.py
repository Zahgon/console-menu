import getpass

from collections import namedtuple
from consolemenu.validators.base import BaseValidator, InvalidValidator


InputResult = namedtuple("InputResult", "input_string validation_result")


class PromptFormatter(object):
    """
    Class for formatting a text input prompt, to allow overriding the message as desired.

    Default answers will appear in [square brackets] and allow the user to return that answer by simply pressing
    the Enter button.

    If a 'Quit' option is desired, set `enable_quit` to True and provide a `quit_string` (default is 'q') and
    a `quit_message` (default is '(enter q to Quit)').

    """
    @staticmethod
    def format_prompt(prompt=None, default=None, enable_quit=False, quit_string='q',
                      quit_message='(enter q to Quit)'):
        """
        Format the message presented to the user during input prompting.

        Args:
            prompt (str): The message to ask the user.
            default (str, optional): The default answer if user does not provide explicit input.
            enable_quit (bool, optional): Flag to determine whether a Quit option will be presented.
            quit_string (str, optional): The string the user must input to quit (default is 'q').
            quit_message (str, optional): The message to the user explaining how to Quit.

        Returns:
            str: The formatted prompt string.
        """
        pass


class PromptUtils(object):
    """
    Utility class with various routines for prompting for user input.
    """

    def __init__(self, screen, prompt_formatter=None):
        """
        Creates a new instance of ConsoleUtils with the specified console. If no console was
        specified, creates a new default console using the ConsoleFactory.

        Args:
            screen (:obj:`consolemenu.screen.Screen`): The Screen instance.
            prompt_formatter (:obj:`PromptFormatter`, optional): The instance of PromptFormatter for displaying
             the prompt.
        """
        self.__screen = screen
        if prompt_formatter is None:
            prompt_formatter = PromptFormatter()
        self.__prompt_formatter = prompt_formatter

    @property
    def screen(self):
        """
        :obj:`consolemenu.screen.Screen`: The Screen instance.
        """
        pass

    def clear(self):
        """
        Clear the screen.
        """
        pass

    def confirm_answer(self, answer, message=None):
        """
        Prompts the user to confirm a question with a yes/no prompt.
        If no message is specified, the default message is:  "You entered {}. Is this correct?"

        Args:
            answer (str): The answer to confirm.
            message (str, optional): Optional message if a different confirmation prompt is desired.

        Returns:
            bool: True if the user confirmed Yes, or False if user specified No.

        """
        pass

    def enter_to_continue(self, message=None):
        """
        A console prompt to ask the user to 'Press [Enter] to continue'.

        Args:
            message (str, optional): A message to display in place of the default.
        """
        pass

    def input(self, prompt=None, default=None, validators=None, enable_quit=False, quit_string='q',
              quit_message='(enter q to Quit)'):
        """
        Generic prompt the user for input.

        Args:
            prompt (str): The message to prompt the user.
            default (str, optional): The default value to suggest as an answer.
            validators (:obj:`BaseValidator`, optional): The list of validators to perform input validation.
            enable_quit (bool, optional): Specifies whether the user can cancel out of the input prompt.
            quit_string (str, optional): The string which the user must input in order to quit.
            quit_message (str, optional): The message to explain how to quit.

        Returns:
            InputResult: an InputResult tuple.

        """
        pass

    def input_password(self, message=None):
        """
        Prompt the user for a password or other confidential data.

        This is equivalent to the input() method, but does not echo inputted characters to the screen.

        Args:
            message (str): The prompt message.

        Returns:
            str: The password provided by the user.
        """
        pass

    def printf(self, *args):
        """
        Prints the specified arguments to the screen.

        Args:
            *args: Variable length argument list.
        """
        pass

    def println(self, *args):
        """
        Prints the specified arguments to the screen, followed by a newline character.

        Args:
            *args: Variable length argument list.
        """
        pass

    def prompt_and_confirm_password(self, message):
        """
        Prompt for a password using the given message, then prompt a second time for a confirmation
        password, and verify both provided passwords match. If the passwords do not match, an error
        is displayed, "Passwords do not match", and the user must input both passwords again.

        Args:
            message (str): The prompt message.

        Returns:
            str: The password.
        """
        pass

    def prompt_for_bilateral_choice(self, prompt, option1, option2):
        """
        Prompt the user for a response that must be one of the two supplied choices.

        NOTE: The user input verification is case-insensitive, but will return the original case provided
        by the given options.

        Args:
            prompt (str): The prompt to present the choices to the user.
            option1 (str): The first option.
            option2 (str): The second option.

        Returns:
            str: The choice selected by the user.

        """
        pass

    def prompt_for_trilateral_choice(self, prompt, option1, option2, option3):
        """
        Prompt the user for a response that must be one of the three supplied choices.

        NOTE: The user input verification is case-insensitive, but will return the original case provided
        by the given options.

        Args:
            prompt (str): The prompt to present the choices to the user.
            option1 (str): The first option.
            option2 (str): The second option.
            option3 (str): The third option.

        Returns:
            str: The choice selected by the user.
        """
        pass

    def prompt_for_yes_or_no(self, prompt):
        """
        Prompts the user with the specified question, and expects a yes (y) or no (n)
        response, returning a boolean value representing the user's answer.

        Args:
            prompt (str): The prompt to display to the user.

        Returns:
            bool: True for yes, False for no.
        """
        pass

    def prompt_for_numbered_choice(self, choices, title=None, prompt=">"):
        """
        Displays a numbered vertical list of choices from the provided list of strings.

        Args:
            choices (:obj:`list` of :obj:`str`): The list of choices to display.
            title (str, optional): Optional title to display above the numbered list.
            prompt (str): The prompt string. Default is ">".

        Returns:
            int: The index of selected choice.
        """
        pass

    def validate_input(self, input_string, validators):
        """
        Validate the given input string against the specified list of validators.

        Args:
            input_string (str): The input string to verify.
            validators (:obj:`list` of :obj:`BaseValidator`): The list of validators.

        Returns:
            bool: The validation result. True if the input is valid; False otherwise.

        Raises:
            InvalidValidator: If the list of validators contains an invalid BaseValidator class.
        """
        pass


class UserQuit(Exception):
    """
    Exception raised when a user chooses to Quit from an input prompt.
    """
    pass
