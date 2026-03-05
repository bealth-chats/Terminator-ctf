import wave
import subprocess
import os

# Unzip the image to get the wav file
subprocess.run(['unzip', '-o', 't3rminator.jpg'], stdout=subprocess.DEVNULL)

w = wave.open('stego.wav', 'r')
frames = w.readframes(w.getnframes())

# We found that extracting bits from every byte and storing them LSB-first gives the flag
extracted_bits = []
for byte in frames:
    extracted_bits.append(byte & 1)

# Group bits into bytes, LSB first (as that worked)
extracted_bytes_lsb_first = bytearray()
for i in range(0, len(extracted_bits), 8):
    byte = 0
    for j in range(8):
        if i + j < len(extracted_bits):
            byte = byte | (extracted_bits[i + j] << j)
    extracted_bytes_lsb_first.append(byte)

# Find flag in the bytes
text = extracted_bytes_lsb_first.decode('latin-1')
start = text.find('t3rmctf{')
if start != -1:
    end = text.find('}', start)
    if end != -1:
        flag = text[start:end+1]
        print(flag)

# Clean up
os.remove('stego.wav')
