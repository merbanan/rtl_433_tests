# CAME Garage door key - TOP432

Compatible with key TOP-432EV, TOP-432NA, TOP-432EE.

This remote control is used for garage door and sliding gate. It transmits on 433.92 MHz (as it is written on the case), built sinc 2006.

It works with CAME radio receiver cards "AF43S", capable of handling 4096 codes. CAME is an italian company. Theses remote controls are mainly sold in europ (France, Italy, Belgium). https://www.came.com


FCC ID is "M48 TOP43XEV" but I could find this exact reference on fcc.gov search engine, but I found an approaching one under reference "M48TOP-NA". It says "Transmitter 433,92 MHz in AM/ASK" . So a decoder should be easily writable for rtl_433 .

Here is attached some pictures of the device and two CU8 samples signals (from the two buttons of the remote control).

By anaylizing the tow signals with `rtl_433 -A -r Button1_433.83M_250k.cu8` we can see the signal is simple. My guess are :
- there is two pulse and gap lengths : short 330us, long 660us (based on average measure off the two signals).
- there should be 12 bits somewhere on the signal to encode the 4096 possible codes.

By looking at the signal with Audacity and PulseView :
- the signals of button 1 differs from button 2 only by the 2nd pulses. It suggests me the code of button 1 should be close to button 2.

But i cant figure out how the encoding work and how to make a decoder, because :
- each frame is made of 13 pulses. Is it sufficient to encode 12 bits + a CRC or a parity ? no preamble ?
- Because gap and pulse have two different possible lengths (resulting in 4 ways to encode a bits), I suppose a bit is simply encoded by the modulation (when mod is here : it is a 1, no mod it is a zero), without any way to synchronize the stream (maybon only on the single pulse?)
- rtl_433 suggest the following flex decoder : " -X 'n=name,m=OOK_MC_ZEROBIT,s=330,l=0,r=660' " but it seems to not being compatible with my own analysis.

