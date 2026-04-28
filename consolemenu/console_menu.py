from __future__ import print_function

import platform
import threading

import os

from consolemenu.menu_formatter import MenuFormatBuilder
from consolemenu.screen import Screen


class ConsoleMenu(object):
    """
    A class that displays a menu and allows the user to select an option.

    Args:
        title (str): The title of the menu, or a method reference that returns a string.
        subtitle (str): The subtitle of the menu, or a method reference that returns a string.
        screen (:obj:`consolemenu.screen.Screen`): The screen object associated with this menu.
        formatter (:obj:`MenuFormatBuilder`): The MenuFormatBuilder instance used to format this menu.
        prologue_text (str): Text or method reference to include in the "prologue" section of the menu.
        epilogue_text (str): Text or method reference to include in the "epilogue" section of the menu.
        show_exit_option (bool): Specifies whether this menu should show an exit item by default. Defaults to True.
            Can be overridden when the menu is started.
        exit_option_text (str): Text for the Exit menu item. Defaults to 'Exit'.
        exit_menu_char (str): Character to use for exiting the menu. Defaults to None.
        clear_screen (bool): Set to False to disable clearing of screen between menus

    Attributes:
        cls.currently_active_menu (:obj:`ConsoleMenu`): Class variable that holds the currently active menu or None
            if no menu is currently active (e.g. when switching between menus)
        items (:obj:`list` of :obj:`MenuItem`): The list of MenuItems that the menu will display
        parent (:obj:`ConsoleMenu`): The parent of this menu
        previous_active_menu (:obj:`ConsoleMenu`): the previously active menu to be restored into the class's
            currently active menu
        current_option (int): The currently highlighted menu option
        selected_option (int): The option that the user has most recently selected
    """

    currently_active_menu = None

    def __init__(self, title=None, subtitle=None, screen=None, formatter=None,
                 prologue_text=None, epilogue_text=None, clear_screen=True,
                 show_exit_option=True, exit_option_text='Exit', exit_menu_char=None):
        if screen is None:
            screen = Screen()
        self.screen = screen

        self.clear_screen_before_render = clear_screen

        if formatter is None:
            formatter = MenuFormatBuilder()
        self.formatter = formatter

        self.title = title
        self.subtitle = subtitle
        self.prologue_text = prologue_text
        self.epilogue_text = epilogue_text

        self.highlight = None
        self.normal = None

        self.show_exit_option = show_exit_option

        self.items = list()

        self.parent = None

        self.exit_item = ExitItem(menu=self, text=exit_option_text, menu_char=exit_menu_char)

        self.current_option = 0
        self.selected_option = -1

        self.returned_value = None

        self.should_exit = False

        self.previous_active_menu = None

        self._main_thread = None

        self._running = threading.Event()

    def __repr__(self):
        return "%s: %s. %d items" % (self.get_title(), self.get_subtitle(), len(self.items))

    @property
    def current_item(self):
        """
        :obj:`consolemenu.items.MenuItem`: The item corresponding to the menu option that is currently highlighted,
            or None.
        """
        pass

    @property
    def selected_item(self):
        """
        :obj:`consolemenu.items.MenuItem`:  The item in :attr:`items` that the user most recently selected, or None.
        """
        pass

    def append_item(self, item):
        """
        Add an item to the end of the menu before the exit item.

        Args:
            item (MenuItem): The item to be added.

        """
        pass

    def remove_item(self, item):
        """
        Remove the specified item from the menu.

        Args:
            item (MenuItem): the item to be removed.

        Returns:
            bool: True if the item was removed; False otherwise.
        """
        pass

    def add_exit(self):
        """
        Add the exit item if necessary. Used to make sure there aren't multiple exit items.

        Returns:
            bool: True if item needed to be added, False otherwise.
        """
        pass

    def remove_exit(self):
        """
        Remove the exit item if necessary. Used to make sure we only remove the exit item, not something else.

        Returns:
            bool: True if item needed to be removed, False otherwise.
        """
        pass

    def is_selected_item_exit(self):
        """
        Checks to determine if the currently selected item is the Exit Menu item.

        Returns:
            bool: True if the currently selected item is the Exit Menu item; False otherwise.
        """
        pass

    def _wrap_start(self):
        pass

    def start(self, show_exit_option=None):
        """
        Start the menu in a new thread and allow the user to interact with it.
        The thread is a daemon, so :meth:`join()<consolemenu.ConsoleMenu.join>` should be called if there's a
        possibility that the main thread will exit before the menu is done

        Args:
            show_exit_option (bool): Specify whether the exit item should be shown, defaults to the value
                set in the constructor

        """
        pass

    def show(self, show_exit_option=None):
        """
        Calls start and then immediately joins.

        Args:
            show_exit_option (bool):  Specify whether the exit item should be shown, defaults to the value set
                in the constructor

        """
        pass

    def _main_loop(self):
        pass

    def draw(self):
        """
        Refresh the screen and redraw the menu. Should be called whenever something changes that needs to be redrawn.
        """
        pass

    def is_running(self):
        """
        Check if the menu has been started and is not paused.

        Returns:
            bool: True if the menu is started and hasn't been paused; False otherwise.
        """
        pass

    def wait_for_start(self, timeout=None):
        """
        Block until the menu is started.

        Args:
            timeout:  How long to wait before timing out.

        Returns:
            bool: False if timeout is given and operation times out, True otherwise. None before Python 2.7.
        """
        pass

    def is_alive(self):
        """
        Check whether the thread is stil alive.

        Returns:
            bool: True if the thread is still alive; False otherwise.
        """
        pass

    def pause(self):
        """
        Temporarily pause the menu until resume is called.
        """
        pass

    def resume(self):
        """
        Sets the currently active menu to this one and resumes it.
        """
        pass

    def join(self, timeout=None):
        """
        Should be called at some point after :meth:`start()<consolemenu.ConsoleMenu.start>` to block until
        the menu exits.

        Args:
            timeout (Number): How long to wait before timing out.

        """
        pass

    def get_input(self):
        """
        Can be overridden to change the input method.
        Called in :meth:`process_user_input()<consolemenu.ConsoleMenu.process_user_input>`

        :return: the ordinal value of a single character
        :rtype: int
        """
        pass

    def process_user_input(self):
        """
        Gets the next single character and decides what to do with it
        """
        pass

    def go_to(self, option):
        """
        Go to the option entered by the user as a number

        :param option: the option to go to
        :type option: int
        """
        pass

    def go_down(self):
        """
        Go down one, wrap to beginning if necessary
        """
        pass

    def go_up(self):
        """
        Go up one, wrap to end if necessary
        """
        pass

    def select(self):
        """
        Select the current item and run it
        """
        pass

    def exit(self):
        """
        Signal the menu to exit, then block until it's done cleaning up
        """
        pass

    def _set_up_colors(self):
        # TODO add color support
        # curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        # self.highlight = curses.color_pair(1)
        # self.normal = curses.A_NORMAL
        pass

    def clear_screen(self):
        """
        Clear the screen belonging to this menu
        """
        pass

    # Getters to get text in case method reference
    def get_title(self):
        pass

    def get_subtitle(self):
        pass

    def get_prologue_text(self):
        pass

    def get_epilogue_text(self):
        pass


