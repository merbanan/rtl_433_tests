# Rodann Driveway Alarm

The TX2000A outdoor motion detector uses two AA batteries and transmits on
418MHz.  It contains six DIP switches: switches 1-4 select an address and
must match corresponding DIP switches in the receiver.  Switches 5-6 select
the tone played by the receiver.

The RX2000A indoor receiver uses a 12VDC plug-in power supply.  It includes
an LCD counter, a speaker, and terminals for attaching a speaker and an
external accessory such as a siren, buzzer, or strobe.  It also contains
six DIP switches: switches 1-4 select an address, and switches 5-6 control
the length of time the external accessory receives power.

FCC ID: U2QTXRX10002000A

[Manual](https://doorannounce.com/wp-content/uploads/2020/01/TXRX2000A-Instructions.pdf).
[Source](https://doorannounce.com/rodann-products/driveway-alarms/).

The signal captures are named:

    g_<aaaa>_<tt>_418M_250k.cu8

where `aaaa` is the 4-bit address from the transmitter DIP switches 1-4 and
`tt` is the 2-bit tone from the transmitter DIP switches 5-6 (interpreted
as ON=0).

Sample output from rtl_433:

    $ rtl_433 -R0 -a4 -r tests/rodann/g_1010_01_418M_250k.cu8
    ...
    [00] {38} 00 3f 49 49 48 : 00000000 00111111 01001001 01001001 010010
    [01] {38} 00 3f 49 49 48 : 00000000 00111111 01001001 01001001 010010
    [02] {38} 00 3f 49 49 48 : 00000000 00111111 01001001 01001001 010010
                                               a aaatt  a aaatt  a aaatt

Note the `aaaa` and `tt` bits are sent three times in each transmission,
and the transmission is repeated three times.
