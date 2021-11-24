from koans_plugs import *


def test_create():
    """
        Множество в python содержат не повторяющиеся элементы.

        Создать множество можно через функцию set(), передав в неё любую последовательность,
        или заключив последовательность в фиурные скобки {1, 2, 3}.

        P.S пустое множество невозможно создать как {}, так-как синтаксис совпадёт с созданием словаря.
    """

    my_set =  set()  # попробуйте такие варианты: set(), {1, 2, 3}, {'qwerty'}, set((1, 2, 3))
    assert isinstance(my_set, set)


def test_create_from_string():
    """
        При создании множества все элементы будут уникальными.
        Создать множество уникальных букв из строки легко через функцию set():

        >>> set('qwerty') == {'q', 'w', 'e', 'r', 't', 'y'}
        True
    """
    my_set = set('Hello, world!')  # попробуйте такие варианты: set('Hello!'), set('Hello, world!')
    assert {'H', 'e', 'l', 'o', 'w', 'r', 'd', '!', ',', ' '} == my_set


def test_words_in_set():
    """
        Множества могут содержать не только цифры и буквы.
    """
    my_set = {True, 'set', 2}  # попробуйте такие варианты: {True, 'set', 2}, {'cow', 'fox', 'cat'}
    assert isinstance(my_set, set)


def test_operator_len():
    """
        У множества есть длина.

        len({"Множество"})
    """
    my_set = {0, 1, 2, 3, 4, 5}
    set_len = 6  # попробуйте такие варианты: 5, 6, 7
    assert len(my_set) == set_len


def test_operator_in():
    """
        Проверить вхождение элемента в множество можно с помощью оператора in

        "Элемент" in {"Множество"}
    """
    my_set = {'cow', 'fox', 'cat'}
    current_element = 'cow'  # попробуйте такие варианты: 'cow', 1, True
    assert current_element in my_set


def test_union():
    """
        Множества можно объединять.

        "Множество  AB" = "Множество A" | "Множество B"
    """
    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}
    set_union = set_A | set_B
    assert set_union == {1, 2, 3, 4, 5, 6, 7, 8}


def test_intersection():
    """
        Пересечение — это операция выделения общих элементов множеств.

        "Множество  AB" = "Множество A" & "Множество B"
    """
    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}
    set_intersection = set_A & set_B
    assert set_intersection == {4,5}


def test_difference():
    """
         Разница — это операция выделения элементов, которых нет в другом множестве.

        "Множество  A-B" = "Множество A" - "Множество B"
    """
    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}
    set_difference = set_A - set_B
    assert set_difference == {1, 2, 3}


def test_multi_difference():
    """
         Разница, объединение и пересечение можно компоновать в строке.

         "Множество  A-B-C" = "Множество A" - "Множество B" - "Множество C"
    """
    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}
    set_C = {1, 2}
    set_difference = set_A - set_B - set_C
    assert set_difference == {3}


def test_duplicate_removal():
    """
        Очень часто множества используют для удаления дублей из списка путём преобразования.

        "Список уникальных элементов" = list(set("Список элементов")).
        Здесь важно применить сортировку к спискам перед сравнением, функцией sorted().
        Иначе легко проверить, что для сравнения списков учитывается порядок эл-тов.

        >>> [1, 2] == [1, 2]
        True
        >>> [1, 2] != [2, 1]
        True
    """
    my_duplicated_list = ['cow', 'cat', 'cat', 'dog', 'cat', 'cow']
    my_unique_list = ['cat', 'cow', 'dog']  # исключите дубликаты вручную
    assert sorted(my_unique_list) == sorted(list(set(my_duplicated_list)))


def test_list_in_set():
    """
        Множество содержит в себе набор уникальных элементов. Их уникальность определяется специальной функцией __hash__,
        содержащейся в типе данных. Проверить наличие данной функции можно командой hash().

        Если у типа нет функции, то при добавлении в множество будет вызванно исключение.
    """
    my_set = {1, (1, 2, 3)} # попробуйте такие варианты: {1, [1, 2, 3]}, {1, (1, 2, 3)}, {1, {'a': 1, 'b': 2}}
    assert isinstance(my_set, set)