import numpy as np

with open("File (1).bmp", "rb") as f:
    data = f.read()

pixels = data[138:]
width = 678
height = 755

a = []
for i in range(3, len(pixels), 4):
    a.append(pixels[i])

indices = [i for i, v in enumerate(a) if v == 254]

# The indices are 1, 5, 6, 8, 11, 12, 13, 16, 17, 20, 21, 22, 23, 26, 27, 32, 33, 37, 38, 39, 45, 49, 52, 53, 58, 59
# This matches the pattern we found earlier, where these bits were 0 (or 1) in the pattern!
# wait, the pattern was:
# 101110010110001100110000110011110011100011111011101100111100
# Indices of 0s in this pattern:
s = "101110010110001100110000110011110011100011111011101100111100"
zeros = [i for i, c in enumerate(s) if c == '0']
print(zeros)

# It is just the alpha channel data.
# BUT we haven't found the flag itself.
# Where else could the flag be?
# Have we tried zsteg with ALL payloads?
import subprocess
