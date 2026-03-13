import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class GatewaySwitcher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gateway Switcher')

        # Vertical layout
        layout = QVBoxLayout()
        self.button1 = QPushButton('Switch to Gateway 1')
        self.button2 = QPushButton('Switch to Gateway 2')

        # Connect buttons to switch functions
        self.button1.clicked.connect(self.switch_gateway_1)
        self.button2.clicked.connect(self.switch_gateway_2)

        # Add buttons to layout
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        # Set layout to central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def switch_gateway_1(self):
        print('Switched to Gateway 1')

    def switch_gateway_2(self):
        print('Switched to Gateway 2')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GatewaySwitcher()
    ex.show()
    sys.exit(app.exec_())