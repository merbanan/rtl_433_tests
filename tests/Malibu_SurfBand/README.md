# Malibu Boat Surf Band

8 Button Remote with an LED:
* SW1: Surf Left
* SW3: Surf Right
* SW4: Volume Up
* SW5: Wedge Up
* SW6: Wedge Down
* SW7: Speed Up
* SW8: Speed Down
* SW9: Volume Down

There appear to be at least 2 models of this remote, I have the "26DRF8/LR2000" model.

Device Photos:
* [Exterior - Front](./Exterior_Front.png)
* [Exterior - Back](./Exterior_Back.png)
* [Interior - Front](./Interior_Front.png)
* [Interior - Back](./Interior_Back.png)

FCC ID: [2AFN315RM01](https://fccid.io/2AFN315RM01) _note: FCC pictures appear to be a different model/chipset_

There are two labelled chips on the board:
```
1026AA
G2D0A
```
```
S14031
BPS1W7
1637
```

The second one appears to be an RF transmitter from SiLabs: [Si4031](https://www.silabs.com/documents/public/data-sheets/Si4030-31-32.pdf)

Per the datasheet there are 3 supported modulation modes:
>Gaussian Frequency Shift Keying (GFSK), Frequency Shift Keying (FSK), and On-Off Keying (OOK). GFSK is the recommended modulation type as it provides the best performance and cleanest modulation spectrum

The datasheet also describes the supported encoding, data whitening and CRC implementation:
>Data whitening can be used to avoid extended sequences of 0s or 1s in the transmitted data stream to achieve a more uniform spectrum. When enabled, the payload data bits are XORed with a pseudorandom sequence output from the built-in PN9 generator. The generator is initialized at the beginning of the payload. The receiver recovers the original data by repeating this operation. 
>Manchester encoding can be used to ensure a dc-free transmission and good synchronization properties. When Manchester encoding is used, the effective datarate is unchanged but the actual datarate (preamble length, etc.) is doubled due to the nature of the encoding. The effective datarate when using Manchester encoding is limited to 128 kbps.
>CRC can be applied to only the data portion of the packet or to the data, packet length and header fields.

There are multiple samples for each button press, they were captured with a [HackRF One](https://greatscottgadgets.com/hackrf/one/) running firmware `2018.01.1 (API:1.02)` using libhackrf `git-97d3e65* (0.5)` and rtl_433 `19.08-146-gc496a5f`.

Additional Links:
* [Product Press Release](https://investors.malibuboats.com/press-releases/press-release-details/2018/Malibu-Boats-Incs-Surf-Band-with-Volume-Control-Recognized-by-Boating-Industry-Magazine/default.aspx)