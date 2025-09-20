# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QMainWindow
import sys
import webbrowser
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# ==Init Application==
app = QApplication(sys.argv)

# ===Main Window Class===
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Windows Game Launcher")

        # Load UI
        self.ui = loadUI("mainwindow.ui")
        self.setCentralWidget(self.ui)

        # Menu bar actions
        self.ui.actionGithub.triggered.connect(openGithub)
        self.ui.actionExit.triggered.connect(sys.exit)
        self.ui.actionSettings.triggered.connect(None)

# ==Load .ui file==
def loadUI(filename):
    file = QFile(filename)
    if not file.open(QFile.ReadOnly):
        raise RuntimeError(f"Cannot open {filename}: {file.errorString()}")
    loader = QUiLoader()
    ui = loader.load(file)
    file.close()
    if ui is None:
        raise RuntimeError(f"Failed to load {filename}")
    return ui

# ==Menu bar buttons==
def openGithub():
    webbrowser.open("https://github.com/archmandan/windows_launcher")

def main():
    window = MainWindow()

    window.show()

    app.exec()

if __name__ == "__main__":
    main()