class MenuItem(object):
    """
    A generic menu item
    """

    def __init__(self, text, menu=None, should_exit=False, menu_char=None):
        """
        :ivar str text: The text shown for this menu item
        :ivar ConsoleMenu menu: The menu to which this item belongs
        :ivar bool should_exit: Whether the menu should exit once this item's action is done
        :ivar str menu_char: The character used to select this menu item. Optional - defaults to None.
        """
        self.text = text
        self.menu = menu
        self.should_exit = should_exit
        self.index_item_separator = " - "
        self.menu_char = menu_char

    def __str__(self):
        return "%s %s" % (self.menu.get_title(), self.get_text())

    def show(self, index):
        """
        How this item should be displayed in the menu. Can be overridden, but should keep the same signature.

        Default is:

            1 - Item 1

            2 - Another Item

        :param int index: The index of the item in the items list of the menu
        :return: The representation of the item to be shown in a menu
        :rtype: str
        """
        pass

    def set_up(self):
        """
        Override to add any setup actions necessary for the item
        """
        pass

    def action(self):
        """
        Override to carry out the main action for this item.
        """
        pass

    def clean_up(self):
        """
        Override to add any cleanup actions necessary for the item
        """
        pass

    def get_return(self):
        """
        Override to change what the item returns.
        Otherwise just returns the same value the last selected item did.
        """
        pass

    def __eq__(self, o):
        return self.text == o.text and self.menu == o.menu and self.should_exit == o.should_exit

    # Getters to get text in case method reference
    def get_text(self):
        pass


class ExitItem(MenuItem):
    """
    Used to exit the current menu. Handled by :class:`consolemenu.ConsoleMenu`
    """

    def __init__(self, text="Exit", menu=None, menu_char=None):
        super(ExitItem, self).__init__(text=text, menu=menu, should_exit=True, menu_char=menu_char)

    def show(self, index, available_width=None):
        """
        ExitItem overrides this method to display appropriate Exit or Return text.
        """
        pass


def clear_terminal():
    """
    Call the platform specific function to clear the terminal: cls on windows, reset otherwise
    """
    pass
