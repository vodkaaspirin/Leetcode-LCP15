import unittest
from src.main import find_path

class TestFindPath(unittest.TestCase):
    def test_example_1(self):
        points = [[1,1], [1,4], [3,2], [2,1]]
        direction = "LL"
        result = find_path(points, direction)
        self.assertIsNotNone(result)
    
    def test_example_2(self):
        points = [[1,3], [2,4], [3,3], [2,1]]
        direction = "LR"
        result = find_path(points, direction)
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
