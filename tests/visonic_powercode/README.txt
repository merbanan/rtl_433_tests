Visonic Powercode

Recorded from an MCT-302 magnetic sensor, but applicable to any device
that transmits powercode packets.

Powercode packet structure is 37 bits. 4 examples follow

          s addr                       data     cksm
          1 01101111 01000111 01110000 10001100 1001 - magnet near, case open
          1 01101111 01000111 01110000 11001100 1101 - magnet away, case open
          1 01101111 01000111 01110000 00001100 0001 - magnet near, case closed
          1 01101111 01000111 01110000 01001100 0101 - magnet away, case closed
          | |                        | |||||||| |  |
 StartBit_/ /                        / |||||||| \__\_checksum, XOR of preceding nibbles
 DeviceID__/________________________/  ||||||||
                                       ||||||||
                                Tamper_/||||||\_Repeater
                                  Alarm_/||||\_Spidernet
                                 Battery_/||\_Supervise
                                     Else_/\_Restore

Protocol cribbed from:
* Visonic MCR-300 UART Manual http://www.el-sys.com.ua/wp-content/uploads/MCR-300_UART_DE3140U0.pdf
* https://metacpan.org/release/Device-RFXCOM/source/lib/Device/RFXCOM/Decoder/Visonic.pm
* https://forum.arduino.cc/index.php?topic=289554.0
