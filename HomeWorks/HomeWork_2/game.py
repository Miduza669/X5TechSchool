# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle
import random

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This function is used to create a field at the very start of the game.

    :return: list with 16 randomly shuffled tiles,
        one of which is a empty space.
    """
    field_list = list(range(1, 16))
    field_list.append(EMPTY_MARK)

    # Простая реализация перемешивания, котороя не гарантирует возможность положительного завершения игры
    # random.shuffle(field_list)

    """
    Альтернативный алгоритм перемешивания полей который гарантирует возможность положительного завершения игры
    Генериуем 200 случайных ходов от эталонного состояния поля
    Так можно реализовать несколько уровней сложности игры в зависимости от глубины перемешивания
    """
    for i in range(0, 200):
        try:
            k = random.choice(list(MOVES.keys()))
            perform_move(field_list, k)
        except IndexError:
            continue
    return field_list


def print_field(field):
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """
    print("\t".join(map(str, field[0:4])))
    print("\t".join(map(str, field[4:8])))
    print("\t".join(map(str, field[8:12])))
    print("\t".join(map(str, field[12:16])))


def is_game_finished(field):
    """
    This function checks if the game is finished.

    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    goal_list = list(range(1, 16))
    goal_list.append(EMPTY_MARK)
    return goal_list == field


def perform_move(field, key):
    """
    Moves empty-tile inside the field.

    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    errors_dict = {'w': [0, 1, 2, 3],
                   's': [12, 13, 14, 15],
                   'a': [0, 4, 8, 12],
                   'd': [3, 7, 11, 15]}
    current_empty_index = field.index(EMPTY_MARK)
    if current_empty_index in list(errors_dict[key]):
        raise IndexError
    else:
        field[current_empty_index] = field[current_empty_index + MOVES[key]]
        field[current_empty_index + MOVES[key]] = EMPTY_MARK


def handle_user_input():
    """
    Handles user input.

    List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right

    :return: <str> current move.
    """
    move = input()
    return move if move in MOVES else False


def main():
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """
    game_field = shuffle_field()
    moves_count = 0
    while not is_game_finished(game_field):
        print_field(game_field)
        move = handle_user_input()
        if move:
            try:
                perform_move(game_field, move)
                moves_count += 1
            except IndexError:
                print('Непозволительный ход')
    print('Игра завершена за {0} ходов'.format(moves_count))
    return None


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    try:
        main()
    except KeyboardInterrupt:
        exit()
