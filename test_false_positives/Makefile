
RM=/bin/rm

.PHONY: run_test

run_test:
	./run_test.sh

clean:
	${RM} -f \
		0x00_out.json 0x00_out.json-old 0x00_out.stderr 0x00_out.stderr-old \
		0x55_out.json 0x55_out.json-old 0x55_out.stderr 0x55_out.stderr-old \
		0xFF_out.json 0xFF_out.json-old 0xFF_out.stderr 0xFF_out.stderr-old

real_clean: clean

	${RM} -f 0x00_data.txt  0x55_data.txt  0xFF_data.txt
