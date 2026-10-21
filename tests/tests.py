import unittest
from main.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_cp1_un_elemento(self):
        # Arrange
        vet = [7]

        # Act
        bubble_sort(vet)

        # Assert
        self.assertEqual(vet, [7])

    def test_cp2_sin_intercambio(self):
        # Arrange
        vet = [1, 2]

        # Act
        bubble_sort(vet)

        # Assert
        self.assertEqual(vet, [1, 2])

    def test_cp3_un_intercambio(self):
        # Arrange
        vet = [2, 1]

        # Act
        bubble_sort(vet)

        # Assert
        self.assertEqual(vet, [1, 2])

    def test_cp4_dos_pasadas(self):
        # Arrange
        vet = [3, 1, 2]

        # Act
        bubble_sort(vet)

        # Assert
        self.assertEqual(vet, [1, 2, 3])

if __name__ == "__main__":
    unittest.main()