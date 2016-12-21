import MyView,MyModel, sys
from PyQt5.QtWidgets import *



class MyController(QWidget):
    """ MVC pattern: Creates a controller - mvc pattern.
    """

    def __init__(self, parent=None):
        """ Create a new controller with a object MyView and a object MyModel
        using the mvc pattern.
        :param parent:
        """
        super().__init__(parent)
        self.myView = MyView.Ui_GoogleNavigation()
        self.myView.setupUi(self)
        self.myModel = MyModel.MyModel()
        self.myView.bsubmit.clicked.connect(self.PushedSubmit)

    def PushedSubmit(self):
        ''' Wenn der Submit Knopf gedrückt wird, wird diese Methode aufgerufen.
        :param: s1: Start punkt eingabe wird gespeichert.
        :param: s2: Ziel punkt eingabe wird gespeichert.
        :return:
        '''
        s1 = self.myView.tstart.text()
        s2 = self.myView.tziel.text()
        self.myView.tergebnis.setText(self.myModel.RestRequest(s1, s2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())
