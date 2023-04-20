import unittest

from buffers import BufferNew


class TestBuffer(unittest.TestCase):

    def setUp(self) -> None:
        self.buffer_new = BufferNew(4)
        self.buffer_full = BufferNew(4)
        self.buffer_full.add_item(1)
        self.buffer_full.add_item(2)
        self.buffer_full.add_item(3)
        self.buffer_full.add_item(4)

    def test_buffer_is_empty(self):
        self.assertTrue(self.buffer_new._buffer_is_empty())
        self.assertFalse(self.buffer_full._buffer_is_empty())

    def test_buffer_is_full(self):
        self.assertTrue(self.buffer_new._buffer_is_empty())
        self.assertTrue(self.buffer_full._is_full_buffer())

    def test_add_item(self):
        self.buffer_full.add_item(5)
        self.buffer_new.add_item(1)
        buffer_full = self.buffer_full.get_buffer()
        buffer_new = self.buffer_new.get_buffer()
        self.assertEqual(buffer_full, [5, 4, 3, 2])
        self.assertEqual(buffer_new, [1, None, None, None])

    def test_del_item_info(self):
        self.assertEqual(self.buffer_full.del_item_info(), 1)
        self.assertEqual(self.buffer_new.del_item_info(), BufferNew.MESSAGE_IF_EMPTY)

    def test_take_item(self):
        self.assertEqual(self.buffer_full.take_item(), 1)
        self.assertEqual(self.buffer_new.take_item(), BufferNew.MESSAGE_IF_EMPTY)


if __name__ == '__main__':
    unittest.main()
