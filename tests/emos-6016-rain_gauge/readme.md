This is additional rain gauge sensor to recently added weather station EMOS 16016 (protocol 214). 
It is a standalone sensor, see picture here: https://www.emos.sk/domaca-bezdrotova-meteostanica-e6016

It operates on 433.92MHz. When you look at the pictures I attached, it only has 2 positions. When looking at the picture, right side of the board has sensors and there is
magnet on the paddle. When it gets filled with rain, it flips to other side, causing magnet to move away off of sensor. If rain fills the other side of the paddle, it flips
back to previous side.

Each time it changes sides, in the weather station it is represented as +0,7mm of rainfalls. Weather station holds the cumulative stats (which can be easily fulfilled in HA or 
other tool)

So basically starting off with 0mm and magnet is on the right side. If it flips to left, it adds 0,7 (total 0,7), when it flips back to right, it adds 0,7 (total 1,4), and so on.

I captured signals as I was manipulating the paddles. First change is captured around the g009 file (can't say precisely), second around g017, and the last around g025.
