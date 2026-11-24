# WA216 alarm system sensors, 868MHz

These are 2 sensors for an alarm system sold in Germany.

They operate in the 868MHz band. The modulation can be seen below:

!(wa216-waterfall.png "Waterfall")

And the corresponding wave form in audacity looks like this:

!(wa216-waveforms.png)

There's a 40 bit 5555.. preamble after which the real transmission starts. I'm attaching an example of a DOOR sensor and a PIR sensor. The modulation looks pretty simple FSK but I'm unable to demodulate and decode it properly in rtl_433. The modulatio analyzer does not return anything usefull.

Inside the modules, there's a SI4010C2 cpu and transmitter. It can be programmed for FSK/OOK modulation. It seems I'm in the presence of a simple 2FSK modulation here. 

The preamble seems to be 40 bits, of 1010101010 sequence. The rest looks like 15 nibbles (7.5 bytes). 
The bit width is about 200-230uS

## Documentation:

The datasheet for the transmitter: https://www.silabs.com/documents/public/data-sheets/Si4010.pdf
