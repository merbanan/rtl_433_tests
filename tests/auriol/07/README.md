
# Testfiles for the Lidl Auriol AFW 2 A1 sensor (IAN 311588)

| Characteristic | Value | Comment |
| --- | --- | --- |
| Manufactured: | 2019-01 | |
| Batteries: | 2 x 1.5 V (direct current) (type AA/LR06) | |
| Temperature measuring range/accuracy: | -20 to +65°C (-4 to +149°F) / ±1.5°C (± 2.7°F) | Just what the station shows. Probably from -25.0°C to 76.7°C. Maybe more, not tetsted. |
| Relative humidity measuring range/accuracy: | 20 to 99% / ± 5% | Just what the station shows. Probably from 0 to 100%. |
| Relative humidity resolution: | 1% | |
| Transmission frequencies: | 433 MHz | ch1:~433919300, ch2:~433915200, ch3:~433918000, various? |
| Transmission output: | < 10 dBm | < 10 mW |
| Wireless range: | max. 100 m (open area) | Fantastic link budget. Maybe with 17.3 cm wire. (7500/Frequency in MHz) |
| Protection type: | IPX4 (splashproof) | Not protected from (continuous) rain. |

filesize: 524288 bytes  
  
write all in one file:  
for i in $(seq 001 001 040); do rtl_433 -vv -R 142 -r g$(printf "%.3d\n" "$i")_433.91xM_250k.cu8 -M level -A -a  >>analysis.txt 2>&1; done  
   
working flex decoder:   
-X "n=auriol_afw2a1,m=OOK_PPM,s=576,l=1536,g=2012,r=3954,t=0,y=0"  
  
file:g001_433.919M_250k.cu8  id:144 ch:1  temperature_C:14.6   rhumidity:67  battery:ok   button:false  
file:g002_433.919M_250k.cu8  id:144 ch:1  temperature_C:15.4   rhumidity:63  battery:ok   button:true  
file:g003_433.919M_250k.cu8  id:144 ch:1  temperature_C:16.7   rhumidity:61  battery:low  button:false  
file:g004_433.919M_250k.cu8  id:144 ch:1  temperature_C:16.7   rhumidity:61  battery:low  button:true  
file:g005_433.919M_250k.cu8  id:144 ch:1  temperature_C:6.9    rhumidity:50  battery:ok   button:false  
file:g006_433.919M_250k.cu8  id:144 ch:1  temperature_C:-2.5   rhumidity:49  battery:ok   button:false  
file:g007_433.919M_250k.cu8  id:144 ch:1  temperature_C:-9.4   rhumidity:47  battery:ok   button:false  
file:g008_433.919M_250k.cu8  id:144 ch:1  temperature_C:-20.3  rhumidity:42  battery:ok   button:false  
file:g009_433.919M_250k.cu8  id:144 ch:1  temperature_C:-18.2  rhumidity:50  battery:ok   button:false  
file:g010_433.919M_250k.cu8  id:144 ch:1  temperature_C:-19.0  rhumidity:50  battery:ok   button:false  
file:g011_433.919M_250k.cu8  id:144 ch:1  temperature_C:-19.7  rhumidity:50  battery:ok   button:false  
file:g012_433.919M_250k.cu8  id:144 ch:1  temperature_C:-20.0  rhumidity:53  battery:ok   button:false  
file:g013_433.919M_250k.cu8  id:144 ch:1  temperature_C:-20.7  rhumidity:53  battery:ok   button:false  
file:g014_433.919M_250k.cu8  id:144 ch:1  temperature_C:-23.2  rhumidity:52  battery:ok   button:false  
file:g015_433.919M_250k.cu8  id:144 ch:1  temperature_C:-1.6   rhumidity:68  battery:ok   button:false  
file:g016_433.919M_250k.cu8  id:144 ch:1  temperature_C:-3.6   rhumidity:69  battery:ok   button:false  
file:g017_433.919M_250k.cu8  id:144 ch:1  temperature_C:-0.8   rhumidity:82  battery:ok   button:false  
file:g018_433.919M_250k.cu8  id:144 ch:1  temperature_C:0.1    rhumidity:76  battery:ok   button:false  
file:g019_433.919M_250k.cu8  id:144 ch:1  temperature_C:20.6   rhumidity:61  battery:ok   button:false  
file:g020_433.919M_250k.cu8  id:144 ch:1  temperature_C:30.7   rhumidity:46  battery:ok   button:false  
file:g021_433.919M_250k.cu8  id:144 ch:1  temperature_C:34.8   rhumidity:46  battery:ok   button:false  
file:g022_433.919M_250k.cu8  id:144 ch:1  temperature_C:40.3   rhumidity:36  battery:ok   button:false  
file:g023_433.919M_250k.cu8  id:144 ch:1  temperature_C:44.5   rhumidity:22  battery:ok   button:false  
file:g024_433.919M_250k.cu8  id:144 ch:1  temperature_C:46.7   rhumidity:19  battery:ok   button:false  
file:g025_433.919M_250k.cu8  id:144 ch:1  temperature_C:53.7   rhumidity:12  battery:ok   button:false  

file:g026_433.915M_250k.cu8  id:213 ch:2  temperature_C:17.5   rhumidity:52  battery:ok   button:false  
file:g027_433.915M_250k.cu8  id:213 ch:2  temperature_C:17.5   rhumidity:52  battery:ok   button:true  
file:g028_433.915M_250k.cu8  id:213 ch:2  temperature_C:20.1   rhumidity:51  battery:low  button:false  
file:g029_433.915M_250k.cu8  id:213 ch:2  temperature_C:19.3   rhumidity:51  battery:low  button:true  
  
file:g030_433.918M_250k.cu8  id:35  ch:3  temperature_C:17.0   rhumidity:55  battery:ok   button:false  
file:g031_433.918M_250k.cu8  id:35  ch:3  temperature_C:16.9   rhumidity:55  battery:ok   button:true  
file:g032_433.918M_250k.cu8  id:35  ch:3  temperature_C:19.7   rhumidity:55  battery:low  button:false  
file:g033_433.918M_250k.cu8  id:35  ch:3  temperature_C:19.3   rhumidity:54  battery:low  button:true  
file:g034_433.918M_250k.cu8  id:35  ch:3  temperature_C:-25.5  rhumidity:32  battery:ok   button:false  
file:g035_433.918M_250k.cu8  id:35  ch:3  temperature_C:-25.7  rhumidity:32  battery:ok   button:false  
file:g036_433.918M_250k.cu8  id:35  ch:3  temperature_C:-25.8  rhumidity:32  battery:ok   button:false  
file:g037_433.918M_250k.cu8  id:35  ch:3  temperature_C:-26.0  rhumidity:32  battery:ok   button:false  
file:g038_433.918M_250k.cu8  id:35  ch:3  temperature_C:-0.4   rhumidity:51  battery:ok   button:false  
file:g039_433.918M_250k.cu8  id:35  ch:3  temperature_C:6.7    rhumidity:59  battery:ok   button:true  
  
weak signals:  
file:g040_433.918M_250k.cu8  id:213  ch:2  temperature_C:17.7  rhumidity:54  battery:ok   button:false   RSSI:-12.1dB   SNR:18.2dB   Noise:-30.4dB  
  
