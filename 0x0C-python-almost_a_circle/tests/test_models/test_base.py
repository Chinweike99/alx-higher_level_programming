import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        b = Base()
        self.assertEqual(b.id, 1)

        b2 = Base(100)
        self.assertEqual(b2.id, 100)
    def test_to_json_string(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

        json_str = Base.to_json_string([{'id': 1, 'name': 'John'}])
        self.assertEqual(json_str, '[{"id": 1, "name": "John"}]')

if __name__ == '__main__':
    unittest.main()
