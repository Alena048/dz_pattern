# import copy
#
# class Publishing_house:
#     def __init__(self, publisher: str, city: str):
#         self.publisher = publisher
#         self.city = city
#
# class Book:
#     def __init__(self, name_book: str, author: str, number_pages: int, publishing_house):
#         self.name_book = name_book
#         self.autor = author
#         self.number_pages = number_pages
#         self.publishing_house = publishing_house
#
#     def clone(self):
#         return copy.deepcopy(self)
#
#     def __str__(self):
#         return (f'Наименование книги: {self.name_book} \n'
#                 f'Автор: {self.autor} \n'
#                 f'Количество страниц: {self.number_pages} \n'
#                 f'Издательство: {self.publishing_house.publisher} \n'
#                 f'Город: {self.publishing_house.city} \n')
#
# book_one = Book("Сказки", "А.С. Пушкин", 50, Publishing_house("Ромашка", "Москва"))
# print(book_one)
# book_two = book_one.clone()
# book_two.autor = "В.А.Жуковский"
# book_two.number_pages = 55
# print(book_two)
