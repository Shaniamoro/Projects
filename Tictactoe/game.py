# -*- coding: utf-8 -*-
"""
    game.py
    ------------

    A simple tic-tac-toe game to play in the CL.
"""

__author__ = "Shania Roberts"
import random


class Game:
    board = []
    user_suite = None
    pc_suite = None

    def __init__(self):
        self.start_game()

    def create_board(self):
        """
        Creates a black board which contains spaces.

        :return board: A list of lists.
        """
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        return self.board

    def start_game(self):
        self.create_board()
        self.choose_suite()
        self.first_play()

    def first_play(self):
        print(" Do you want to play first? Y / N ")
        first_play = input().upper()
        if first_play == 'Y':
            self.user_move()
        elif first_play == 'N':
            self.pc_move()

    def choose_suite(self):
        print(" Do you want to be X or O ? X / O ")
        self.user_suite = input().upper()
        if self.user_suite == 'X':
            self.pc_suite = 'O'
        else:
            self.pc_suite = 'X'
        return self.pc_suite

    def print_board(self):
        print('   |   |')
        print(' ' + self.board[0][0] + ' | ' + self.board[0][1] + ' | ' + self.board[0][2])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1][0] + ' | ' + self.board[1][1] + ' | ' + self.board[1][2])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[2][0] + ' | ' + self.board[2][1] + ' | ' + self.board[2][2])
        print('   |   |')

    def random_generator(self):
        i = random.randrange(3)
        j = random.randrange(3)
        return i, j

    def is_full(self) -> bool:
        if ' ' not in self.board:
            return True
        else:
            return False

    def available(self, i, j) -> bool:
        if self.board[i][j] == ' ':
            return True
        else:
            return False

    def pc_move(self):
        print('PC move')
        i, j = self.random_generator()
        if self.available(i, j):
            self.board[i][j] = self.pc_suite
            self.print_board()
            if self.check_for_winner() is False:
                self.user_move()
        else:
            print("That space isn't open")
            self.pc_move()

    def combinations(self):
        for i in range(3):
            # rows
            if len(set(self.board[i])) == 1:
                return set(self.board[i])
            # columns
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return [self.board[0][i], self.board[1][i], self.board[2][i]]
            # diagonal
            elif self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
                return [self.board[0][0], self.board[1][1], self.board[2][2]]
            # diagonal 2
            elif self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
                return [self.board[0][2], self.board[1][1], self.board[2][0]]
        return '0'

    def user_move(self):
        print('Where do you want to play row #, column #')
        temp = input().split()
        i, j = int(temp[0]), int(temp[1])
        if self.available(i, j):
            self.board[i][j] = self.user_suite
            print('User move')
            self.print_board()
            if self.check_for_winner() is False:
                self.pc_move()
        else:
            print("That space isn't open")
            self.user_move()

    def check_for_winner(self) -> bool:
        temp = self.combinations()
        if self.user_suite in temp:
            print('You Win! ')
            self.retry()
            return True
        elif self.pc_suite in temp:
            print('You Loose!, Try again')
            self.retry()
            return True
        else:
            return False

    def retry(self):
        print("Do you want to play again? Y / N ")
        if input().upper() == 'Y':
            self.start_game()
        else:
            print('Great game')
            exit()


New_Game = Game()
