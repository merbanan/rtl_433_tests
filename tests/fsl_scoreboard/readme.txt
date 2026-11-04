FSL Cricket Scoreboard Controller

See https://github.com/merbanan/rtl_433/pull/3443 and
https://github.com/InTheAbsenceOfAHorse/rtl_433_tests/tree/master/tests/FSL%20Cricket%20Scoreboard%20Controlller

FSK PCM, Manchester-encoded, 38-bit alternating preamble followed by 10
repeated 72-bit blocks (3-bit sync + 32-bit Manchester payload + padding).
Each block reports one scoreboard field: a field ID and a 3-digit value,
framed by fixed digit-position markers (no CRC).

Contents:
- 01/g001_433.954M_250k.cu8 / .json - real capture from the "DLS Recordings"
  session (field id 14, value 0).
- 02/g014_433.954M_250k.cu8 / .json - real capture from the "Total Recordings"
  session; this one is a double-length file containing two separate RF
  bursts (field id 5 then field id 8, both value 40), decoded as two events.
- codes_test.txt / codes_test.json - 22 synthesized (not captured) codes
  covering all four field IDs seen across the three real recording sessions
  (3, 5, 8, 14) at every value documented in that repo's commit history
  (0, 10, 20, 30, 40, 50). Each was independently verified against the
  decoder logic and matches the ground truth.

Verified against all 18 real captures in the linked repo (DLS/LHB/Total
Recordings): field IDs stayed constant per session while values stepped
cleanly by 10 up to 50, matching that repo's own commit messages exactly.
