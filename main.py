# импортирование библиотеки sys для выхода из игры
import sys
# импортирование главной библиотеки pygame 
import pygame as pg

# инициализация шрифта, для написания победителя
pg.font.init()
# сам шрифт
pg.display.set_caption('Шахматы')
font = pg.font.SysFont('comicsansms.ttf', 50)
# размер окна
size = (790, 790)
# отображение окна
screen = pg.display.set_mode(size)
# черный цвет
BLACK = (0, 0, 0)
# белый цвет
WHITE = (255, 255, 255)
# загружаем изображения фигур на доске
pawn_w = pg.image.load('wh pawn.png')
pawn_b = pg.image.load('bl pawn.png')
rook_w = pg.image.load('wh rook.png')
rook_b = pg.image.load('bl rook.png')
horse_w = pg.image.load('wh horse.png')
horse_b = pg.image.load('bl horse.png')
elephant_w = pg.image.load('wh elephant.png')
elephant_b = pg.image.load('bl elephant.png')
queen_w = pg.image.load('wh queen.png')
queen_b = pg.image.load('bl queen.png')
king_w = pg.image.load('wh king.png')
king_b = pg.image.load('bl king.png')
# расположение белых фигур на доске
white_pieces = {'rook_a': (8, 3), 'horse_b': (108, 3), 'elephant_c': (208, 3), 'king': (308, 3), 'queen': (408, 3),
                'elephant_f': (508, 3), 'horse_g': (608, 3), 'rook_h': (708, 3),
                'pawn_a': (8, 103), 'pawn_b': (108, 103), 'pawn_c': (208, 103), 'pawn_d': (308, 103),
                'pawn_e': (408, 103), 'pawn_f': (508, 103), 'pawn_g': (608, 103), 'pawn_h': (708, 103)}
# расположение черных фигур на доске

black_pieces = {'rook_a': (8, 703), 'horse_b': (108, 703), 'elephant_c': (208, 703), 'king': (308, 703),
                'queen': (408, 703), 'elephant_f': (508, 703), 'horse_g': (608, 703), 'rook_h': (708, 703),
                'pawn_a': (8, 603), 'pawn_b': (108, 603), 'pawn_c': (208, 603), 'pawn_d': (308, 603),
                'pawn_e': (408, 603), 'pawn_f': (508, 603), 'pawn_g': (608, 603), 'pawn_h': (708, 603)}


def draw_pieces_start():
    '''
    функция для рааставления белых и черных фигур на доске
    '''
    # расставление белые фигуры
    for piece in white_pieces.keys():
        if piece in ('pawn_a', 'pawn_b', 'pawn_c', 'pawn_d', 'pawn_e', 'pawn_f', 'pawn_g', 'pawn_h'):
            screen.blit(pawn_w, white_pieces[piece])
        elif piece in ('rook_a', 'rook_h'):
            screen.blit(rook_w, white_pieces[piece])
        elif piece in ('horse_b', 'horse_g'):
            screen.blit(horse_w, white_pieces[piece])
        elif piece in ('elephant_c', 'elephant_f'):
            screen.blit(elephant_w, white_pieces[piece])
        elif piece == 'queen':
            screen.blit(queen_w, white_pieces[piece])
        elif piece == 'king':
            screen.blit(king_w, white_pieces[piece])
    # расставление черных фигур на доске
    for piece in black_pieces.keys():
        if piece in ('pawn_a', 'pawn_b', 'pawn_c', 'pawn_d', 'pawn_e', 'pawn_f', 'pawn_g', 'pawn_h'):
            screen.blit(pawn_b, black_pieces[piece])
        elif piece in ('rook_a', 'rook_h'):
            screen.blit(rook_b, black_pieces[piece])
        elif piece in ('horse_b', 'horse_g'):
            screen.blit(horse_b, black_pieces[piece])
        elif piece in ('elephant_c', 'elephant_f'):
            screen.blit(elephant_b, black_pieces[piece])
        elif piece == 'queen':
            screen.blit(queen_b, black_pieces[piece])
        elif piece == 'king':
            screen.blit(king_b, black_pieces[piece])


