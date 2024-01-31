# qa_python
# qa_python

Класс для тестирования - BooksCollector

Класс BooksCollector содержит:

1. Словарь:
   books_genre со значениями в формате Название книги: Жанр книги
2. Списки:
    Избранные книги - favorites
    Жанры - genres
    Жанры по возрастному рейтингу - self.genre_age_rating
3. Методы:
    add_new_book - Добавление книги в словарь без указания жанра 
    set_book_genre - Устанавливает жанр книги
    get_book_genre - Выводит жанр книги по её имени
    get_book_with_specific_genre - Выводит список книг с определенным жанром
    get_list_books_genre - Выводит текущий словарь books_genre
    get_books_for_children - Возвращает книги для детей 
    add_book_in_favorites - Добваляет книгу в список Избранное 
    delete_book_from_favorites - Удаляет книгу из списка Избранное
    get_list_of_favorites_books - Получает из списка Избранное список книг 


На каждый метод были написаны тесты:
add_new_book - 9 тестов
set_book_genre - 2 теста
get_book_genre - 2 теста
get_book_with_specific_genre - 1 тест
get_list_books_genre - 2 теста 
get_books_for_children - 2 теста
add_book_in_favorites - 3 теста 
delete_book_from_favorites - 2 теста 
get_list_of_favorites_books - 1 тест 

Общее количество 24 теста 

В тестах используются методы @pytest.mark.parametrize, @pytest.fixture 
Фикстура находится в файле fixture.py


Информация о заруске: 

Запуск всех тестов. 
pytest-v test_tests.py

Запуск оценки покрытия 
pytest --Cov=main

Запус с подробной оценкой покрытия
pytest --cov=main --cov-report=html   
(смотреть файл main_py.html после запуска)

