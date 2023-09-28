# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setMinimumSize(QSize(600, 800))
        MainWindow.setMaximumSize(QSize(600, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_logo = QFrame(self.centralwidget)
        self.fr_logo.setObjectName(u"fr_logo")
        self.fr_logo.setMaximumSize(QSize(16777215, 100))
        self.fr_logo.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.fr_logo.setFrameShape(QFrame.NoFrame)
        self.fr_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_logo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.l_logo = QLabel(self.fr_logo)
        self.l_logo.setObjectName(u"l_logo")
        self.l_logo.setMaximumSize(QSize(100, 100))
        self.l_logo.setPixmap(QPixmap(u"UI/icons/AGH.png"))
        self.l_logo.setScaledContents(True)
        self.l_logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.l_logo)


        self.verticalLayout.addWidget(self.fr_logo)

        self.fr_title = QFrame(self.centralwidget)
        self.fr_title.setObjectName(u"fr_title")
        self.fr_title.setMaximumSize(QSize(16777215, 80))
        self.fr_title.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.fr_title.setFrameShape(QFrame.NoFrame)
        self.fr_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fr_title)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.l_title = QLabel(self.fr_title)
        self.l_title.setObjectName(u"l_title")
        font = QFont()
        font.setFamilies([u"Terminal"])
        font.setPointSize(15)
        font.setBold(True)
        self.l_title.setFont(font)
        self.l_title.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.l_title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_3.addWidget(self.l_title)


        self.verticalLayout.addWidget(self.fr_title)

        self.fr_body = QFrame(self.centralwidget)
        self.fr_body.setObjectName(u"fr_body")
        self.fr_body.setMaximumSize(QSize(16777215, 100142))
        self.fr_body.setFrameShape(QFrame.NoFrame)
        self.fr_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_body)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fr_bodybody = QFrame(self.fr_body)
        self.fr_bodybody.setObjectName(u"fr_bodybody")
        self.fr_bodybody.setFrameShape(QFrame.StyledPanel)
        self.fr_bodybody.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_bodybody)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_body_left = QFrame(self.fr_bodybody)
        self.fr_body_left.setObjectName(u"fr_body_left")
        self.fr_body_left.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.fr_body_left.setFrameShape(QFrame.NoFrame)
        self.fr_body_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.fr_body_left)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.fr_body_l = QFrame(self.fr_body_left)
        self.fr_body_l.setObjectName(u"fr_body_l")
        self.fr_body_l.setFrameShape(QFrame.StyledPanel)
        self.fr_body_l.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fr_body_l)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.fr_body_l)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(600, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(200, 202, 214);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.l_fname = QLabel(self.frame_2)
        self.l_fname.setObjectName(u"l_fname")
        self.l_fname.setMinimumSize(QSize(125, 0))
        self.l_fname.setMaximumSize(QSize(125, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Fixedsys"])
        self.l_fname.setFont(font1)
        self.l_fname.setStyleSheet(u"\n"
"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")

        self.horizontalLayout_5.addWidget(self.l_fname)

        self.le_fname = QLineEdit(self.frame_2)
        self.le_fname.setObjectName(u"le_fname")
        self.le_fname.setMinimumSize(QSize(120, 25))
        self.le_fname.setMaximumSize(QSize(120, 25))
        self.le_fname.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"gridline-color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(250, 244, 255);")
        self.le_fname.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.le_fname)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.fr_body_l)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(600, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(200, 202, 214);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.l_secname = QLabel(self.frame_3)
        self.l_secname.setObjectName(u"l_secname")
        self.l_secname.setMinimumSize(QSize(125, 0))
        self.l_secname.setMaximumSize(QSize(125, 16777215))
        self.l_secname.setFont(font1)
        self.l_secname.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")

        self.horizontalLayout_6.addWidget(self.l_secname)

        self.le_secname = QLineEdit(self.frame_3)
        self.le_secname.setObjectName(u"le_secname")
        self.le_secname.setMinimumSize(QSize(120, 25))
        self.le_secname.setMaximumSize(QSize(120, 25))
        self.le_secname.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(250, 244, 255);")
        self.le_secname.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.le_secname)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.fr_body_l)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(600, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(200, 202, 214);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.l_surname = QLabel(self.frame_4)
        self.l_surname.setObjectName(u"l_surname")
        self.l_surname.setMinimumSize(QSize(125, 0))
        self.l_surname.setMaximumSize(QSize(125, 16777215))
        self.l_surname.setFont(font1)
        self.l_surname.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")

        self.horizontalLayout_7.addWidget(self.l_surname)

        self.le_surname = QLineEdit(self.frame_4)
        self.le_surname.setObjectName(u"le_surname")
        self.le_surname.setMinimumSize(QSize(120, 25))
        self.le_surname.setMaximumSize(QSize(120, 25))
        self.le_surname.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(250, 244, 255);")
        self.le_surname.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.le_surname)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.fr_body_l)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(600, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(200, 202, 214);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.l_showdate = QLabel(self.frame_5)
        self.l_showdate.setObjectName(u"l_showdate")
        self.l_showdate.setMinimumSize(QSize(125, 0))
        self.l_showdate.setMaximumSize(QSize(125, 16777215))
        self.l_showdate.setFont(font1)
        self.l_showdate.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")

        self.horizontalLayout_8.addWidget(self.l_showdate)

        self.de_showdate = QDateEdit(self.frame_5)
        self.de_showdate.setObjectName(u"de_showdate")
        self.de_showdate.setMaximumSize(QSize(120, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Fixedsys"])
        font2.setPointSize(11)
        self.de_showdate.setFont(font2)
        self.de_showdate.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(237, 244, 255);")

        self.horizontalLayout_8.addWidget(self.de_showdate)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.fr_body_l)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(600, 16777215))
        self.frame_6.setStyleSheet(u"background-color: rgb(200, 202, 214);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setSpacing(90)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 85, -1)
        self.l_random = QLabel(self.frame_6)
        self.l_random.setObjectName(u"l_random")
        self.l_random.setMinimumSize(QSize(125, 0))
        self.l_random.setMaximumSize(QSize(125, 16777215))
        self.l_random.setFont(font1)
        self.l_random.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.l_random.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.l_random)

        self.check_random = QCheckBox(self.frame_6)
        self.check_random.setObjectName(u"check_random")
        self.check_random.setMaximumSize(QSize(15, 15))
        self.check_random.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.check_random)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.fr_body_l)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(600, 16777215))
        self.frame_7.setStyleSheet(u"background-color: rgb(200, 202, 214);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.l_birth = QLabel(self.frame_7)
        self.l_birth.setObjectName(u"l_birth")
        self.l_birth.setMinimumSize(QSize(125, 0))
        self.l_birth.setMaximumSize(QSize(125, 16777215))
        self.l_birth.setFont(font1)
        self.l_birth.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")

        self.horizontalLayout_10.addWidget(self.l_birth)

        self.de_birth = QDateEdit(self.frame_7)
        self.de_birth.setObjectName(u"de_birth")
        self.de_birth.setMaximumSize(QSize(120, 16777215))
        self.de_birth.setFont(font2)
        self.de_birth.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(237, 244, 255);")

        self.horizontalLayout_10.addWidget(self.de_birth)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.fr_body_l)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(600, 16777215))
        self.frame_8.setStyleSheet(u"background-color: rgb(200, 202, 214);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.l_pesel = QLabel(self.frame_8)
        self.l_pesel.setObjectName(u"l_pesel")
        self.l_pesel.setMinimumSize(QSize(125, 0))
        self.l_pesel.setMaximumSize(QSize(125, 16777215))
        self.l_pesel.setFont(font1)
        self.l_pesel.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")

        self.horizontalLayout_11.addWidget(self.l_pesel)

        self.le_pesel = QLineEdit(self.frame_8)
        self.le_pesel.setObjectName(u"le_pesel")
        self.le_pesel.setMinimumSize(QSize(120, 25))
        self.le_pesel.setMaximumSize(QSize(120, 25))
        self.le_pesel.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(250, 244, 255);")
        self.le_pesel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.le_pesel)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.fr_body_l)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(600, 16777215))
        self.frame_9.setStyleSheet(u"background-color: rgb(200, 202, 214);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.l_album = QLabel(self.frame_9)
        self.l_album.setObjectName(u"l_album")
        self.l_album.setMinimumSize(QSize(125, 0))
        self.l_album.setMaximumSize(QSize(125, 16777215))
        self.l_album.setFont(font1)
        self.l_album.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")

        self.horizontalLayout_12.addWidget(self.l_album)

        self.le_album = QLineEdit(self.frame_9)
        self.le_album.setObjectName(u"le_album")
        self.le_album.setMinimumSize(QSize(120, 25))
        self.le_album.setMaximumSize(QSize(120, 25))
        self.le_album.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(250, 244, 255);")
        self.le_album.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.le_album)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.fr_body_l)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(600, 16777215))
        self.frame_10.setStyleSheet(u"background-color: rgb(200, 202, 214);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.l_savedir = QLabel(self.frame_10)
        self.l_savedir.setObjectName(u"l_savedir")
        self.l_savedir.setMinimumSize(QSize(125, 0))
        self.l_savedir.setMaximumSize(QSize(125, 16777215))
        self.l_savedir.setFont(font1)
        self.l_savedir.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")

        self.horizontalLayout_13.addWidget(self.l_savedir)

        self.le_savedir = QLineEdit(self.frame_10)
        self.le_savedir.setObjectName(u"le_savedir")
        self.le_savedir.setMinimumSize(QSize(180, 25))
        self.le_savedir.setMaximumSize(QSize(180, 25))
        self.le_savedir.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(250, 244, 255);")

        self.horizontalLayout_13.addWidget(self.le_savedir)

        self.bt_savedir = QPushButton(self.frame_10)
        self.bt_savedir.setObjectName(u"bt_savedir")
        self.bt_savedir.setMinimumSize(QSize(30, 30))
        self.bt_savedir.setMaximumSize(QSize(30, 30))
        self.bt_savedir.setFont(font1)
        self.bt_savedir.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")

        self.horizontalLayout_13.addWidget(self.bt_savedir)


        self.verticalLayout_3.addWidget(self.frame_10)


        self.horizontalLayout_4.addWidget(self.fr_body_l)

        self.fr_body_r = QFrame(self.fr_body_left)
        self.fr_body_r.setObjectName(u"fr_body_r")
        self.fr_body_r.setMinimumSize(QSize(180, 0))
        self.fr_body_r.setMaximumSize(QSize(180, 16777215))
        self.fr_body_r.setStyleSheet(u"background-color: rgb(200, 202, 214);")
        self.fr_body_r.setFrameShape(QFrame.NoFrame)
        self.fr_body_r.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fr_body_r)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.fr_body_r)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(40, 130, -1, -1)
        self.l_photo = QLabel(self.frame)
        self.l_photo.setObjectName(u"l_photo")
        self.l_photo.setMinimumSize(QSize(80, 104))
        self.l_photo.setMaximumSize(QSize(80, 104))
        self.l_photo.setFrameShape(QFrame.NoFrame)
        self.l_photo.setPixmap(QPixmap(u"UI/icons/chooseimage.jpg"))
        self.l_photo.setScaledContents(True)
        self.l_photo.setAlignment(Qt.AlignCenter)
        self.l_photo.setWordWrap(False)

        self.verticalLayout_5.addWidget(self.l_photo)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_11 = QFrame(self.fr_body_r)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(40, -1, -1, 230)
        self.bt_addphoto = QPushButton(self.frame_11)
        self.bt_addphoto.setObjectName(u"bt_addphoto")
        self.bt_addphoto.setMinimumSize(QSize(80, 0))
        self.bt_addphoto.setMaximumSize(QSize(80, 30))
        self.bt_addphoto.setFont(font2)
        self.bt_addphoto.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")

        self.verticalLayout_6.addWidget(self.bt_addphoto)


        self.verticalLayout_4.addWidget(self.frame_11)


        self.horizontalLayout_4.addWidget(self.fr_body_r)


        self.horizontalLayout.addWidget(self.fr_body_left)


        self.verticalLayout_2.addWidget(self.fr_bodybody)

        self.fr_foot = QFrame(self.fr_body)
        self.fr_foot.setObjectName(u"fr_foot")
        self.fr_foot.setMaximumSize(QSize(16777215, 80))
        self.fr_foot.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.fr_foot.setFrameShape(QFrame.NoFrame)
        self.fr_foot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.fr_foot)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.bt_generate = QPushButton(self.fr_foot)
        self.bt_generate.setObjectName(u"bt_generate")
        self.bt_generate.setMaximumSize(QSize(90, 16777215))
        self.bt_generate.setFont(font2)
        self.bt_generate.setStyleSheet(u"color: qlineargradient(spread:reflect, x1:0, y1:0.534, x2:1, y2:0.523, stop:0 rgba(0, 142, 0, 255), stop:0.513812 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")

        self.horizontalLayout_14.addWidget(self.bt_generate)


        self.verticalLayout_2.addWidget(self.fr_foot)


        self.verticalLayout.addWidget(self.fr_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.l_logo.setText("")
        self.l_title.setText(QCoreApplication.translate("MainWindow", u"AGH Identificator Faker App", None))
        self.l_fname.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.l_secname.setText(QCoreApplication.translate("MainWindow", u"Second Name", None))
        self.l_surname.setText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.l_showdate.setText(QCoreApplication.translate("MainWindow", u"Show Date", None))
        self.l_random.setText(QCoreApplication.translate("MainWindow", u"Random Info", None))
        self.check_random.setText("")
        self.l_birth.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.l_pesel.setText(QCoreApplication.translate("MainWindow", u"PESEL", None))
        self.l_album.setText(QCoreApplication.translate("MainWindow", u"Album No.", None))
        self.l_savedir.setText(QCoreApplication.translate("MainWindow", u"Save Directory", None))
        self.bt_savedir.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.l_photo.setText("")
        self.bt_addphoto.setText(QCoreApplication.translate("MainWindow", u"Add Photo", None))
        self.bt_generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

