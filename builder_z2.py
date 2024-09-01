# """Задача 2 (Билдер без строителя)"""
#
# from enum import Enum, auto
#
#
# """Классы по содержанию типов пасты, соусов и начинки"""
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
# """Класс компонуемого продукта"""
#
#
# class Pasta:
#     def __init__(self, builder):
#         self.name = builder.name
#         self.type = builder.type
#         self.sauce = builder.sauce
#         self.filling = builder.filling
#         self.additives = builder.additives
#         self.cooking_time = builder.cooking_time
#
#     def __str__(self):
#         info: str = (f'Название пасты: {self.name} \n'
#                      f'Тип пасты: {self.type} \n'
#                      f'Соус для пасты: {self.sauce} \n'
#                      f'Начинка для пасты: {self.filling} \n'
#                      f'Добавки для пасты: {self.additives} \n'
#                      f'Время приготовления: {self.cooking_time} \n')
#         return info
#
#     @staticmethod
#     def getBuilder():
#         return _Builder()
#
# """Реализация строителя (шеф-повара) для сборки пасты"""
#
# class _Builder:
#     def set_name(self, name: str):
#         self.name = name
#
#     def set_type(self, type: PastaType):
#         self.type = type
#
#     def set_sauce(self, sauce: PastaSauсe):
#         self.sauce = sauce
#
#     def set_filling(self, filling: PastaFilling):
#         self.filling = filling
#
#     def set_additives(self, additives: PastaAdditives):
#         self.additives = additives
#
#     def set_cooking_time(self, cooking_time: int):
#          self.cooking_time = cooking_time
#
#     def build(self):
#         return Pasta(self)
#
#
# """Готовим пасту"""
#
# if __name__ == '__main__':
#
#     builder = Pasta.getBuilder()
#     builder.set_name('Карбонара')
#     builder.set_type(PastaType.SPAGHETTI)
#     builder.set_sauce(PastaSauсe.PESTO)
#     builder.set_filling(PastaFilling.BACON)
#     builder.set_additives(PastaAdditives.CHEESE)
#     builder.set_cooking_time(15)
#     all_pasta = builder.build()
#     print(all_pasta)