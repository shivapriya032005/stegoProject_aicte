# Data Hiding Using Steganography in Images

## Introduction
This project implements **image-based steganography**, allowing users to securely hide and retrieve text messages within an image. By subtly modifying pixel values, the hidden message remains undetectable to the human eye. The project ensures secure data transmission without raising suspicion, making it ideal for cybersecurity, confidential communication, and digital forensics.

## Features
- **Lossless Data Embedding:** Uses PNG format to prevent image distortion.
- **Passcode-Based Security:** Ensures only authorized users can decrypt the hidden message.
- **Dynamic Pixel Encoding:** Distributes data across image pixels for enhanced secrecy.
- **Quick & Efficient Retrieval:** Optimized decryption process for fast message extraction.
- **Cross-Platform Compatibility:** Runs on Windows, Linux, and macOS without special dependencies.

## Installation
### **Prerequisites:**
- Python 3.x
- OpenCV (`cv2`)
- NumPy

### **Install Dependencies:**
```sh
pip install opencv-python numpy
```

## Usage
### **Encryption (Hiding Data in an Image)**
1. Run `encrypt.py`:
   ```sh
   python encrypt.py
   ```
2. Enter the **image path**, **secret message**, and **passcode**.
3. The encrypted image will be saved as `encryptedImage.png`.

### **Decryption (Extracting Hidden Data)**
1. Run `decrypt.py`:
   ```sh
   python decrypt.py
   ```
2. Enter the **encrypted image path**, **message length**, and **passcode**.
3. If the passcode matches, the hidden message will be displayed.

## Example Workflow
```
Enter the image path: mypic.png
Enter secret message: Hello123
Enter a passcode: 1234
Message encrypted and saved as encryptedImage.png
```
```
Enter the encrypted image path: encryptedImage.png
Enter the length of the original message: 7
Enter the original passcode: 1234
Decrypted message: Hello123
```

## Future Scope
- **Advanced Cryptographic Security:** AES/RSA encryption before embedding.
- **Support for Other File Types:** Hiding documents, audio, or images.
- **AI-Resistant Steganography:** Counteracting AI-based detection techniques.
- **Video-Based Steganography:** Expanding the concept to video files.
- **Cloud-Based Secure Communication:** Developing a web-based tool.

## Contributors
- **[S Lalitha Shivapriya]** – Project Developer
