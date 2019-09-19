import pygame

from api import Api
from helpers import get_grid_ref
from vars import *
from pygame.rect import Rect


class AttackBoard():

    # board = ['??????????',
    #          '.????XX???',
    #          '??????????',
    #          '??????.???',
    #          '??.??X????',
    #          '???????.??',
    #          '??.???????',
    #          '??X???????',
    #          '??X???????',
    #          '??????.???']
    board = [['?' for j in range(board_size_h)] for i in range(board_size_v)]
    my_turn = True

    top = 20
    width = 300
    height = 300
    margin = 5

    outer_rect = Rect(screen_middle_h - width / 2, top, width, height)
    inner_rect = outer_rect.inflate(-10, -10)
    border_rect = outer_rect.inflate(20, 20)

    item_width = float(inner_rect.width - (margin * (board_size_h - 1))) / board_size_h
    item_height = float(inner_rect.height - (margin * (board_size_v - 1))) / board_size_v

    rects = [[] for i in range(board_size_h)]
    for i in range(board_size_h):
        for j in range(board_size_v):
            left = inner_rect.left + int(i * (item_width + margin))
            top = inner_rect.top + int(j * (item_height + margin))
            right = inner_rect.left + int(i * (item_width + margin) + item_width)
            bottom = inner_rect.top + int(j * (item_height + margin) + item_height)
            item_rect = Rect(left, top, right - left, bottom - top)
            rects[i].append(item_rect)

    def draw(self, screen) -> None:
        if self.my_turn:
            pygame.draw.rect(screen, border_color, self.border_rect)
        pygame.draw.rect(screen, grid_color, self.outer_rect)
        for i in range(0, board_size_h):
            for j in range(0, board_size_v):
                pygame.draw.rect(screen, get_color(self.board[i][j]), self.rects[i][j])

    def mouse_hover(self, mouse_pos):
        if not self.inner_rect.collidepoint(mouse_pos):
            return None

        for i in range(board_size_h):
            for j in range(board_size_v):
                if self.rects[i][j].collidepoint(mouse_pos):
                    return (i,j)

        return None

    def make_move(self, mouse_pos, api_id):
        coords = self.mouse_hover(mouse_pos)
        if coords is None:
            return
        
        r = Api.makeMove(api_id, "joao1", get_grid_ref(*coords))
    
    def update_board(self, board, is_attacking):
        self.board = board
        self.my_turn = is_attacking

        