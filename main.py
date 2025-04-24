# Running the application
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from app import ExpenseApp
from database import init_db


def main():
    app = QApplication(sys.argv)  # Create a QApplication instance

    if not init_db("expenseapp.db"):
        # If the database initialization fails, show an error message and exit
        QMessageBox.critical(None, "Error", "Failed to load the database.")
        sys.exit(1)

    window = ExpenseApp()  # Create an instance of the ExpenseApp class
    window.show()  # Show the main window
    sys.exit(app.exec())  # Start the event loop and exit when done


if __name__ == "__main__":
    main()  # Call the main function to run the application
