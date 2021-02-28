import pygame

player_1, player_2 = {1: 1, 2: 3}, {1: 2, 2: 4}


def field_building():
    field = [[0 for _ in range(8)] for _ in range(8)]
    return field


def space_for_figures():
    for col in range(0, 8, 2):
        for r in range(5, 8, 2):
            field[r][col] = player_1[1]
        for r in range(1, 2):
            field[r][col] = player_2[1]
    for col in range(1, 8, 2):
        for r in range(0, 3, 2):
            field[r][col] = player_2[1]
        for r in range(6, 7):
            field[r][col] = player_1[1]


def checking_pos(field, x, y):
    pos = field[y][x]
    if pos == player_1[1] or player_1[2]:
        return True
    elif pos == player_2[1] or player_2[2]:
        return False
    else:
        return False


def move_checking(field, x, y, x1, y1):
    if field[y1][x1] != 0:
        return False

    if field[y][x] == 1:
        if x1 - x == 1 and y1 - y == -1:
            return True
        elif x1 - x == -1 and y1 - y == -1:
            return True
        elif x1 - x == 2 and y1 - y == -2:
            if field[y1 + 1][x1 - 1] == player_2[1] or player_2[2]:
                field[y1 + 1][x1 - 1] = 0
                return True
            else:
                return False
        elif x1 - x == -2 and y1 - y == -2:
            if field[y1 + 1][x1 + 1] == player_2[1] or player_2[2]:
                field[y1 + 1][x1 + 1] = 0
                return True
            else:
                return False

    elif field[y][x] == 2:
        if x1 - x == 1 and y1 - y == 1:
            return True
        elif x1 - x == -1 and y1 - y == 1:
            return True
        elif x1 - x == 2 and y1 - y == 2:
            if field[y1 - 1][x1 - 1] == player_2[1] or player_2[2]:
                field[y1 - 1][x1 - 1] = 0
                return True
            else:
                return False
        elif (y1 - y) == 2 and (x1 - x) == -2:
            if field[y1 - 1][x1 + 1] == player_2[1] or player_2[2]:
                field[y1 - 1][x1 + 1] = 0
                return True
            else:
                return False
        else:
            return False


def checking(field, x, y, x1, y1):
    x_cor = []
    y_cor = []
    if x < x1:
        for col in range(x, x1):
            x_cor.append(col)
    if x > x1:
        for col in range(x, x1, -1):
            x_cor.append(col)
    if y < y1:
        for row in range(y, y1):
            y_cor.append(row)
    if y > y1:
        for row in range(y, y1, -1):
            y_cor.append(row)

    mas = list(zip(x_cor, y_cor))
    vals = [field[y][x] for x, y in mas]
    if len(vals) > 2:
        if all(i == 0 for i in vals[1:-1]):
            field[y1][x1] = field[y][x]
            field[y][x] = 0
            return True

    if len(vals) == 2:
        if all(i == player_2[1] for i in vals[1:]):
            field[y1][x1] = field[y][x]
            field[y][x] = 0
            return True
        elif all(i == player_2[2] for i in vals[1:]):
            field[y1][x1] = field[y][x]
            field[y][x] = 0
            return True
        elif all(i == 0 for i in vals[1:]):
            field[y1][x1] = field[y][x]
            field[y][x] = 0
            return True

    elif len(vals) == 1:
        if all(i == 0 for i in vals[1:]):
            field[y1][x1] = field[y][x]
            field[y][x] = 0
            return True
    else:
        return False


def checking_queen_move(field, x, y, x1, y1):
    if field[y1][x1] != 0:
        return False
    if y1 == y:
        return False
    if x1 == x:
        return False
    if x1 < x and y1 > y:
        if (x - x1) != (y1 - y):
            return False
    if x1 > x and y1 < y:
        if (x1 - x) != (y - y1):
            return False
    if x1 > x and y1 > y:
        if (x1 - x) != (y1 - y):
            return False
    if x1 < x and y1 < y:
        if (x - x1) != (y - y1):
            return False

    if field[y][x] == player_1[2]:
        try:
            if field[y1 + 1][x1 - 1] == player_2[1] or player_2[2]:
                if x < x1 and y > y1:
                    if checking(field, x, y, x1, y1):
                        field[y1][x1] = player_1[2]
                        field[y1 + 1][x1 - 1] = 0
                        return True
        except IndexError:
            pass
        try:
            if field[y1 + 1][x1 + 1] == player_2[1] or player_2[2]:
                if x > x1 and y > y1:
                    if checking(field, x, y, x1, y1):
                        field[y1][x1] = player_1[2]
                        field[y1 + 1][x1 + 1] = 0
                        return True
        except IndexError:
            pass
        try:
            if field[y1 - 1][x1 - 1] == player_2[1] or player_2[2]:
                if checking(field, x, y, x1, y1):
                    if x < x1 and y < y1:
                        field[y1][x1] = player_1[2]
                        field[y1 - 1][x1 - 1] = 0
                        return True
        except IndexError:
            pass
        try:
            if field[y1 - 1][x1 + 1] == player_2[1] or player_2[1]:
                if checking(field, x, y, x1, y1):
                    if x > x1 and y < y1:
                        field[y1][x1] = player_1[2]
                        field[y1 - 1][x1 + 1] = 0
                        return True
        except IndexError:
            pass


