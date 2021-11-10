# CircuitPython_XAC_Gamepad

## Setup process  

  1. Install [CircuitPython 7](https://circuitpython.org/downloads) or above in your board.
  2. Add the __init__.py file under \lib\adafruit_hid directory of CIRCUITPY drive.
  3. Add the boot.py file inside main directory of CIRCUITPY drive.
  4. Add the code.py file (demo code) inside main directory of CIRCUITPY drive.
  5. Add the hid_xac_gamepad.py file inside main directory of CIRCUITPY drive.
  6. Hard reset the board using the reset button or software reset.

## Notes
  1. You may need to remove the device in Windows for it to update the HID profile and press the restart if it doesn't show the correct HID profiles.
  2. REPL is disabled in boot.py file. You can comment ``` usb_cdc.disable() ``` depending on your dev board. It might be a good idea to comment it during the development stage. Don't forget pressing the reset button.

## Validation 

 <table style="width:100%">
  <tr>
    <th>Board</th>
    <th>MCU</th>
    <th>Status</th>
  <tr>
    <td>ItsyBitsy NRF52840 Express</td>
    <td>Nordic NRF52840</td>
    <td>Tested and fully functional</td>
  </tr>
  </table> 
