#!/usr/bin/python
import sys, math, numpy, textwrap

sys.stdout.flush()
input_phrase=raw_input()

phrase_array = list(input_phrase)
bitstream = ""
for i in phrase_array:
	print(i),
	char = ord(i)
	print(char),
	char_bin =format(ord(i), '08b')
	print(char_bin)
	# pad the 7bit ascii into 8 bits
	bitstream += char_bin
print("				   "),
print(bitstream)


# add padding
bs_length = len(bitstream)
rem_bs_length = ""
rem_bs_length = bs_length % 6
if rem_bs_length == 2:
	bitstream = bitstream+"0000"
if rem_bs_length == 4:
	 bitstream = bitstream+"00"
print("Padded bit stream: "),
print(bitstream)

senary = textwrap.wrap(bitstream, 6)
print("Senary bit stream: "),
print(senary)

ascii_code = []
for i in senary:
	print("Decimal: "),
	print(int(i,2))
	print("ASCII  : "),
	print(chr(int(i,2)))
	ascii_code.append(chr(int(i,2)))
print(ascii_code)


# Need to figure out how to use USASCII encoding and not UTF


