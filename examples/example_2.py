from pwdgenerator import Generator
from rich.table import Table
from rich.console import Console

ENG_UPPER = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ENG_LOWER = list('abcdefghijklmnopqrstuvwxyz')
RUS_UPPER = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
RUS_LOWER = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
DIGITS = list('0123456789')
SYMBOLS = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*']

console = Console()


def main():
    ID = console.input('Введите идентификатор пользователя: ')
    N = len(ID)

    console.print(f'Идентификатор пользователя [magenta]{ID}[/magenta]')
    console.print(f'Длина идентификатора пользователя [magenta]{N}[/magenta]')

    passwords, variants = [], dict(
        zip(tuple(range(1, 28 + 1)), (list() for _ in range(1, 28 + 1))))

    # Вариант 1
    variants[1].extend([
        *[ENG_UPPER] * 2,
        [str(N ** 2 % 10)],
        DIGITS,
        SYMBOLS,
        ENG_LOWER
    ])

    # Вариант 2
    variants[2].extend([
        *[ENG_LOWER] * 3,
        *[ENG_UPPER] * 2
    ])
    Q = str(N ** 4 % 100)
    if len(Q) >= 2:
        variants[2].extend([[Q[0]], [Q[1]]])
    else:
        variants[2].extend([['0'], [Q]])

    # Вариант 3
    P = N ** 2 % 10 + N ** 3 % 10 + 1
    variants[3].extend([
        *[DIGITS] * 3,
        *[SYMBOLS] * 2,
        ENG_UPPER,
        ENG_UPPER,
        [ENG_LOWER[P - 1]]
    ])

    # Вариант 4
    Q = N % 5
    for _ in range(1, Q + 1 + 1):
        variants[4].append(SYMBOLS)
    for _ in range(Q + 1 + 1, 8 + 1):
        variants[4].append(ENG_LOWER)
    variants[4].append(DIGITS)

    # Вариант 5
    Q = N % 6
    variants[5].extend([
        *[ENG_UPPER] * 2
    ])
    for _ in range(3, 10 - Q - 1 + 1):
        variants[5].append(ENG_LOWER)
    for _ in range(10 - Q, 11):
        variants[5].append(DIGITS)

    # Вариант 6
    Q = N % 8
    variants[6].extend([
        *[DIGITS] * 2
    ])
    for _ in range(3, Q + 3 + 1):
        variants[6].append(ENG_UPPER)
    for _ in range(Q + 3 + 1, 11 + 1):
        variants[6].append(SYMBOLS)

    # Вариант 7
    Q = N % 8
    variants[7].extend([
        *[DIGITS] * 2
    ])
    for _ in range(3, Q + 3 + 1):
        variants[7].append(RUS_LOWER)
    for _ in range(Q + 3 + 1, 11 + 1):
        variants[7].append(SYMBOLS)

    # Вариант 8
    Q = N ** 3 % 5
    P = N ** 2 % 6
    for _ in range(1, Q + 1 + 1):
        variants[8].append(ENG_LOWER)
    for _ in range(Q + 1 + 1, Q + 1 + 1 + P + 1):
        variants[8].append(ENG_UPPER)
    for _ in range(Q + 1 + 1 + P + 1, 12 + 1):
        variants[8].append(DIGITS)

    # Вариант 9
    Q = N ** 3 % 5
    P = N ** 2 % 6
    for _ in range(1, Q + 1 + 1):
        variants[9].append(RUS_LOWER)
    for _ in range(Q + 1 + 1, Q + 1 + 1 + P + 1):
        variants[9].append(RUS_UPPER)
    for _ in range(Q + 1 + 1 + P + 1, 12 + 1):
        variants[9].append(DIGITS)

    # Вариант 10
    Q = N % 6
    variants[10].extend([
        *[RUS_UPPER] * 2
    ])
    for _ in range(3, 10 - Q - 1 + 1):
        variants[10].append(RUS_LOWER)
    for _ in range(10 - Q - 1 + 1, 10 + 1):
        variants[10].append(DIGITS)

    # Вариант 11
    Q = N % 5
    for _ in range(1, Q + 1 + 1):
        variants[11].append(SYMBOLS)
    for _ in range(Q + 1 + 1, 8 + 1):
        variants[11].append(RUS_LOWER)
    variants[11].append(DIGITS)

    # Вариант 12
    P = N ** 2 % 15 + N ** 3 % 15 + 1
    variants[12].extend([
        *[DIGITS] * 3,
        *[SYMBOLS] * 2,
        RUS_UPPER,
        RUS_UPPER,
        [RUS_LOWER[P - 1]]
    ])

    # Вариант 13
    variants[13].extend([
        *[RUS_LOWER] * 3,
        *[RUS_UPPER] * 2
    ])
    Q = str(N ** 4 % 100)
    if len(Q) >= 2:
        variants[13].extend([[Q[0]], [Q[1]]])
    else:
        variants[13].extend([['0'], [Q]])

    # Вариант 14
    variants[14].extend([
        *[RUS_UPPER] * 2,
        [str(N ** 2 % 10)],
        DIGITS,
        SYMBOLS,
        RUS_LOWER
    ])

    # Вариант 15
    variants[15].extend([
        *[ENG_UPPER] * 2,
        [str(N ** 2 % 10)],
        DIGITS,
        SYMBOLS,
        RUS_LOWER
    ])

    # Вариант 16
    variants[16].extend([
        *[RUS_LOWER] * 3,
        *[ENG_UPPER] * 2
    ])
    Q = str(N ** 4 % 100)
    if len(Q) >= 2:
        variants[16].extend([[Q[0]], [Q[1]]])
    else:
        variants[16].extend([['0'], [Q]])

    # Вариант 17
    P = N ** 2 % 10 + N ** 3 % 10 + 1
    variants[17].extend([
        *[DIGITS] * 3,
        *[SYMBOLS] * 2,
        ENG_UPPER,
        ENG_UPPER,
        [RUS_LOWER[P - 1]]
    ])

    # Вариант 18
    Q = N % 5
    for _ in range(1, Q + 1 + 1):
        variants[18].append(DIGITS)
    for _ in range(Q + 1 + 1, 8 + 1):
        variants[18].append(ENG_LOWER)
    variants[18].append(DIGITS)

    # Вариант 19
    Q = N % 6
    variants[19].extend([
        *[ENG_UPPER] * 2
    ])
    for _ in range(3, 10 - Q - 1 + 1):
        variants[19].append(RUS_LOWER)
    for _ in range(10 - Q - 1 + 1, 10 + 1):
        variants[19].append(DIGITS)

    # Вариант 20
    Q = N % 8
    variants[20].extend([
        *[SYMBOLS] * 2
    ])
    for _ in range(3, Q + 3 + 1):
        variants[20].append(ENG_UPPER)
    for _ in range(Q + 3 + 1, 11 + 1):
        variants[20].append(DIGITS)

    # Вариант 21
    Q = N % 8
    variants[21].extend([
        *[SYMBOLS] * 2
    ])
    for _ in range(3, Q + 3 + 1):
        variants[21].append(RUS_LOWER)
    for _ in range(Q + 3 + 1, 11 + 1):
        variants[21].append(DIGITS)

    # Вариант 22
    Q = N ** 3 % 5
    P = N ** 2 % 6
    for _ in range(1, Q + 1 + 1):
        variants[22].append(RUS_LOWER)
    for _ in range(Q + 1 + 1, Q + 1 + 1 + P + 1):
        variants[22].append(ENG_UPPER)
    for _ in range(Q + 1 + 1 + P + 1, 12 + 1):
        variants[22].append(DIGITS)

    # Вариант 23
    Q = N ** 3 % 5
    P = N ** 2 % 6
    for _ in range(1, Q + 1 + 1):
        variants[23].append(ENG_LOWER)
    for _ in range(Q + 1 + 1, Q + 1 + 1 + P + 1):
        variants[23].append(RUS_UPPER)
    for _ in range(Q + 1 + 1 + P + 1, 12 + 1):
        variants[23].append(DIGITS)

    # Вариант 24
    Q = N % 6
    variants[24].extend([
        *[ENG_UPPER] * 2
    ])
    for _ in range(3, 10 - Q - 1 + 1):
        variants[24].append(RUS_LOWER)
    for _ in range(10 - Q - 1 + 1, 10 + 1):
        variants[24].append(DIGITS)

    # Вариант 25
    Q = N % 5
    for _ in range(1, Q + 1 + 1):
        variants[25].append(DIGITS)
    for _ in range(Q + 1 + 1, 8 + 1):
        variants[25].append(RUS_LOWER)
    variants[25].append(SYMBOLS)

    # Вариант 26
    P = N ** 2 % 15 + N ** 3 % 15 + 1
    variants[26].extend([
        *[DIGITS] * 3,
        *[SYMBOLS] * 2,
        ENG_UPPER,
        ENG_UPPER,
        [RUS_LOWER[P - 1]]
    ])

    # Вариант 27
    variants[27].extend([
        *[RUS_LOWER] * 3,
        *[ENG_UPPER] * 2
    ])
    Q = str(N ** 4 % 100)
    if len(Q) >= 2:
        variants[27].extend([[Q[0]], [Q[1]]])
    else:
        variants[27].extend([['0'], [Q]])

    # Вариант 28
    variants[28].extend([
        *[ENG_UPPER] * 2,
        [str(N ** 2 % 10)],
        DIGITS,
        SYMBOLS,
        RUS_LOWER
    ])

    # Генерация паролей

    for variant in variants.values():
        passwords.append(Generator.generate_by_templates(variant))

    # for i in range(1, len(variants) + 1):
    #     print('')
    #     print(f'Вариант {i}')
    #     for row in variants[i]:
    #         print(row)

    table = Table(show_header=True,
                  header_style='bold magenta', show_lines=True)

    table.add_column('Вариант')
    table.add_column('Пароль')
    table.add_column('Длина пароля')

    for index, password in enumerate(passwords):
        table.add_row(
            str(index + 1),
            str(password),
            str(len(password))
        )

    console.print(table)


if __name__ == '__main__':
    while(True):
        main()
        console.input('Продолжить...')
