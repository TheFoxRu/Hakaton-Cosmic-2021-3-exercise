# -*- coding: utf-8 -*-

#  Copyright TheFox (c) 2021.

# Form implementation generated from reading ui file 'MainTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import requests
import translators
from loguru import logger
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from sqlalchemy import Column, create_engine, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker


class Ui_MainWindow(object):
    @logger.catch
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 600)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(206, 222, 242);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.labelTitle.setFont(font)
        self.labelTitle.setAutoFillBackground(False)
        self.labelTitle.setStyleSheet("color:rgb(242, 80, 80);")
        self.labelTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelTitle.setTextFormat(QtCore.Qt.AutoText)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setWordWrap(True)
        self.labelTitle.setOpenExternalLinks(True)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.tableMain = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableMain.sizePolicy().hasHeightForWidth())
        self.tableMain.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tableMain.setFont(font)
        self.tableMain.setStyleSheet("QHeaderView::section{background-color:rgb(191, 150, 99);color: rgb(191, 90, 54);} QTableWidget {background-color: rgb(167, 200, 242);}")
        self.tableMain.setFrameShape(QtWidgets.QFrame.Box)
        self.tableMain.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableMain.setLineWidth(1)
        self.tableMain.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableMain.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableMain.setObjectName("tableMain")
        self.tableMain.setColumnCount(7)
        self.tableMain.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        item.setBackground(QtGui.QColor(167, 200, 242))
        brush = QtGui.QBrush(QtGui.QColor(191, 90, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableMain.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        item.setBackground(QtGui.QColor(167, 200, 242))
        brush = QtGui.QBrush(QtGui.QColor(242, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableMain.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        item.setBackground(QtGui.QColor(167, 200, 242))
        brush = QtGui.QBrush(QtGui.QColor(242, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableMain.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        item.setBackground(QtGui.QColor(167, 200, 242))
        brush = QtGui.QBrush(QtGui.QColor(242, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableMain.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        item.setBackground(QtGui.QColor(167, 200, 242))
        brush = QtGui.QBrush(QtGui.QColor(242, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableMain.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        item.setBackground(QtGui.QColor(167, 200, 242))
        brush = QtGui.QBrush(QtGui.QColor(242, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableMain.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        item.setFont(font)
        item.setBackground(QtGui.QColor(167, 200, 242))
        brush = QtGui.QBrush(QtGui.QColor(242, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableMain.setHorizontalHeaderItem(6, item)
        self.tableMain.horizontalHeader().setCascadingSectionResizes(True)
        self.tableMain.horizontalHeader().setDefaultSectionSize(150)
        self.tableMain.horizontalHeader().setSortIndicatorShown(True)
        self.tableMain.horizontalHeader().setStretchLastSection(True)
        self.tableMain.verticalHeader().setCascadingSectionResizes(True)
        self.tableMain.verticalHeader().setSortIndicatorShown(False)
        self.tableMain.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableMain)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @logger.catch
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SpaceX ракеты"))
        self.labelTitle.setText(_translate("MainWindow", "SpaceX ракеты"))
        self.tableMain.setToolTip(_translate("MainWindow", "Для сортировки таблицы нужно нажать заголовок столбца"))
        self.tableMain.setSortingEnabled(True)
        item = self.tableMain.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableMain.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Высота"))
        item = self.tableMain.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Диаметр"))
        item = self.tableMain.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Масса"))
        item = self.tableMain.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Тип топлива"))
        item = self.tableMain.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Текст с описанием"))
        item = self.tableMain.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Ссылка на Wikipedia"))

    @logger.catch
    def create_table(self, data: list, is_write: bool):
        """
        Заполнить QTableWidget данными с опр. модом, если мод False, то записать в бд данные, если мод True, то в бд данные записывать не надо
        """
        x = 0
        for rocket in data:
            self.tableMain.setItem(x, 0, QtWidgets.QTableWidgetItem(rocket[0]))  # name
            height_int = QTableWidgetItem()
            height_int.setData(Qt.EditRole, rocket[1])
            self.tableMain.setItem(x, 1, height_int)  # height
            diam_int = QTableWidgetItem()
            diam_int.setData(Qt.EditRole, rocket[2])
            self.tableMain.setItem(x, 2, diam_int)  # diam
            mass_int = QTableWidgetItem()
            mass_int.setData(Qt.EditRole, rocket[3])
            self.tableMain.setItem(x, 3, mass_int)  # mass
            self.tableMain.setItem(x, 4, QtWidgets.QTableWidgetItem(rocket[4]))  # fuel
            self.tableMain.setItem(x, 5, QtWidgets.QTableWidgetItem(rocket[5]))  # desc
            self.tableMain.setItem(x, 6, QtWidgets.QTableWidgetItem(rocket[6]))  # wiki
            x += 1
        self.tableMain.resizeColumnsToContents()
        self.tableMain.resizeRowsToContents()
        if not is_write:
            write_table(data)


@logger.catch
def get_data(url: str):
    """
    Проверить существование данных в бд, если есть, то сортировать данные по опр. алгоритму, если нет, то получить данные по api, преобразовать в json и начать соритровку по
    другому алгоритму
    """
    session: Session = Session()
    rockets = session.query(Rocket).all()
    if rockets:
        sort_data(rockets, False)
    else:
        response = requests.get(url).json()
        sort_data(response, True)
    session.close()


@logger.catch
def sort_data(rockets: list, mode: bool):
    """
    Сортировать данные по опр. моду, который передаётся в функции get_data, если mode равен True, то сортировка происходит по алгоритму для json формата, если mode равен
    False, то сортировка происходит по алгоритму для бд формата
    Json сортировка: [(*name*,..., *перевод описания ракеты*,...),(*name*,..., *перевод описания ракеты*,...),...]
    Бд сортировка: из [<Rocket(*name*,...)>, <Rocket(*name*,...)>,...] в [(*name*,...),(*name*,...),...]
    """
    sort_rockets = []
    if mode:
        for rocket in rockets:
            # sort_rocket = name, height, diam, mass, fuel, desc, wiki
            sort_rocket = (rocket['name'], rocket['height']['meters'], rocket['diameter']['meters'], rocket['mass']['kg'],
                           rocket['engines']['propellant_1'] + '\n' + rocket['engines']['propellant_2'],
                           translators.google(rocket['description'].lower(), from_language='en', to_language='ru'), rocket['wikipedia'])
            sort_rockets.append(sort_rocket)
        ui.create_table(sort_rockets, False)
    else:
        for rocket in rockets:
            local_sort = (rocket.name, rocket.height, rocket.diam, rocket.mass, rocket.fuel, rocket.desc, rocket.wiki)
            sort_rockets.append(local_sort)
        ui.create_table(sort_rockets, True)


@logger.catch
def write_table(data: list):
    """
    Записать данные в бд
    """
    session = Session()
    rockets_objs = []
    for rocket in data:
        rocket_obj = Rocket(rocket[0], rocket[1], rocket[2], rocket[3], rocket[4], rocket[5], rocket[6])
        rockets_objs.append(rocket_obj)
    session.add_all(rockets_objs)
    session.commit()
    session.close()


Base = declarative_base()


class Rocket(Base):
    """
    Описание таблицы бд
    Название таблицы: rockets
    id: int
    name: str
    height: float
    diam: float
    mass: int
    fuel: str
    desc: str
    wiki: str
    """
    __tablename__ = 'rockets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    height = Column(Float)
    diam = Column(Float)
    mass = Column(Integer)
    fuel = Column(String)
    desc = Column(String)
    wiki = Column(String)

    @logger.catch
    def __init__(self, name, height, diam, mass, fuel, desc, wiki):
        self.name = name
        self.height = height
        self.diam = diam
        self.mass = mass
        self.fuel = fuel
        self.desc = desc
        self.wiki = wiki

    @logger.catch
    def __repr__(self):
        return "<Rocket('%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.name, self.height, self.diam, self.mass, self.fuel, self.desc, self.wiki)


if __name__ == "__main__":
    import sys

    URL = 'https://api.spacexdata.com/v4/rockets/'  # url
    logger.add('debug.log', format="{time} {level} {message}", level='INFO', rotation='10 KB', compression='zip', backtrace=True, diagnose=True)  # конфиг логгера
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    DB = create_engine('sqlite:///rockets.db')  # Связь с бд
    Base.metadata.create_all(DB)  # Создание бд
    Session = sessionmaker(bind=DB)  # Конфиг сессии с бд
    get_data(URL)
    MainWindow.show()
    sys.exit(app.exec_())