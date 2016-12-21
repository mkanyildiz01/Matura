from xml.etree import ElementTree
import requests


class MyModel:
    def __init__(self):
        '''
            Klassen Attribute werden deffiniert.
        '''
        self.s1 = ""
        self.s2 = ""
        self.o1 = ""
        self.status = ""
        self.s2 = ""

    def RestRequest(self, s1, s2):
        ''' Ihr wird die ganze Information an die Google Api seite geschickt und
         die benötifte Information von der XML datei rausgefiltert.
        :return:
        '''

        params = {"origin": s1, "destination": s2, "language": "de"}
        xml = requests.get("http://maps.googleapis.com/maps/api/directions/xml", params)
        elemente = ElementTree.fromstring(xml.text)
        status = elemente.find("status").text

        if status == "OK":
            self.status = "Berechnung: " + status
            route = elemente[1]
            for self.o2 in route.iter('step'):
                self.o2 += self.o2.find("./html_instructions").text + \
                    ", Entfernung: " + self.o2.find("./distance/text").text + \
                    ", Dauer: " + self.o2.find("./duration/text").text + "<br>"
            self.text = "Die Gesamtdauer beträgt <b>" + route.find("./leg/duration/text").text + \
                        "</b> <br><br>" + self.o2
            return self.text
        else:
            self.status = "Ein Fehler wurde gefunden"
