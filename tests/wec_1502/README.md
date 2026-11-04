# Fuzhou Emax Temperature Sensor (Taylor, AccuTemp, ...)

``` 
/*
 * 
 *   Short pulse (32µs), to get a falling edge for Message Start Gap
 *   | Message Start Gap 3900µs (~8x smallest Gap)
 *   | |      Signal 500µs duration
 *   | |      |  Long Gap (1950µs (~4x smallest Gap): "1" Bit
 *   | |      |  |  Signal
 *   | |      |  |  |  Short Gap( 970µs (~2x smallest Gap)
 *   | |      |  |  |  |                     Signal terminating last bit
 *   | |      |  |  |  |                     | End Message Gap; 480µs (~1x) before next Message Start
 *   | |      |  |  |  |                     | |  Message Start Gap 3900µs (~8x)
 *   | v      |  |  |  |                     | |  |
 *   v 1950µs v  v  v  v                     v v  v
 *   |--------||----||--||--|| ... ||----||--||-||--------||---|| ... 
 *             ^ from falling edge to rising ^             ^ repeats 11 more times
 *              \----- 36-bit message ------/               \----- 36-bit message 
 */
```

