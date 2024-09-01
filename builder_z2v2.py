# """Задача 2, вариант второй, с директором, сделала на примере твоего кода"""
#
# from enum import Enum, auto
# from abc import ABC, abstractmethod
#
#
#
# class PastaType(Enum):
#     SPAGHETTI = auto()
#     LASAGNE = auto()
#     RAVIOLI = auto()
#     PENNE = auto()
#
# class PastaSauсe(Enum):
#     TOMATO = auto()
#     CREAMY = auto()
#     PESTO = auto()
#
# class PastaFilling(Enum):
#     BACON = auto()
#     CHICKEN = auto()
#     BEEF = auto()
#     VEGAN = auto()
#
# class PastaAdditives(Enum):
#     CHEESE = auto()
#     GARLIC = auto()
#     GREENERY = auto()
#
#
# class Pasta:
#     def __init__(self, name: str):
#         self.name = name
#         self.type = None
#         self.sauce = None
#         self.filling = None
#         self.additives = None
#
#     def __str__(self):
#         info: str = (f'Название пасты: {self.name} \n'
#                      f'Тип пасты: {self.type} \n'
#                      f'Соус для пасты: {self.sauce} \n'
#                      f'Начинка для пасты: {self.filling} \n'
#                      f'Добавки для пасты: {self.additives} \n')
#         return info
#
#
#
# class IBuilder(ABC):
#
#     @abstractmethod
#     def add_type(self) -> None:
#         pass
#
#     @abstractmethod
#     def add_sauce(self) -> None:
#         pass
#
#     @abstractmethod
#     def add_filling(self) -> None:
#         pass
#
#     @abstractmethod
#     def add_additives(self) -> None:
#         pass
#
#     @abstractmethod
#     def get_pasta(self):
#         pass
#
#
# class Carbonara(IBuilder):
#
#     def __init__(self):
#         self.name = Pasta('Карбонара')
#
#     def add_type(self) -> None:
#         self.name.type = PastaType.SPAGHETTI
#
#     def add_sauce(self) -> None:
#         self.name.sauce = PastaSauсe.CREAMY
#
#     def add_filling(self) -> None:
#         self.name.filling = PastaFilling.BACON
#
#     def add_additives(self) -> None:
#         self.name.additives = PastaAdditives.CHEESE
#
#     def get_pasta(self) -> Pasta:
#         return self.name
#
#
# class Ravioli(IBuilder):
#
#     def __init__(self):
#         self.name = Pasta('Равиоли')
#
#     def add_type(self) -> None:
#         self.name.type = PastaType.RAVIOLI
#
#     def add_sauce(self) -> None:
#         self.name.sauce = PastaSauсe.TOMATO
#
#     def add_filling(self) -> None:
#         self.name.filling = PastaFilling.VEGAN
#
#     def add_additives(self) -> None:
#         self.name.additives = PastaAdditives.GREENERY
#
#     def get_pasta(self) -> Pasta:
#         return self.name
#
#
#
# class Director:
#     def __init__(self, builder: IBuilder):
#         self.builder = builder
#
#     def set_buider(self, builder):
#         self.builder = builder
#
#     def make_pasta(self):
#         self.builder.add_type()
#         self.builder.add_sauce()
#         self.builder.add_filling()
#         self.builder.add_additives()
#         return self.builder.get_pasta()
#
#
#
# carbonara = Carbonara()
# ravioli = Ravioli()
# director_one = Director(carbonara)
# director_two = Director(ravioli)
# pasta_one = director_one.make_pasta()
# pasta_two = director_two.make_pasta()
# print(pasta_one)
# print(pasta_two)
#
