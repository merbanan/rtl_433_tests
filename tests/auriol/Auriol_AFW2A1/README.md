# Lidl Auriol AFW 2 A1 sensor (IAN 311588)

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

    file:g017_433.919M_250k.cu8  id:144 ch:1  temperature_C:-0.8   humidity:82  battery:ok   button:false
    file:g020_433.919M_250k.cu8  id:144 ch:1  temperature_C:30.7   humidity:46  battery:ok   button:false
    file:g025_433.919M_250k.cu8  id:144 ch:1  temperature_C:53.7   humidity:12  battery:ok   button:false
    file:g029_433.915M_250k.cu8  id:213 ch:2  temperature_C:19.3   humidity:51  battery:low  button:true
    file:g034_433.918M_250k.cu8  id:35  ch:3  temperature_C:-25.5  humidity:32  battery:ok   button:false
    file:g036_433.918M_250k.cu8  id:35  ch:3  temperature_C:-25.8  humidity:32  battery:ok   button:false

Further testfiles, pictures and more can be found at:
https://github.com/LiberationFrequency/ISMinfo/tree/master/devices/auriol/afw2a1

