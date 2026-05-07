import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class TicTacToeGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Крестики-нолики на PyQt5")
        self.setGeometry(710, 200, 500, 420)
        self.game_over = False
        self.first_move = "X"          # кто начинает партию (чередуется тольк в PvP)
        self.current_player = "X"      # кто сейчас ходит 
        self.move_count = 0
        self.score_X = 0
        self.score_O = 0
        self.game_mode = None           # а будет "pvp" или "pve"

        # левая панель с X и счётом
        self.label_X = QLabel("X", self)
        self.label_X.setGeometry(30, 120, 80, 80)
        self.label_X.setAlignment(Qt.AlignCenter)
        self.label_X.setFont(QFont("Arial", 36, QFont.Bold))
        self.label_X.setStyleSheet("color: blue;")
        
        self.score_X_label = QLabel("0", self)
        self.score_X_label.setGeometry(30, 200, 80, 50)
        self.score_X_label.setAlignment(Qt.AlignCenter)
        self.score_X_label.setFont(QFont("Arial", 18, QFont.Bold))

        # правая панель с O и счётом
        self.label_O = QLabel("O", self)
        self.label_O.setGeometry(390, 120, 80, 80)
        self.label_O.setAlignment(Qt.AlignCenter)
        self.label_O.setFont(QFont("Arial", 36, QFont.Bold))
        self.label_O.setStyleSheet("color: red;")
        
        self.score_O_label = QLabel("0", self)
        self.score_O_label.setGeometry(390, 200, 80, 50)
        self.score_O_label.setAlignment(Qt.AlignCenter)
        self.score_O_label.setFont(QFont("Arial", 18, QFont.Bold))

        # кнопка новой игры
        self.restart_button = QPushButton("Новая игра", self)
        self.restart_button.setGeometry(200, 350, 100, 30)
        self.restart_button.clicked.connect(self.reset_game)
        self.restart_button.setEnabled(False)

        # кнопка смена режима игры
        self.change_mode_button = QPushButton("Сменить режим", self)
        self.change_mode_button.setGeometry(200, 380, 100, 30)
        self.change_mode_button.clicked.connect(self.show_mode_choice)
        self.change_mode_button.setEnabled(False)

        # поле 
        self.buttons = []
        self.create_buttons()

        # статусная строка
        self.status_label = QLabel(self)
        self.status_label.setGeometry(100, 320, 300, 20)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setText("Выберите режим игры")

        # кнопки выбора режима 
        self.pvp_button = QPushButton("Играть с другом (PvP)", self)
        self.pvp_button.setGeometry(160, 120, 180, 40)
        self.pvp_button.clicked.connect(self.set_pvp_mode)

        self.pve_button = QPushButton("Играть с компьютером (PvE)", self)
        self.pve_button.setGeometry(160, 160, 180, 40)
        self.pve_button.clicked.connect(self.set_pve_mode)

        # пока не выбран режим все блок
        self.set_field_enabled(False)

    # методы для работы с полем 
    def set_field_enabled(self, enabled):
        for row in self.buttons:
            for button in row:
                button.setEnabled(enabled)

    def clear_field(self):
        for row in self.buttons:
            for button in row:
                button.setText("")

    # создание кнопок для игрового поля
    def create_buttons(self):
        offset_x = 100 # сдвиг вправо, чтобы освободить место слева
        for row in range(3):
            row_buttons = []
            for col in range(3):
                button = QPushButton(self)
                button.setText("")
                button.setFont(QFont("Arial", 18, QFont.Bold))
                button.setGeometry(offset_x + col * 100, 10 + row * 100, 100, 100)
                button.clicked.connect(self.on_click)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def on_click(self):
        if self.game_over or self.game_mode is None:
            return
        if self.game_mode == "pve" and self.current_player != "X":
            return
        button = self.sender()
        if button.text() == "":
            button.setText(self.current_player)
            self.move_count += 1
            self.check_winner()
            if self.game_over == False:
                self.switch_player()
                self.update_status_text()
                if self.game_mode == "pve" and self.game_over == False and self.current_player == "O":
                    self.computer_move()

    def check_winner(self):
        win_combinations = [
            [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)],
            [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)],
            [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]
        ]
        for combo in win_combinations:
            symbols = [self.buttons[r][c].text() for r, c in combo]
            if symbols[0] == symbols[1] == symbols[2] != "":
                winner = symbols[0]
                self.end_game(winner)
                return
        if self.move_count == 9:
            self.end_game(None)

    def end_game(self, winner):
        self.game_over = True
        if winner == "X":
            self.score_X += 1
            self.score_X_label.setText(str(self.score_X))
            self.status_label.setText("Победил X! Нажмите «Новая игра»")
        elif winner == "O":
            self.score_O += 1
            self.score_O_label.setText(str(self.score_O))
            self.status_label.setText("Победил O! Нажмите «Новая игра»")
        else:
            self.status_label.setText("Ничья! Нажмите «Новая игра»")
        self.set_field_enabled(False)

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    # изменение статуса статусной панели, да тавталогия
    def update_status_text(self):
        if self.game_over:
            return
        if self.game_mode == "pvp":
            self.status_label.setText(f"Сейчас ход {self.current_player}")
        else:  # то есть pve
            if self.current_player == "X":
                self.status_label.setText("Ваш ход")
            else:
                self.status_label.setText("Ход компьютера...")

    # сброс игры (новая партия) 
    def reset_game(self):
        self.game_over = False
        self.move_count = 0
        self.clear_field()
        self.set_field_enabled(True)

        if self.game_mode == "pvp":
            # справедливое начало игры, кто ходит первым
            if self.first_move == "X":
                self.current_player = "O"
                self.first_move = "O"
            else:
                self.current_player = "X"
                self.first_move = "X"
        else:  # ну то есть pve
            # Всегда начинает человек, иначе нет смысла :)
            self.current_player = "X"
        self.update_status_text()

    # Методы для минимакса (для pve режима) 
    def get_available_moves(self, board):
        moves = []
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    moves.append((r, c))
        return moves

    def check_winner_on_board(self, board):
        win_combinations = [
            [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)],
            [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)],
            [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]
        ]
        for combo in win_combinations:
            symbols = [board[r][c] for r, c in combo]
            if symbols[0] == symbols[1] == symbols[2] != "":
                return symbols[0]
        if all(board[r][c] != "" for r in range(3) for c in range(3)):
            return "draw"
        return None

    def minimax(self, board, player, depth):
        computer = "O"
        human = "X"
        winner = self.check_winner_on_board(board)
        if winner == computer:
            return (10 - depth, None)
        elif winner == human:
            return (depth - 10, None)
        elif winner == "draw":
            return (0, None)

        moves = self.get_available_moves(board)
        if not moves:
            return (0, None)

        best_score = None
        best_move = None

        for (r, c) in moves:
            board[r][c] = player
            score, _ = self.minimax(board, "O" if player == "X" else "X", depth + 1)
            board[r][c] = ""

            if player == computer:
                if best_score is None or score > best_score:
                    best_score = score
                    best_move = (r, c)
            else:
                if best_score is None or score < best_score:
                    best_score = score
                    best_move = (r, c)

        return (best_score, best_move)

    def computer_move(self):
        # текущее состояние поля
        board = [[self.buttons[r][c].text() for c in range(3)] for r in range(3)]
        _, best_move = self.minimax(board, "O", 0)
        if best_move:
            row, col = best_move
            self.buttons[row][col].setText("O")
            self.move_count += 1
            self.check_winner()
            if not self.game_over:
                self.switch_player()
                self.update_status_text()
                # если после хода компьютера не конец, то ход к человеку (X)

    # выбор режима 
    def set_pvp_mode(self):
        self.game_mode = "pvp"
        self.first_move = "X"
        self.current_player = "X"
        self.game_over = False
        self.move_count = 0
        self.clear_field()
        self.set_field_enabled(True)
        self.restart_button.setEnabled(True)
        self.change_mode_button.setEnabled(True)   # разрешаем смену режима
        self.update_status_text()
        # скрытие кнопок выбора режима
        self.pvp_button.setVisible(False)
        self.pve_button.setVisible(False)

    def set_pve_mode(self):
        self.game_mode = "pve"
        self.current_player = "X"
        self.game_over = False
        self.move_count = 0
        self.clear_field()
        self.set_field_enabled(True)
        self.restart_button.setEnabled(True)
        self.change_mode_button.setEnabled(True)
        self.update_status_text()
        self.pvp_button.setVisible(False)
        self.pve_button.setVisible(False)

    def show_mode_choice(self):
        # сброс игры
        self.game_over = True   # чтобы нельзя было кликать
        self.set_field_enabled(False)
        self.restart_button.setEnabled(False)
        self.change_mode_button.setEnabled(False)
        self.clear_field()
        # не знаю надо ли сбрасывать счет
        #self.score_X = 0
        #self.score_O = 0
        #self.score_X_label.setText("0")
        #self.score_O_label.setText("0")
        self.game_mode = None
        self.status_label.setText("Выберите режим игры")
        # видимость кнопок выбора режима
        self.pvp_button.setVisible(True)
        self.pve_button.setVisible(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToeGame()
    window.show()
    sys.exit(app.exec_())