# App Design
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit, QTableWidget, QVBoxLayout, \
    QHBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt, QDate


# QWidget represents the main window of the application
# Alternative is QMainWindow
class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()  # Initialize the parent class QWidget
        self.settings()  # Call the settings method to set up the window properties

    def settings(self):
        self.setWindowTitle("Expense Tracker App")
        self.setGeometry(300, 300, 800, 600)
