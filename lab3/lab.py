class MyName:
    """class describtion /documentation
    """
    total_names = 0  # Class Variable
    __anonymous_name = "Anonymous"

    def __init__(self, name=None) -> None:
        MyName.total_names += 1  # modify class variable
        # Class attributes / Instance variables
        self.name = name if name is not None else self.__anonymous_name
        self.my_id = self.total_names

    @property
    def whoami(self):
        """Class property
        return: name
        """
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property
        return: email
        """
        return self.create_email()

    def create_email(self) -> str:
        """Instance method
        """
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls(cls.__anonymous_name)

    @staticmethod
    def say_hello(message="Hello to everyone!"):
        """Static method
        """
        return f"You say: {message}"

    def __len__(self) -> str:
        """Class property
        return: name.len()
        """
        return len(self.name)


print("Let's Start!")

names = ("Bogdan", "Notbogdan", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(name, " ", me.name)
    print(f"""{">*<"*20}

This is object: {me}
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello("f*ck you, Nvidia")}
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")

# class variable is 4 because objects are created before the cycle

print(
    f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")
print(len(me))  # Anonymous
