### What I Learned
- Learned how XOR encryption works for simple file encryption and decryption.
- Practiced reading from and writing to files in Python.
- Gained experience with handling user input and validating it.
- Understood the importance of numeric keys for encryption and how XOR can be reversed using the same key.

### What I Built
- Built a simple command-line tool to encrypt and decrypt files using XOR.
- Implemented a menu-driven interface that lets users choose between encryption, decryption, or exiting the program.
- Added basic file existence checking and key validation.

### What Failed
- Initially struggled with ensuring that the decrypted content matches the original content exactly.
- Writing and reading non-text files caused errors because the program was set up for text mode only.

### How I Fixed It
- Switched to consistent encoding handling for reading and writing text files.
- Ensured that the XOR operation uses the same key for encryption and decryption.

### Security Insight
- XOR encryption is very basic and should **not** be used for real security purposes—it can be easily broken.
- Always use established cryptographic libraries for sensitive data.
- Numeric keys must be kept secret; otherwise, the encryption can be reversed easily.
