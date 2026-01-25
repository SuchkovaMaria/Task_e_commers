class MixinPrint:
    """Класс определяющий вывод информации о параметрах созданного экземпляра (другого класса)"""

    def __init__(self):
        """Вывод информации при создании экземпляра класса"""
        print(repr(self))

    def __repr__(self):
        """Dывод информации о параметрах экземпляра"""

        self_parameters = ""
        for v in self.__dict__.values():
            self_parameters += "," + " " + str(v)
        return f"{self.__class__.__name__}, {self_parameters}"
