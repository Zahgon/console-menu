try:
    import ansiwrap as textwrap
except ImportError:
    import textwrap

from consolemenu.format import MenuStyle


def ansilen(s):
    """
    Return the length of the string minus any ANSI control codes.
    Args:
        s (string): The input string to check.
    Returns:
        int: The string length.
    """
    pass


class Dimension(object):
    """
    The Dimension class encapsulates the height and width of a component.

    Args:
        width (int): the width of the Dimension, in columns.
        height (int): the height of the Dimension, in rows.
        dimension (Dimension, optional): an existing Dimension from which to duplicate the height and width.
    """

    def __init__(self, width=0, height=0, dimension=None):
        self.width = width
        self.height = height
        if dimension is not None:
            self.width = dimension.width
            self.height = dimension.height


class MenuComponent(object):
    """
    Base class for a menu component.

    Args:
        menu_style (:obj:`MenuStyle`): the style for this component.
        max_dimension (:obj:`Dimension`): the maximum Dimension (width x height) for the menu. Defaults to width=80
            and height=40 if not specified.

    Raises:
        TypeError: if menu_style is not a :obj:`MenuStyle`.
    """

    def __init__(self, menu_style, max_dimension=None):
        if not isinstance(menu_style, MenuStyle):
            raise TypeError('menu_style must be of type MenuStyle')
        if max_dimension is None:
            max_dimension = Dimension(width=80, height=40)
        self.__max_dimension = max_dimension
        self.__style = menu_style

    @property
    def max_dimension(self):
        """
        :obj:`Dimension`: The maximum dimension for the menu.
        """
        pass

    @property
    def style(self):
        """
        :obj:`consolemenu.format.MenuStyle`: The style for this component.
        """
        pass

    @property
    def margins(self):
        """
        :obj:`consolemenu.format.MenuMargins`: The margins for this component.
        """
        pass

    @property
    def padding(self):
        """
        :obj:`consolemenu.format.MenuPadding`: The padding for this component.
        """
        pass

    @property
    def border_style(self):
        """
        :obj:`consolemenu.format.MenuBorderStyle`: The border style for this component.
        """
        pass

    def calculate_border_width(self):
        """
        Calculate the width of the menu border. This will be the width of the maximum allowable
        dimensions (usually the screen size), minus the left and right margins and the newline character.
        For example, given a maximum width of 80 characters, with left and right margins both
        set to 1, the border width would be 77 (80 - 1 - 1 - 1 = 77).

        Returns:
            int: the menu border width in columns.
        """
        pass

    def calculate_content_width(self):
        """
        Calculate the width of inner content of the border.  This will be the width of the menu borders,
        minus the left and right padding, and minus the two vertical border characters.
        For example, given a border width of 77, with left and right margins each set to 2, the content
        width would be 71 (77 - 2 - 2 - 2 = 71).

        Returns:
            int: the inner content width in columns.
        """
        pass

    def generate(self):
        """
        Generate this component.

        Yields:
            str: The next string of characters for drawing this component.
        """
        raise NotImplemented()

    def inner_horizontals(self):
        """
        The string of inner horizontal border characters of the required length for this component (not including
        the menu margins or verticals).

        Returns:
            str: The inner horizontal characters.
        """
        pass

    def inner_horizontal_border(self):
        """
        The complete inner horizontal border section, including the left and right border verticals.

        Returns:
            str: The complete inner horizontal border.
        """
        pass

    def outer_horizontals(self):
        """
        The string of outer horizontal border characters of the required length for this component (not including
        the menu margins or verticals).

        Returns:
            str: The outer horizontal characters.
        """
        pass

    def outer_horizontal_border_bottom(self):
        """
        The complete outer bottom horizontal border section, including left and right margins.

        Returns:
            str: The bottom menu border.
        """
        pass

    def outer_horizontal_border_top(self):
        """
        The complete outer top horizontal border section, including left and right margins.

        Returns:
            str: The top menu border.
        """
        pass

    def _generate_single_row(self, content='', align='left'):
        """
        A row of the menu, which comprises the left and right verticals plus the given content.

        Returns:
            str: A row of this menu component with the specified content.
        """
        pass

    def row(self, content='', align='left', indent_len=0):
        """
        A row of the menu, which comprises the left and right verticals plus the given content.
        If the content is larger than the alloted space for a single row, the content is wrapped
        onto multiple lines, while also respecting user-included newline characters.

        Returns:
            str: One or more rows of this menu component with the specified content.
        """
        pass

    @staticmethod
    def _alignment_char(align):
        pass

    def _format_content(self, content='', align='left'):
        pass


