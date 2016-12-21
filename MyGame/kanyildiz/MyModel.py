class MyModel(object):
    def __init__(self):
        ''' Diese Methode wird dann aufgerufen wenn das Programm zum Ersten mal gestartet wird
        '''
        self.lo = 15
        self.lk = 0
        self.lf = 0
        self.lg = 0
        self.ls = 0

    def Neu(self):
        ''' Diese Methode wird beim aufrufen des Neu Buttons aufgerufen.

        :return:
        '''
        self.ls += 1
        self.lo = 15
        self.lk = 0
        self.lf = 0
        self.lg = 0

    def rreihenfolge(self):
        ''' Diese Methode wird aufgerufen wenn ein Richtiger Button gedrückt wird.

        :return:
        '''
        self.lo -= 1
        self.lk += 1
        self.lg += 1

    def freihenfolge(self):
        ''' Diese Methode wird aufgerufen wenn ein Falscher Button gedrückt wird.
        :return:
        '''
        self.lf += 1
        self.lg += 1