# App Design
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit, QTableWidget, QVBoxLayout, \
    QHBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt, QDate
from database import add_expense, delete_expense, get_expenses


# QWidget represents the main window of the application
# Alternative is QMainWindow
class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()  # Initialize the parent class QWidget
        self.settings()  # Call the settings method to set up the window properties
        self.init_ui()  # Call the initUI method to set up the user interface
        self.load_table_data()

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
        self.table.setHorizontalHeaderLabels(
            ["ID", "Date", "Category", "Amount", "Description"])
        # table width equal to the window width
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.populate_dropdown()  # Call the method to populate the dropdown with categories

        # Connect buttons to their respective functions
        self.btn_add.clicked.connect(self.add_new_expense)
        self.btn_delete.clicked.connect(self.delete_expense)

        self.apply_styles()  # Call the method to apply CSS styles

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

    # Apply CSS styles to the widgets
    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #e3e9f2;
                font-family: Arial, sans-serif;
                font-size: 14px;
                color: #333;
            }
            QLabel {
                font-size: 16px;
                color: #2c3e50;
                font-weight: bold;
                padding: 5px;
            }
            QLineEdit, QComboBox, QDateEdit {
                background-color: #FFF;
                font-size: 14px;
                color: #333;
                padding: 5px;
                border: 1px solid #b0bfc6;
                border-radius: 6px;
            }
            QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
                border: 1px solid #2a9d8f;
                background-color: #f5f9fc;
            }
            QLineEdit:hover, QComboBox:hover, QDateEdit:hover {
                border: 1px solid #4caf50;
            }
            QTableWidget {
                background-color: #FFF;
                alternate-background-color: #f2f7fb;
                gridline-color: #c0c9d0;
                selection-background-color: #4caf50;
                selection-color: white;
                font-size: 14px;
                border: 1px solid #cfd9e1;
            }
            QPushButton {
                background-color: #007BFF;
                color: white;
                padding: 10px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

    # Function to add a new expense category for the dropdown
    def populate_dropdown(self):
        categories = ["Food", "Rent", "Entertainment",
                      "Utilities", "Shopping", "Other"]
        self.dropdown.addItems(categories)  # Add categories to the dropdown

    # Function to display the data from DB in the table
    def load_table_data(self):
        expenses = get_expenses()
        self.table.setRowCount(len(expenses))
        for row, expense in enumerate(expenses):
            for column, data in enumerate(expense):
                self.table.setItem(row, column, QTableWidgetItem(str(data)))

    # Function to clear the input fields after adding the expense
    def clear_inputs(self):
        self.date_box.setDate(QDate.currentDate())
        self.dropdown.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()

    # Function to add an expense to the database

    def add_new_expense(self):
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        if not date or not category or not amount:
            QMessageBox.warning(self, "Input Error",
                                "Please fill in all fields.")
            return

        if add_expense(date, category, amount, description):
            self.load_table_data()
            self.clear_inputs()
        else:
            QMessageBox.critical(self, "Error", "Failed to add expense.")

    # Function to delete an expense from the database
    def delete_expense(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Selection Error",
                                "Please select an expense to delete.")
            return

        expense_id = int(self.table.item(selected_row, 0).text())
        confirm = QMessageBox.question(
            self, "Confirm Delete", "Are you sure you want to delete this expense?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        # If the user confirms, delete the expense
        if confirm == QMessageBox.StandardButton.Yes and delete_expense(expense_id):
            self.load_table_data()
        else:
            QMessageBox.critical(self, "Error", "Failed to delete expense.")
