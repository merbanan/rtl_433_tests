# Microchip HCS362 KeeLoq Code Hopping Encoder keyfob

Samples captured by @yashikada, see https://github.com/merbanan/rtl_433/issues/3112
and decoder discussion at https://github.com/merbanan/rtl_433/pull/3113.

The HCS362 supports two transmission modes: PWM (mode 0) and Manchester (mode 1).
These samples were recorded from the same physical remote reprogrammed for each mode.

- `hcs362-mc-button3-868.3M_1000k.cu8` / `-alt-` : Manchester mode (mode 1), button 3, two separate transmissions
- `hcs362-pwm-button2-868.3M_1000k.cu8` / `-alt-` : PWM mode (mode 0), button 2, two separate transmissions

The serial number (`id`) is stable across all four captures for each mode as expected,
while the `encrypted` rolling code field changes on every transmission.
