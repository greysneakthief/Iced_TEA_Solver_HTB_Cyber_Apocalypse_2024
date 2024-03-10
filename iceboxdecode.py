from Crypto.Util.Padding import unpad
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from enum import Enum
import os

class Mode(Enum):
    ECB = 0x01
    CBC = 0x02

class Cipher:
    def __init__(self, key, iv=None):
        self.BLOCK_SIZE = 64
        self.KEY = [b2l(key[i:i+self.BLOCK_SIZE//16]) for i in range(0, len(key), self.BLOCK_SIZE//16)]
        self.DELTA = 0x9e3779b9
        self.IV = iv
        if self.IV:
            self.mode = Mode.CBC
        else:
            self.mode = Mode.ECB
    
    def _xor(self, a, b):
        return b''.join(bytes([_a ^ _b]) for _a, _b in zip(a, b))

    def decrypt(self, ct):
        blocks = [ct[i:i+self.BLOCK_SIZE//8] for i in range(0, len(ct), self.BLOCK_SIZE//8)]
        
        msg = b''
        if self.mode == Mode.ECB:
            for ct_block in blocks:
                msg += self.decrypt_block(ct_block)
        elif self.mode == Mode.CBC:
            X = self.IV
            for ct_block in blocks:
                dec_block = self.decrypt_block(ct_block)
                msg += self._xor(X, dec_block)
                X = ct_block
        return unpad(msg, self.BLOCK_SIZE//8)

    def decrypt_block(self, ct_block):
        c = b2l(ct_block)
        m0 = c >> (self.BLOCK_SIZE//2)
        m1 = c & ((1 << (self.BLOCK_SIZE//2)) - 1)
        K = self.KEY
        msk = (1 << (self.BLOCK_SIZE//2)) - 1

        s = self.DELTA * 32
        for i in range(32):
            m1 -= ((m0 << 4) + K[2]) ^ (m0 + s) ^ ((m0 >> 5) + K[3])
            m1 &= msk
            m0 -= ((m1 << 4) + K[0]) ^ (m1 + s) ^ ((m1 >> 5) + K[1])
            m0 &= msk
            s -= self.DELTA
        
        m = ((m0 << (self.BLOCK_SIZE//2)) + m1) & ((1 << self.BLOCK_SIZE) - 1)

        return l2b(m)

# Read the key from input
KEY = bytes.fromhex("850c1413787c389e0b34437a6828a1b2")

# Read the ciphertext from the file
with open('output.txt', 'r') as f:
    lines = f.readlines()
    ct_hex = lines[1].split(': ')[1].strip()
    ciphertext = bytes.fromhex(ct_hex)

# Decrypt the ciphertext
cipher = Cipher(KEY)
plaintext = cipher.decrypt(ciphertext)

# Print the decrypted plaintext
print("Decrypted plaintext:", plaintext.decode())
