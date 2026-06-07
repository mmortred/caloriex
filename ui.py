#part 1
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, 
    QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

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
        self.main_canvas.setStyleSheet("background-color: #2b2b2b;")

#part 4 layout isolation and centering
        self.outer_layout = QVBoxLayout(self.main_canvas)#a vertical layout 

#4.5 main content card (left and right)
        self.login_card = QWidget()
        self.login_card.setFixedSize(800,500)
        
#global
        self.login_card.setStyleSheet("""
            QWidget #left_panel {
            background-color: #3aafa9;
            border-top-left-radius: 15px;
            border-radius: 20px;
            }
            QWidget #right_panel {
            background-color: #ffffff;
            border-top-right-radius: 15px;
            border-radius: 20px;
            }
                                      
            QLineEdit {
            background-color: #f4f7f6;
            color: #333333;
            border-bottom: 2px solid #cccccc;
            border-radius: 5px;
            padding: 8px 4px;
            font-size: 14px;
            }                              
                                      
            QPushButton #action_btn{
            background-color: #3aafa9;
            color: #ffffff;
            border: none;
            border-radius: 20px;
            padding: 12px 40px;
            font-size: 14px;
            font-weight: bold;
            }
                                      
            QPushButton:hover {
            background-color: black;
            }
                                      
            QPushButton #ghost_btn{
            background-color: blue;
            color: #3aafa9;
            border: 2px solid #3aafa9;
            border-radius: 20px;
            padding: 12px 40px;
            font-size: 14px;
            font-weight: bold;    
            }
            QPushButton#ghost_btn:hover {
            background-color: rgba(255, 255, 255, 0.2);
            }                     
        """)

        self.outer_layout.addWidget(self.login_card, alignment=Qt.AlignmentFlag.AlignCenter)
        

        #split the card horizontally
        self.card_layout = QHBoxLayout(self.login_card)
        self.card_layout.setContentsMargins(0, 0, 0, 0)
        self.card_layout.setSpacing(0)

        #left panel -----------------------------------
        self.left_panel = QWidget()
        self.left_panel.setObjectName("left_panel")
        self.left_layout = QVBoxLayout(self.left_panel) 
        self.left_layout.setContentsMargins(40, 40, 40, 40)
        self.left_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.left_title = QLabel("Welcome Back!")
        self.left_title.setStyleSheet("color: white; font-size: 32px; font-weight: bold; background: transparent;")

        self.left_desc = QLabel("Please login to your account")
        self.left_desc.setStyleSheet("color: #ffffff; font-size: 16px; margin-bottom: 30px; background: transparent;")
        self.left_desc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.switch_to_login_btn = QPushButton("Sign In")
        self.switch_to_login_btn.setObjectName("ghost_btn")

        self.left_layout.addWidget(self.left_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.left_layout.addSpacing(20)
        self.left_layout.addWidget(self.left_desc, alignment=Qt.AlignmentFlag.AlignCenter)
        self.left_layout.addSpacing(30)
        self.left_layout.addWidget(self.switch_to_login_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        #right panel -----------------------------------
        self.right_panel = QWidget()
        self.right_panel.setObjectName("right_panel")
        self.right_layout = QVBoxLayout(self.right_panel)
        self.right_layout.setContentsMargins(50, 40, 40, 40)
        self.right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.right_title = QLabel("Create Your Account")
        self.right_title.setStyleSheet("color: #3aafa9; font-size: 32px; font-weight: bold; background: transparent;")       

        self.social_label = QLabel("Or use your email for registration")
        self.social_label.setStyleSheet("color: #333333; font-size: 16px; margin-bottom: 30px; background: transparent;")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
    
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color: #2b8882; font-size: 12px; font-weight: bold; background: transparent;")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


      

        self.signup_btn = QPushButton("Sign Up")
        self.signup_btn.setObjectName("action_btn")

        self.right_layout.addWidget(self.right_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.right_layout.addSpacing(15)
        self.right_layout.addWidget(self.social_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.right_layout.addSpacing(15)

        self.right_layout.addWidget(self.name_input)
        self.right_layout.addWidget(self.email_input)
        self.right_layout.addWidget(self.password_input)

        self.right_layout.addWidget(self.status_label)
        self.right_layout.addSpacing(15)
        self.right_layout.addWidget(self.signup_btn, alignment=Qt.AlignmentFlag.AlignCenter) 

        #assemble panels into card
        self.card_layout.addWidget(self.left_panel, stretch=4)
        self.card_layout.addWidget(self.right_panel, stretch=6)

        #event pipelines
        self.signup_btn.clicked.connect(self.handle_registration_attempt)
        self.switch_to_login_btn.clicked.connect(self.handle_switch_view)

    def handle_registration_attempt(self):
        name = self.name_input.text()
        email = self.email_input.text()
        password = self.password_input.text()

        #empty field validation (placeholder for actual logic)
        if not name or not email or not password:
            self.status_label.setText("Please fill in all fields.")
        else:
            self.status_label.setText("Registration successful! (placeholder)")
        
        if "@" not in email or "." not in email:
            self.status_label.setText("Please enter a valid email address.")
            return
        
        self.status_label.setStyleSheet("color: #2b8882; font-size: 12px; font-weight: bold; background: transparent;")
        self.status_label.setText("Registration successful! (Simulated)")
        print(f"Registered User -> Name: {name}, Email: {email}, Password: {password}")
        
        # TODO: Implement actual database or backend verification logic here

    def handle_switch_view(self):
        print("Redirecting user to the Login interface pane...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Optional: Setting crisp default font rendering for app windows
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())