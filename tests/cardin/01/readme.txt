Cardin S466-TX2 garage door remote control

9 dispswitchs inside the remote can be set as "-", "o" or "+" to chosse a
"code". There is 3^9=19683 possibilities.

Dual switch on the right set right button usage as chan A, B, C or D.
When left button is used dual switch can not be probed, it's allways chan A.

Sample output :

% rtl_433 -r S466-TX2_01.data 
Found 1 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: Generic RTL2832U OEM
Found Rafael Micro R820T tuner
Exact sample rate is: 250000.000414 Hz
Sample rate set to 250000.
Sample rate decimation set to 0. 250000->250000
Bit detection level set to 10000.
Tuner gain set to Auto.
Test mode active. Reading samples from file: S466-TX2_01.data
------------------------------
protocol       = Cardin S466
message        = 10101101 10101001 00001100 

                 123456789
dipswitch      = +-+-+-+-o

                 -->ON
right button   = 2 o-- (this is left button or two buttons on same channel)
                 1 o--
Test mode file issued 9 packets
Filter coeffs used:
a: 32768 31754
b: 506 506



% rtl_433 -r S466-TX2_02.data
Found 1 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: Generic RTL2832U OEM
Found Rafael Micro R820T tuner
Exact sample rate is: 250000.000414 Hz
Sample rate set to 250000.
Sample rate decimation set to 0. 250000->250000
Bit detection level set to 10000.
Tuner gain set to Auto.
Test mode active. Reading samples from file: S466-TX2_02.data
------------------------------
protocol       = Cardin S466
message        = 10101101 10101001 00001001 

                 123456789
dipswitch      = +-+-+-+-o

                 -->ON
right button   = 2 --o (this is right button)
                 1 o--
Test mode file issued 8 packets
Filter coeffs used:
a: 32768 31754
b: 506 506

