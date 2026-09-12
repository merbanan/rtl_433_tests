# Olympia Protect 9571

Olympia Protect 9571 alarm system sensors (Contact, PIR-Motion and
Keyfob), transmitting around 868.3-868.5 MHz using FSK-PCM, 366 us per
bit.

Decoded by `olympia_9571` (protocol 386), preamble `aa aa 2d d4` followed by a
48-bit payload:

    NNNN NNNN  NNNN NNNN  NNNN NNNN  XXXX IYYY  WZZZ TTTS  CCCC CCCC

- N[23:0]  device ID          @0:{24}
- X[3:0]   constant = 0x8     @24:{4}   (marker, always 0x8)
- I        battery inserted   @28:{1}
- Y[2:0]   constant = 0x6     @29:{3}   (marker, always 0x6)
- W        battery weak       @32:{1}
- Z[2:0]   device class       @33:{3}   0x0=sensor  0x1=keyfob
- T[2:0]   type / command     @36:{3}   sensor: 0x4=Contact, 0x7=PIR-Motion
- S        state / button     @39:{1}   Contact: 0=closed, 1=open / PIR-Motion: 0=idle, 1=motion
- C[7:0]   checksum           @40:{8}   sum(bytes 0-4) & 0xFF

## Files

- `pir_motion_d6f84d_868.3M_1000k.cu8`: PIR-Motion detector, ID d6f84d, motion
- `pir_idle_d6f84d_868.3M_1000k.cu8`: same PIR-Motion, idle (several retransmissions)
- `door_open_4ddf3b_868.4M_2048k.cu8`: Contact, ID 4ddf3b, open,
  battery just inserted
- `keyfob_arm_home_only_19e755_868.5M_1200k.cu8`: Keyfob remote, ID 19e755,
  "arm home only" command
- `pir_motion_d6f84d_868.42M_1000k.cu8`: PIR-Motion, motion,
  868.42 MHz capture at 1000 kHz. Detector regression sample: a leading
  ~84 us carrier blip precedes the FSK data, so a detector that only
  evaluates the first OOK pulse misclassifies the transmission as OOK.
- `pir_motion_d6f84d_868.465M_250k.cu8`: PIR-Motion, motion,
  868.465 MHz capture at 250 kHz. Detector regression sample: a short
  blip precedes each ~38 ms FSK burst, so the data only appears in
  non-leading pulses — the detector must evaluate later pulses afresh
  but only trust sustained (> 1 ms) ones.
- `pir_idle_d6f84d_868.465M_250k.cu8`: same PIR-Motion, idle, 868.465 MHz
  at 250 kHz.

Verify manually with:

    rtl_433 -r pir_motion_d6f84d_868.3M_1000k.cu8
    rtl_433 -r pir_idle_d6f84d_868.3M_1000k.cu8
    rtl_433 -r door_open_4ddf3b_868.4M_2048k.cu8
    rtl_433 -r keyfob_arm_home_only_19e755_868.5M_1200k.cu8
    rtl_433 -r pir_motion_d6f84d_868.42M_1000k.cu8
    rtl_433 -r pir_motion_d6f84d_868.465M_250k.cu8
    rtl_433 -r pir_idle_d6f84d_868.465M_250k.cu8
