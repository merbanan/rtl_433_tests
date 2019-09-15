# Byron BY101 doorbell

Captures taken from Byron BY101 doorbell for example https://www.screwfix.com/p/wireless-by101-portable-door-chime-with-li-ion-powered-bell-push/26396

Pressing the button in the sender to change melody appears to cycle through 8
different settings (although receiver only has 4 different tunes). Have created
one dump for each different transmission.

http://doorchimesuk.co.uk/pdf/BY101.pdf for guide

Produces values that should probably be rounded to::

    Short distance: 125, long distance: 250, packet distance: 750

`-a` produces cycle through the different values of::

    [04] {21} 18 97 00 : 00011000 10010111 00000
    [04] {21} 18 97 08 : 00011000 10010111 00001
    [07] {21} 18 97 10 : 00011000 10010111 00010
    [11] {21} 18 97 18 : 00011000 10010111 00011
    [10] {21} 18 97 20 : 00011000 10010111 00100
    [11] {21} 18 97 28 : 00011000 10010111 00101
    [09] {21} 18 97 30 : 00011000 10010111 00110
    [11] {21} 18 97 38 : 00011000 10010111 00111

`-A` produces the same but bitwise flipped
