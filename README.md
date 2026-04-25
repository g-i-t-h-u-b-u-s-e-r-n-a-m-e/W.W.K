# W.W.K
The world's worst keyboard! Push buttons and hold lights to the camera in order to type in morse code and copypastas

Created for Hack Club Blueprint Build Guild Boston, inspired by a joke from my Spanish class

Name inspired by W.W.B (World's Worst Board Game)
## Stuff you need to make this

### Hardware

- 1 Arduino Nano
- 2 LED lights, 1 blue 1 yellow
- 2 220 ohm resistors
- A USB cable for the Arduino
- Buttons (2 necessary, 4+ recommended to have some fake ones)
- Wires (I guess you *could* assemble this without any, but why would you?)
- Breadboard (other forms of doing wiring could also work, bonus points if you make it with a literal bread board)
- Some sort of adhesive to adhere this to somewhere near your webcam (optional, recommended if you want anyone to actually choose to use it, not suggested if you want to use this on multiple devices but not sure why you would)
- Batteries, if you want it to be fancy and wireless

### Software

- Python
- OpenCV for Python
- Arduino IDE

## Wiring it

Connect 1 leg of both LEDs and real buttons to ground on the Arduino

Connect the other leg of both LEDs to one of the legs of the resistor

Connect the remaining leg of 1 resistor to D8 on the Arduino, the other to D9

On the buttons, connect the leg diagonal of the one connected to ground to D10 on one, D3 on the other

Plug in the Arduino, or connect it to batteries

## Running the software

1) Push the Arduino script to the Arduino

2) Run the Python script
