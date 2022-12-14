from math import sqrt


class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        # return self.type # робимо помилку
        return self.length

    @property
    def get_figure_area(self):
        area = 0

        match self.type:
            case "квадрат":
                area = self.length * self.length
            case "прямокутник":
                # поки що беремо квадрат, щоб не ламати зворотню сумісність
                area = self.length * self.length
            case "трикутник":
                area = self.length * self.length * sqrt(3) / 4
            case _:
                pass

        return area


def test_app_triangle():
    """Test if we create triangle figure.
    """
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.type == fig, f"Фігура має бути {fig}"
