/*
 * *** Fine Offset WH1080 Weather Station ***
 * (aka Watson W-8681)
 * (aka Digitech XC0348 Weather Station)
 * (aka PCE-FWS 20) 
 * (aka Elecsa AstroTouch 6975)
 * (aka Froggit WH1080)
 * (aka .....)
 *
 * This module is based on Stanisław Pitucha ('viraptor' https://github.com/viraptor ) earl code for the Digitech XC0348 Weather Station, 
 * which seems to be a rebranded Fine Offset WH1080 Weather Station (see pictures in this same folder).
 *
 * Some info and code derived from Kevin Sangelee's page: 
 * http://www.susa.net/wordpress/2012/08/raspberry-pi-reading-wh1081-weather-sensors-using-an-rfm01-and-rfm12b/ .
 *
 * See also Frank 'SevenW' page ( https://www.sevenwatt.com/main/wh1080-protocol-v2-fsk/ ) for some other useful info.
 *
 * I only have re-elaborated and merged their works. Credits (and kudos) should go to them all (and to many others too).
 *
 *********************
 *
 * This weather station is based on an indoor touchscreen receiver, and on a 5+1 outdoor wireless sensors group (rain, wind speed, 
 * wind direction, temperature, humidity, plus a DCF77 time signal decoder, maybe capable to decode some other time signal standard).
 * See the product page here: http://www.foshk.com/weather_professional/wh1080.htm . 
 * It's a very popular weather station, you can easily find it on eBay or Amazon (just do a search for 'WH1080').
 *
 * The module seems to work fine, decoding all of the data as read into the original console (there is some minimal difference
 * sometime on the decimals due to the different architecture of the console processor, which is a little less precise).
 * 
 * Please note that the pressure sensor (barometer) is enclosed in the indoor console unit, NOT in the outdoor wireless sensors group. 
 * That's why it's NOT possible to get pressure data by wireless communication. If you need pressure data you should try 
 * an Arduino/Raspberry solution wired with a BMP180 or BMP085 sensor.
 *
 * Data are trasmitted in a 48 seconds cycle (data packet, then wait 48 seconds, then data packet...).
 * 
 * This module is also capable to decode the DCF77 time signal sent by the wireless time signal decoder: 
 * around the minute 59 of the even hours the sensor's TX stops sending weather data, probably to receive (and sync with) DCF77 signal.
 * After around 3-4 minutes of silence it starts to send just time data for some minute, then it starts again with weather data as usual.
 *
 * To recognize message type (weather or time) you can use the 'msg_type' field on json output:
 * msg_type 0 = weather data
 * msg_type 1 = time data
 *
 * By living in Europe I can only test DCF77 time decoding, so if you live outside Europe and you find garbage instead of correct time,
 * you should disable time decoding (or, better, try to implement a more complete time decoding system :) ).
 *
 * The 'Total rainfall' field is a cumulative counter, increased by 0.3 millimeters of rain at once.
 *
 * The station comes in three TX operating frequency versions: 433, 868.3 and 915 Mhz. 
 * I've had tested the module with a 'Froggit WH1080' on 868.3 Mhz, using '-f 868140000' as frequency parameter and it works fine 
 * (compiled in x86, RaspberryPi 1 (v2) and RaspberryPi 2, and also on a BananaPi platform. Everything is OK). 
 * I don't know if it works also with other versions and, generally speaking, with ALL of the rebranded versions of this weather station. 
 * I guess it *should* do... Just give it a try! :)
 *
 * 
 * ***TODO***: check if negative temperature values (and sign) are OK (no real winter this year where I live, so cannot test...) .
 * 
 *
 * 2016 Nicola Quiriti ('ovrheat')
 *
 *
 */