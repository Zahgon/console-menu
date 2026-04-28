import logging
import sys


class MenuBorderStyle(object):
    """
    Base class for console menu border. Each property should be overridden by a subclass.
    """

    @property
    def bottom_left_corner(self):
        """ The outer, bottom left corner of the menu. """
        raise NotImplementedError()

    @property
    def bottom_right_corner(self):
        """ The outer, bottom right corner of the menu. """
        raise NotImplementedError()

    @property
    def inner_horizontal(self):
        """ The character for inner horizontal section lines. """
        raise NotImplementedError()

    @property
    def inner_vertical(self):
        """ The character for inner vertical section lines. """
        raise NotImplementedError()

    @property
    def intersection(self):
        """ The character for intersecting inner vertical and inner horizontal lines (a "+" shape). """
        raise NotImplementedError()

    @property
    def outer_horizontal(self):
        """ The character for outer, horizontal lines (the top and bottom lines of the menu)."""
        raise NotImplementedError()

    @property
    def outer_horizontal_inner_down(self):
        """ The character for a top horizontal line with a downward inner line (a "T" shape). """
        raise NotImplementedError()

    @property
    def outer_horizontal_inner_up(self):
        """ The character for a bottom horizontal line with an upward inner line (an inverted "T" shape). """
        raise NotImplementedError()

    @property
    def outer_vertical(self):
        """ The character for an outer vertical line of the menu (the left and right sides of the menu). """
        raise NotImplementedError()

    @property
    def outer_vertical_inner_left(self):
        """ The character for an outer vertical line, with a protruding inner line to the left. """
        raise NotImplementedError()

    @property
    def outer_vertical_inner_right(self):
        """ The character for an outer vertical line, with a protruding inner line to the right. """
        raise NotImplementedError()

    @property
    def top_left_corner(self):
        """ The top left corner of the menu. """
        raise NotImplementedError()

    @property
    def top_right_corner(self):
        """ The top right corner of the menu. """
        raise NotImplementedError()


class AsciiBorderStyle(MenuBorderStyle):
    """
    A Menu Border Style using only ASCII characters.
    """

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass


class LightBorderStyle(MenuBorderStyle):
    """
    MenuBorderStyle class using Unicode "light" box drawing characters.
    """

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass


class HeavyBorderStyle(MenuBorderStyle):
    """
    MenuBorderStyle class using Unicode "heavy" box drawing characters.
    """

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass


class HeavyOuterLightInnerBorderStyle(HeavyBorderStyle):
    """
    MenuBorderStyle class using Unicode "heavy" box drawing characters for the outer borders, and
    "light" box drawing characters for the inner borders.
    """

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass


class DoubleLineBorderStyle(MenuBorderStyle):
    """
    MenuBorderStyle class using "double-line" box drawing characters.
    """

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass


class DoubleLineOuterLightInnerBorderStyle(DoubleLineBorderStyle):
    """
    MenuBorderStyle class using Unicode "double-line" box drawing characters for the outer borders, and
    "light" box drawing characters for the inner borders.
    """

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass

    @property
    pass


class MenuBorderStyleType(object):
    """
    Defines the various menu border styles, as expected by the border factory.
    """

    ASCII_BORDER = 0
    """ int: Menu Border using pure ASCII characters. Usable on all platforms. """

    LIGHT_BORDER = 1
    """ int: Menu Border using the "light" box drawing characters. Should be usable on all platforms. """

    HEAVY_BORDER = 2
    """ int: Menu Border using the "heavy" box drawing characters.
        NOTE: On Windows, this border style will work ONLY on Python 3.6 and later.  It will raise a UnicodeEncodeError
        exception on earlier Python versions. If requesting this border style via the MenuBorderStyleFactory when on
        Windows/Python 3.5 or earlier, this border style will be substituted by the `DOUBLE_LINE_BORDER`. """

    DOUBLE_LINE_BORDER = 3
    """ int: Menu Border using "double-line" box drawing characters. """

    HEAVY_OUTER_LIGHT_INNER_BORDER = 4
    """ int: Menu Border using the "heavy" box drawing characters for the outer border elements, and "light" box-drawing
        characters for the inner border elements.
        NOTE: On Windows, this border style will work ONLY on Python 3.6 and later.  It will raise a UnicodeEncodeError
        exception on earlier Python versions. If requesting this border style via the MenuBorderStyleFactory when
        on Windows/Python 3.5 or earlier, this border style will be substituted by the `DOUBLE_LINE_BORDER`. """

    DOUBLE_LINE_OUTER_LIGHT_INNER_BORDER = 5
    """ int: Menu Border using the "double-line" box drawing characters for the outer border elements, and "light"
        box-drawing characters for the inner border elements."""


class MenuBorderStyleFactory(object):
    """
    Factory class for creating  MenuBorderStyle instances.
    """

    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)

    def create_border(self, border_style_type):
        """
        Create a new MenuBorderStyle instance based on the given border style type.

        Args:
            border_style_type (int):  an integer value from :obj:`MenuBorderStyleType`.

        Returns:
            :obj:`MenuBorderStyle`: a new MenuBorderStyle instance of the specified style.

        """
        pass

    def create_ascii_border(self):
        """
        Create an ASCII border style.

        Returns:
            :obj:`AsciiBorderStyle`:  a new instance of AsciiBorderStyle.
        """
        pass

    def create_light_border(self):
        """
        Create a border style using "light" box drawing characters.

        Returns:
            :obj:`LightBorderStyle`: a new instance of LightBorderStyle
        """
        pass

    def create_heavy_border(self):
        """
        Create a border style using "heavy" box drawing characters.

        NOTE: The Heavy border style will work on Windows ONLY when using Python 3.6 or later. If on Windows and
        using an earlier version of Python, the heavy border will be substituted with the DOUBLE_LINE_BORDER.

        Returns:
            :obj:`HeavyBorderStyle` or :obj:`DoubleLineBorderStyle`: a new instance of HeavyBorderStyle, unless on
            Windows and pre-Python 3.5, in which case a new instance of DoubleLineBorderStyle will be returned.
        """
        pass

    def create_heavy_outer_light_inner_border(self):
        """
        Create a border style using "heavy" box drawing characters for outer border elements, and "light"
        box drawing characters for inner border elements.

        NOTE: The Heavy border style will work on Windows ONLY when using Python 3.6 or later. If on Windows and
        using an earlier version of Python, the heavy border will be substituted with the DOUBLE_LINE_BORDER.

        Returns:
            :obj:`HeavyOuterLightInnerBorderStyle` or :obj:`DoubleLineOuterLightInnerBorderStyle`: a new instance of
            HeavyOuterLightInnerBorderStyle, unless on Windows and pre-Python 3.5, in which case a new instance of
            DoubleLineOuterLightInnerBorderStyle will be returned.
        """
        pass

    def create_doubleline_border(self):
        """
        Create a border style using "double-line" box drawing characters.

        Returns:
            :obj:`DoubleLineBorderStyle`: a new instance of DoubleLineBorderStyle.
        """
        pass

    def create_doubleline_outer_light_inner_border(self):
        """
        Create a border style using "double-line" box drawing characters for outer border elements, and "light"
        box drawing characters for inner border elements.

        Returns:
            :obj:`DoubleLineOuterLightInnerBorderStyle`: a new instance of DoubleLineOuterLightInnerBorderStyle
        """
        pass

    @staticmethod
    def is_win_python35_or_earlier():
        """
        Convenience method to determine if the current platform is Windows and Python version 3.5 or earlier.

        Returns:
            bool: True if the current platform is Windows and the Python interpreter is 3.5 or earlier; False otherwise.

        """
        pass
