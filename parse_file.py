# If zsteg fails because of dib_hdr_size 124, we can modify the header!
# Let's change dib_hdr_size to 40 temporarily for zsteg to run.
with open("File (1).bmp", "rb") as f:
    data = bytearray(f.read())

import struct
# Write 40 to offset 14 (DIB size)
data[14:18] = struct.pack("<I", 40)

with open("mod.bmp", "wb") as f:
    f.write(data)
