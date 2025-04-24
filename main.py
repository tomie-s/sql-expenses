# Running the application
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from app import ExpenseApp


def main():
    app = QApplication(sys.argv)  # Create a QApplication instance
    window = ExpenseApp()  # Create an instance of the ExpenseApp class
    window.show()  # Show the main window
    sys.exit(app.exec())  # Start the event loop and exit when done


if __name__ == "__main__":
    main()  # Call the main function to run the application
