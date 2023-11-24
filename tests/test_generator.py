
from generator import Generator_example


def test_get_row():
    reader = Generator_example()

    output = list(reader.get_row('/Users/peter/PycharmProjects/PyhtonInterview/username.csv'))

    assert output == ['Username,Identifier,First name,Last name\n', 'booker12,9012,Rachel,Booker\n', 'grey07,2070,Laura,Grey\n', 'johnson81,4081,Crai,Johnson\n', 'jenkins46,9346,Mary,Jenkins\n', 'smith,7079,Jamie,Smith']


def test_infinite_sequence():
    reader = Generator_example()
    gen = reader.infinite_sequence()

    output = [next(gen) for i in range(5)]

    assert output == [0, 1, 2, 3, 4]


def test_get_rows_numbered():
    reader = Generator_example()

    output = reader.get_rows_numbered('/Users/peter/PycharmProjects/PyhtonInterview/username.csv')

    assert output == [
        (0, 'Username,Identifier,First name,Last name\n'),
        (1, 'booker12,9012,Rachel,Booker\n'),
        (2, 'grey07,2070,Laura,Grey\n'),
        (3, 'johnson81,4081,Crai,Johnson\n'),
        (4, 'jenkins46,9346,Mary,Jenkins\n'),
        (5, 'smith,7079,Jamie,Smith'),
    ]
