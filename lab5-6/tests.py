import unittest
from random import choice, randint

from figures import Figure


class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Виконається лише раз на початку тестів
        """
        pass

    def setUp(self) -> None:
        """Виконується кожного разу коли запускається тест
        """
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(
            f"Тестуємо вивід, має бути: {self.figure} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure, self.obj.get_figure_type,
                         "Властивість get_figure_type повертає непривильну фігуру!")

    def test_figure_lengh(self):
        self.assertEqual(self.length, self.obj.get_figure_length,
                         "Властивість get_figure_length повертає непривильну довжину!")

    def test_obj(self):
        with self.assertRaises(AssertionError):
            # Спробуємо створити обєкт з недозволеними параметрими, в нас має
            # бути помилка AssertionError
            Figure("коло", 1)

    def test_area(self):
        triangle = Figure("трикутник", 4)
        self.assertAlmostEqual(triangle.get_figure_area, 6.928203230275509)

        square = Figure("квадрат", 4)
        self.assertEqual(square.get_figure_area, 16)

        # поки що прямокутник буде представлений лише квадратом
        rectangle = Figure("прямокутник", 4)
        self.assertEqual(rectangle.get_figure_area, 16)


if __name__ == '__main__':
    unittest.main()  # unittest.main(verbosity=2) щоб був більш детальний вивід