def double_jumps(field, x1, y1):
    if player == 1:
        try:
            if field[y1 - 2][x1 + 2] == 0:
                if field[y1 - 1][x1 + 1] == player_2[1] or player_2[2]:
                    return True
            elif field[y1 - 2][x1 - 2] == 0:
                if field[y1 - 1][x1 + 1] == player_2[1] or player_2[2]:
                    return True
        except IndexError:
            pass
    if player == 2:
        try:
            if field[y1 + 2][x1 + 2] == 0:
                if field[y1 - 1][x1 + 1] == player_2[1] or player_2[2]:
                    return True
            elif field[y1 + 2][x1 - 2] == 0:
                if field[y1 - 1][x1 + 1] == player_2[1] or player_2[2]:
                    return True
        except IndexError:
            pass
    if field[y1][x1] == player_1[2]:
        try:
            for i in range(8):
                if field[y1 - i][x1 + i] == player_2[2]:
                    if field[y1 - (i + 1)][x1 + (i + 1)] == 0:
                        return True
                if field[y1 + i][x1 + i] == player_2[2]:
                    if field[y1 + (i + 1)][x1 + (i + 1)] == 0:
                        return True
                if field[y1 + i][x1 - i] == player_2[2]:
                    if field[y1 + (i + 1)][x1 - (i + 1)] == 0:
                        return True
                if field[y1 - i][x1 - i] == player_2[2]:
                    if field[y1 - (i + 1)][x1 - (i + 1)] == 0:
                        return True
        except IndexError:
            pass
    else:
        return False


def win_checking(player, field):
    arr = []
    for row in field:
        arr.append(row.count(player_2[1]))
        arr.append(row.count(player_2[2]))
    if sum(arr) == 0:
        print(f"Player {player} is winner!")
        return True


def field_drawing(field):
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = white
            else:
                color = brown
            rect = pygame.draw.rect(screen, color, [w * col, h * row, w, h])
            centr = rect.center
            if field[row][col] == 1:
                pygame.draw.circle(screen, red, centr, r)
            if field[row][col] == 2:
                pygame.draw.circle(screen, brown, centr, r)
                pygame.draw.circle(screen, beige, centr, r)
            if field[row][col] == 3:
                pygame.draw.circle(screen, red, centr, r)
                pygame.draw.circle(screen, yellow, centr, r, extra)
            if field[row][col] == 4:
                pygame.draw.circle(screen, beige, centr, r)
                pygame.draw.circle(screen, yellow, centr, r, extra)


pygame.init()
size = [560, 560]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Шашки")
clock = pygame.time.Clock()
player = 1
w, h, r = (size[0] // 8), (size[1] // 8), (size[0] // 25)
extra = (size[0] // 250)
game_off = False
field = field_building()
space_for_figures()
white, brown = (255, 255, 255), (87, 61, 47)
red, beige, yellow = (200, 44, 2), (213, 196, 161), (255, 215, 0)
while not game_off:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game_off = True
        elif i.type == pygame.MOUSEBUTTONDOWN:
            current_pos = pygame.mouse.get_pos()
            x, y = (current_pos[0] // w), (current_pos[1] // h)
            k = sum([sum(row) for row in field])
            if checking_pos(field, x, y):
                pass
            else:
                continue
            while True:
                i = pygame.event.wait()
                if i.type == pygame.QUIT:
                    game_off = True
                elif i.type == pygame.MOUSEBUTTONUP:
                    new_pos = pygame.mouse.get_pos()
                    x1, y1 = (new_pos[0] // w), (new_pos[1] // h)
                    if field[y][x] == player_1[1]:
                        if move_checking(field, x, y, x1, y1) is True:
                            field[y1][x1] = player_1[1]
                            field[y][x] = 0
                            if win_checking(player, field) is True:
                                game_off = True
                            u = sum([sum(row) for row in field])
                            if k > u:
                                if double_jumps(field, x1, y1):
                                    pass
                                else:
                                    if player == 1:
                                        player = 2
                                    else:
                                        player = 1

                                    player_1, player_2 = player_2, player_1
                            else:
                                if player == 1:
                                    player = 2
                                else:
                                    player = 1

                                player_1, player_2 = player_2, player_1

                    if field[y][x] == (player_1[2]):
                        if checking_queen_move(field, x, y, x1, y1):
                            if win_checking(player, field):
                                game_off = True
                            u = sum([sum(row) for row in field])
                            if k > u:
                                if double_jumps(field, x1, y1):
                                    pass
                                else:
                                    if player == 1:
                                        player = 2
                                    else:
                                        player = 1
                                    player_1, player_2 = player_2, player_1
                            else:
                                if player == 1:
                                    player = 2
                                else:
                                    player = 1
                                player_1, player_2 = player_2, player_1
                    for row in range(8):
                        for col in range(8):
                            if field[7][col] == 2:
                                field[7][col] = 4
                            if field[0][col] == 1:
                                field[0][col] = 3
                    break
    clock.tick(60)
    field_drawing(field)
    pygame.display.flip()
pygame.quit()
