

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile

from game.gui import field
from game.sea import sea

class Main(QtWidgets.QMainWindow):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(500, 500)
        self.central = QtWidgets.QFrame(self)
        self.setCentralWidget(self.central)
        self.box = QtWidgets.QHBoxLayout(self.central)

        self.sea = sea.Sea()
        # self.sea.create_fleet()
        self.field = field.Field("pc", self.sea)
        self.box.addWidget(self.field)
        self.field.update_sea()



    def load_style_sheet(self, sheetName):
        """

        :param sheetName: str имя стиля
        """
        file_name = sheetName + '.css'
        file = QFile('../css/{}'.format(file_name))
        file.open(QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        QtWidgets.QApplication.instance().setStyleSheet(styleSheet)

    def wheelEvent(self, event):
        if event.angleDelta().y() / 120 > 0:
            self.sea.create_fleet()
            self.field.update_sea()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    main.load_style_sheet("grey")
    sys.exit(app.exec_())