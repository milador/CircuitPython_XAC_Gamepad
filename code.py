# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
====================================================

* Author(s): Adafruit Industries
* Edited: Milad Hajihassan
"""

# Setup and usage Guide in details:

# 1) Install CircuitPython 7 or above in your board : https://circuitpython.org/downloads
# 2) Add the __init__.py file under \lib\adafruit_hid directory of CIRCUITPY drive
# 3) Add the boot.py file inside main directory of CIRCUITPY drive
# 4) Add the code.py file inside main directory of CIRCUITPY drive
# 5) Add the hid_xac_gamepad.py file inside main directory of CIRCUITPY drive
# 6) Hard reset the board using the reset button or software reset.
# You may need to remove the device in Windows for it to update the HID profile

import time
import board
import digitalio
import analogio
import usb_hid

from hid_xac_gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

# Create some buttons. The physical buttons are connected
# to ground on one side and these and these pins on the other.
button_pins = (board.D10, board.D11, board.D12, board.D13)

# Map the buttons to button numbers on the Gamepad.
# gamepad_buttons[i] will send that button number when buttons[i]
# is pushed.
gamepad_buttons = (1, 2, 3, 4)

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

# Connect an analog two-axis joystick to A4 and A5.
ax = analogio.AnalogIn(board.A4)
ay = analogio.AnalogIn(board.A5)

# Equivalent of Arduino's map() function.
def range_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

gp.move_joysticks(x=0, y=0)
while True:
    # Buttons are grounded when pressed (.value = False).
    for i, button in enumerate(buttons):
        gamepad_button_num = gamepad_buttons[i]
        gp.press_buttons(gamepad_button_num)
        time.sleep(2)
        gp.release_buttons(gamepad_button_num)
        print(" press", gamepad_button_num, end="")

    # Convert range[0, 65535] to -127 to 127
    gp.move_joysticks(x=127, y=0)
    time.sleep(2)
    gp.move_joysticks(x=0, y=127)
    time.sleep(2)
    # print(" x", ax.value, "y", ay.value)
