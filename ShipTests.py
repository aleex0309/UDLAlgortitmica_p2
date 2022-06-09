import unittest

from main import shipDetectorIterativo, image_generator
from main import shipDetectorRecursivo

class MyTestCase(unittest.TestCase):
    def test1(self):
        image= [[29, 150, 22], [244, 71, 21], [226, 229, 223]]
        detector = shipDetectorIterativo(image)
        your_solution = detector
        solution = [[0,1], [1, 0], [2,1]]

        self.assertListEqual(your_solution, solution)

    def test2(self):
        image= [[94, 15, 34], [56, 240, 141], [13, 145, 136]]
        detector = shipDetectorIterativo(image)
        your_solution = detector
        solution = [[0, 0], [1, 1]]

        self.assertListEqual(your_solution, solution)

    def test3(self):
        image = [[64, 194, 139, 216, 13, 254, 136, 253, 206, 240], [32, 161, 80, 52, 1, 162, 211, 125, 139, 234], [247, 217, 38, 189, 130, 218, 170, 203, 208, 116], [75, 4, 6, 96, 112, 7, 204, 174, 111, 37], [20, 162, 64, 7, 165, 50, 244, 154, 132, 130], [54, 44, 127, 76, 217, 51, 12, 163, 215, 92], [247, 202, 247, 92, 189, 221, 112, 191, 114, 94], [210, 104, 2, 2, 23, 202, 190, 109, 120, 23], [58, 166, 91, 143, 222, 140, 168, 19, 19, 253], [22, 236, 185, 222, 251, 194, 83, 60, 170, 118]]
        detector = shipDetectorIterativo(image)
        your_solution = detector
        solution = [[0, 1], [0, 3], [0, 5], [0, 7], [0, 9], [1, 6], [2, 0], [2, 3], [2, 5], [2, 8], [4, 1], [4, 6], [5, 4], [5, 8], [6, 0], [6, 2], [6, 5], [6, 7], [7, 8], [8, 9], [9, 1], [9, 4], [9, 8]]

        self.assertListEqual(your_solution, solution)

    def test1Recursive(self):
        image= [[29, 150, 22], [244, 71, 21], [226, 229, 223]]
        detector = shipDetectorRecursivo(image)
        your_solution = detector
        solution = [[0,1], [1, 0], [2,1]]

        self.assertListEqual(your_solution, solution)

    def test2Recursive(self):
        image= [[94, 15, 34], [56, 240, 141], [13, 145, 136]]
        detector = shipDetectorRecursivo(image)
        your_solution = detector
        solution = [[0, 0], [1, 1]]

        self.assertListEqual(your_solution, solution)

    def test3Recursive(self):
        image = [[64, 194, 139, 216, 13, 254, 136, 253, 206, 240], [32, 161, 80, 52, 1, 162, 211, 125, 139, 234], [247, 217, 38, 189, 130, 218, 170, 203, 208, 116], [75, 4, 6, 96, 112, 7, 204, 174, 111, 37], [20, 162, 64, 7, 165, 50, 244, 154, 132, 130], [54, 44, 127, 76, 217, 51, 12, 163, 215, 92], [247, 202, 247, 92, 189, 221, 112, 191, 114, 94], [210, 104, 2, 2, 23, 202, 190, 109, 120, 23], [58, 166, 91, 143, 222, 140, 168, 19, 19, 253], [22, 236, 185, 222, 251, 194, 83, 60, 170, 118]]
        detector = shipDetectorRecursivo(image)
        your_solution = detector
        solution = [[0, 1], [0, 3], [0, 5], [0, 7], [0, 9], [1, 6], [2, 0], [2, 3], [2, 5], [2, 8], [4, 1], [4, 6], [5, 4], [5, 8], [6, 0], [6, 2], [6, 5], [6, 7], [7, 8], [8, 9], [9, 1], [9, 4], [9, 8]]

        self.assertListEqual(your_solution, solution)

if __name__ == '__main__':
    unittest.main()