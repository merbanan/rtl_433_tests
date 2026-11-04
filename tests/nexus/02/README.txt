# technoLine Weather Station WS_9116: (Sensor: TX9116) (Sensor Type: TX96)
# http://www.technoline-berlin.com/details.php?id=1711&kat=4
# The Sensor can be bought at different stores in germany
# The LCD shows no decimal places (values rounded up to the next signed int)

# can be decoded with rtl_433 (nexus protocol):
# https://github.com/merbanan/rtl_433/

# [id0] [id1], [unk0] [temp0], [temp1] [temp2], [unk1] [unk2], [unk3]
# * The id changes when the battery is changed in the sensor
# * unk0 is always 1 0 0 0 (low battery indication???)
# * unk1 is always 1 1 1 1
# * unk2 is always 0 0 0 0
# * unk3 is always 0 0 0 0
# * temp is 12 bit signed scaled by 10 (1 digit precision)
