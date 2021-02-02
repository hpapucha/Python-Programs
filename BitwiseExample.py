s = 0b00111001
t = 0b01111011

bitwise_or = s | t
bitwise_and = s & t
bitwise_xor = s ^ t

print("{0:d} {1:08b} {2:02x}".format( \
    bitwise_or, bitwise_or, bitwise_or))

print("{0:d} {1:08b} {2:02x}".format( \
    bitwise_and, bitwise_and, bitwise_and))

print("{0:d} {1:08b} {2:02x}".format( \
    bitwise_xor, bitwise_xor, bitwise_xor))
