import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from QtUI import Ui_MainWindow
import config
Model = declarative_base()


class NoteDB(Model):
    __tablename__ = "Notes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(180), nullable=False, unique=False)
    datetime = Column(DateTime, nullable=False, unique=False)


engine = create_engine(config.dbBaseUrl + "mini_progect")

db_session = sessionmaker(binds={Model: engine}, expire_on_commit=False)
session = db_session()

Model.metadata.create_all(engine)


class Note:
    def addNote(self):
        date = self.calendarWidget.selectedDate().getDate()
        time = [self.timeEdit.time().hour(), self.timeEdit.time().minute()]
        datetime_note = datetime(date[0], date[1], date[2], time[0], time[1])
        description = self.lineEdit.text()
        note = NoteDB(description=description, datetime=datetime_note)
        session.add(note)
        session.commit()
        self.renders()

    def renders(self):
        all_dates = self.getAll()
        self.textBrowser.clear()
        for i in all_dates:
            self.textBrowser.append(f"{i.datetime} | {i.description}")

    def getAll(self):
        try:
            return session.query(NoteDB).order_by(NoteDB.datetime.asc()).all()
        except NoResultFound:
            return None


class Example(QMainWindow, Ui_MainWindow, Note):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.renders()

    def initUI(self):
        self.setWindowTitle('Задачник')
        self.pushButton.clicked.connect(self.addNote)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    expamle = Example()
    expamle.show()
    sys.exit(app.exec_())
