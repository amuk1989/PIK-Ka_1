import time
from UI import WindowInicilizer


def startClock():
    now = 0
    while True:
        time.sleep(1)
        now += 1
        clock = time.localtime(now)
        WindowInicilizer.mainWindow.onTimerLabel.setText(f'{clock.tm_hour - 7} : {clock.tm_min} : {clock.tm_sec}')

