Kingspan/Watchman Plus (Niveau) oil tank monitor

See https://github.com/merbanan/rtl_433/issues/2133 for the main discussion, and
the earlier https://groups.google.com/g/rtl_433/c/VJSPl7h0848 thread (the issue
was opened as a direct continuation of that thread, at zuckschwerdt's request).
Manual: https://www.commercialfuelsolutions.co.uk/downloads/manuals/oil_watchman.pdf

An older (~2004) probe/pole-based oil tank level sensor -- distinct from the
newer ultrasonic "Watchman Sonic" / "Watchman Sonic Advanced" (already
supported by oil_watchman.c / oil_watchman_advanced.c). It displays (and
transmits) a single digit 0-9 or "F" (full), not a depth in cm.

OOK PWM, raw chip width ~800 us: a "1" bit is 4 chips (~3300 us), a "0" bit is
5 chips (~4100 us). 64 bit message for a normal reading (a longer message is
sent for Full+Bund-alarm or connection-error, not decoded):

    13 bit fixed preamble "1111111111110", then 3 ID bytes each followed by a
    2 bit "10" stuffing marker, then (also "10" stuffed every 2 bits): a 4 bit
    level nibble, 3 unknown bits, a battery-low bit, a 4 bit "complement"
    nibble, and a 7 bit tail.

- Device ID: reverse the entire 24 raw ID bits (not per-byte) then split into
  8 octal (0-7 only) digits -- reproduces the printed serial number exactly,
  byte for byte, on all 3 known real devices: 007353167 (Carl S, from the
  Google Groups thread), 05073745 and 05404105 (Scoff123 and arfond, from the
  GitHub issue).
- Level: 4 bits, LSB-first (weights 1,2,4,8). Confirmed against all 10 real
  digits 0-9 from Scoff123's systematic bucket-of-water test, plus a sentinel
  value 10 for "F" (full).
- Battery low: 1 bit, confirmed by diffing two otherwise-identical real
  captures (same device, same level) that differ only in battery state.
- No confirmed whole-message checksum. A "complement" nibble right after the
  level looked at first like a rolling counter, but is actually
  (K - level) mod 16 for a device-specific constant K (confirmed on 2 devices
  with different K) -- a level-integrity check, not a general checksum. What
  determines K isn't known, and one real sample (arfond's, captured right
  after reseating batteries) breaks the pattern outright. The final 7 bits
  stay constant across messages with different level/ID content on the same
  device, so they don't look like a per-message checksum either -- more
  likely a small status/flags field. Neither is used for validation.

- codes_test.txt/json - all 18 real messages available across both threads
  (12 from Scoff123's device, id 05073745, covering all 10 display digits plus
  "F" and a battery-low reading; 5 from arfond's device, id 05404105; 1 from
  Carl S's device, id 07353167) as -y test vectors. All match the decoder's
  output exactly.

5 real raw .cu8 captures were recovered from the Google Groups thread's
attachments (g005/g010, 1024k sample rate; g030/g031/g163, 250k) while working
on this decoder, but are deliberately NOT included here: they don't decode
end-to-end with the current rtl_433 build. The community's own
previously-reported flex decoder parameters (e.g.
`-X n=Watchman,m=OOK_PWM,s=3299,l=4107,r=5000`) produce no decode against
them, and rtl_433's automatic pulse-width classifier (-A) doesn't cleanly
separate the two real pulse widths on these captures either (they get lumped
into one over-wide bucket); g030/g031/g163 are also noted in the original
thread as likely truncated/incomplete captures. Whoever picks up the
RF-timing side of this decoder can re-fetch them from the Google Groups
thread's attachments (linked above) rather than from a copy checked in here.
