I have a few of these alarm sensors in the house I just bought but no alarm panel. I would love to integrate them into my home automation project.

The sensors are PIR motion sensors and door contact sensors 319.5 MHz SAW devices made by ge/interlogix. These are a common protocol for GE Alarm/Interlogix panels and from my reading, I think DSC and Elk panels support these as well.

Here are some links I found for these:
Motion sensors:
-http://www.interlogix.com/intrusion/product/indoor-wireless-pet-immune-saw-pir-detector
-http://static.interlogix.com/library/466-1837-B_60-807-01-95r_install_instr.pdf
Door contacts
- http://www.home-technology-store.com/ITI-60-670-95R.aspx

I took some photos of the board of one of the motion sensors. See front.jpg and back.jpg.

From my reading, I believe these devices send 3 signal types.
1-Trip
2-Low battery
3-"Supervisory signals transmitted every 64 minutes" (so says motion sensor installation manual)

I'm finding that these sensors are not properly demodulated by rtl_433 (or I'm doing something wrong). I believe they are OOK/ASK modulation with no spacing between pulses. Pulses appear to be 33 samples long. I'm new to this so I very well could be wrong. I can't get the raw bits and so I can't even start to decode the packets. Help would be greatly appreciated!

To record tests I am using:

rtl_433 -a -t -p 67 -g 38 -f 319500000 -R 0

I've recorded the following tests:
1-Motion sensor #1 - manual trip by pushing the tamper button
2-Motion sensor #2 - manual trip by pushing the tamper button
3-Door contact sensor #1 - trip by opening door

If someone can help get me off the ground by properly demodulating these signals I will try and decode the trip, low batt and supervisory packets. 

I did try and create a device in rtl_433 to see if I could get a successful modulation. I've tried all kinds of timings and modulation combinations. Am I doing something wrong here? Below is my registration function.

r_device GE = {
    .name		= "GE Security Contact",
    .modulation		= OOK_PULSE_PCM_RZ,
    .short_limit	= 31,	// Pulse length, 250 µs
    .long_limit		= 33,	// Bit period, 500 µs
    .reset_limit	= 500, // Max gap, 
    .json_callback	= &GE_callback,
    .disabled		= 0,
    .demod_arg		= 0,
};


