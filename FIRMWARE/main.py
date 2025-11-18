import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [board.D3, board.D4, board.D2, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Keymap: Numpad 1,2,3,4
keyboard.keymap = [
    [KC.P1, KC.P2, KC.P3, KC.P4]
]

if __name__ == '__main__':
    keyboard.go()
