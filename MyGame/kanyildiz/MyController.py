import sys
from random import shuffle

from PyQt5.QtWidgets import *

from kanyildiz import MyModel
from kanyildiz import MyView


class MyController(QWidget):
    """ MVC pattern: Creates a controller - mvc pattern.
    """

    def __init__(self, parent=None):
        """ Create a new controller with a object MyView and a object MyModel
        using the mvc pattern.
        :param parent:
        """
        super().__init__(parent)
        # Object of MyView
        self.myView = MyView.Ui_Window()
        self.myView.setupUi(self)
        # Object of MyModel
        self.myModel = MyModel.MyModel()
        # List with all 15 buttons (1-15)(without "Neu" and "Ende")
        self.buttons = [self.myView.B01, self.myView.B02, self.myView.B03, self.myView.B04, self.myView.B05,
                        self.myView.B06, self.myView.B07, self.myView.B08, self.myView.B09, self.myView.B10,
                        self.myView.B11, self.myView.B12, self.myView.B13, self.myView.B14, self.myView.B15]

        self.Value = 0
        self.textbutton = "1"
        self.itextbutton = 1
        # connect the buttons with the clicked signal
        self.connectButtons()
        # start a new game
        self.start()
        # set "Spiel" Counter to its String
        self.myView.SLabel.setText(str(self.myModel.ls))

    def bhs(self):
        ''' sender: Der gedrückte Button
            Überprüfen des gedrückten Buttons ob sie in richtigerReihenfolge gedrückt wurden.
            Je nach dem werden die Werte erhöt oder niedriger.
        :return:
        '''
        sender = self.sender()
        value = ""
        if isinstance(sender, QPushButton):
            value = int(sender.text())

        if value == self.Value:
            sender.setEnabled(False)
            self.myModel.rreihenfolge()
            self.myView.KLabel.setText(str(self.myModel.lk))
            self.myView.GLabel.setText(str(self.myModel.lg))
            self.myView.OLabel.setText(str(self.myModel.lo))
            self.Value += 1
        else:
            self.myModel.freihenfolge()
            self.myView.FLabel.setText(str(self.myModel.lf))
            self.myView.GLabel.setText(str(self.myModel.lg))

    def start(self):
        ''' Jedes mal wenn des Program aufgerufen wird oder der Neu Button gedrückt wird
            wird diese Methode aufgerufen und die Buttons werden wieder zufällig beschriftet.
        :return:
        '''
        self.shuffleButtons()
        self.myModel.Neu()
        self.shuffleButtons()
        self.LabelSetNew()

    def connectButtons(self):
        for i in self.buttons:
            i.clicked.connect(self.bhs)
            # c = ""
            # i.setEnabled(False)
        self.myView.NeuButton.clicked.connect(self.start)

    def LabelSetNew(self):
        ''' Hier werden die Labels neu beschriftet wenn der Neu Button
            gedrückt wird.
        :return:
        '''
        self.myView.KLabel.setText(str(self.myModel.lk))
        self.myView.GLabel.setText(str(self.myModel.lg))
        self.myView.OLabel.setText(str(self.myModel.lo))
        self.myView.FLabel.setText(str(self.myModel.lf))
        self.myView.SLabel.setText(str(self.myModel.ls))

    def shuffleButtons(self):
        ''' Vermischen der Liste in dem die Buttons enthalten sind.
            Verweisen von Strings auf die Buttons.
        :return:
        '''
        shuffle(self.buttons)

        for i in self.buttons:
            i.setEnabled(True)
            if self.itextbutton == 1:
                i.setText(self.textbutton)
                self.textbutton = "2"
                self.itextbutton = 2

            elif self.itextbutton == 2:
                i.setText(self.textbutton)
                self.textbutton = "3"
                self.itextbutton = 3

            elif self.itextbutton == 3:
                i.setText(self.textbutton)
                self.textbutton = "4"
                self.itextbutton = 4

            elif self.itextbutton == 4:
                i.setText(self.textbutton)
                self.textbutton = "5"
                self.itextbutton = 5

            elif self.itextbutton == 5:
                i.setText(self.textbutton)
                self.textbutton = "6"
                self.itextbutton = 6

            elif self.itextbutton == 6:
                i.setText(self.textbutton)
                self.textbutton = "7"
                self.itextbutton = 7

            elif self.itextbutton == 7:
                i.setText(self.textbutton)
                self.textbutton = "8"
                self.itextbutton = 8

            elif self.itextbutton == 8:
                i.setText(self.textbutton)
                self.textbutton = "9"
                self.itextbutton = 9

            elif self.itextbutton == 9:
                i.setText(self.textbutton)
                self.textbutton = "10"
                self.itextbutton = 10

            elif self.itextbutton == 10:
                i.setText(self.textbutton)
                self.textbutton = "11"
                self.itextbutton = 11

            elif self.itextbutton == 11:
                i.setText(self.textbutton)
                self.textbutton = "12"
                self.itextbutton = 12

            elif self.itextbutton == 12:
                i.setText(self.textbutton)
                self.textbutton = "13"
                self.itextbutton = 13

            elif self.itextbutton == 13:
                i.setText(self.textbutton)
                self.textbutton = "14"
                self.itextbutton = 14

            elif self.itextbutton == 14:
                i.setText(self.textbutton)
                self.textbutton = "15"
                self.itextbutton = 15

            elif self.itextbutton == 15:
                i.setText(self.textbutton)
                self.textbutton = "1"
                self.itextbutton = 1

        self.Value = 1
        self.myView.OLabel.setText(str(self.myModel.lo))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())
