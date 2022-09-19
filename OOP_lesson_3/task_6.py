# Шахматный король ходит по горизонтали, вертикали и диагонали,
# но только на 1 клетку. Даны две различные клетки шахматной доски,
# определите, может ли король попасть с первой клетки на вторую одним ходом.

class ChessFigure:
    figure_base = dict()

    def __init__(self, figure: str):
        self.figure = figure.lower()
        self.figure_base.update({self.figure: None})

    def cell_figure(self, coord_w, coord_h):
        if coord_w != 0 and coord_h != 0 and coord_h <= 8 and coord_w <= 8:
            self.figure_base.update({self.figure: [coord_w, coord_h]})
        else: print("Can't place out of table!")

    def move_figure(self, w_m, h_m):
        [w_c, h_c] = self.figure_base[self.figure]
        horse_movement = [[w_c-1, h_c-2], [w_c+1, h_c-2], [w_c+2, h_c-1], [w_c+2, h_c+1],
                          [w_c-1, h_c+2], [w_c+1, h_c+2], [w_c-2, h_c+1], [w_c-2, h_c-1]]
        queen_diag1 = [[w_c+i, h_c+i] for i in range(1, min([8-w_c, 8-h_c]) + 1)]
        queen_diag2 = [[w_c-i, h_c+i] for i in range(1, max([8-w_c, 8-h_c]) + 1) if w_c-i > 0]
        queen_diag3 = [[w_c-i, h_c-i] for i in range(1, max([8-w_c, 8-h_c]) + 1) if 9 > h_c-i > 0]
        queen_diag4 = [[w_c+i, h_c-i] for i in range(1, min([8-w_c, 8-h_c]) + 1) if 9 > h_c-i > 0]
        queen_diag = queen_diag1 + queen_diag2 + queen_diag3 + queen_diag4
        queen_vert1 = [[w_c, h_c+i] for i in range(1, 9) if h_c+i < 9]
        queen_vert2 = [[w_c, h_c-i] for i in range(1, 9) if 0 < h_c-i < 9]
        queen_horiz1 = [[w_c+i, h_c] for i in range(1, 9) if 0 < w_c+i < 9]
        queen_horiz2 = [[w_c-i, h_c] for i in range(1, 9) if 0 < w_c-i < 9]
        queen_line = queen_horiz2 + queen_horiz1 + queen_vert2 + queen_vert1
        queen_movement = queen_line + queen_diag

        if 8 >= w_m > 0 and 8 >= h_m > 0:
            if self.figure == 'король':
                if (w_c + 1 == w_m or w_c - 1 == w_m or w_c == w_m) and (h_c + 1 == h_m or h_c - 1 == h_m or h_c == h_m):
                    print(f'Фигура {self.figure} передвинута с координат: {w_c, h_c} на координаты {w_m, h_m}.')
                    self.figure_base.update({self.figure: [w_m, h_m]})
                else: print('NO!')
            elif self.figure == 'конь':
                if [w_m, h_m] in horse_movement:
                    print(f'Фигура {self.figure} передвинута с координат: {w_c, h_c} на координаты {w_m, h_m}.')
                    self.figure_base.update({self.figure: [w_m, h_m]})
                else: print('NO!')
            elif self.figure == 'слон':
                if [w_m, h_m] in queen_diag:
                    print(f'Фигура {self.figure} передвинута с координат: {w_c, h_c} на координаты {w_m, h_m}.')
                    self.figure_base.update({self.figure: [w_m, h_m]})
                else: print('NO!')
            elif self.figure == 'ладья':
                if [w_m, h_m] in queen_line:
                    print(f'Фигура {self.figure} передвинута с координат: {w_c, h_c} на координаты {w_m, h_m}.')
                    self.figure_base.update({self.figure: [w_m, h_m]})
                else:
                    print('NO!')
            elif self.figure == 'ферзь':
                if [w_m, h_m] in queen_movement:
                    print(f'Фигура {self.figure} передвинута с координат: {w_c, h_c} на координаты {w_m, h_m}.')
                    self.figure_base.update({self.figure: [w_m, h_m]})
                else:
                    print('NO!')
            else: print("Работа над фигурами кроме (король,конь,слон,ферзь,ладья) в процессе :)")
        else: print("Can't move out of table!")


konb = ChessFigure('ферзь')
konb.cell_figure(1, 1)
konb.move_figure(5, 5)
konb.move_figure(8, 5)
konb.move_figure(5, 2)