def check_options(pieces, turn):
    '''
    функция для проверки всех допустимых параметров фигур на доске
    '''
    moves_list = []
    all_moves_list = []
    for piece, location in pieces.items():
        if piece in ('pawn_a', 'pawn_b', 'pawn_c', 'pawn_d', 'pawn_e', 'pawn_f', 'pawn_g', 'pawn_h'):
            moves_list = check_pawn(location, turn)
        # проверка фигры ладьи    
        elif piece in ('rook_a', 'rook_h'):
            moves_list = check_rook(location, turn)
        # проверка фигуры лощади на доске
        elif piece in ('horse_b', 'horse_g'):
            moves_list = check_knight(location, turn)
        # проверка фигуры слона на доске
        elif piece in ('elephant_c', 'elephant_f'):
            moves_list = check_bishop(location, turn)
        # проверка фигуры королевы на досен
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        # проверка фигуры король на доке
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    # вернем список all_moves_list
    return all_moves_list


def check_king(position, color):
    '''
    проверка допустимых ходов короля
    '''
    moves_list = []
    # x, y позициии
    x = position[0]
    y = position[1]
    # если цвет белый то мы записываем в переменную
    if color == 'white':
        # enemies_list = black_pieces.values()
        friends_list = white_pieces.values()
    # если цвет черный, то мы записываем в переменную
    else:
        friends_list = black_pieces.values()

    # эти 8 пар чисел отвечают за проверку наличия короля на доске. Король может переместиться только на одну
    # клетку в любом направлении
    targets = [(100, 0), (100, 100), (100, -100), (-100, 0), (-100, 100), (-100, -100), (0, 100), (0, -100)]
    for i in range(8):
        target = (x + targets[i][0], y + targets[i][1])
        if target not in friends_list and 8 <= target[0] <= 708 and 3 <= target[1] <= 703:
            moves_list.append(target)
    return moves_list


def check_queen(position, color):
    '''
    проверка допустимых ходов ферзя
    '''
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


