class Cell:
    def __init__(self, num):
        self.num = num
        self.symbol = ' '

    def __str__(self):
        return self.symbol


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        for i in range(3):
            print('-' * 13)
            out = '| '
            for j in range(3):
                out += str(self.cells[i * 3 + j]) + ' | '
            print(out)
        print('-' * 13)

    def update(self, cell_num, symbol):
        if self.cells[cell_num - 1].symbol == ' ':
            self.cells[cell_num - 1].symbol = symbol
            return True
        else:
            return False

    def is_game_over(self):
        for i in range(3):
            if self.cells[i * 3].symbol == self.cells[i * 3 + 1].symbol == self.cells[i * 3 + 2].symbol and \
                    self.cells[i * 3].symbol != ' ':
                return True
        for i in range(3):
            if self.cells[i].symbol == self.cells[i + 3].symbol == self.cells[i + 6].symbol and self.cells[i].symbol != ' ':
                return True
        if self.cells[0].symbol == self.cells[4].symbol == self.cells[8].symbol and self.cells[0].symbol != ' ':
            return True
        if self.cells[2].symbol == self.cells[4].symbol == self.cells[6].symbol and self.cells[2].symbol != ' ':
            return True
        for cell in self.cells:
            if cell.symbol == ' ':
                return False
        return None


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0

    def get_move(self):
        try:
            cell_num = int(input(self.name + ', Введите номер ячейки: '))
            return cell_num
        except ValueError:
            print('Введите номер ячейки.')
            return self.get_move()


class Game:
    def __init__(self, player1, player2, flag):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        if flag == 1:
            self.current_player = player1
        else:
            self.current_player = player2

    def play_turn(self):
        print(self.current_player.name + 'ходит :\n')
        self.board.display()
        cell_num = self.current_player.get_move()
        while not self.board.update(cell_num, self.current_player.symbol):
            print('Ячейка занята, повторите ввод')
            cell_num = self.current_player.get_move()

        if self.board.is_game_over():
            print(self.current_player.name + ' Выиграл !\n')
            self.board.display()
            self.current_player.score += 1
            return True
        elif self.board.is_game_over() is None:
            print('Ничейный результат !\n')
            self.board.display()
            return True

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

        return False

    def play_game(self, flag):
        print('Игра началась!')
        self.board = Board()
        if flag == 1:
            self.current_player = player1
        else:
            self.current_player = player2
        while not self.board.is_game_over():
            if self.play_turn():
                break

        print('Score:')
        print(self.player1.name + ': ' + str(self.player1.score))
        print(self.player2.name + ': ' + str(self.player2.score))


name1 = input('Введите имя Игрока1 (его символ: X): ')
name2 = input('Введите имя Игрока2 (его символ: O): ')
player1 = Player(name1, 'X')
player2 = Player(name2, 'O')
while True:
    flag = int(input('Кто ходит первым: 1 - Игрок1, 2 - Игрок2: '))
    game = Game(player1, player2, flag)
    game.play_game(flag)

    again = input('Играем еще раз? (Y/N): ')
    if again.lower() != 'y':
        break

print('Игра окончена!')
