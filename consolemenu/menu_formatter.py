from consolemenu.format.menu_borders import MenuBorderStyle, MenuBorderStyleFactory
from consolemenu.format.menu_style import MenuStyle
from consolemenu.menu_component import Dimension, MenuHeader, MenuTextSection, MenuItemsSection, MenuFooter, MenuPrompt


class MenuFormatBuilder(object):
    """
    Builder class for generating the menu format.
    """

    def __init__(self, max_dimension=None):
        if max_dimension is None:
            max_dimension = Dimension(width=80, height=40)
        self.__max_dimension = max_dimension
        self.__border_style_factory = MenuBorderStyleFactory()
        self.__header = MenuHeader(menu_style=MenuStyle(), max_dimension=max_dimension)
        self.__prologue = MenuTextSection(menu_style=MenuStyle(), max_dimension=max_dimension)
        self.__items_section = MenuItemsSection(menu_style=MenuStyle(), max_dimension=max_dimension)
        self.__epilogue = MenuTextSection(menu_style=MenuStyle(), max_dimension=max_dimension)
        self.__footer = MenuFooter(menu_style=MenuStyle(), max_dimension=max_dimension)
        self.__prompt = MenuPrompt(menu_style=MenuStyle(), max_dimension=max_dimension)
        # Indent items deeper than other sections
        self.__items_section.style.padding.left = 3
        # Change default top border of prompt to 0, so it hugs the bottom of the menu
        self.__prompt.style.padding.top = 0

    # ============================================================
    # Margins and Border style applies to entire menu
    # ============================================================

    def set_border_style(self, border_style):
        """
        Set the border style using the specified MenuBorderStyle instance.
        :param border_style: the instance of MenuBorderStyle to use for border style formatting.
        """
        pass

    def set_border_style_type(self, border_style_type):
        """
        Set the border style using the specified border style type. The border style type should be an
        integer value recognized by the border style factory for this formatter instance.
        The built-in border style types are provided by the `MenuBorderStyleType` class, or custom
        border style types can be provided if using a custom border style factory.
        :param border_style_type: an integer value representing the border style type.
        """
        pass

    def set_border_style_factory(self, border_style_factory):
        """
        Set the instance of MenuBorderStyleFactory to use for generating border styles.
        Typically, this method will never need to be used, unless the default MenuBorderStyleFactory
        has been subclassed to provide custom border styles.
        :param border_style_factory: an instance of MenuBorderStyleFactory.
        """
        pass

    def set_bottom_margin(self, bottom_margin):
        """
        Set the bottom margin of the menu. This will determine the number of console lines appear between the
        bottom of the menu border and the menu input prompt.
        :param bottom_margin: an integer value
        """
        pass

    def set_left_margin(self, left_margin):
        """
        Set the left margin of the menu.  This will determine the number of spaces between the left edge of the
        screen and the left menu border.
        :param left_margin: an integer value
        """
        pass

    def set_right_margin(self, right_margin):
        """
        Set the right margin of the menu.  This will determine the number of spaces between the right edge of the
        screen and the right menu border.
        :param right_margin: an integer value
        """
        pass

    def set_top_margin(self, top_margin):
        """
        Set the top margin of the menu.  This will determine the number of console lines between the top edge
        of the screen and the top menu border.
        :param top_margin: an integer value
        """
        pass

    # ============================================================
    # Header Settings
    # ============================================================

    def set_title_align(self, align='left'):
        pass

    def set_subtitle_align(self, align='left'):
        pass

    def set_header_left_padding(self, x):
        pass

    def set_header_right_padding(self, x):
        pass

    def set_header_bottom_padding(self, x):
        pass

    def set_header_top_padding(self, x):
        pass

    def show_header_bottom_border(self, flag):
        pass

    # ============================================================
    # Footer Settings
    # ============================================================

    def set_footer_left_padding(self, x):
        pass

    def set_footer_right_padding(self, x):
        pass

    def set_footer_bottom_padding(self, x):
        pass

    def set_footer_top_padding(self, x):
        pass

    # ============================================================
    # Items Section Settings
    # ============================================================

    def set_items_left_padding(self, x):
        pass

    def set_items_right_padding(self, x):
        pass

    def set_items_bottom_padding(self, x):
        pass

    def set_items_top_padding(self, x):
        pass

    def show_item_bottom_border(self, item_text, flag):
        # Allow a menu item to be passed in instead of text.
        pass

    def show_item_top_border(self, item_text, flag):
        # Allow a menu item to be passed in instead of text.
        pass

    # ============================================================
    # Prologue Section Settings
    # ============================================================

    def set_prologue_text_align(self, align='left'):
        pass

    def show_prologue_top_border(self, flag):
        pass

    def show_prologue_bottom_border(self, flag):
        pass

    # ============================================================
    # Epilogue Section Settings
    # ============================================================

    def set_epilogue_text_align(self, align='left'):
        pass

    def show_epilogue_top_border(self, flag):
        pass

    def show_epilogue_bottom_border(self, flag):
        pass

    # ============================================================
    # Prompt Settings
    # ============================================================

    def set_prompt(self, prompt):
        pass

    # ============================================================
    # Menu generation
    # ============================================================

    def clear_data(self):
        """
        Clear menu data from previous menu generation.
        """
        pass

    def format(self, title=None, subtitle=None, prologue_text=None, epilogue_text=None, items=None):
        """
        Format the menu and return as a string.
        :return:  a string representation of the formatted menu.
        """
        pass
