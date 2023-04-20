class BufferNew:
    """
    Data structure "Circle buffer".
    It saves data to an instance of a class.
    Instance can:
    - add data and returns it
    - delete data(the oldest data) and returns it
    - returns info about the oldest data
    """

    MESSAGE_IF_EMPTY = 'Buffer is empty'

    def __init__(self, length: int) -> None:
        self._max_size = length
        self._size = 0
        self._slots = [None] * length

    def __repr__(self) -> str:
        return f'{self._slots}. size: {self._size}, max_size:{self._max_size}, delete item info: {self.del_item_info()}'

    def get_buffer(self) -> list:
        return self._slots

    def _buffer_is_empty(self) -> bool:
        """Check buffer is empty."""

        if self._size == 0:
            return True
        return False

    def _is_full_buffer(self) -> bool:
        """Check buffer is full."""

        if self._size == self._max_size:
            return True
        return False

    def add_item(self, item: any) -> any:
        """
        Add item in Buffer.
        :param item: Any data
        """

        new_item = self._slots.insert(0, item)
        self._slots = self._slots[:self._max_size]
        if not self._is_full_buffer():
            self._size += 1
        return new_item

    def del_item_info(self):
        """
        Returns info about the oldest data.
        """

        if self._buffer_is_empty():
            return self.MESSAGE_IF_EMPTY
        if self._is_full_buffer():
            return self._slots[-1]
        return self._slots[self._size - 1]

    def take_item(self) -> any:
        """
        Takes the oldest data from the buffer
        :return:
        oldest data
        """

        if self._buffer_is_empty():
            return self.MESSAGE_IF_EMPTY
        if self._is_full_buffer():
            del_item = self._slots[-1]
            self._slots[-1] = None
        else:
            del_item = self._slots[self._size - 1]
            self._slots[self._size - 1] = None
        self._size -= 1
        return del_item
