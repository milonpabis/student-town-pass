from UI.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, QSize, QDate
from PySide6.QtGui import QIcon, QFont, QPixmap
from faker import Faker, DATE


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("AGH ID Faker App")
        self.setWindowIcon(QIcon("UI/icons/AGH.png"))
        self.year: str = ""
        self.month: str = ""
        self.day: str = ""
        self.name: str = ""
        self.second_name: str = ""
        self.surname: str = ""
        self.photo: str = ""
        self.album: str = ""
        self.show_day: str = ""
        self.show_month: str = ""
        self.pesel: str = ""
        self.dir: str = ""
        self.random: bool = False

        self.bt_generate.pressed.connect(self._generate)
        self.bt_addphoto.pressed.connect(self._add_photo)
        self.bt_savedir.pressed.connect(self._save_dir)
        self.check_random.stateChanged.connect(self._checked_random)

        self.de_showdate.setDate(QDate(DATE.year, DATE.month, DATE.day))

    def _generate(self):
        self._receive_data()
        if self._check_inputs():
            Faker(year=self.year, month=self.month, day=self.day, name=self.name, second_name=self.second_name,
                  surname=self.surname, photo=self.photo, album=self.album, show_day=self.show_day,
                  show_month=self.show_month, pesel=self.pesel, directory=self.dir, random=self.random)
        else:
            msg = QMessageBox()
            msg.setText("Missing values!")
            msg.setFont(QFont("Fixedsys", 11))
            msg.setWindowTitle("Ooops!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

    def _check_inputs(self) -> bool:
        if (self.name and self.second_name and self.surname and self.dir and self.photo and self.show_month
                and self.show_day):
            if (not self.random and self.year and self.month and self.day and self.album and self.pesel) or self.random:
                return True
        return False

    def _save_dir(self):
        dialog = QFileDialog.getSaveFileName(self, "Save as",
                                             "id.jpg",
                                             "Images (*.jpg *.png);;All Files (*)",
                                             "Images (*.jpg *.png)")
        self.dir = dialog[0]
        self.le_savedir.setText(self.dir)

    def _add_photo(self):
        dialog = QFileDialog.getOpenFileName(self, "Choose image",
                                             "id.jpg",
                                             "Images (*.jpg *.png);;All Files (*)",
                                             "Images (*.jpg *.png)")
        self.photo = dialog[0]
        self.l_photo.setPixmap(QPixmap(self.photo))

    def _receive_data(self):
        self.name = self.le_fname.text().upper()
        self.second_name = self.le_secname.text().upper()
        self.surname = self.le_surname.text().upper()
        self.show_day = str(self.de_showdate.date().day())
        self.show_month = str(self.de_showdate.date().month())
        self.random = self.check_random.isChecked()
        self.pesel = self.le_pesel.text()
        self.album = self.le_album.text()
        self.year = str(self.de_birth.date().year())
        self.month = str(self.de_birth.date().month())
        self.day = str(self.de_birth.date().day())

    def _checked_random(self):
        if self.check_random.isChecked():
            self.le_pesel.setDisabled(True)
            self.le_album.setDisabled(True)
            self.de_birth.setDisabled(True)
        else:
            self.le_pesel.setDisabled(False)
            self.le_album.setDisabled(False)
            self.de_birth.setDisabled(False)


if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec()
