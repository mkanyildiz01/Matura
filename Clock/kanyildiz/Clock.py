import os, sys, pygame, math, datetime
from pygame.locals import *
from subprocess import *
import time
#---------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------ Digital ------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
def Benutzer():
    ''' Zuhören ob irgendwelche (bzw A,D,Escape) Tasten gedrückt werden.
        Wenn ja wird in der If-Schleife Bestimmt welche Uhr gedrückt wird.
        Bzw. wenn Escape defrückt wird wird das Programm geschlossen.
    '''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ClockA()
            elif event.key == pygame.K_d:
                ClockD()
            elif event.key == pygame.K_ESCAPE:
                sys.exit()



def ClockD():
    ''' Die Digitale Uhr wird erstellt.
    :param size: Die breite und höhe des Fensters.
    :param screen: Anwendung von size auf das Fenster.
    :param font: Bestimmung von font und Größe der Schrift.
    :param commandeDate: ["date", "+%Y-%m-%d %H:%M:%S.%N"]
    :param now: Die Zeit von jetzt
    '''
    size = width, height = 600, 110
    screen = pygame.display.set_mode(size)

    # Der Fenstername wieder bestimmt.
    pygame.display.set_caption("Kanyildiz ClockDigital")

    # pygame wird angewendet
    pygame.init()

    black = 0, 0, 0
    white = 255, 255, 255
    font = pygame.font.SysFont('ActionIsShaded', 175)

    commandeDate = ["date", "+%S.%N"]
    delta = datetime.timedelta(seconds=0)

    while True:
        Benutzer()

        screen.fill(white)

        now = datetime.datetime.today()
        secPython = float(str(now)[17:26])
        Benutzer()
        dt = str(now - delta)
        clock = dt[11:19]

        fontt = font.render(clock, 1, black)
        screen.blit(fontt, (50, 0))
        Benutzer()
        pygame.display.update()
        pygame.time.delay(1000)

        out = Popen(commandeDate, stdout=PIPE)
        Benutzer()
        (secUnix, serr) = out.communicate()
        delta = datetime.timedelta(seconds=int(float(secUnix) - float(secPython)))
        Benutzer()
# ---------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------- Analog ------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------#

# Same as Digital at this Place
pygame.init()
screen = pygame.display.set_mode((640, 400))
sec_angle, min_angle, hr_angle = 0, 0, 0
old_time = {"hr": time.localtime().tm_hour, "min": time.localtime().tm_min, "sec": time.localtime().tm_sec}


def new_coords(radius, angle):
    '''
    Diese Methode rechnet die neuen Koordinaten die für die Zeiger benötigt werden.
    :param radius: Radius der Zeiger
    :param angle: Richtigund er Zeiger
    :param xend: Die x Koordinaten
    :param yend: Die y Koordinaten
    :return: xemd, yend
    '''
    xend = 300 + (radius * math.cos(math.radians(angle)))
    yend = 200 + (radius * math.sin(math.radians(angle)))
    return (xend, yend)


def find_angles():
    '''
    Diese Methode findet die Richtung.

    :param: tme: Speichert die aktuelle Zeit ein.
    :param: hr_angel: sec_angle: min_angle: Setzt die Richtung aller Zeigern
    '''
    global hr_angle, min_angle, sec_angle
    tme = {'hr': time.localtime().tm_hour, 'min': time.localtime().tm_min, 'sec': time.localtime().tm_sec}
    hr_angle = 30 * tme['hr'] + (tme['min'] / 12.0 * 6)
    min_angle = tme['min'] * 6
    sec_angle = tme['sec'] * 6


def ClockA():
    '''
    Die Analoge Uhr wird erstellt.
    :param: clock: PyGame Uhr.
    :param: size: Die breite und höhe des Fensters.
    :param screen: Anwendung von size auf das Fenster.
    '''

    clock = pygame.time.Clock()
    size = width, height = 600, 400

    # Der Fenstername wieder bestimmt.
    pygame.display.set_caption("Kanyildiz ClockAnalog")
    screen = pygame.display.set_mode(size)
    while True:
        Benutzer()
        # Alle elemente werden Schwarz gemacht.
        screen.fill((255, 255, 255))
        # Die Zahlen werden Gezeichnet
        screen.blit(pygame.font.SysFont(None, 25).render("12", True, (0, 0, 0)), (290, 57))
        screen.blit(pygame.font.SysFont(None, 25).render("6", True, (0, 0, 0)), (294, 330))
        screen.blit(pygame.font.SysFont(None, 25).render("9", True, (0, 0, 0)), (160, 190))
        screen.blit(pygame.font.SysFont(None, 25).render("3", True, (0, 0, 0)), (425, 190))
        Benutzer()
        clock.tick(150)
        # Der Rahmen der Uhr wird gezeichnet
        pygame.draw.circle(screen, (0, 0, 0), (300, 200), 150, 3)
        # Die einzelnen Zeiger werden entsprechend gezeichnet.
        pygame.draw.line(screen, (255, 0, 0), (300, 200), new_coords(120, 270 + sec_angle), 2)  # the second hand
        pygame.draw.line(screen, (0, 0, 0), (300, 200), new_coords(115, 270 + min_angle), 4)  # the minute hand
        pygame.draw.line(screen, (0, 0, 0), (300, 200), new_coords(85, 270 + hr_angle), 5)  # the hour hand
        Benutzer()
        find_angles()
        new_coords(140, 270)
        tme = time.localtime()
        current_time = {"hr": tme.tm_hour, "min": tme.tm_min, "sec": tme.tm_sec}
        e = pygame.event.poll()
        pygame.display.update()
        Benutzer()

if __name__ == '__main__':
    ClockA()