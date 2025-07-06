import pytest 
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_initial_state(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {} and collector.get_list_of_favorites_books() == []

    def test_add_new_book_correct_add_book_successful_add(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert collector.get_book_genre('Гарри Поттер') == ''

    @pytest.mark.parametrize("name, expected_count", [
        ('Гарри Поттер', 1),
        ('', 0),
        ('Гарри Поттер' * 10, 0)
    ])
    def test_add_new_book_incorrect_add_book_unsuccessful_add(self, name, expected_count):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == expected_count

    def test_set_book_genre_correct_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Ужасы')
        assert collector.books_genre['Гарри Поттер'] == 'Ужасы'

    def test_set_book_genre_incorrect_genre_unsuccess(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'FFFFFF')
        assert collector.books_genre['Гарри Поттер'] == ''

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Ужасы')
        assert collector.get_book_genre('Гарри Поттер') == 'Ужасы'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        books = ['Гарри Поттер', 'Война и мир', 'Вишневый сад']
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Ужасы')
        
        collector.add_new_book('Незнайка на луне')
        collector.set_book_genre('Незнайка на луне', 'Мультфильмы')

        assert collector.get_books_with_specific_genre('Ужасы') == books

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert collector.get_books_genre() == {'Гарри Поттер': ''}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Детская')
        collector.add_new_book('Взрослая')
        collector.set_book_genre('Детская', 'Фантастика')
        collector.set_book_genre('Взрослая', 'Ужасы')

        assert collector.get_books_for_children() == ['Детская']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Война и мир')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер', 'Война и мир']

