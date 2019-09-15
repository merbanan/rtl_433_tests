# GE/Interlogix sensors

These tests are for GE/Interlogix sensors and include:

pir motion sensor

door and window contact sensor

*will soon include other devices like key fob and garage door sensors. Do note current code should parse these devices correctly as is.


These devices send poll/supervisory messages approxmately every hour (4 messages) and when an event occurs (8 messages). See interlogix.c source for addtional detail.

frequency used is -f 319500000 

Recordings include:

01-Motion sensor #1 - manual trip by pushing the tamper button

02-Motion sensor #2 - manual trip by pushing the tamper button

03-Door contact sensor #1 - trip by opening door

04-Door contact sensor #2 - open and close sequence


