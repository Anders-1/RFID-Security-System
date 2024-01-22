# RFID-Security-System
An RFID Security System based on the Raspberry Pi Pico (revised from the Zero to Pico).

Version History:

<!--If you put two spaces after a line it makes a new line but not as big 🤷-->

V1. RPi Zero  
V2. RPi Pico  
V3. :shipit: :trollface: :octocat:


[Tutorial 1](https://littlebirdelectronics.com.au/guides/181/nfc-module-with-raspberry-pi)

[Tutorial 2](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/testing-it-out)

[Tutorial 3](https://core-electronics.com.au/guides/piicodev-rfid-module-guide-for-raspberry-pi/)

[Tutorial 4](http://wiki.sunfounder.cc/index.php?title=PN532_NFC_Module_for_Raspberry_Pi) (with pinout!!!)

[Tutorial 5](https://www.waveshare.com/w/upload/8/83/Nfc-tools_reference_manual.pdf) (reference manual; scroll down)

TODO: 

- [X] Add green light

- [ ] Add startup checker (with beeps and stuff)

- [ ] Document what lights and beeps mean

- [ ] Email when alarm goes off

- [ ] Check todo list in the code too

NOTE: Design also works with RPi Zero

Pinout:

| **PN532 NFC RFID Reader** | **Raspberry Pi** |
| --- | --- |
| 5V                        | 5V               |
| GND                       | GND              |
| RX                        | UART TX          |
| TX                        | UART RX          |

| **Breadboard**                   | **Raspberry Pi**      |
| -------------------------------- | --------------------- |
| Button                           | GND, GPIO 23          |
| Button 2 (external?)             | GND, GPIO 25          |
| Red LED                          | 220 Ohm resistor, GND |
| 220 Ohm Resistor (for red led)   | Red LED, GPIO 17      |
| Green LED                        | 220 Ohm resistor, GND |
| 220 Ohm Resistor (for green led) | Green LED, GPIO 24    |
| Door Sensor                      | GND, GPIO 22          |
| Buzzer                           | GND, GPIO 27          |

Prices:

| Name | Price (totals ignore “other”s) |
| --- | --- |
| [RFID Tag](https://www.adafruit.com/product/4033) | $2.95 |
| [(other) Pi Cobbler](https://www.adafruit.com/product/2029) | $6.95 |
| [(other) RFID Controller](https://www.adafruit.com/product/364) | $39.95 |
| [(other) RFID Controller](https://www.amazon.com/dp/B01I1J17LC) | $8.69 |
| [(other) RFID Controller](https://www.amazon.com/HiLetgo-RFID-Kit-Arduino-Raspberry/dp/B01CSTW0IA/ref=sr_1_1_sspa?keywords=rc522+rfid+reader\&linkCode=ll2\&linkId=5c768527322a93c3f1ae3883817b8d14\&qid=1661434446\&s=electronics\&sr=1-1-spons\&psc=1\&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFUWDZGRjdQR01aVzEmZW5jcnlwdGVkSWQ9QTA5OTEzNDNVQjBDOTlMNVlTSEkmZW5jcnlwdGVkQWRJZD1BMDAxMjEzNzNNTEVBRUszQTlRS0cmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl) | $5.49 |
| [RFID Controller](https://www.ebay.com/itm/381374529898) | $7.88 |
| [Jumper Wires](https://www.adafruit.com/product/1956) | $3.95 |
| [Breadboard](https://www.adafruit.com/product/4539) | $5.00 |
| [Buzzer](https://www.adafruit.com/product/160) | $1.50 |
| [Magnetic Door Switch](https://www.adafruit.com/product/375) | $3.95 |
| [(other) Pi 4 Model B](https://www.pishop.us/product/raspberry-pi-4-model-b-2gb/?src=raspberrypi) | $45.00 |
| [(other) Resistor Pack](https://www.amazon.com/Elegoo-Values-Resistor-Assortment-Ohm-1M/dp/B072BL2VX1) | $11.99 |
| [(other) Resistors + Others Pack](https://www.amazon.com/Smraza-Breadboard-Resistors-Mega2560-Raspberry/dp/B01HRR7EBG) | $12.69 |
| **Total** | **$25.23** |
| _other_| |
| **Grand Total** | **$25.23** |

Getting the pack saves $8.45

I could get the pack and also get Jumper Wires for $3.95, I could get to tinkering earlier.

I could get the pack and get all the other products, $10.45 more expensive than just getting the pack.
