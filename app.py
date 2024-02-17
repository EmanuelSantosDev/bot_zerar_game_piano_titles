import pyautogui
import keyboard
import win32api
import win32con
from time import sleep


# aperta o botão 'START'
pyautogui.click(1405,-562, duration=2)


# usando a biblioteca 'pywin32' para efetuar o click rapidamente
def click_rapido(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# pausa o game quando o usuário apertar a tecla '1'
while keyboard.is_pressed('1') == False:
    # mapeando cada uma das 4 teclas do game
    if pyautogui.pixelMatchesColor(1256, -505, (0, 0, 0)):
        click_rapido(1256, -505)
    if pyautogui.pixelMatchesColor(1360, -507, (0, 0, 0)):
        click_rapido(1360, -507)
    if pyautogui.pixelMatchesColor(1444, -507, (0, 0, 0)):
        click_rapido(1444, -507)
    if pyautogui.pixelMatchesColor(1536, -489, (0, 0, 0)):
        click_rapido(1536, -489)
