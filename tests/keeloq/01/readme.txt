Unknown car remote

Signal layout
Preamble
pause
32 bits or random bits (rolling code, most likely KeeLoq)
32 bits of static data

1 byte from the end contains the different buttons pressed. 02 or 04.


-X 'n=name,m=OOK_PWM,s=432,l=892,r=4420,g=916,t=184,y=0'

[00] {12} ff f0                      : 11111111 1111
[01] {66} 20 66 67 67 b3 52 e8 02 40 


[00] {12} ff f0                      : 11111111 1111
[01] {66} 55 a8 22 25 b3 52 e8 04 40 

 
