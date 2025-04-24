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
        self.init_ui()  # Call the initUI method to set up the user interface

    def settings(self):
        self.setWindowTitle("Expense Tracker App")
        self.setGeometry(300, 300, 800, 600)

    # Design
    def init_ui(self):
        # create all objects
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.btn_add = QPushButton("Add Expense")
        self.btn_delete = QPushButton("Delete Expense")

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["ID", "Date", "Category", "Amount", "Description"])
        # table width equal to the window width
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.setup_layout()  # Call the method to set up the layout

    # Add widget to the layout (Row/Column)
    def setup_layout(self):
        # Create a vertical layout for the main window
        main_layout = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        # Row 1
        row1.addWidget(QLabel("Date:"))
        row1.addWidget(self.date_box)
        row1.addWidget(QLabel("Category:"))
        row1.addWidget(self.dropdown)

        # Row 2
        row2.addWidget(QLabel("Amount:"))
        row2.addWidget(self.amount)
        row2.addWidget(QLabel("Description:"))
        row2.addWidget(self.description)

        # Row 3
        row3.addWidget(self.btn_add)
        row3.addWidget(self.btn_delete)

        main_layout.addLayout(row1)
        main_layout.addLayout(row2)
        main_layout.addLayout(row3)
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)  # Set the main layout for the window

