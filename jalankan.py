from PyQt5.QtWidgets import QApplication
from tugask import MainWindow

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())