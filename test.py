from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

#     # пример теста:
#     # обязательно указывать префикс test_
#     # дальше идет название метода, который тестируем add_new_book_
#     # затем, что тестируем add_two_books - добавление двух книг
#     def test_add_new_book_add_two_books(self):
#         # создаем экземпляр (объект) класса BooksCollector
#         collector = BooksCollector()

#         # добавляем две книги
#         collector.add_new_book('Гордость и предубеждение и зомби')
#         collector.add_new_book('Что делать, если ваш кот хочет вас убить')

#         # проверяем, что добавилось именно две
#         # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
#         assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    #добавление книги
    def test_add_new_book_without_genre_successfully(self,books_collector):
            books_collector.add_new_book('BookOfbook')
            result = {'BookOfbook':''}
            assert books_collector.get_books_genre() == result
    
    def test_add_2_new_book_without_genre_successfully(self,books_collector):
            books_collector.add_new_book('BookOfbook')
            books_collector.add_new_book('BookOfbook2')
            result = {'BookOfbook':'','BookOfbook2': ''}
            assert books_collector.get_books_genre() == result
    
    @pytest.mark.parametrize('name', ['F', 'FF', '123456789012345678901234567890123456789','1234567890123456789012345678901234567890'])
    def test_add_new_book_without_genre_len_name_positive_successfully(self, name,books_collector):
        books_collector.add_new_book(name)
        assert books_collector.get_book_genre(name) == ''

    @pytest.mark.parametrize('name', ['', '12345678901234567890123456789012345678901'])
    def test_add_new_book_without_genre_len_name_negative_is_impossible(self, name,books_collector):
        books_collector.add_new_book(name)
        assert not books_collector.get_book_genre(name) == ''
    
    def test_add_two_similar_book_is_impossible(self,books_collector):
        books_collector.add_new_book('Book')
        books_collector.add_new_book('Book')
        assert not len(books_collector.get_books_genre()) == 2 #ок
    


#установка жанра 
    def test_set_book_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Book')
        collector.set_book_genre('Book', 'Фантастика')
        assert collector.books_genre['Book'] == 'Фантастика' #ок

    def test_set_book_genre_which_doesnt_exist_in_list_is_impossible(self):
          collector = BooksCollector()
          collector.add_new_book('Book')
          collector.set_book_genre('Book', 'Ааа')
          
          assert not  collector.books_genre['Book'] == 'Ааа' #ок
   

    # выводит жанр книги по её имени.
    def test_get_book_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Book')
        collector.set_book_genre('Book', 'Фантастика')
        assert collector.get_book_genre('Book') == 'Фантастика'
    
    def test_get_book_empty_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Book')
        assert collector.get_book_genre('Book') == ''

    # выводит список книг с определённым жанром.
    def test_get_book_with_specific_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Book')
        collector.set_book_genre('Book', 'Фантастика')
        collector.add_new_book('Book1')
        collector.set_book_genre('Book1', 'Ужасы')
        excepted_result = ['Book']
        assert excepted_result == collector.get_books_with_specific_genre ('Фантастика')
    
        
    #выводит текущий словарь books_genre.
    def test_get_list_books_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Book')
        collector.set_book_genre('Book', 'Фантастика')
        expected_result = {'Book': 'Фантастика'}
        assert collector.get_books_genre() == expected_result

    def test_get_empty_list_books_genre_successfully(self):
        collector = BooksCollector()
        expected_result = {}
        assert collector.get_books_genre() == expected_result
    

        
    # возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга.
    
    def test_get_books_for_children_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Человек-Паук')
        collector.set_book_genre('Человек-Паук', 'Мультфильмы')   
        expected_result = ['Человек-Паук']
        assert collector.get_books_for_children()  == expected_result
    
    
    def test_get_books_for_children_is_impossible(self):
        collector = BooksCollector()
        collector.add_new_book('Звонок')
        collector.set_book_genre('Звонок', 'Ужасы')  
        expected_result = []
        assert  collector.get_books_for_children() ==  expected_result

    #добавить книгу в избранное
    #добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя.
   
    def test_add_book_in_favorites_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Book')
        collector.add_book_in_favorites('Book')
        expected_result = ['Book']
        assert collector.get_list_of_favorites_books() == expected_result

    
    def test_add_book_in_favorites_but_book_not_in_list_is_failed(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Book')
        expected_result = 0
        assert  len(collector.favorites) == expected_result
    
    
    def test_add_1_book_2_times_in_favorites_is_failed(self):
        collector = BooksCollector()
        collector.add_new_book('Book')
        collector.add_book_in_favorites('Book')
        collector.add_book_in_favorites('Book')
        expected_result = ['Book']
        assert collector.get_list_of_favorites_books() == expected_result
    

   
    # удаляет книгу из избранного, если она там есть.
    
    def test_delete_book_from_favorites_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Book')
        collector.add_book_in_favorites('Book')
        collector.delete_book_from_favorites('Book')
        expected_result = []
        assert collector.get_list_of_favorites_books() == expected_result
    
    def test_delete_book_from_favorites_if_not_exists_in_favorites_list(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('book')
        expected_result = []
        assert collector.get_list_of_favorites_books() == expected_result
    
    # получает список избранных книг.
    @pytest.mark.parametrize('name,genre', [['Book', 'Фантастика']])
    def test_get_list_of_favorites_books_successfully(self,name,genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre) 
        collector.add_book_in_favorites(name)
        result = collector.get_list_of_favorites_books()  
        expected_result = ['Book']  
        assert result == expected_result
    
    
