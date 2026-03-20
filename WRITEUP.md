# Steganography CTF Write-up

## Challenge Description
The secret lies in the smallest changes.

## Files
- `t3rminator.jpg`

## Step-by-Step Solution

### 1. File Inspection
Initially, we are given a file named `t3rminator.jpg`. Since this is a steganography challenge, checking the actual file type is always a good first step.
Running the `file` command reveals it is not an image, but a Zip archive.

```bash
$ file t3rminator.jpg
t3rminator.jpg: Zip archive data, at least v2.0 to extract, compression method=deflate
```

### 2. Extracting Hidden Files
Using `unzip`, we extract the contents of `t3rminator.jpg`.

```bash
$ unzip t3rminator.jpg
Archive:  t3rminator.jpg
  inflating: stego.wav
```

This yields a new file called `stego.wav`.

### 3. Analyzing the Audio File
The `stego.wav` file is a standard uncompressed WAV audio file. The description "The secret lies in the smallest changes" is a strong hint for Least Significant Bit (LSB) steganography.
In LSB steganography, data is hidden by modifying the least significant bit of each byte (or sample) of the host file, which results in differences so minor they go unnoticed.

### 4. Extracting the LSB
We can write a simple Python script to read the raw audio frames from the WAV file and extract the LSB of every byte.

We iterate through all the frames, take the last bit of each byte (`byte & 1`), and concatenate these bits back into bytes (LSB-first).

### 5. Finding the Flag
Once we have constructed the hidden bytes from the LSBs, we decode them into a string using the `latin-1` encoding (which handles arbitrary byte values without raising `UnicodeDecodeError`).
We then search the resulting string for the known flag format `t3rmctf{`.

This reveals the flag:
`t3rmctf{Audi0_st3g4n0graphy_i$_4asy}`
