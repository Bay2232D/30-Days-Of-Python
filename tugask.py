import sqlite3
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox, QTableView, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Aplikasi Data Mahasiswa")
        self.setGeometry(100, 100, 800, 600)

        # Set stylesheet for the entire application
        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                font-family: Arial;
            }
            QLabel {
                font-weight: bold;
                font-size: 16px;
                color: #ecf0f1;
            }
            QLineEdit {
                border: 2px solid #34495e;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                background-color: #ecf0f1;
                color: #2c3e50;
            }
            QPushButton {
                background-color: #3e7fbf;
                border: none;
                border-radius: 10px;
                padding: 10px;
                color: white;
                font-size: 14px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QTableView {
                background-color: #ecf0f1;
                border: 1px solid #34495e;
                color: #2c3e50;
            }
            QHeaderView::section {
                background-color: #3e7fbf;
                color: white;
                padding: 5px;
                border: 1px solid #34495e;
            }
        """)

        # Header
        header_label = QLabel("Aplikasi Data Mahasiswa")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("font-size: 24px; margin-bottom: 20px;")

        self.id_label = QLabel("ID:")
        self.id_input = QLineEdit()
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.kelas_label = QLabel("Kelas:")
        self.kelas_input = QLineEdit()

        self.create_button = QPushButton("Create")
        self.create_button.setIcon(QIcon("icons/create.png"))
        self.read_button = QPushButton("Read")
        self.read_button.setIcon(QIcon("icons/read.png"))
        self.update_button = QPushButton("Update")
        self.update_button.setIcon(QIcon("icons/update.png"))
        self.delete_button = QPushButton("Delete")
        self.delete_button.setIcon(QIcon("icons/delete.png"))

        # Layouts for form inputs
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.id_label)
        form_layout.addWidget(self.id_input)
        form_layout.addWidget(self.name_label)
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.kelas_label)
        form_layout.addWidget(self.kelas_input)

        # Layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.create_button)
        button_layout.addWidget(self.read_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(header_label)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.table_view = QTableView()
        main_layout.addWidget(self.table_view)
        self.setLayout(main_layout)

        self.create_button.clicked.connect(self.create_user)
        self.read_button.clicked.connect(self.read_user)
        self.update_button.clicked.connect(self.update_user)
        self.delete_button.clicked.connect(self.delete_user)

        self.conn = sqlite3.connect('users.db')
        self.create_table()
        self.load_data()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS users')
        cursor.execute('''
            CREATE TABLE users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                kelas TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def load_data(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('users.db')
        db.open()

        self.model = QSqlTableModel()
        self.model.setTable('users')
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def create_user(self):
        id = self.id_input.text()
        name = self.name_input.text()
        kelas = self.kelas_input.text()
        if not id or not name or not kelas:
            QMessageBox.warning(self, "Error", "Please fill all fields.")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (id, name, kelas) VALUES (?, ?, ?)", (id, name, kelas))
            self.conn.commit()
            QMessageBox.information(self, "Success", "User created successfully.")
            self.clear_inputs()
            self.load_data()  # Refresh the table view
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Error", "User with this ID already exists.")

    def read_user(self):
        id = self.id_input.text()
        if not id:
            QMessageBox.warning(self, "Error", "Please enter an ID.")
            return

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (id,))
        user = cursor.fetchone()
        if user:
            self.name_input.setText(user[1])
            self.kelas_input.setText(user[2])
        else:
            QMessageBox.warning(self, "Error", "User not found.")
            self.clear_inputs()

    def update_user(self):
        id = self.id_input.text()
        name = self.name_input.text()
        kelas = self.kelas_input.text()
        if not id or not name or not kelas:
            QMessageBox.warning(self, "Error", "Please fill all fields.")
            return

        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET name=?, kelas=? WHERE id=?", (name, kelas, id))
        self.conn.commit()
        if cursor.rowcount > 0:
            QMessageBox.information(self, "Success", "User updated successfully.")
            self.clear_inputs()
            self.load_data()  # Refresh the table view
        else:
            QMessageBox.warning(self, "Error", "User not found.")

    def delete_user(self):
        id = self.id_input.text()
        if not id:
            QMessageBox.warning(self, "Error", "Please enter an ID.")
            return

        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=?", (id,))
        self.conn.commit()
        if cursor.rowcount > 0:
            QMessageBox.information(self, "Success", "User deleted successfully.")
            self.clear_inputs()
            self.load_data()  # Refresh the table view
        else:
            QMessageBox.warning(self, "Error", "User not found.")

    def clear_inputs(self):
        self.id_input.clear()
        self.name_input.clear()
        self.kelas_input.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
