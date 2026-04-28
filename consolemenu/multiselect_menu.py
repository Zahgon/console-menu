import itertools

from consolemenu import ConsoleMenu
from consolemenu.items import SubmenuItem


class MultiSelectMenu(ConsoleMenu):
    """
    Console menu that allows the selection of multiple menu items at a single prompt.

    Args:
        title: The menu title.
        subtitle: The menu subtitle.
        formatter: The menu formatter instance for styling the menu.
        prologue_text: The text to display in the prologue section of the menu.
        epilogue_text: The text to display in the epilogue section of the menu.
        show_exit_option (bool): Determines if the exit item should be displayed.
        exit_option_text (str): Text for the Exit menu item. Defaults to 'Exit'.
        clear_screen (bool): Set to False to disable clearing of screen between menus
    """

    def __init__(self, title=None, subtitle=None, formatter=None,
                 prologue_text=None, epilogue_text=None, ack_item_completion=True,
                 show_exit_option=True, exit_option_text='Exit', clear_screen=True):
        super(MultiSelectMenu, self).__init__(title, subtitle, formatter=formatter,
                                              prologue_text=prologue_text, epilogue_text=epilogue_text,
                                              show_exit_option=show_exit_option, exit_option_text=exit_option_text,
                                              clear_screen=clear_screen)
        self.ack_item_completion = ack_item_completion

    def append_item(self, item):
        """
        Add an item to the end of the menu before the exit item.

        Note that Multi-Select Menus will not allow a SubmenuItem to be added, as multi-select menus
        are expected to be used only for executing multiple actions.

        Args:
            item (:obj:`MenuItem`): The item to be added

        Raises:
            TypeError: If the specified MenuIem is a SubmenuItem.
        """
        pass

    def process_user_input(self):
        """
        This overrides the method in ConsoleMenu to allow for comma-delimited and range inputs.

        Examples:
            All of the following inputs would have the same result:
                * 1,2,3,4
                * 1-4
                * 1-2,3-4
                * 1 - 4
                * 1, 2, 3, 4
        Raises:
            ValueError: If the input cannot be correctly parsed.
        """
        pass

    @staticmethod
    def __parse_range(rng):
        pass

    def __parse_range_list(self, rngs):
        pass
