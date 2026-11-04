# Oil Standard collision regression

The Apollo Smart packet from
[rtl_433 issue #3533](https://github.com/merbanan/rtl_433/issues/3533) contains
the Oil Standard decoder's shorter sync at bit offset 10. If the Smart packet
is clipped after its first 32 decoded payload bits, the checksumless Standard
decoder used to report those bits as ID `5b7b`, flags `71`, and binding
countdown `81`.

This fixture runs that clipped packet against protocol 81 and expects no
output. A complete Smart packet is tested separately by the parent directory
against protocol 235.
