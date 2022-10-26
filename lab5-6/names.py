class Name:
    def __init__(self, name) -> None:
        if name not in ["Богдан", "Астроном"]:
            raise ValueError(f"Я тобі не {name}!")
        self.name = name


a = Name("Павук")
