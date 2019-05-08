from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

keys = {
    'move_keys': {
        'up': 'k', 
        'down': 'j',
        'left': 'h',
        'right': 'l',
        'up-right': 'u',
        'up-left': 'y',
        'down-right': 'n',
        'down-left': 'b'
    },
    'inven_key': 'i',
    'auto_attack': Key.tab,
    'wait_key': '.',
    'descend_key': '>',
    'ascend_key': '<',
    'menu_keys': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'skills_key': 'm',
    'ability_key': 'a'
}

time.sleep(5)

for char in 'Robot':
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)

keyboard.press(Key.tab)
keyboard.release(Key.tab)

