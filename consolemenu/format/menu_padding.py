class MenuPadding(object):
    """
    Class for menu padding. Padding is the area between the menu border and the content of the menu.

    Args:
        top (int): The top padding.
        left (int):  The left padding.
        bottom (int): The bottom padding.
        right (int): The right padding.
    """

    def __init__(self, top=1, left=2, bottom=1, right=2):
        self.__left = left
        self.__right = right
        self.__top = top
        self.__bottom = bottom

    @property
    def left(self):
        """
        The left padding.

        Returns:
            int: The left padding.
        """
        pass

    @left.setter
    def left(self, left):
        pass

    @property
    def right(self):
        """
        The right padding.

        Returns:
            int: The right padding.
        """
        pass

    @right.setter
    def right(self, right):
        pass

    @property
    def top(self):
        """
        The top padding.

        Returns:
            int: The top padding.
        """
        pass

    @top.setter
    def top(self, top):
        pass

    @property
    def bottom(self):
        """
        The bottom padding.

        Returns:
            int: The bottom padding.
        """
        pass

    @bottom.setter
    def bottom(self, bottom):
        pass