class MenuHeader(MenuComponent):
    """
    The menu header section.
    The menu header contains the top margin, menu top, title/subtitle verticals, bottom padding verticals,
    and optionally a bottom border to separate the header from the next section.
    """

    def __init__(self, menu_style, max_dimension=None, title=None, title_align='left',
                 subtitle=None, subtitle_align='left', show_bottom_border=False):
        super(MenuHeader, self).__init__(menu_style, max_dimension)
        self.title = title
        self.title_align = title_align
        self.subtitle = subtitle
        self.subtitle_align = subtitle_align
        self.show_bottom_border = show_bottom_border

    def generate(self):
        pass


class MenuTextSection(MenuComponent):
    """
    The menu text block section.
    A text block section can be used for displaying text to the user above or below the main items section.
    """

    def __init__(self, menu_style, max_dimension=None, text=None, text_align='left',
                 show_top_border=False, show_bottom_border=False):
        super(MenuTextSection, self).__init__(menu_style, max_dimension)
        self.text = text
        self.text_align = text_align
        self.show_top_border = show_top_border
        self.show_bottom_border = show_bottom_border

    def generate(self):
        pass


class MenuItemsSection(MenuComponent):
    """
    The menu section for displaying the menu items.
    """

    def __init__(self, menu_style, max_dimension=None, items=None, items_align='left'):
        super(MenuItemsSection, self).__init__(menu_style, max_dimension)
        if items is not None:
            self.__items = items
        else:
            self.__items = list()
        self.items_align = items_align
        self.__top_border_dict = dict()
        self.__bottom_border_dict = dict()

    @property
    def items(self):
        pass

    @items.setter
    def items(self, items):
        pass

    @property
    def items_with_bottom_border(self):
        """
        Return a list of the names (the item text property) of all items that should show a bottom border.
        :return: a list of item names that should show a bottom border.
        """
        pass

    @property
    def items_with_top_border(self):
        """
        Return a list of the names (the item text property) of all items that should show a top border.
        :return: a list of item names that should show a top border.
        """
        pass

    def show_item_bottom_border(self, item_text, flag):
        """
        Sets a flag that will show a bottom border for an item with the specified text.
        :param item_text: the text property of the item
        :param flag: boolean specifying if the border should be shown.
        """
        pass

    def show_item_top_border(self, item_text, flag):
        """
        Sets a flag that will show a top border for an item with the specified text.
        :param item_text: the text property of the item
        :param flag: boolean specifying if the border should be shown.
        """
        pass

    def generate(self):
        pass


class MenuFooter(MenuComponent):
    """
    The menu footer section.
    The menu footer contains the menu bottom, bottom padding verticals, and bottom margin.
    """

    def generate(self):
        pass


class MenuPrompt(MenuComponent):
    """
    A string representing the menu prompt for user input.
    """

    def __init__(self, menu_style, max_dimension=None, prompt_string=">>"):
        super(MenuPrompt, self).__init__(menu_style, max_dimension)
        self.__prompt = prompt_string

    @property
    def prompt(self):
        pass

    @prompt.setter
    def prompt(self, prompt):
        pass

    def generate(self):
        pass