# check bishop moves
def check_bishop(position, color):
    '''
    # проверка допустимых ходов слона
    '''
    moves_list = []
    x = position[0]
    y = position[1]
    # проверка, что цвет белый
    if color == 'white':
        enemies_list = black_pieces.values()
        friends_list = white_pieces.values()
    # проверка на то, что цвет чёрный
    else:
        friends_list = black_pieces.values()
        enemies_list = white_pieces.values()
    for i in range(4):  # вверх-вправо, вверх-влево, вниз-вправо, вниз-влево
        path = True
        chain = 1
        if i == 0:
            a = 100
            b = -100
        elif i == 1:
            a = -100
            b = -100
        elif i == 2:
            a = 100
            b = 100
        else:
            a = -100
            b = 100
        while path:
            if ((x + (chain * a), y + (chain * b)) not in friends_list and 8 <= x + (chain * a) <= 708 \
                    and 3 <= y + (chain * b) <= 703):
                moves_list.append((x + (chain * a), y + (chain * b)))
                if (x + (chain * a), y + (chain * b)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# проверка ходов ладьи
def check_rook(position, color):
    moves_list = []
    x = position[0]
    y = position[1]
    if color == 'white':
        enemies_list = black_pieces.values()
        friends_list = white_pieces.values()
    else:
        friends_list = black_pieces.values()
        enemies_list = white_pieces.values()
    for i in range(4):  # вниз, вверх, вправо, влево
        path = True
        chain = 1
        if i == 0:
            a = 0
            b = 100
        elif i == 1:
            a = 0
            b = -100
        elif i == 2:
            a = 100
            b = 0
        else:
            a = -100
            b = 0
        while path:
            if (x + (chain * a), y + (chain * b)) not in friends_list and \
                    0 <= x + (chain * a) <= 7 and 0 <= y + (chain * b) <= 7:
                moves_list.append((x + (chain * a), y + (chain * b)))
                if (x + (chain * a), y + (chain * b)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check valid pawn moves
def check_pawn(position, color):
    '''
    проверка допустимых ходов пешки
    '''
    moves_list = []
    x = position[0]
    y = position[1]
    # если цвет белый
    if color == 'white':
        if (x, y + 100) not in white_pieces.values() and (x, y + 100) not in black_pieces.values() and y < 703:
            moves_list.append((x, y + 100))
        if (x, y + 200) not in white_pieces.values() and (x, y + 200) not in black_pieces.values() and y == 103:
            moves_list.append((x, y + 200))
        if (x + 100, y + 100) in black_pieces.values():
            moves_list.append((x + 100, y + 100))
        if (x - 100, y + 100) in black_pieces.values():
            moves_list.append((x - 100, y + 100))
    # если цыет черный
    else:
        if (x, y - 100) not in white_pieces.values() and (x, y - 100) not in black_pieces.values() and y > 3:
            moves_list.append((x, y - 100))
        if (x, y - 200) not in white_pieces.values() and (x, y - 200) not in black_pieces.values() and y == 603:
            moves_list.append((x, y - 200))
        if (x + 100, y - 100) in white_pieces.values():
            moves_list.append((x + 100, y - 100))
        if (x - 100, y - 100) in white_pieces.values():
            moves_list.append((x - 100, y - 100))
    return moves_list


def check_knight(position, color):
    '''
    # проверка допустимых ходов коня
    '''
    moves_list = []
    x = position[0]
    y = position[1]
    if color == 'white':
        friends_list = white_pieces.values()
    else:
        friends_list = black_pieces.values()
    # 8 пар чисео, для того чтобы проверить наличие коней, а далее могут ли они пройти два квадрата в одном направлении и один в другом
    targets = [(100, 200), (100, -200), (200, 100), (200, -100), (-100, 200), (-100, -200), (-200, 100), (-200, -100)]
    for i in range(8):
        target = (x + targets[i][0], y + targets[i][1])
        if target not in friends_list and 8 <= target[0] <= 708 and 3 <= target[1] <= 703:
            moves_list.append(target)
    return moves_list


def check_valid_moves():
    '''
    проверка правильности хода для выбранной фигуры
    '''
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


def draw_valid(moves):
    '''
    гарисовать правильные ходы на экране
    '''
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pg.draw.circle(screen, color, (moves[i][0] // 100 * 100 + 50, moves[i][1] // 100 * 100 + 50), 5)


def draw_game_over():
    '''
    функция для отображения на экране окна, где говорится, кто выиграл и нажмите ENTER для новой игры
    '''
    # шрифт
    font = pg.font.Font('freesansbold.ttf', 20)
    # заготовка черного фона для отбражения надписи
    pg.draw.rect(screen, 'black', [200, 200, 400, 70])
    # надпись о том, что кто-то выиграл
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    # нажать ENTER для того чтобы начать новую игру
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


def draw_pieces():
    if turn_step < 2 and selection < 16:
        x = white_pieces[list(white_pieces.keys())[selection]][0]
        y = white_pieces[list(white_pieces.keys())[selection]][1]
        pg.draw.rect(screen, 'red', [x // 100 * 100, y // 100 * 100, 100, 100], 2)
    if turn_step >= 2 and selection < 16:
        x = black_pieces[list(black_pieces.keys())[selection]][0]
        y = black_pieces[list(black_pieces.keys())[selection]][1]
        pg.draw.rect(screen, 'blue', [x // 100 * 100 + 1, y // 100 * 100 + 1, 100, 100], 2)


counter = 0
game_over = False
# 0 - белый поворот без выбора: 1-выбран белый поворотный элемент: 2- черный поворот без выбора, 3 - выбран черный поворотный элемент
turn_step = 0
selection = 100
valid_moves = []
winner = ''
done = False
clock = pg.time.Clock()
black_options = check_options(black_pieces, 'black')
white_options = check_options(white_pieces, 'white')
captured_pieces_white = []
captured_pieces_black = []
while not done:
    # рисование поля
    for row in range(0, 8):
        for column in range(0, 8):
            if (row + column) % 2 == 0:
                color = BLACK
            else:
                color = WHITE
            pg.draw.rect(screen, color, [(column * 100), (row * 100), 100, 100])

    if counter < 30:
        counter += 1
    else:
        counter = 0
    draw_pieces_start()
    if selection != 100:
        black_options = check_options(black_pieces, 'black')
        white_options = check_options(white_pieces, 'white')
        draw_pieces()
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100 * 100 + 8
            y_coord = event.pos[1] // 100 * 100 + 3
            click_coords = (x_coord, y_coord)
            # print(1)
            if turn_step <= 1:
                # print(2, turn_step)
                if click_coords == (808, 803) or click_coords == (908, 803):
                    winner = 'black'
                    # print(3, turn_step)
                if click_coords in white_pieces.values():
                    # print(4, valid_moves, turn_step)
                    selection = list(white_pieces.values()).index(click_coords)
                    if turn_step == 0:
                        # print(5, valid_moves)
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    # print(6, turn_step)
                    if click_coords in black_pieces.values():
                        black_piece = list(black_pieces.keys())[list(black_pieces.values()).index(click_coords)]
                        if black_piece == 'king':
                            winner = 'white'
                        del black_pieces[black_piece]
                    white_pieces[list(white_pieces.keys())[selection]] = click_coords
                    black_options = check_options(black_pieces, 'black')
                    white_options = check_options(white_pieces, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (808, 803) or click_coords == (908, 803):
                    winner = 'white'
                if click_coords in black_pieces.values():
                    selection = list(black_pieces.values()).index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    if click_coords in white_pieces.values():
                        white_piece = list(white_pieces.keys())[list(white_pieces.values()).index(click_coords)]
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_piece == 'king':
                            winner = 'black'
                        del white_pieces[white_piece]
                    black_pieces[list(black_pieces.keys())[selection]] = click_coords
                    black_options = check_options(black_pieces, 'black')
                    white_options = check_options(white_pieces, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == pg.KEYDOWN and game_over:
            if event.key == pg.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = {'rook_a': (8, 3), 'horse_b': (108, 3), 'elephant_c': (208, 3), 'king': (308, 3),
                                'queen': (408, 3),
                                'elephant_f': (508, 3), 'horse_g': (608, 3), 'rook_h': (708, 3),
                                'pawn_a': (8, 103), 'pawn_b': (108, 103), 'pawn_c': (208, 103), 'pawn_d': (308, 103),
                                'pawn_e': (408, 103), 'pawn_f': (508, 103), 'pawn_g': (608, 103), 'pawn_h': (708, 103)}

                black_pieces = {'rook_a': (8, 703), 'horse_b': (108, 703), 'elephant_c': (208, 703), 'king': (308, 703),
                                'queen': (408, 703), 'elephant_f': (508, 703), 'horse_g': (608, 703),
                                'rook_h': (708, 703),
                                'pawn_a': (8, 603), 'pawn_b': (108, 603), 'pawn_c': (208, 603), 'pawn_d': (308, 603),
                                'pawn_e': (408, 603), 'pawn_f': (508, 603), 'pawn_g': (608, 603), 'pawn_h': (708, 603)}
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, 'black')
                white_options = check_options(white_pieces, 'white')

        if winner != '':
            game_over = True
            draw_game_over()

        pg.display.flip()
        clock.tick(60)

pg.quit()
