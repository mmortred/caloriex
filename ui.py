#part 1
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, 
    QLineEdit, QPushButton, QGridLayout, QVBoxLayout
)
from PyQt6.QtCore import Qt

#part 2
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setMinimumSize(854,480)
        self.showMaximized()
#part 3 canvas styling
        self.main_canvas = QWidget(self)
        self.setCentralWidget(self.main_canvas)
        self.main_canvas.setStyleSheet("background-color: #f0f0f0)")
#part 4 layout isolation and centering
        self.outer_layout = QVBoxLayout(self.main_canvas)#a vertical layout 
        self.login_card = QWidget()
        self.login_card.setFixedHeight(300)
        self.login_card.setFixedWidth(400)

        self.login_card.setStyleSheet("""
            QWidget {
            background-color: #ffffff;
            border-radius: 8px;
            }
                                      
            QLabel {
            font-size: 18px;
            font-weight: bold;
            borner: none;
            font-family: Arial, sans-serif;
            }
                                      
            QLineEdit {
            background-color: #f0f0f0;
            color: #333333;
            border: 1px solid #cccccc;
            border-radius: 4px;
            padding: 6px;
            font-size: 14px;
            }
                                      
            QPushButton {
            background-color: #007acc;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            padding: 10px;
            font-size: 14px;
            font-weight: bold;
            }
            QPushButton:hover {
            background-color: #005f99;
            }
        """)
        self.outer_layout.addWidget(self.login_card, alignment=Qt.AlignmentFlag.AlignCenter)

    #part 5 grid matrix
        #initialize spreadsheet layout matrix
        self.grid = QGridLayout(self.login_card)

        #set padding between card and widgets (left, top, right bottom)
        self.grid.setContentsMargins(30, 30, 30, 30)
        #set spacing between widgets 
        self.grid.setSpacing(15)

        #row 0 - title label
        self.title_label = QLabel("CalorieX Login!")
        self.title_label.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 10px;")
        self.grid.addWidget(self.title_label, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)

        #row 1 - Username setup
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit() 
        self.username_input.setPlaceholderText("Enter your username")
        self.grid.addWidget(self.username_label, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        self.grid.addWidget(self.username_input, 1, 1)

        #row 2 - Password setup
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.grid.addWidget(self.password_label, 2, 0)

        self.login_card.setLayout(self.grid)
        self.grid.addWidget(self.password_input, 2, 1)
        #row 3 - Login button
        self.login_button = QPushButton("Login")
        self.grid.addWidget(self.login_button, 3, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
    #part 6 event pipelines
        self.login_button.clicked.connect(self.handle_login_attempt)
    def handle_login_attempt(self):


        username = self.username_input.text()
        password = self.password_input.text()

        print(f"Username: {username}, Password: {password}")

        if username == "admin" and password == "password":
            print("Login successful!")
        else:
            print("Login failed. Please check your credentials.")

#part 7 main loop
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())

#TODO - add error handling for empty fields
#    - create a registration page
#     - add password recovery options
#      - implement actual authentication logic (e.g., check against a database)