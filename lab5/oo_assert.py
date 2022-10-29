from random import randint


class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник",
                        "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length


figure_params = [("трапеція", 12), ("квадрат", 0), ("квадрат", 1)]

params = figure_params[randint(0, 2)]

type, length = params
figure = Figure(type, length)
