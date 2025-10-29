### __AES__

AES (Advanced Encryption Standard) is a symmetric block cipher designed to securely encrypt data in fixed-size blocks (128 bits). It uses keys of length 128, 192, or 256 bits and performs multiple rounds of transformations to convert plaintext into ciphertext.

Block Size and Key Length:

AES operates on 128-bit blocks arranged in a 4x4 matrix of bytes called the state.

Supported key lengths: 128-bit (10 rounds), 192-bit (12 rounds), 256-bit (14 rounds).

Step 1

Key Expansion:

The original key is expanded into multiple round keys using a key schedule algorithm.

Initial Round:

AddRoundKey: XOR the plaintext state with the first round key.

Main Rounds (9, 11, or 13 rounds depending on key size):

SubBytes: Substitute each byte using a fixed S-box for non-linearity.

ShiftRows: Cyclically shift each row of the state matrix to the left by different offsets.

MixColumns: Mix bytes in each column via matrix multiplication over G(28)

AddRoundKey: XOR the current state with the round key.

Final Round (same as above but without MixColumns):

SubBytes → ShiftRows → AddRoundKey.

Pros of AES:

Strong Security: Resistant to known attacks like linear and differential cryptanalysis.

Efficiency: Designed for fast implementation in both hardware and software.

Flexibility: Supports multiple key sizes for varying security needs.

Standardisation: Globally recognised and widely used encryption standard.

Parallelizable: Several AES operations can be parallelised to enhance performance.

Cons of AES:

Block Size Limitation: A fixed block size of 128 bits can be limiting in some contexts.

Key Management: Like all symmetric ciphers, secure key distribution is crucial and challenging.

Complexity: The mathematical operations (especially MixColumns and key expansion) can be complex to implement.

Side-Channel Attacks: Vulnerable if physical implementations leak information (e.g., timing attacks).
