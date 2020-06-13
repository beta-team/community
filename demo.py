r"""This document is a demo."""


class NoteDemo(object):
    r"""A class used to sort an unsorted array with different kind of algorithm.

    Including quick-sort, merge-sort, shell-sort, etc. Please refer to :class:`NoteDemo`

    for more details.

    .. note::
        If you want to let user switch to specific class, please add :class:`class-name`

    .. math::
        a^{2} + b^{2} = c{^2}

    If you want to use unordered list, try as follows:

    * :attr:`a`: first params.
    * :attr:`b`: second params.

    Class information...

    Class information...

    Attributes:
        init_array: unsorted array, :math:`\sum_{i=0}^{n}a_i` is inline math example.
    """

    def __init__(self, init_array):
        r"""Init the demo class."""
        self.array = init_array

    def return_function(self, param1, param2):
        r"""Show how to write notes correctly.

        I will show math, example, yield in this function.

        Please follow this standard to write your code.

        .. note::
            If you want to write some note, please add `Note:`
            as this example.

        Example:

            >>> demo = NoteDemo([1, 2, 3, 4])
            ... demo.return_function("Hello", true)

        Args:
            param1 (str): string type parameter example.
            param2 (bool): bool type parameter example.

        Returns:
            bool: True if yes, False if no.

        Raises:
            None.
        """
        pass

    def yield_function(self, param1, param2):
        r"""Show how to write notes when you are ready to write a function with yield.

        Please follow these standard to finish your code.

        Args:
            param1 (int): int type parameter
            param2 (list): list tpye parameter

        Returns:
            (bool, int): a bool and an int.
            
        Yields:
            (string, torch.Tensor): Tuple containing a string type and a tensor type.
        """
        pass