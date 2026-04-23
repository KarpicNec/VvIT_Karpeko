import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class TicTacToeGame(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Крестики-нолики на PyQt5")
		# Ширина увеличена для боковых панелей (было 300 → 500)
		self.setGeometry(100, 100, 500, 400)  
		self.game_over = False
		self.current_player = "X"
		self.move_count = 0
		self.score_X = 0
		self.score_O = 0

		# Создаём левую панель с X и счётом
		self.label_X = QLabel("X", self)
		self.label_X.setGeometry(30, 120, 80, 80)
		self.label_X.setAlignment(Qt.AlignCenter)
		self.label_X.setFont(QFont("Arial", 36, QFont.Bold))
		self.label_X.setStyleSheet("color: blue;")
		
		self.score_X_label = QLabel("0", self)
		self.score_X_label.setGeometry(30, 200, 80, 50)
		self.score_X_label.setAlignment(Qt.AlignCenter)
		self.score_X_label.setFont(QFont("Arial", 18, QFont.Bold))

		# Создаём правую панель с O и счётом
		self.label_O = QLabel("O", self)
		self.label_O.setGeometry(390, 120, 80, 80)
		self.label_O.setAlignment(Qt.AlignCenter)
		self.label_O.setFont(QFont("Arial", 36, QFont.Bold))
		self.label_O.setStyleSheet("color: red;")
		
		self.score_O_label = QLabel("0", self)
		self.score_O_label.setGeometry(390, 200, 80, 50)
		self.score_O_label.setAlignment(Qt.AlignCenter)
		self.score_O_label.setFont(QFont("Arial", 18, QFont.Bold))

		# Кнопка новой игры (центрирована, чуть ниже поля)
		self.restart_button = QPushButton("Новая игра", self)
		self.restart_button.setGeometry(200, 340, 100, 30)
		self.restart_button.clicked.connect(self.reset_game)

		# Игровое поле (сдвинуто на 100 пикселей вправо)
		self.buttons = []
		self.create_buttons()

		# Статусная строка (под полем, но выше кнопки)
		self.status_label = QLabel(self)
		self.status_label.setGeometry(100, 310, 300, 20)
		self.status_label.setAlignment(Qt.AlignCenter)

	def create_buttons(self):
		offset_x = 100  # сдвиг вправо, чтобы освободить место слева
		for row in range(3):
			row_buttons = []
			for col in range(3):
				button = QPushButton(self)
				button.setText("")
				button.setGeometry(offset_x + col * 100, row * 100, 100, 100)
				button.clicked.connect(self.on_click)
				row_buttons.append(button)
			self.buttons.append(row_buttons)

	def on_click(self):
		if self.game_over:
			return
		button = self.sender()
		if button.text() == "":
			button.setText(self.current_player)
			self.move_count += 1
			self.check_winner()
			if not self.game_over:   # игра продолжается
				self.switch_player()

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
			self.end_game(None)   # ничья

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
		else:   # ничья
			self.status_label.setText("Ничья! Нажмите «Новая игра»")
		# Отключаем все кнопки поля
		for row in self.buttons:
			for button in row:
				button.setEnabled(False)

	def switch_player(self):
		self.current_player = "O" if self.current_player == "X" else "X"

	def reset_game(self):
		# Сбрасываем состояние игры (счёт побед НЕ обнуляем)
		self.game_over = False
		self.current_player = "X"
		self.move_count = 0
		self.status_label.setText("")
		# Очищаем и включаем кнопки
		for row in self.buttons:
			for button in row:
				button.setText("")
				button.setEnabled(True)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = TicTacToeGame()
	window.show()
	sys.exit(app.exec_())