# Nidec - Car Remote (313 MHz)

## Manufacturer
- Nidec

## Supported Models
- OUCG8D-344H-A (OEM for Honda)

## Notes
The transmitter uses a rolling code message.

### Button operation
* The unlock, lock buttons can be pressed once to transmit a single message.
* The trunk, panic buttons will transmit the same code on a short press.
* The trunk, panic buttons will transmit the unique code on a long press.
* The panic button will repeat the panic code as long as it is held.

## Images
* Front - Example 1

  ![front](pics/front_1.jpg)

* Front - Example 2

  ![front](pics/front_2.jpg)

## Expected Test Output

* 01/lock_313.8M_1024k.cu8
  ```
  model     : Nidec-OUCG8D ID        : CCCE80
  code      : 4604         Sequence  : 34375         Button Code: 3            Button    : Lock
  ```
* 01/trunk_long_press_313.8M_1024k.cu8
  ```
  model     : Nidec-OUCG8D ID        : CCCE80
  code      : 0200         Sequence  : 34378         Button Code: 15           Button    : Trunk Long Press
  ```
* 01/trunk_panic_short_press_313.8M_1024k.cu8
  ```
  model     : Nidec-OUCG8D ID        : CCCE80
  code      : 9F00         Sequence  : 34377         Button Code: 5            Button    : Trunk/Panic Short Press
  ```
* 01/unlock_313.8M_1024k.cu8
  ```
  model     : Nidec-OUCG8D ID        : CCCE80
  code      : EC00         Sequence  : 34376         Button Code: 4            Button    : Unlock
  ```
* 02/lock_313.8M_1024k.cu8
  ```
  model     : Nidec-OUCG8D ID        : DD4151
  code      : C580         Sequence  : 5445          Button Code: 3            Button    : Lock
  ```
* 02/panic_long_press_313.8M_1024k.cu8
  ```
  model     : Nidec-OUCG8D ID        : DD4151
  code      : 2D80         Sequence  : 5450          Button Code: 6            Button    : Panic Long Press
  ```

