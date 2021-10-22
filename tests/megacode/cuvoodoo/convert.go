// Binary converts from 24kHz 16bit little-endian demodulated amplitude samples
// to 250kHz 8-bit I&Q samples by modulating an offset frequency
// and applying squelch and gain.
package main

import (
	"bufio"
	"encoding/binary"
	"flag"
	"fmt"
	"io"
	"math"
	"os"
)

var (
	sampleRate      = flag.Int("sample_rate", 24000, "Sample rate to read in Hz")
	outSampleRate   = flag.Int("out_sample_rate", 250000, "Sample rate to output in Hz")
	offsetFrequency = flag.Float64("offset_freqency", 3001, "Offset from beat frequency in Hz")
	squelch         = flag.Float64("squelch", 0.25, "Level between silence and signal")
	gain            = flag.Float64("gain", 4.0, "Amplification")
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func Squelch(v float64) float64 {
	if v < *squelch {
		return 0.0
	}
	return v
}

func Gain(v float64) float64 {
	v *= *gain
	v = math.Min(v, 1.0)
	v = math.Max(v, 0.0)
	return v
}

func iq(a2 uint16, t float64) (uint8, uint8) {
	a := Gain(Squelch(float64(a2)/65535.0)) * 127.0
	wt := 2.0 * math.Pi * *offsetFrequency * t
	s, c := math.Sincos(wt)
	return uint8(128 + a*s), uint8(128 + a*c)
}

func main() {
	flag.Parse()
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	var recordsIn, recordsOut int
	var v uint16

	for {
		err := binary.Read(r, binary.LittleEndian, &v)
		if err == io.EOF {
			break
		}
		check(err)
		recordsIn++
		t := float64(recordsIn) / float64(*sampleRate)
		for t >= float64(recordsOut)/float64(*outSampleRate) {
			i, q := iq(v, float64(recordsOut)/float64(*outSampleRate))
			check(w.WriteByte(i))
			check(w.WriteByte(q))
			recordsOut++
		}
	}
	fmt.Fprintln(os.Stderr, "Read", recordsIn, "records")
	fmt.Fprintln(os.Stderr, "Wrote", recordsOut, "records")
	fmt.Fprintln(os.Stderr, "Read", float64(recordsIn)/float64(*sampleRate), "seconds")
	fmt.Fprintln(os.Stderr, "Wrote", float64(recordsOut)/float64(*outSampleRate), "seconds")
}
