from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QFileDialog

class MainWindow:
    def __init__(self):
        ui_path = Path(__file__).with_name("main_window.ui")

        ui_file = QFile(str(ui_path))
        ui_file.open(QFile.OpenModeFlag.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)

        ui_file.close()

        if self.window is None:
            raise RuntimeError(loader.errorString())

        # put this down here after we have verified that self.window is valid
        self.window.actionLoad.triggered.connect(self.load_action)

    def show(self):
        self.window.show()

    def load_action(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.window,
            "Open File",
            "",
            "Supported Files (*.svg *.gcode *.nc *.tap);;"
            "SVG Files (*.svg);;"
            "G-code Files (*.gcode *.nc *.tap);;"
            "All Files (*)",
        )

        if filename:
            print(f"You selected {filename}")
