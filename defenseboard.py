import pygame
from vars import *
from pygame.rect import Rect

class DefenseBoard():

    # board = ['??????????',
    #          '??O???.???',
    #          '??O???????',
    #          '??X??.????',
    #          '??O???OO??',
    #          '??O???????',
    #          '??????????',
    #          '?.??O?????',
    #          '????O?????',
    #          '????O?????']
    board = [['?' for j in range(board_size_h)] for i in range(board_size_v)]
    my_turn = False
    counter = 100

    top = 330.0
    width_top = 300.0
    width_bottom = 400.0
    height = 150.0
    bottom = top + height
    margin_h = 5.0
    margin_v = 3.0

    outer_poly = [
        (screen_middle_h - width_top / 2, top),
        (screen_middle_h + width_top / 2, top),
        (screen_middle_h + width_bottom / 2, bottom),
        (screen_middle_h - width_bottom / 2, bottom)
    ]

    def interp(x, x0, x1, y0, y1):
        return (x - x0) / (x1 - x0) * (y1 - y0) + y0

    inner_top = top + margin_v
    inner_bottom = bottom - margin_v
    inner_height = inner_bottom - inner_top

    item_height = (inner_height - margin_v * (board_size_v - 1)) / board_size_v
    item_width_top = (width_top - margin_h * (board_size_h + 1)) / board_size_h
    margin_h_bottom = margin_h * width_bottom / width_top
    item_width_bottom = (width_bottom - margin_h_bottom * (board_size_h + 1)) / board_size_h

    border_poly = [
        (screen_middle_h - width_top / 2 - margin_h * 1.8, top - margin_v * 2),
        (screen_middle_h + width_top / 2 + margin_h * 1.8, top - margin_v * 2),
        (screen_middle_h + width_bottom / 2 + margin_h_bottom * 2.2, bottom + margin_v * 2),
        (screen_middle_h - width_bottom / 2 - margin_h_bottom * 2.2, bottom + margin_v * 2)
    ]

    margin_h_percent = margin_h / width_top
    item_width_percent = (1 - (board_size_h + 1) * margin_h_percent) / board_size_h

    polys = [[] for i in range(board_size_v)]
    for i in range(board_size_v):
        row_top = inner_top + i * (item_height + margin_v)
        row_bottom = row_top + item_height
        for j in range(board_size_h):
            left_top = screen_middle_h - width_top / 2 + margin_h + (item_width_top + margin_h) * j
            right_top = left_top + item_width_top
            left_bottom = screen_middle_h - width_bottom / 2 + margin_h_bottom + (item_width_bottom + margin_h_bottom) * j
            right_bottom = left_bottom + item_width_bottom

            poly = [
                (interp(row_top, top, bottom, left_top, left_bottom), row_top),
                (interp(row_top, top, bottom, right_top, right_bottom), row_top),
                (interp(row_bottom, top, bottom, right_top, right_bottom), row_bottom),
                (interp(row_bottom, top, bottom, left_top, left_bottom), row_bottom)
            ]
            polys[i].append(poly)

    def draw(self, screen) -> None:
        if self.my_turn:
            pygame.draw.polygon(screen, border_color, self.border_poly)

        pygame.draw.polygon(screen, grid_color, self.outer_poly)

        for i in range(board_size_v):
            for j in range(board_size_h):
                pygame.draw.polygon(screen, get_color(self.board[i][j]), self.polys[i][j])

    def update_board(self, board, is_attacking):
        self.board = board
        self.my_turn = not is_attacking

    def frame_update(self):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

        self.counter = self.counter - 1
        if self.counter == 0:
            self.counter = 100
            return True

        return False

    def handle_event(self, event):
        return False