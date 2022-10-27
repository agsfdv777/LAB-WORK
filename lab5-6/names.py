class Name:
    def __init__(self, name:str,hobby:str) -> None:
        if name not in ["Богдан", "Астроном"]:
            raise ValueError(f"Я тобі не {name}!")
        if not hobby is str:
              raise AttributeError(f"Ти нероба!")
          
        self.name = name
        self.hobby = hobby


a = Name("Астроном",4)
