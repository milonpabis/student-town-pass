from UI.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, QSize, QDate, QDateTime
from PySide6.QtGui import QIcon, QFont, QPixmap
from faker import Faker, DATE, UNIVERSITY_NAMES
import io


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.faker = Faker()

        self.setupUi(self)
        self.setWindowTitle("AGH ID Faker App")
        self.setWindowIcon(QIcon("UI/icons/AGH.png"))


        self.bt_generate.pressed.connect(self._generate)
        self.bt_addphoto.pressed.connect(self._add_photo)
        self.bt_savedir.pressed.connect(self._save_dir)

        self.le_fname.textChanged.connect(self._set_name)
        self.le_secname.textChanged.connect(self._set_second_name)
        self.le_surname.textChanged.connect(self._set_surname)
        self.le_album.textChanged.connect(self._set_album)
        self.de_birth.dateChanged.connect(self._set_date)
        self.de_showdate.dateTimeChanged.connect(self._set_show_date)
        self.cb_university.currentIndexChanged.connect(self._set_university)
        


        self.de_showdate.setDateTime(QDateTime(DATE.year, DATE.month, DATE.day, DATE.hour, DATE.minute, DATE.second))
        self.de_birth.setDate(QDate(DATE.year-20, DATE.month, DATE.day))
        self._populate_universities()


    def _generate(self):
        if self._check_inputs():
            print("SAVING", self.faker.directory, "\n", self.faker.image)
            self.faker.image.save(self.faker.directory)
        else:
            msg = QMessageBox()
            msg.setText("Missing values!")
            msg.setFont(QFont("Fixedsys", 11))
            msg.setWindowTitle("Ooops!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()


    def _update_preview(self) -> None:
        pixmap = QPixmap()
        image = self.faker._fake()
        pixmap.loadFromData(image.getvalue())
        self.l_preview.setPixmap(pixmap)


    def _check_inputs(self) -> bool:
        if all([self.faker.name, self.faker.second_name, self.faker.surname,
                self.faker.directory, self.faker.photo, self.faker.show_month,
                self.faker.album, self.faker.pesel, self.faker.university]):
            return True
        return False


    def _save_dir(self):
        dialog = QFileDialog.getSaveFileName(self, "Save as",
                                             "id.jpg",
                                             "Images (*.jpg *.png);;All Files (*)",
                                             "Images (*.jpg *.png)")
        self.faker.directory = dialog[0]
        self.le_savedir.setText(self.faker.directory)


    def _add_photo(self):
        dialog = QFileDialog.getOpenFileName(self, "Choose image",
                                             "id.jpg",
                                             "Images (*.jpg *.png);;All Files (*)",
                                             "Images (*.jpg *.png)")
        photo = dialog[0]
        self.l_photo.setPixmap(QPixmap(photo))
        self.faker.set_photo(photo)
        self._update_preview()


    def _populate_universities(self):
        self.cb_university.addItem("AGH")
        self.cb_university.addItem("UJ")
        self.cb_university.addItem("UP")
        self.cb_university.addItem("UEK")
        self.cb_university.addItem("PK")

        self.cb_university.setCurrentIndex(0)


    def _format_hour(self, hour: int, minute: int) -> str:
        if hour < 10:
            hour = "0" + str(hour)
        if minute < 10:
            minute = "0" + str(minute)
        return str(hour) + ":" + str(minute)
    

    def _set_name(self, name: str) -> None:
        self.faker.set_name(name.upper())
        self._update_preview()


    def _set_second_name(self, second_name: str) -> None:
        self.faker.set_second_name(second_name.upper())
        self._update_preview()


    def _set_surname(self, surname: str) -> None:
        self.faker.set_surname(surname.upper())
        self._update_preview()


    def _set_photo(self, photo: str) -> None:
        self.faker.set_photo(photo)
        self._update_preview()


    def _set_album(self, album: str) -> None:
        self.faker.set_album(album)
        self._update_preview()


    def _set_show_date(self, date: QDateTime) -> None:
        show_day = str(date.date().day())
        show_month = str(date.date().month())
        show_hour = self._format_hour(date.time().hour(), date.time().minute())
        self.faker.set_show_date(show_day, show_month, show_hour)
        self._update_preview()


    def _set_university(self, *args) -> None:
        self.faker.set_university(self.cb_university.currentText())
        self._update_preview()


    def _set_directory(self, directory: str) -> None:
        self.faker.set_directory(directory)
        self._update_preview()


    def _set_date(self, date: QDate) -> None:
        self.faker.set_date(str(date.year()), str(date.month()), str(date.day()))
        self.faker._gen_pesel()
        self._update_preview()


    def _set_age(self, age: str) -> None:
        self.faker.set_age(age)
        self._update_preview()

    




if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec()
