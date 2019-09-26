import pygame

from api import Api
from helpers import get_grid_ref
from vars import *
from pygame.rect import Rect


class AttackBoard():

    pointer_cursor = pygame.cursors.compile(pointer_cursor_string, 'X', '.')
    board = [['?' for c in range(board_size_h)] for r in range(board_size_v)]
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

    rects = [[] for r in range(board_size_v)]
    for r in range(board_size_v):
        for c in range(board_size_h):
            left = inner_rect.left + int(c * (item_width + margin))
            top = inner_rect.top + int(r * (item_height + margin))
            right = inner_rect.left + int(c * (item_width + margin) + item_width)
            bottom = inner_rect.top + int(r * (item_height + margin) + item_height)
            item_rect = Rect(left, top, right - left, bottom - top)
            rects[r].append(item_rect)

    def __init__(self, game_id, player) -> None:
        super().__init__()
        self.game_id = game_id
        self.player = player

    def draw(self, screen) -> None:
        if self.my_turn:
            pygame.draw.rect(screen, border_color, self.border_rect)
        pygame.draw.rect(screen, grid_color, self.outer_rect)
        for r in range(board_size_v):
            for c in range(board_size_h):
                pygame.draw.rect(screen, get_color(self.board[r][c]), self.rects[r][c])

    def mouse_hover(self, mouse_pos):
        if not self.inner_rect.collidepoint(mouse_pos):
            return None

        for r in range(board_size_v):
            for c in range(board_size_h):
                if self.rects[r][c].collidepoint(mouse_pos):
                    return (r,c)

        return None

    def make_move(self, mouse_pos):
        coords = self.mouse_hover(mouse_pos)
        if coords is None:
            return
        Api.makeMove(self.game_id, self.player, get_grid_ref(*coords))
    
    def update_board(self, board, is_attacking):
        self.board = board
        self.my_turn = is_attacking

    def frame_update(self):
        if self.mouse_hover(pygame.mouse.get_pos()) is None:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        else:
            pygame.mouse.set_cursor((24, 24), (6, 0), *self.pointer_cursor)
        
        return False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.make_move(pygame.mouse.get_pos())
            return True
        
        return False