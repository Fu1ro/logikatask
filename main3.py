from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.show()
main_win.setWindowTitle("Test")
winer = QLabel("Переможець: ")
winer.setText("34")
button = QPushButton("Згенерувати")
v_line = QVBoxLayout()
v_line.addWidget(
    winer, alignment= Qt.AlignCenter
)
main_win.setLayout(v_line)
app.exec_()
